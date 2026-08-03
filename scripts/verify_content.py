#!/usr/bin/env python3
"""Verificações editoriais e de publicação para a estrutura canônica."""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
CANON = [
    ROOT / "README.md",
    ROOT / "livro/MAPES.md",
    ROOT / "formacao-docente",
    ROOT / "pesquisa",
    ROOT / "recursos",
    ROOT / "dossie-valor-institucional-mapes",
]
texts = []
for item in CANON:
    files = [item] if item.is_file() else item.rglob("*.md")
    texts.extend((f, f.read_text(encoding="utf-8")) for f in files)
errors = []
obsolete_patterns = {
    "MAPES Essencial": r"\bMAPES\s+Essencial\b",
    "MAPES Padrão": r"\bMAPES\s+Padrão\b",
    "MAPES Pesquisa": r"\bMAPES\s+Pesquisa\b",
    "MAPES Core": r"\bMAPES\s+Core\b",
    "Secretário-Geral": r"\bSecretário-Geral\b",
    "Secretario-Geral": r"\bSecretario-Geral\b",
    "formação modular": r"\bformação\s+modular\b",
    "RACI": r"(?<![A-Za-zÀ-ÖØ-öø-ÿ])RACI(?![A-Za-zÀ-ÖØ-öø-ÿ])",
}
for label, pattern in obsolete_patterns.items():
    hits = [
        str(f.relative_to(ROOT))
        for f, content in texts
        if re.search(pattern, content, flags=re.IGNORECASE)
    ]
    if hits:
        errors.append(f"Termo obsoleto '{label}': {', '.join(hits)}")
for f, content in texts:
    heading_re = re.compile(r"^(#{1,3})\s+(.+)$", re.M)
    headings = list(heading_re.finditer(content))

    for index, match in enumerate(headings):
        level = len(match.group(1))
        if level < 2:
            continue

        next_match = headings[index + 1] if index + 1 < len(headings) else None
        start_pos = match.end()
        end_pos = next_match.start() if next_match else len(content)
        body = content[start_pos:end_pos].strip()

        # Um título-pai pode introduzir subseções sem exigir um parágrafo próprio.
        if next_match and len(next_match.group(1)) > level:
            continue

        if len(re.findall(r"\w+", body)) < 12:
            heading = f"{match.group(1)} {match.group(2)}"
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
