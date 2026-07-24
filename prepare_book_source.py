import re
import os

input_file = "entregaveis-v0.9.0/MAPES — Método de Aprendizagem por Estruturação Sistêmica.md"

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix math display brackets \[ \] -> $$ $$
content = re.sub(r'\\\[\s*', '$$\n', content)
content = re.sub(r'\s*\\\]', '\n$$', content)

# 2. Fix inline math \( \) -> $ $
content = re.sub(r'\\\(\s*', '$', content)
content = re.sub(r'\s*\\\)', '$', content)

# 3. Extract title, metadata, authors, abstract
lines = content.split('\n')

new_lines = []

# Header YAML metadata
yaml_header = """---
title: "MAPES — Método de Aprendizagem por Estruturação Sistêmica"
subtitle: "Versão 0.9.0 — Versão teórico-metodológica para implementação piloto"
author:
  - "Hugo de Paula"
  - "Ricardo Guimarães"
  - "Cláudio de Moura Castro"
date: "24 de julho de 2026"
institute: "LAPAN / UFMG"
lang: pt-BR
documentclass: book
classoption:
  - 11pt
  - a4paper
  - oneside
geometry:
  - top=2.5cm
  - bottom=2.5cm
  - left=3cm
  - right=2.5cm
---
"""

in_appendix = False
skip_until_intro = True

for line in lines:
    # Check for start of main content
    if line.startswith("## 1. Introdução"):
        skip_until_intro = False
    
    if skip_until_intro:
        if line.startswith("> **Nota"):
            new_lines.append(line)
        elif line.startswith("## Resumo / Abstract"):
            new_lines.append("# Resumo / Abstract {.unnumbered}")
        elif line.startswith("### Resumo") or line.startswith("### Abstract"):
            new_lines.append("## " + line.lstrip("# ").strip() + " {.unnumbered}")
        elif line.strip() and not line.startswith("#") and not line.startswith("**Versão") and not line.startswith("**Data") and not line.startswith("**Status") and not line.startswith("de Paula, H.") and not line.startswith("Citação") and not line.startswith("**Hugo") and not line.startswith("**Ricardo") and not line.startswith("**Cláudio"):
            new_lines.append(line)
        continue

    # Main text processing: handle headings
    if line.startswith("## Apêndices"):
        in_appendix = True
        new_lines.append("\\cleardoublepage\n\\appendix")
        continue

    if in_appendix:
        if line.startswith("### Apêndice "):
            title = re.sub(r'^### Apêndice [A-Z] — ', '', line).strip()
            title = re.sub(r'^### Apêndice [A-Z] \– ', '', title).strip()
            new_lines.append(f"# {title}")
        elif line.startswith("#### "):
            title = re.sub(r'^#### ', '', line).strip()
            new_lines.append(f"## {title}")
        elif line.startswith("##### "):
            title = re.sub(r'^##### ', '', line).strip()
            new_lines.append(f"### {title}")
        elif line.startswith("# Canvas MAPES"):
            pass
        elif line.startswith("# CHANGELOG"):
            pass
        elif line.startswith("## ") and not line.startswith("## 1."):
            title = re.sub(r'^## \d+\. ', '', line).strip()
            title = re.sub(r'^## ', '', title).strip()
            new_lines.append(f"## {title}")
        else:
            new_lines.append(line)
    else:
        if re.match(r'^## \d+\.\s+', line):
            title = re.sub(r'^## \d+\.\s+', '', line).strip()
            new_lines.append(f"# {title}")
        elif re.match(r'^### \d+\.\d+\s+', line):
            title = re.sub(r'^### \d+\.\d+\s+', '', line).strip()
            new_lines.append(f"## {title}")
        elif re.match(r'^#### \d+\.\d+\.\d+\s+', line):
            title = re.sub(r'^#### \d+\.\d+\.\d+\s+', '', line).strip()
            new_lines.append(f"### {title}")
        elif line.startswith("### Programa "):
            title = re.sub(r'^### ', '', line).strip()
            new_lines.append(f"### {title}")
        else:
            new_lines.append(line)

final_md = yaml_header + "\n".join(new_lines)

output_md = "entregaveis-v0.9.0/MAPES_Livro_Fonte.md"
with open(output_md, "w", encoding="utf-8") as f:
    f.write(final_md)

print(f"Generated {output_md} successfully.")
