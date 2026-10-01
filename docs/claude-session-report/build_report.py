"""Convierte REPORT.md en REPORT.pdf con portada, índice, tablas, imágenes y números de página.

Admite el subconjunto de Markdown que usa REPORT.md: títulos #/##/###, párrafos, listas
(- y 1.), tablas con |, bloques ``` de código, imágenes ![alt](ruta) y **negrita**/`código`.
Uso: python build_report.py
"""
import pathlib
import re

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, Image, PageBreak, PageTemplate, Paragraph,
                                Preformatted, Spacer, Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

HERE = pathlib.Path(__file__).parent
F = r"C:\Windows\Fonts"
for name, file in [("Arial", "arial"), ("Arial-Bold", "arialbd"), ("Arial-Italic", "ariali"),
                   ("Arial-BoldItalic", "arialbi"), ("Consolas", "consola")]:
    pdfmetrics.registerFont(TTFont(name, rf"{F}\{file}.ttf"))
pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold", italic="Arial-Italic",
                              boldItalic="Arial-BoldItalic")

INK, ACCENT, GREY, SOFT = (colors.HexColor(c) for c in ("#1f2937", "#3b4cca", "#6b7280", "#f3f4f6"))
W = A4[0] - 4.6 * cm
base = ParagraphStyle("b", fontName="Arial", fontSize=9.5, leading=13.5, textColor=INK, spaceAfter=5)
h1 = ParagraphStyle("h1", parent=base, fontName="Arial-Bold", fontSize=16, leading=20, textColor=ACCENT,
                    spaceBefore=6, spaceAfter=8, keepWithNext=1)
h2 = ParagraphStyle("h2", parent=base, fontName="Arial-Bold", fontSize=12, leading=15, spaceBefore=8,
                    spaceAfter=4, keepWithNext=1)
h3 = ParagraphStyle("h3", parent=base, fontName="Arial-Bold", fontSize=10, leading=13, spaceBefore=6,
                    spaceAfter=3, keepWithNext=1, textColor=GREY)
bul = ParagraphStyle("bul", parent=base, leftIndent=14, bulletIndent=3, spaceAfter=2)
cell = ParagraphStyle("c", parent=base, fontSize=7.8, leading=10, spaceAfter=0)
cellh = ParagraphStyle("ch", parent=cell, fontName="Arial-Bold", textColor=colors.white)
code = ParagraphStyle("code", fontName="Consolas", fontSize=7.6, leading=9.6, textColor=INK)
cap = ParagraphStyle("cap", parent=base, fontSize=8, textColor=GREY, alignment=1)


def inline(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"`([^`]+)`", r"<font name='Consolas'>\1</font>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"<link href='\2' color='#3b4cca'>\1</link>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", t)
    return t


def table(rows):
    rows = [r for r in rows if not re.fullmatch(r"\|?[\s:\-|]+\|?", r)]
    data = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    n = max(len(r) for r in data)
    data = [r + [""] * (n - len(r)) for r in data]
    flow = [[Paragraph(inline(c), cellh if i == 0 else cell) for c in r] for i, r in enumerate(data)]
    t = Table(flow, colWidths=[W / n] * n, repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), ACCENT),
                           ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#fafafa")]),
                           ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#d1d5db")),
                           ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4)]))
    return t


class Doc(BaseDocTemplate):
    def afterFlowable(self, f):
        if isinstance(f, Paragraph) and f.style.name in ("h1", "h2"):
            self.notify("TOCEntry", (0 if f.style.name == "h1" else 1, f.getPlainText(), self.page))


def build():
    lines = (HERE / "REPORT.md").read_text(encoding="utf-8").splitlines()
    title = lines[0].lstrip("# ").strip()
    story = [Spacer(1, 4 * cm), Paragraph(title, ParagraphStyle("t", parent=h1, fontSize=24, leading=30)),
             Paragraph("printquote · modelduel · commitling", ParagraphStyle("s", parent=base, fontSize=13,
                                                                           textColor=GREY, leading=18)),
             Paragraph("1 de octubre de 2026 · equipo de agentes coordinado por Claude Code", base),
             Spacer(1, 1 * cm)]
    cover = HERE / "diagrams" / "equipo.png"
    if cover.exists():
        iw, ih = ImageReader(str(cover)).getSize()
        story.append(Image(str(cover), width=W, height=W * ih / iw))
    story += [PageBreak(), Paragraph("Índice", h1)]
    toc = TableOfContents()
    toc.levelStyles = [ParagraphStyle("t1", parent=base, fontName="Arial-Bold", leftIndent=0),
                       ParagraphStyle("t2", parent=base, leftIndent=14, fontSize=8.5)]
    story += [toc, PageBreak()]
    i, buf = 1, []
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                j += 1
            story.append(Preformatted("\n".join(lines[i + 1:j]), code, maxLineLength=110))
            story.append(Spacer(1, 5)); i = j + 1; continue
        if ln.startswith("|"):
            j = i
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            story += [table(lines[i:j]), Spacer(1, 7)]; i = j; continue
        m = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", ln.strip())
        if m:
            p = (HERE / m.group(2)).resolve()
            if p.exists():
                iw, ih = ImageReader(str(p)).getSize()
                w = min(W, iw * 0.5)
                h = w * ih / iw
                if h > 18 * cm:
                    w, h = w * 18 * cm / h, 18 * cm
                story += [Image(str(p), width=w, height=h), Paragraph(inline(m.group(1)), cap)]
            i += 1; continue
        if ln.startswith("### "):
            story.append(Paragraph(inline(ln[4:]), h3))
        elif ln.startswith("## "):
            story.append(Paragraph(inline(ln[3:]), h2))
        elif ln.startswith("# "):
            if story and not isinstance(story[-1], PageBreak):
                story.append(PageBreak())
            story.append(Paragraph(inline(ln[2:]), h1))
        elif re.match(r"\s*[-*] ", ln):
            story.append(Paragraph(inline(re.sub(r"^\s*[-*] ", "", ln)), bul, bulletText="•"))
        elif re.match(r"\s*\d+\. ", ln):
            n = re.match(r"\s*(\d+)\. ", ln).group(1)
            story.append(Paragraph(inline(re.sub(r"^\s*\d+\. ", "", ln)), bul, bulletText=f"{n}."))
        elif ln.strip():
            story.append(Paragraph(inline(ln), base))
        i += 1

    def footer(c, d):
        c.saveState(); c.setFont("Arial", 7.5); c.setFillColor(GREY)
        c.drawString(2.3 * cm, 1.2 * cm, "Reporte de sesión · Claude Code · 01/10/2026")
        c.drawRightString(A4[0] - 2.3 * cm, 1.2 * cm, str(d.page))
        c.setFillColor(ACCENT); c.rect(0, A4[1] - 0.22 * cm, A4[0], 0.22 * cm, stroke=0, fill=1)
        c.restoreState()

    doc = Doc(str(HERE / "REPORT.pdf"), pagesize=A4, leftMargin=2.3 * cm, rightMargin=2.3 * cm,
              topMargin=2 * cm, bottomMargin=2 * cm, title=title, author="Alberto Martínez")
    doc.addPageTemplates([PageTemplate(id="p", frames=[Frame(doc.leftMargin, doc.bottomMargin, doc.width,
                                                            doc.height)], onPage=footer)])
    doc.multiBuild(story)
    print("OK", HERE / "REPORT.pdf")


if __name__ == "__main__":
    build()
