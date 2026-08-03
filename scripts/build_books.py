#!/usr/bin/env python3
"""Renderiza as quatro publicações MAPES com Quarto e prepara a inspeção visual."""
from pathlib import Path
import os
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
RENDERED = DIST / "rendered"
QUARTO = os.environ.get("QUARTO", "quarto")
PUBLICATIONS = {
    "MAPES-Livro": ROOT / "quarto/livro/MAPES.qmd",
    "MAPES-Revisao-da-Literatura": ROOT / "quarto/pesquisa/REVISAO-DA-LITERATURA-MAPES.qmd",
    "MAPES-Formacao-Docente": ROOT / "quarto/formacao/FORMACAO-DOCENTE-MAPES.qmd",
    "MAPES-Valor-Institucional": ROOT / "quarto/valor-institucional/MAPES-VALOR-INSTITUCIONAL.qmd",
}

for command in (QUARTO, "pdftoppm", "pdfinfo"):
    if not shutil.which(command):
        sys.exit(f"Dependência ausente: {command}")

DIST.mkdir(exist_ok=True)
RENDERED.mkdir(exist_ok=True)
for name, source in PUBLICATIONS.items():
    for extension in ("html", "pdf"):
        target = DIST / f"{name}.{extension}"
        subprocess.run(
            [QUARTO, "render", str(source), "--to", extension, "--output", target.name],
            check=True,
            cwd=ROOT,
        )
        rendered = ROOT / "quarto" / target.name
        if not rendered.is_file():
            sys.exit(f"Quarto não produziu a publicação esperada: {rendered}")
        shutil.copy2(rendered, target)
        if extension == "html":
            assets = ROOT / "quarto/_site" / source.relative_to(ROOT / "quarto").parent / f"{source.stem}_files"
            if assets.is_dir():
                shutil.copytree(assets, DIST / assets.name, dirs_exist_ok=True)
            html = target.read_text(encoding="utf-8")
            html = html.replace('"../../livro/', '"../livro/')
            html = html.replace('"../../dossie-valor-institucional-mapes/', '"../dossie-valor-institucional-mapes/')
            target.write_text(html, encoding="utf-8")
        rendered.unlink()
    pdf = DIST / f"{name}.pdf"
    info = subprocess.check_output(["pdfinfo", str(pdf)], text=True)
    pages = next(line for line in info.splitlines() if line.startswith("Pages:")).split()[1]
    prefix = RENDERED / name
    for image in RENDERED.glob(prefix.name + "-*.png"):
        image.unlink()
    subprocess.run(["pdftoppm", "-png", "-r", "150", str(pdf), str(prefix)], check=True)
    images = sorted(RENDERED.glob(prefix.name + "-*.png"))
    if len(images) != int(pages) or not images:
        sys.exit(f"Falha de renderização visual: {pdf}")
    print(f"{pdf.name}: {pages} páginas renderizadas")
shutil.rmtree(ROOT / "quarto/_site", ignore_errors=True)
shutil.rmtree(ROOT / "quarto/livro/livro", ignore_errors=True)
