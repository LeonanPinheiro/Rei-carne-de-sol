"""Validações de formato dos campos do profissional (MED 03 e RN07).

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
    return "(00) 0000-0000 ou (00) 00000-0000"


def validar_celular(telefone: str) -> Optional[str]:
    """Celular com WhatsApp: DDD + 9 + 8 dígitos (RN07)."""
    numeros = somente_digitos(telefone)
    if len(numeros) == 11 and numeros[2] == "9":
        return None
    return "celular com WhatsApp, (00) 90000-0000"


def validar_email(email: str) -> Optional[str]:
    if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", (email or "").strip()):
        return None
    return "nome@dominio.com"


def validar_profissional(nome, cpf, telefone, email, funcao):
    """Devolve a lista de erros como pares (campo, formato esperado)."""
    validar_fone = validar_celular if funcao == Funcao.ENTREGADOR else validar_telefone
    erros = []
    for campo, erro in (
        ("NOME", validar_nome(nome)),
        ("CPF", validar_cpf(cpf)),
        ("TELEFONE", validar_fone(telefone)),
        ("E-MAIL", validar_email(email)),
    ):
        if erro:
            erros.append((campo, erro))
    return erros
