#!/usr/bin/env python3
"""Gera e renderiza as três publicações oficiais MAPES."""
from pathlib import Path
import shutil, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
RENDERED = DIST / "rendered"
BOOKS = {
    "MAPES-Livro.pdf": ROOT / "livro/MAPES.md",
    "MAPES-Formacao-Docente.pdf": ROOT / "formacao-docente/FORMACAO-DOCENTE-MAPES.md",
    "MAPES-Revisao-da-Literatura.pdf": ROOT / "pesquisa/REVISAO-DA-LITERATURA-MAPES.md",
}
for command in ("pandoc", "xelatex", "pdftoppm", "pdfinfo"):
    if not shutil.which(command):
        sys.exit(f"Dependência ausente: {command}")
DIST.mkdir(exist_ok=True)
RENDERED.mkdir(exist_ok=True)
for output, source in BOOKS.items():
    target = DIST / output
    resource_path = f"{source.parent}:{ROOT}"
    subprocess.run(["pandoc", str(source), "--from", "markdown", "--pdf-engine=xelatex", "--include-in-header", str(ROOT / "styles/mapes-book.tex"), "--resource-path", resource_path, "-o", str(target)], check=True, cwd=ROOT)
    info = subprocess.check_output(["pdfinfo", str(target)], text=True)
    pages = next(line for line in info.splitlines() if line.startswith("Pages:")).split()[1]
    prefix = RENDERED / target.stem
    subprocess.run(["pdftoppm", "-png", "-r", "150", str(target), str(prefix)], check=True)
    rendered = sorted(RENDERED.glob(prefix.name + "-*.png"))
    if len(rendered) != int(pages) or not rendered:
        sys.exit(f"Falha de renderização: {target}")
    print(f"{target.name}: {pages} páginas renderizadas")
