"""Entidade Profissional (MED 03)."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Funcao(str, Enum):
    ATENDENTE = "Atendente"
    COZINHEIRO = "Cozinheiro"
    EXPEDIDOR = "Expedidor"
    ENTREGADOR = "Entregador"
    GERENTE = "Gerente"


class Status(str, Enum):
    ATIVO = "Ativo"
    INATIVO = "Inativo"


@dataclass
class Profissional:
    nome: str
    cpf: str
    telefone: str
    email: str
    funcao: Funcao
    status: Status = Status.ATIVO
    cnh: Optional[str] = None
    placa: Optional[str] = None
    id: Optional[int] = field(default=None, compare=False)

    @property
    def ativo(self) -> bool:
        return self.status == Status.ATIVO

    @property
    def cpf_mascarado(self) -> str:
        """CPF exibido na lista e na planilha (RNF 01 · LGPD): 529.***.***-25."""
        return f"{self.cpf[:3]}.***.***-{self.cpf[9:]}"
