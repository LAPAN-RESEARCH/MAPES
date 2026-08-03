#!/usr/bin/env python3
"""Remove apenas saídas regeneráveis que não são fontes editoriais."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
for directory in (ROOT / "quarto/_site", ROOT / "dist/rendered"):
    if directory.exists():
        shutil.rmtree(directory)
for path in (ROOT / "dist").glob("MAPES-*.html"):
    path.unlink()
for directory in (ROOT / "dist").glob("*_files"):
    if directory.is_dir():
        shutil.rmtree(directory)
for path in (ROOT / "quarto").glob("MAPES-*.*"):
    path.unlink()
shutil.rmtree(ROOT / "quarto/livro/livro", ignore_errors=True)
print("Saídas HTML e imagens de inspeção removidas; PDFs e DOCX versionados foram preservados.")
