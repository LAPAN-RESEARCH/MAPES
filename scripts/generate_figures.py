#!/usr/bin/env python3
"""Gera diagramas SVG legíveis em A4 para as publicações MAPES."""
from pathlib import Path
import subprocess

OUT = Path("livro/figuras")
OUT.mkdir(parents=True, exist_ok=True)
FIGURES = [
    ("01-visao-geral.svg", "MAPES: estrutura, decisão pedagógica e revisão", ["Situação-problema", "BTTA", "Plano da Aula", "Evidência e revisão"]),
    ("02-btta-situacao.svg", "Quatro pilares sobre uma situação-problema", ["Blueprint", "Teleonomia", "Taxonomia Acelerada", "Ancoragem Contextual"]),
    ("03-blueprint-sistema.svg", "Blueprint: fronteira, componentes e relações", ["Fronteira da aula", "Componentes", "Relações", "Decisão"]),
    ("04-teleonomia.svg", "Teleonomia: explicar contribuição sem finalismo", ["Componente", "Mecanismo", "Função", "Consequência"]),
    ("05-relevancia-complexidade.svg", "Relevância e complexidade: decisões independentes", ["Núcleo • Apoio • Aprofundamento", "Reconhecer", "Analisar", "Justificar"]),
    ("06-relevancia.svg", "Relevância Sistêmica", ["Núcleo", "Apoio", "Aprofundamento", "Prioridade, não dificuldade"]),
    ("07-ancoragem.svg", "Ancoragem Contextual", ["Contexto", "Abstração", "Transferência", "Novo contexto"]),
    ("08-taxonomia.svg", "Taxonomia Acelerada", ["Problema", "Hipótese", "Fundamento necessário", "Uso justificado"]),
    ("09-processo-seis-etapas.svg", "Processo MAPES em seis etapas", ["Preparar", "Estruturar", "Planejar", "Organizar e produzir", "Implementar", "Avaliar e revisar"]),
    ("10-plano-aula.svg", "Composição do Plano MAPES da Aula", ["Contexto e fontes", "Estrutura BTTA", "Prioridades e objetivos", "Atividade, evidência e revisão"]),
    ("11-producao.svg", "Produção de materiais sem ator fixo", ["Decisões docentes", "Equipe humana", "Apoio tecnológico", "Aprovação docente"]),
    ("12-avaliacao.svg", "Avaliação e revisão", ["Tarefa", "Evidência", "Feedback", "Próxima versão"]),
    ("13-implementacao-pesquisa.svg", "Implementação e pesquisa", ["Aula MAPES", "Evidência pedagógica", "Pesquisa associada", "Método adicional"]),
]

def svg(title, labels):
    width, height = 1200, 430
    n = len(labels)
    boxw = min(260, (width - 120 - (n - 1) * 28) // n)
    x0 = (width - (n * boxw + (n - 1) * 28)) // 2
    boxes = []
    for i, label in enumerate(labels):
        x = x0 + i * (boxw + 28)
        arrow = "" if i == n - 1 else f'<path d="M{x+boxw+5} 235 H{x+boxw+23}" stroke="#17365D" stroke-width="5" marker-end="url(#arrow)"/>'
        boxes.append(f'<rect x="{x}" y="175" width="{boxw}" height="120" rx="14" fill="#F4F7FA" stroke="#17365D" stroke-width="4"/><text x="{x+boxw/2}" y="225" text-anchor="middle" class="label">{label}</text>{arrow}')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc"><title id="title">{title}</title><desc id="desc">Diagrama MAPES: {'; '.join(labels)}.</desc><defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#17365D"/></marker><style>.title{{font:700 30px Arial,sans-serif;fill:#17365D}}.label{{font:600 20px Arial,sans-serif;fill:#172B4D}}</style></defs><rect width="100%" height="100%" fill="white"/><text x="600" y="82" text-anchor="middle" class="title">{title}</text>{''.join(boxes)}<text x="600" y="365" text-anchor="middle" style="font:16px Arial,sans-serif;fill:#425466">Leitura sequencial; a forma e as setas também codificam a relação.</text></svg>'''

for name, title, labels in FIGURES:
    (OUT / name).write_text(svg(title, labels), encoding="utf-8")
    # XeLaTeX needs a PDF asset in this environment. It is generated alongside
    # the canonical, accessible SVG from the same labels and relationship.
    dot = "digraph G { graph [rankdir=LR, bgcolor=white, pad=0.25, nodesep=0.35, ranksep=0.45, label=\"" + title.replace('"', "'") + "\", labelloc=t, fontsize=22, fontname=Arial]; node [shape=box, style=\"rounded,filled\", fillcolor=\"#F4F7FA\", color=\"#17365D\", penwidth=2, fontname=Arial, fontsize=15, margin=\"0.18,0.12\"]; edge [color=\"#17365D\", penwidth=2]; "
    dot += "; ".join(f'n{i} [label=\"{label.replace(chr(34), chr(39))}\"]' for i, label in enumerate(labels))
    dot += "; " + " -> ".join(f"n{i}" for i in range(len(labels))) + "; }"
    subprocess.run(["dot", "-Tpdf", "-o", str(OUT / name.replace(".svg", ".pdf"))], input=dot, text=True, check=True)
print(f"{len(FIGURES)} figuras geradas em {OUT}")
