#!/usr/bin/env python3
"""Verificações editoriais e de publicação para a estrutura canônica."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
CANON = [ROOT / "README.md", ROOT / "livro/MAPES.md", ROOT / "formacao-docente", ROOT / "pesquisa", ROOT / "recursos"]
texts = []
for item in CANON:
    files = [item] if item.is_file() else item.rglob("*.md")
    texts.extend((f, f.read_text(encoding="utf-8")) for f in files)
errors = []
for term in ("MAPES Essencial", "MAPES Padrão", "MAPES Core", "Secretário-Geral", "Secretario-Geral", "formação modular"):
    hits = [str(f.relative_to(ROOT)) for f, content in texts if term.lower() in content.lower()]
    if hits:
        errors.append(f"Termo obsoleto '{term}': {', '.join(hits)}")
for f, content in texts:
    for heading, body in re.findall(r'^(#{1,3} .+?)\n(.*?)(?=^#{1,3} |\Z)', content, re.M | re.S):
        if heading.startswith("##") and len(re.findall(r'\w+', body)) < 12:
            errors.append(f"Seção curta: {f.relative_to(ROOT)} — {heading}")
    for match in re.finditer(r'\[[^]]+\]\(([^)#]+)(?:#[^)]+)?\)', content):
        link = match.group(1)
        if not re.match(r'https?://', link) and not (f.parent / link).exists():
            errors.append(f"Link quebrado: {f.relative_to(ROOT)} -> {link}")
for name in ("MAPES-Livro.pdf", "MAPES-Formacao-Docente.pdf", "MAPES-Revisao-da-Literatura.pdf"):
    if not (ROOT / "dist" / name).is_file():
        errors.append(f"PDF ausente: dist/{name}")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("Verificação de conteúdo concluída sem erros.")
