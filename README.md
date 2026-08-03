# MAPES — Método de Aprendizagem por Estruturação Sistêmica

O MAPES é um framework pedagógico para organizar conhecimentos como sistemas e orientar planejamento, produção, implementação, avaliação e revisão de experiências de aprendizagem. Pode ser aplicado manualmente, por equipes humanas ou com apoio tecnológico; tecnologia e IA não integram sua definição conceitual.

O professor é a autoridade acadêmica: responde pelo conteúdo, estratégia pedagógica, atividades, avaliação e aprovação dos materiais antes do uso.

## Leitura e aplicação

- [Livro MAPES](livro/MAPES.md) e [PDF](dist/MAPES-Livro.pdf)
- [Formação Docente MAPES](formacao-docente/FORMACAO-DOCENTE-MAPES.md), [Plano MAPES da Aula](formacao-docente/PLANO-MAPES-DA-AULA.md) e [PDF](dist/MAPES-Formacao-Docente.pdf)
- [Revisão da Literatura](pesquisa/REVISAO-DA-LITERATURA-MAPES.md), [protocolo](pesquisa/PROTOCOLO-REVISAO-SISTEMATICA-MAPES.md), [análise crítica](pesquisa/ANALISE-CRITICA-POS-REVISAO.md) e [PDF](dist/MAPES-Revisao-da-Literatura.pdf)
- [Valor Institucional MAPES](dossie-valor-institucional-mapes/MAPES-VALOR-INSTITUCIONAL.md) e [PDF](dossie-valor-institucional-mapes/dist/MAPES-VALOR-INSTITUCIONAL.pdf): material executivo para decisão sobre piloto institucional.
- [Manifesto da Aula](recursos/MANIFESTO-DA-AULA.md), um registro técnico opcional.

## Publicações e verificações

São necessários Python 3, Pandoc, XeLaTeX, Poppler e Graphviz.

```bash
make books
make verify
```

`make books` gera as figuras e os três PDFs em `dist/`, renderiza todas as páginas para inspeção e mantém as imagens de revisão em `dist/rendered/` (ignoradas pelo Git). `make verify` verifica termos obsoletos, estrutura, links locais e publicações esperadas.

## Estado da evidência

O framework está em desenvolvimento. A revisão publicada é **sistematizada**, não uma revisão sistemática concluída; o protocolo reproduzível ainda precisa ser executado. Não há alegação de eficácia do MAPES como sistema integrado.
