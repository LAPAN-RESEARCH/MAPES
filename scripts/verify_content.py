#!/usr/bin/env python3
"""Verificações editoriais, de fontes Quarto e de publicações MAPES."""
from pathlib import Path
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
QUARTO = ROOT / "quarto"
SOURCES = [ROOT / "README.md", QUARTO]
errors = []
texts = []
for item in SOURCES:
    files = [item] if item.is_file() else sorted(item.rglob("*.qmd"))
    texts.extend((file, file.read_text(encoding="utf-8")) for file in files)

if not (QUARTO / "_quarto.yml").is_file() or not (QUARTO / "_metadata.yml").is_file():
    errors.append("Configuração Quarto ausente")

bibliography = QUARTO / "references.bib"
if not bibliography.is_file() or not re.search(r"^@\w+\{[^,]+,", bibliography.read_text(encoding="utf-8"), re.M):
    errors.append("Bibliografia Quarto ausente ou inválida")

obsolete_patterns = {
    "MAPES Essencial": r"\bMAPES\s+Essencial\b",
    "MAPES Padrão": r"\bMAPES\s+Padrão\b",
    "MAPES Pesquisa": r"\bMAPES\s+Pesquisa\b",
    "MAPES Core": r"\bMAPES\s+Core\b",
    "VELCRO": r"\bVELCRO\b",
    "conciliação entre visões": r"\bconcilia[cç][aã]o\s+entre\s+visões\b",
    "RACI": r"(?<![A-Za-zÀ-ÖØ-öø-ÿ])RACI(?![A-Za-zÀ-ÖØ-öø-ÿ])",
    "gates": r"\bgates\b",
    "Secretário-Geral": r"\bSecretário-Geral\b",
    "revisores ad hoc obrigatórios": r"\brevisores\s+ad\s+hoc\s+obrigatórios\b",
}
for label, pattern in obsolete_patterns.items():
    hits = [str(file.relative_to(ROOT)) for file, content in texts if re.search(pattern, content, re.I)]
    if hits:
        errors.append(f"Termo obsoleto '{label}': {', '.join(hits)}")

for file, content in texts:
    for match in re.finditer(r"!?(?:\[[^]]*\])\(([^)#]+)(?:#[^)]+)?\)", content):
        link = match.group(1).strip()
        if re.match(r"(?:https?:|mailto:|#)", link):
            continue
        if not (file.parent / link).exists():
            errors.append(f"Link quebrado: {file.relative_to(ROOT)} -> {link}")
    for match in re.finditer(r"!\[[^]]*\]\([^)]*\)\{([^}]*)\}", content):
        if "#fig-" not in match.group(1):
            errors.append(f"Figura sem identificador estável: {file.relative_to(ROOT)}")

for svg in ROOT.rglob("*.svg"):
    try:
        root = ET.parse(svg).getroot()
        if root.tag.rsplit("}", 1)[-1] != "svg":
            errors.append(f"SVG inválido (raiz não é <svg>): {svg.relative_to(ROOT)}")
    except (OSError, ET.ParseError) as exc:
        errors.append(f"SVG inválido ({exc}): {svg.relative_to(ROOT)}")

publications = (
    "MAPES-Livro",
    "MAPES-Revisao-da-Literatura",
    "MAPES-Formacao-Docente",
    "MAPES-Valor-Institucional",
)
for name in publications:
    for extension in ("html", "pdf"):
        artifact = ROOT / "dist" / f"{name}.{extension}"
        if not artifact.is_file():
            errors.append(f"Publicação ausente: {artifact.relative_to(ROOT)}")
        elif extension == "pdf" and not artifact.read_bytes().startswith(b"%PDF-"):
            errors.append(f"PDF inválido: {artifact.relative_to(ROOT)}")

for pdf in ROOT.rglob("*.pdf"):
    if not pdf.read_bytes().startswith(b"%PDF-"):
        errors.append(f"PDF inválido: {pdf.relative_to(ROOT)}")

for docx in ROOT.rglob("*.docx"):
    if not zipfile.is_zipfile(docx):
        errors.append(f"DOCX inválido (não é ZIP): {docx.relative_to(ROOT)}")
    else:
        with zipfile.ZipFile(docx) as archive:
            if "[Content_Types].xml" not in archive.namelist():
                errors.append(f"DOCX inválido ([Content_Types].xml ausente): {docx.relative_to(ROOT)}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("Verificação Quarto concluída sem erros.")
