"""Mensagens do sistema (MSG), conforme docs/catalogo-de-referencias.md."""

MSG = {
    "MSG 01": "Cadastro realizado com sucesso.",
    "MSG 02": "Profissional já cadastrado.",
    "MSG 03": "O preenchimento do campo {campo} deve seguir o formato {formato}.",
    "MSG 04": "Dado alterado com sucesso.",
    "MSG 05": "Deseja realmente excluir esse registro?",
    "MSG 11": "O profissional não foi localizado.",
    "MSG 14": "Sistema não permite esta operação.",
    "MSG 17": "Registro excluído com sucesso.",
}


def texto(codigo: str, **valores: str) -> str:
    """Devolve o texto da mensagem, preenchendo campo e formato na MSG 03."""
    return MSG[codigo].format(**valores)
