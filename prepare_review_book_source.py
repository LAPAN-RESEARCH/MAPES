import re

input_file = "entregaveis-v0.10.0/01-revisao-sistematizada-literatura-MAPES.md"

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix math display brackets \[ \] -> $$ $$
content = re.sub(r'\\\[\s*', '$$\n', content)
content = re.sub(r'\s*\\\]', '\n$$', content)

# 2. Fix inline math \( \) -> $ $
content = re.sub(r'\\\(\s*', '$', content)
content = re.sub(r'\s*\\\)', '$', content)

lines = content.split('\n')
new_lines = []

yaml_header = """---
title: "Revisão Sistematizada da Literatura para Fundamentação e Validação do MAPES"
subtitle: "Síntese Crítica, Fundamentação Epistemológica e Mapeamento de Evidências (Versão 0.10.0)"
author:
    - "Ricardo Queiroz Guimaães"
    - "Hugo de Paula"
    - "Cláudio de Moura Castro"
date: "29 de julho de 2026"
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
skip_until_ch1 = True

for line in lines:
    if line.strip() == "---" and skip_until_ch1:
        continue

    if line.startswith("## 1. Finalidade"):
        skip_until_ch1 = False

    if skip_until_ch1:
        if line.startswith("## Resumo executivo"):
            new_lines.append("# Resumo Executivo {.unnumbered}")
        elif line.strip() and not line.startswith("#") and not line.startswith("**Projeto") and not line.startswith("**Versão") and not line.startswith("**Data") and not line.startswith("**Natureza") and not line.startswith("**Status"):
            new_lines.append(line)
        continue

    # Appendix handling
    if line.startswith("## Apêndices") or line.startswith("# Apêndices"):
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
            title = re.sub(r'^[A-Z]\.\d+(?:\.\d+)*\s+', '', title).strip()
            new_lines.append(f"## {title}")
        elif line.startswith("## ") and not line.startswith("## 1."):
            title = re.sub(r'^## \d+\. ', '', line).strip()
            title = re.sub(r'^## ', '', title).strip()
            new_lines.append(f"## {title}")
        else:
            new_lines.append(line)
    else:
        # Chapter headings
        if re.match(r'^## \d+\.\s+', line):
            title = re.sub(r'^## \d+\.\s+', '', line).strip()
            new_lines.append(f"# {title}")
        # Section headings
        elif re.match(r'^### \d+\.\d+\s+', line):
            title = re.sub(r'^### \d+\.\d+\s+', '', line).strip()
            new_lines.append(f"## {title}")
        # Subsection headings
        elif re.match(r'^#### \d+\.\d+\.\d+\s+', line):
            title = re.sub(r'^#### \d+\.\d+\.\d+\s+', '', line).strip()
            new_lines.append(f"### {title}")
        else:
            new_lines.append(line)

final_md = yaml_header + "\n".join(new_lines)

output_md = "entregaveis-v0.10.0/MAPES_Revisao_Livro_Fonte.md"
with open(output_md, "w", encoding="utf-8") as f:
    f.write(final_md)

print(f"Generated {output_md} successfully.")
