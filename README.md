# MAPES — Método de Aprendizagem por Estruturação Sistêmica

O MAPES é um framework pedagógico para organizar conhecimentos como sistemas e orientar planejamento, produção, implementação, avaliação e revisão de experiências de aprendizagem. Pode ser aplicado manualmente, por equipes humanas ou com apoio tecnológico; tecnologia e IA não integram sua definição conceitual.

O professor é a autoridade acadêmica: responde pelo conteúdo, estratégia pedagógica, atividades, avaliação e aprovação dos materiais antes do uso.

## Leitura e aplicação

- [Livro MAPES](quarto/livro/MAPES.qmd), [HTML](dist/MAPES-Livro.html) e [PDF](dist/MAPES-Livro.pdf)
- [Formação Docente MAPES](quarto/formacao/FORMACAO-DOCENTE-MAPES.qmd), [Plano MAPES da Aula](quarto/formacao/PLANO-MAPES-DA-AULA.qmd), [HTML](dist/MAPES-Formacao-Docente.html) e [PDF](dist/MAPES-Formacao-Docente.pdf)
- [Revisão da Literatura](quarto/pesquisa/REVISAO-DA-LITERATURA-MAPES.qmd), [protocolo](quarto/pesquisa/PROTOCOLO-REVISAO-SISTEMATICA-MAPES.qmd), [análise crítica](quarto/pesquisa/ANALISE-CRITICA-POS-REVISAO-MAPES.qmd), [HTML](dist/MAPES-Revisao-da-Literatura.html) e [PDF](dist/MAPES-Revisao-da-Literatura.pdf)
- [Valor Institucional MAPES](quarto/valor-institucional/MAPES-VALOR-INSTITUCIONAL.qmd), [HTML](dist/MAPES-Valor-Institucional.html) e [PDF](dist/MAPES-Valor-Institucional.pdf): material executivo para decisão sobre piloto institucional.
- [Manifesto da Aula](recursos/MANIFESTO-DA-AULA.md), um registro técnico opcional.

## Publicações e verificações

São necessários Python 3, Quarto, XeLaTeX, Poppler e Graphviz.

```bash
make books
make verify
```

`make books` gera as figuras, renderiza as quatro publicações em HTML e PDF e mantém as imagens de revisão em `dist/rendered/` (ignoradas pelo Git). `make verify` verifica termos obsoletos, estrutura, links locais, bibliografia, SVGs, PDFs e DOCX institucionais existentes. Durante a transição, os Markdown originais são mantidos para compatibilidade e comparação; as fontes de publicação são os `.qmd` em `quarto/`.

## Estado da evidência

O framework está em desenvolvimento. A revisão publicada é **sistematizada**, não uma revisão sistemática concluída; o protocolo reproduzível ainda precisa ser executado. Não há alegação de eficácia do MAPES como sistema integrado.
