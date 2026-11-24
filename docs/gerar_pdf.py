"""Gera o PDF da estória no formato da disciplina a partir dos arquivos Markdown.

Uso: python docs/gerar_pdf.py
Saída: docs/estorias/US-03-cadastro-de-profissionais.pdf
"""

import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (BaseDocTemplate, Frame, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

PASTA = Path(__file__).parent
ESTORIA = PASTA / "estorias" / "US-03-cadastro-de-profissionais.md"
CATALOGO = PASTA / "catalogo-de-referencias.md"
SAIDA = PASTA / "estorias" / "US-03-cadastro-de-profissionais.pdf"

SISTEMA = "O REI DA CARNE DE SOL – GESTÃO DE PEDIDOS E DELIVERY"
TIPO = "Estória de Usuário:"
TITULO = "US 03 Cadastro de Profissionais"

base = ParagraphStyle("base", fontName="Helvetica", fontSize=10, leading=13.5,
                      alignment=TA_JUSTIFY, spaceAfter=4)
celula = ParagraphStyle("celula", parent=base, fontSize=8, leading=10, alignment=0, spaceAfter=0)
cabecalho_celula = ParagraphStyle("cab", parent=celula, fontName="Helvetica-Bold")
secao = ParagraphStyle("secao", fontName="Helvetica-Bold", fontSize=11, leading=14,
                       spaceBefore=10, spaceAfter=4)
subsecao = ParagraphStyle("sub", parent=secao, fontSize=10, spaceBefore=6)
marcador = ParagraphStyle("marcador", parent=base, leftIndent=14, bulletIndent=4, alignment=0)


def inline(texto: str) -> str:
    texto = texto.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    codigos = []

    def guardar(m):
        codigos.append(m.group(1))
        return f"\x00{len(codigos) - 1}\x00"

    texto = re.sub(r"`(.+?)`", guardar, texto)  # protege o código do negrito
    texto = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", texto)
    texto = re.sub(r"\x00(\d+)\x00",
                   lambda m: f"<font name='Courier'>{codigos[int(m.group(1))]}</font>", texto)
    texto = re.sub(r"\[(.+?)\]\((.+?)\)", r"\1", texto)  # links viram texto
    return texto


def larguras(cabecalho):
    n = len(cabecalho)
    total = 17 * cm
    if n == 7:  # tabela de cenários, mesmas colunas da US 30
        return [p * total for p in (0.16, 0.15, 0.14, 0.08, 0.19, 0.16, 0.12)]
    if n == 2:
        return [0.17 * total, 0.83 * total]
    if n == 3 and cabecalho[0].startswith("Atributo"):
        return [0.18 * total, 0.12 * total, 0.70 * total]
    if n == 3 and cabecalho[1] == "Regra":
        return [0.12 * total, 0.70 * total, 0.18 * total]
    if n == 3 and cabecalho[1] == "Entidade":
        return [0.12 * total, 0.18 * total, 0.70 * total]
    if n == 3 and cabecalho[0] == "Campo":
        return [0.18 * total, 0.42 * total, 0.40 * total]
    if n == 3:
        return [0.18 * total, 0.30 * total, 0.52 * total]
    if n == 5:
        return [p * total for p in (0.10, 0.12, 0.38, 0.20, 0.20)]
    return [total / n] * n


def tabela(linhas):
    cab = linhas[0]
    dados = [[Paragraph(inline(c), cabecalho_celula) for c in cab]]
    dados += [[Paragraph(inline(c), celula) for c in linha] for linha in linhas[1:]]
    t = Table(dados, colWidths=larguras(cab), repeatRows=1)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D9D9D9")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def markdown_para_flowables(texto: str, pular_ate: str = None):
    """Converte o subconjunto de Markdown usado nas estórias."""
    linhas = texto.splitlines()
    if pular_ate:
        linhas = linhas[next(i for i, l in enumerate(linhas) if l.startswith(pular_ate)):]
    saida, tabela_atual = [], []

    def fechar_tabela():
        if tabela_atual:
            saida.append(tabela(tabela_atual))
            saida.append(Spacer(1, 6))
            tabela_atual.clear()

    for linha in linhas:
        if linha.startswith("|"):
            celulas = [c.strip() for c in linha.strip().strip("|").split("|")]
            if not all(re.fullmatch(r"-+", c) for c in celulas):
                tabela_atual.append(celulas)
            continue
        fechar_tabela()
        if not linha.strip():
            continue
        if linha.startswith("#### "):
            saida.append(Paragraph(inline(linha[5:]), subsecao))
        elif linha.startswith("### "):
            saida.append(Paragraph(inline(linha[4:]), subsecao))
        elif linha.startswith("## "):
            saida.append(Paragraph(inline(linha[3:]), secao))
        elif linha.startswith("# "):
            continue
        elif linha.startswith("- "):
            saida.append(Paragraph(inline(linha[2:]), marcador, bulletText="•"))
        elif re.match(r"\d+\. ", linha):
            numero, resto = linha.split(". ", 1)
            saida.append(Paragraph(inline(resto), marcador, bulletText=f"{numero}."))
        elif linha.startswith(">"):
            conteudo = linha.lstrip("> ").strip()
            if conteudo:
                saida.append(Paragraph(inline(conteudo), ParagraphStyle(
                    "cartao", parent=base, leftIndent=12, borderColor=colors.black,
                    borderWidth=0.5, borderPadding=6, spaceBefore=4, spaceAfter=8)))
        else:
            saida.append(Paragraph(inline(linha), base))
    fechar_tabela()
    return saida


def desenhar_moldura(canvas, doc):
    canvas.saveState()
    largura, altura = A4
    canvas.setFont("Helvetica-Bold", 12)
    canvas.drawCentredString(largura / 2, altura - 1.4 * cm, SISTEMA)
    canvas.setFont("Helvetica-Bold", 10)
    canvas.drawCentredString(largura / 2, altura - 1.95 * cm, TIPO)
    canvas.drawCentredString(largura / 2, altura - 2.45 * cm, TITULO)
    canvas.setLineWidth(0.6)
    canvas.line(2 * cm, altura - 2.75 * cm, largura - 2 * cm, altura - 2.75 * cm)
    canvas.setFont("Helvetica", 9)
    canvas.drawRightString(largura - 2 * cm, 1.2 * cm, f"Pág. {doc.page} de {doc.total_paginas}")
    canvas.drawString(2 * cm, 1.2 * cm, "Os 3 Devs · Análise Orientada a Objetos · UVA")
    canvas.restoreState()


class Documento(BaseDocTemplate):
    total_paginas = 0


def montar(total_paginas: int) -> int:
    doc = Documento(str(SAIDA), pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                    topMargin=3.3 * cm, bottomMargin=2 * cm, title=TITULO, author="Os 3 Devs")
    doc.total_paginas = total_paginas
    quadro = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="corpo")
    doc.addPageTemplates([PageTemplate(id="pagina", frames=[quadro], onPage=desenhar_moldura)])

    texto = ESTORIA.read_text(encoding="utf-8")
    historico, resto = texto.split("## Descrição", 1)
    corpo = markdown_para_flowables(historico, pular_ate="## Histórico")
    corpo.append(PageBreak())
    anexos_inicio = resto.index("## Cartão, conversa")
    corpo += markdown_para_flowables("## Descrição" + resto[:anexos_inicio])
    corpo.append(PageBreak())
    corpo.append(Paragraph("Anexo A · Cartão, INVEST e tarefas", secao))
    corpo += markdown_para_flowables(resto[anexos_inicio:].replace("## ", "### "))
    corpo.append(PageBreak())
    corpo.append(Paragraph("Anexo B · Catálogo de referências", secao))
    corpo += markdown_para_flowables(
        CATALOGO.read_text(encoding="utf-8").replace("## ", "### "))
    doc.build(corpo)
    return doc.page


if __name__ == "__main__":
    paginas = montar(0)  # primeira passada conta as páginas
    montar(paginas)
    print(f"{SAIDA} ({paginas} páginas)")
