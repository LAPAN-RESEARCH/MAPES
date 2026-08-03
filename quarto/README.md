# Publicações Quarto

As fontes `.qmd` nesta pasta são as fontes editoriais canônicas para novas publicações. A migração preserva, temporariamente, os arquivos Markdown nas pastas históricas do repositório para comparação textual, links externos e rastreabilidade Git.

`make books` renderiza as quatro publicações principais em HTML e PDF. As saídas ficam em `dist/`; as imagens usadas na inspeção visual ficam em `dist/rendered/` e são ignoradas pelo Git. Os documentos complementares de pesquisa, formação e valor institucional permanecem como fontes Quarto independentes e são ligados pelas publicações correspondentes.

Os SVGs permanecem nas pastas de ativos originais e são a fonte preferencial das figuras. PDFs e DOCX legados só são mantidos quando já constituem artefatos institucionais de distribuição; esta primeira migração não cria novos DOCX.
