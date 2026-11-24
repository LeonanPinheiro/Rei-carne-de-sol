"""Testes de aceitação da US 03 · Cadastro de Profissionais.

Um teste por padrão de comportamento (CPO), na ordem da tabela de
cenários e critérios de aceitação da estória.
"""

import pytest
from openpyxl import load_workbook

from rei_carne_de_sol.profissionais import Funcao, ServicoProfissionais, Status

CPF_MARIA = "529.982.247-25"
CPF_JOAO = "111.444.777-35"


@pytest.fixture
def em_rota():
    """IDs de entregadores com lote Em Rota (informação que vem da US 02)."""
    return set()


@pytest.fixture
def servico(em_rota):
    return ServicoProfissionais(entregadores_em_rota=lambda: em_rota)


def incluir_atendente(servico, status=Status.ATIVO):
    return servico.incluir("Maria da Silva", CPF_MARIA, "(22) 98824-1488",
                           "maria@email.com", Funcao.ATENDENTE, status)


def incluir_entregador(servico, status=Status.ATIVO):
    return servico.incluir("João Souza", CPF_JOAO, "22 99999-0000", "joao@email.com",
                           Funcao.ENTREGADOR, status, cnh="12345678901", placa="rio2a18")


# ---------- Incluir ----------
def test_cpo_1_1_incluir_profissional(servico):
    resultado = incluir_atendente(servico)
    assert resultado.sucesso and resultado.mensagens == ["MSG 01"]
    assert resultado.textos == ["Cadastro realizado com sucesso."]
    assert len(servico.listar()) == 1


def test_cpo_1_2_incluir_entregador(servico):
    resultado = incluir_entregador(servico)
    assert resultado.sucesso and resultado.mensagens == ["MSG 01"]
    assert resultado.dados.placa == "RIO2A18"


def test_cpo_1_3_incluir_profissional_ja_cadastrado(servico):
    incluir_atendente(servico)
    resultado = servico.incluir("Maria Souza", "52998224725", "22988241488",
                                "outra@email.com", Funcao.COZINHEIRO)
    assert not resultado.sucesso and resultado.mensagens == ["MSG 02"]
    assert len(servico.listar()) == 1


def test_cpo_1_4_incluir_com_erros_de_validacao(servico):
    resultado = servico.incluir("Maria da Silva", "123.456.789-00", "2299",
                                "maria-email", Funcao.ATENDENTE)
    assert not resultado.sucesso
    assert resultado.mensagens == ["MSG 03", "MSG 03", "MSG 03"]
    assert "O preenchimento do campo CPF deve seguir o formato" in resultado.textos[0]
    assert servico.listar() == []


def test_cpo_1_5_incluir_entregador_sem_cnh_ou_placa(servico):
    resultado = servico.incluir("João Souza", CPF_JOAO, "22999990000", "joao@email.com",
                                Funcao.ENTREGADOR)
    assert not resultado.sucesso
    assert resultado.mensagens == ["MSG 03", "MSG 03"]
    assert any("campo CNH" in t for t in resultado.textos)
    assert any("campo PLACA" in t for t in resultado.textos)


# ---------- Alterar ----------
def test_cpo_2_1_alterar_dados(servico):
    maria = incluir_atendente(servico).dados
    resultado = servico.alterar(maria.id, telefone="(22) 2665-1234", funcao=Funcao.EXPEDIDOR)
    assert resultado.sucesso and resultado.mensagens == ["MSG 04"]
    assert servico.detalhes(maria.id).dados.funcao == Funcao.EXPEDIDOR


def test_cpo_2_2_alterar_com_erro_de_validacao(servico):
    maria = incluir_atendente(servico).dados
    resultado = servico.alterar(maria.id, email="sem-arroba")
    assert not resultado.sucesso and resultado.mensagens == ["MSG 03"]
    assert servico.detalhes(maria.id).dados.email == "maria@email.com"


def test_invariante_cpf_nao_pode_ser_alterado(servico):
    maria = incluir_atendente(servico).dados
    resultado = servico.alterar(maria.id, cpf=CPF_JOAO)
    assert not resultado.sucesso and resultado.mensagens == ["MSG 14"]
    assert servico.detalhes(maria.id).dados.cpf == "52998224725"


# ---------- Consultar ----------
def test_cpo_3_1_consultar_profissional(servico):
    incluir_atendente(servico)
    por_nome = servico.consultar("maria")
    por_cpf = servico.consultar(CPF_MARIA)
    assert por_nome.sucesso and por_nome.dados[0].nome == "Maria da Silva"
    assert por_cpf.sucesso and len(por_cpf.dados) == 1


def test_cpo_3_2_profissional_nao_localizado(servico):
    incluir_atendente(servico)
    resultado = servico.consultar("Carlos")
    assert not resultado.sucesso and resultado.mensagens == ["MSG 11"]


# ---------- Excluir ----------
def test_cpo_4_1_excluir_profissional_inativo(servico):
    maria = incluir_atendente(servico, Status.INATIVO).dados
    resultado = servico.excluir(maria.id, confirmado=True)
    assert resultado.sucesso and resultado.mensagens == ["MSG 05", "MSG 17"]
    assert servico.listar() == []


def test_cpo_4_2_cancelar_exclusao(servico):
    maria = incluir_atendente(servico, Status.INATIVO).dados
    resultado = servico.excluir(maria.id, confirmado=False)
    assert not resultado.sucesso and resultado.mensagens == ["MSG 05"]
    assert len(servico.listar()) == 1


def test_cpo_4_3_nao_permite_excluir_profissional_ativo(servico):
    maria = incluir_atendente(servico, Status.ATIVO).dados
    resultado = servico.excluir(maria.id, confirmado=True)
    assert not resultado.sucesso and resultado.mensagens == ["MSG 05", "MSG 14"]
    assert len(servico.listar()) == 1


def test_cpo_4_3_nao_permite_excluir_entregador_em_rota(servico, em_rota):
    joao = incluir_entregador(servico, Status.INATIVO).dados
    em_rota.add(joao.id)
    resultado = servico.excluir(joao.id, confirmado=True)
    assert resultado.mensagens == ["MSG 05", "MSG 14"]


# ---------- Exportar ----------
def test_cpo_5_1_exportar_excel_com_cpf_mascarado(servico, tmp_path):
    incluir_atendente(servico)
    incluir_entregador(servico)
    arquivo = tmp_path / "profissionais.xlsx"
    assert servico.exportar_excel(arquivo).sucesso

    linhas = list(load_workbook(arquivo).active.iter_rows(values_only=True))
    assert linhas[0][2] == "CPF" and "CNH" not in linhas[0]  # RNF 01
    assert linhas[1][2] == "529.***.***-25"
    assert len(linhas) == 3


# ---------- Ativar e desativar ----------
def test_cpo_6_1_ativar_selecionados(servico):
    maria = incluir_atendente(servico, Status.INATIVO).dados
    joao = incluir_entregador(servico, Status.INATIVO).dados
    assert servico.ativar_selecionados([maria.id, joao.id]).sucesso
    assert all(p.ativo for p in servico.listar())


def test_cpo_7_1_desativar_selecionados(servico):
    maria = incluir_atendente(servico).dados
    joao = incluir_entregador(servico).dados
    assert servico.desativar_selecionados([maria.id, joao.id]).sucesso
    assert not any(p.ativo for p in servico.listar())


def test_cpo_7_2_nao_permite_desativar_entregador_em_rota(servico, em_rota):
    maria = incluir_atendente(servico).dados
    joao = incluir_entregador(servico).dados
    em_rota.add(joao.id)
    resultado = servico.desativar_selecionados([maria.id, joao.id])
    assert not resultado.sucesso and resultado.mensagens == ["MSG 14"]
    assert servico.detalhes(joao.id).dados.ativo
    assert not servico.detalhes(maria.id).dados.ativo
