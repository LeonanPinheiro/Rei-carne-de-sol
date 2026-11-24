"""Regras da US 03 · Cadastro de Profissionais.

Cada método corresponde a um padrão de comportamento (CPO) da estória e
devolve um Resultado com os códigos das mensagens exibidas ao usuário.
O armazenamento é em memória: basta trocar o dicionário por um banco de
dados sem mudar as regras.
"""

from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Callable, Iterable, List, Optional, Set

from openpyxl import Workbook

from ..mensagens import texto
from .modelo import Funcao, Profissional, Status
from .validacoes import somente_digitos, validar_profissional


@dataclass
class Resultado:
    sucesso: bool
    mensagens: List[str] = field(default_factory=list)  # códigos, ex.: ["MSG 01"]
    textos: List[str] = field(default_factory=list)  # textos exibidos ao usuário
    dados: object = None

    def adicionar(self, codigo: str, **valores: str) -> "Resultado":
        self.mensagens.append(codigo)
        self.textos.append(texto(codigo, **valores))
        return self


class ServicoProfissionais:
    def __init__(self, entregadores_em_entrega: Callable[[], Set[int]] = lambda: set()):
        """`entregadores_em_entrega` informa os IDs de entregadores com pedido
        no status Saiu para Entrega (informação que vem da US 02)."""
        self._profissionais: dict[int, Profissional] = {}
        self._proximo_id = 1
        self._entregadores_em_entrega = entregadores_em_entrega

    # ---------- apoio ----------
    def _erros_de_validacao(self, resultado: Resultado, erros) -> Resultado:
        resultado.sucesso = False
        for campo, formato in erros:
            resultado.adicionar("MSG 03", campo=campo, formato=formato)
        return resultado

    def _buscar_por_cpf(self, cpf: str) -> Optional[Profissional]:
        numeros = somente_digitos(cpf)
        return next((p for p in self._profissionais.values() if p.cpf == numeros), None)

    def _em_entrega(self, profissional: Profissional) -> bool:
        return (
            profissional.funcao == Funcao.ENTREGADOR
            and profissional.id in self._entregadores_em_entrega()
        )

    def listar(self) -> List[Profissional]:
        return list(self._profissionais.values())

    # ---------- CPO 1.1 a 1.5 · Incluir ----------
    def incluir(self, nome, cpf, telefone, email, funcao: Funcao,
                status: Status = Status.ATIVO) -> Resultado:
        resultado = Resultado(sucesso=False)
        erros = validar_profissional(nome, cpf, telefone, email, funcao)
        if erros:  # CPO 1.4 e CPO 1.5
            return self._erros_de_validacao(resultado, erros)
        if self._buscar_por_cpf(cpf):  # CPO 1.3 · RN06
            return resultado.adicionar("MSG 02")

        profissional = Profissional(
            nome=nome.strip(),
            cpf=somente_digitos(cpf),
            telefone=somente_digitos(telefone),
            email=email.strip().lower(),
            funcao=funcao,
            status=status,
            id=self._proximo_id,
        )
        self._profissionais[profissional.id] = profissional
        self._proximo_id += 1
        resultado.sucesso, resultado.dados = True, profissional
        return resultado.adicionar("MSG 01")  # CPO 1.1 e CPO 1.2

    # ---------- CPO 2.1 e 2.2 · Alterar ----------
    def alterar(self, id_profissional: int, **novos_dados) -> Resultado:
        resultado = Resultado(sucesso=False)
        atual = self._profissionais.get(id_profissional)
        if atual is None:
            return resultado.adicionar("MSG 11")
        if "cpf" in novos_dados:  # invariante: o CPF não muda (RN06)
            return resultado.adicionar("MSG 14")

        candidato = replace(atual, **novos_dados)
        erros = validar_profissional(
            candidato.nome, candidato.cpf, candidato.telefone, candidato.email,
            candidato.funcao,
        )
        if erros:  # CPO 2.2
            return self._erros_de_validacao(resultado, erros)

        candidato.email = candidato.email.strip().lower()
        candidato.telefone = somente_digitos(candidato.telefone)
        self._profissionais[id_profissional] = candidato
        resultado.sucesso, resultado.dados = True, candidato
        return resultado.adicionar("MSG 04")  # CPO 2.1

    # ---------- CPO 3.1 e 3.2 · Consultar ----------
    def consultar(self, termo: str) -> Resultado:
        termo_digitos = somente_digitos(termo)
        termo_texto = (termo or "").strip().lower()
        encontrados = [
            p for p in self._profissionais.values()
            if (termo_digitos and len(termo_digitos) == 11 and p.cpf == termo_digitos)
            or (termo_texto and termo_texto in p.nome.lower())
        ]
        if not encontrados:  # CPO 3.2
            return Resultado(sucesso=False).adicionar("MSG 11")
        return Resultado(sucesso=True, dados=encontrados)  # CPO 3.1

    def detalhes(self, id_profissional: int) -> Resultado:
        profissional = self._profissionais.get(id_profissional)
        if profissional is None:
            return Resultado(sucesso=False).adicionar("MSG 11")
        return Resultado(sucesso=True, dados=profissional)

    # ---------- CPO 4.1 a 4.3 · Excluir ----------
    def excluir(self, id_profissional: int, confirmado: bool) -> Resultado:
        resultado = Resultado(sucesso=False).adicionar("MSG 05")
        profissional = self._profissionais.get(id_profissional)
        if profissional is None:
            return resultado.adicionar("MSG 11")
        if not confirmado:  # CPO 4.2
            return resultado
        if profissional.ativo or self._em_entrega(profissional):  # CPO 4.3 · RN08 e RN09
            return resultado.adicionar("MSG 14")
        del self._profissionais[id_profissional]
        resultado.sucesso = True
        return resultado.adicionar("MSG 17")  # CPO 4.1

    # ---------- CPO 5.1 · Exportar para Excel ----------
    def exportar_excel(self, caminho: Path) -> Resultado:
        planilha = Workbook()
        aba = planilha.active
        aba.title = "Profissionais"
        aba.append(["ID", "Nome", "CPF", "Telefone", "E-mail", "Função", "Status"])
        for p in self.listar():  # RNF03: CPF mascarado
            aba.append([p.id, p.nome, p.cpf_mascarado, p.telefone, p.email,
                        p.funcao.value, p.status.value])
        caminho = Path(caminho)
        planilha.save(caminho)
        return Resultado(sucesso=True, dados=caminho)

    # ---------- CPO 6.1, 7.1 e 7.2 · Ativar e desativar selecionados ----------
    def ativar_selecionados(self, ids: Iterable[int]) -> Resultado:
        for id_profissional in ids:
            profissional = self._profissionais.get(id_profissional)
            if profissional:
                profissional.status = Status.ATIVO
        return Resultado(sucesso=True)

    def desativar_selecionados(self, ids: Iterable[int]) -> Resultado:
        resultado = Resultado(sucesso=True, dados=[])
        for id_profissional in ids:
            profissional = self._profissionais.get(id_profissional)
            if profissional is None:
                continue
            if self._em_entrega(profissional):  # CPO 7.2 · RN09
                resultado.sucesso = False
                resultado.dados.append(profissional.id)
                continue
            profissional.status = Status.INATIVO
        if not resultado.sucesso:
            resultado.adicionar("MSG 14")
        return resultado
