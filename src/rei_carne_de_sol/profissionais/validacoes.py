"""Validações de formato dos campos do profissional (MED 03 e RNE 07).

Cada validador devolve None se o valor é válido, ou o texto do formato
esperado, que entra na MSG 03.
"""

import re
from typing import Optional

from .modelo import Funcao


def somente_digitos(valor: str) -> str:
    return re.sub(r"\D", "", valor or "")


def validar_nome(nome: str) -> Optional[str]:
    nome = (nome or "").strip()
    if 3 <= len(nome) <= 100 and len(nome.split()) >= 2:
        return None
    return "nome e sobrenome, com 3 a 100 caracteres"


def validar_cpf(cpf: str) -> Optional[str]:
    formato = "000.000.000-00, com dígitos verificadores válidos"
    numeros = somente_digitos(cpf)
    if len(numeros) != 11 or numeros == numeros[0] * 11:
        return formato
    for tamanho in (9, 10):
        soma = sum(int(numeros[i]) * (tamanho + 1 - i) for i in range(tamanho))
        digito = (soma * 10) % 11 % 10
        if digito != int(numeros[tamanho]):
            return formato
    return None


def validar_telefone(telefone: str) -> Optional[str]:
    if len(somente_digitos(telefone)) in (10, 11):
        return None
    return "(00) 00000-0000"


def validar_email(email: str) -> Optional[str]:
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", (email or "").strip()):
        return None
    return "nome@dominio.com"


def validar_cnh(cnh: Optional[str]) -> Optional[str]:
    if len(somente_digitos(cnh or "")) == 11:
        return None
    return "11 dígitos"


def validar_placa(placa: Optional[str]) -> Optional[str]:
    if re.fullmatch(r"[A-Z]{3}\d[A-Z0-9]\d{2}", (placa or "").upper().replace("-", "")):
        return None
    return "ABC1234 ou ABC1D23"


def validar_profissional(nome, cpf, telefone, email, funcao, cnh=None, placa=None):
    """Devolve a lista de erros como pares (campo, formato esperado)."""
    erros = []
    for campo, erro in (
        ("NOME", validar_nome(nome)),
        ("CPF", validar_cpf(cpf)),
        ("TELEFONE", validar_telefone(telefone)),
        ("E-MAIL", validar_email(email)),
    ):
        if erro:
            erros.append((campo, erro))
    if funcao == Funcao.ENTREGADOR:  # RNE 07
        for campo, erro in (("CNH", validar_cnh(cnh)), ("PLACA", validar_placa(placa))):
            if erro:
                erros.append((campo, erro))
    return erros
