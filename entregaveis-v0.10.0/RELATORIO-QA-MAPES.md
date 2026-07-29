# Relatório de controle de qualidade — MAPES v0.10.0

**Data:** 29 de julho de 2026  
**Escopo:** documento fundador, plano de pesquisa, revisão de literatura, especificação do MAPES Core, manual de implementação, Perfil Institucional, glossário, formação docente, backlog do piloto, metadados, fontes de livro e PDFs.  
**Limite:** esta auditoria documental e técnica não substitui revisão por pares, validação empírica, avaliação ética nem aprovação pelos autores e pelas instituições competentes.

## 1. Integridade estrutural e técnica

| Verificação | Resultado |
|---|---|
| Leitura dos documentos finais em UTF-8 | aprovada |
| Blocos Markdown cercados por crases | balanceados |
| Links Markdown relativos | nenhum destino inexistente detectado |
| JSON | válido |
| RDF/XML | dois arquivos bem-formados |
| Conversão Markdown por Pandoc dos documentos normativos centrais | aprovada |
| PDF do documento fundador | regenerado, 99 páginas |
| PDF da revisão de literatura | regenerado, 49 páginas |
| Inspeção visual de capa, página interna e apêndice aplicado | aprovada |
| Manifestos SHA-256 | regenerados e validados após o fechamento dos arquivos |

Foram auditados 31 arquivos Markdown no corpus final selecionado. Os documentos fundador, manual, Core, Perfil Institucional e glossário também foram submetidos a conversão estrutural por Pandoc, sem erro de análise.

## 2. Definição, arquitetura e nomenclatura

As buscas e a leitura cruzada confirmaram:

- adoção da definição canônica de framework pedagógico, metodológico e institucional;
- autoridade acadêmica do professor e independência conceitual em relação a software ou inteligência artificial;
- distinção `MAPES ≠ BTTA ≠ MAPES Core`;
- Core definido como arquitetura operacional normativa, cujas funções podem ser executadas manualmente, digitalmente ou por combinação entre trabalho humano e automação;
- Blueprint funcional, grafo sistêmico funcional e mapa funcional diferenciados;
- topologia, semântica funcional, operações e tarefas, portas de entrada e prioridade articuladas em seção própria;
- Taxonomia Acelerada mantida como ciclo não linear, separada da Estratificação de Relevância;
- Estratificação preservada como dimensão complementar, sem estatuto de quinto pilar;
- Ancoragem, desancoragem e transferência preservadas;
- MAPES Essencial, Padrão e Pesquisa preservados;
- PDCA restrito à macroestrutura administrativa;
- individualização, personalização e adaptação tratadas como conceitos distintos;
- PDI usado somente como Plano de Desenvolvimento Institucional, externo ao escopo do MAPES.

## 3. Core, autoria e inferências

A especificação do Core e seus reflexos no documento fundador, manual, Perfil Institucional, formação e glossário foram confrontados. Estão presentes:

- fontes autorizadas, proveniência, rastreabilidade, conflitos, lacunas, aprovação docente e versionamento;
- matriz normativa com objetivo, nó principal, nós relacionados, relação, função, operação cognitiva, relevância, tarefa, evidência, feedback, fonte e confiança;
- autoria assistida com responsabilidades distintas para IA, professor e instituição;
- inferências sobre lacunas do estudante sempre provisórias, com evidência, confiança, alternativas, confirmação e revisão;
- relatórios docentes com evidência, confiança, alternativas explicativas, intervenções, evolução, recomendação e decisão docente;
- níveis de risco baixo, intermediário e alto;
- direito do estudante de solicitar ajuda, contestar inferências e pedir revisão humana;
- governança separada entre framework, produto/Core digital e instituição.

## 4. Mensuração da qualidade

O corpus normativo contém uma seção explícita, sem escore único, para os seis domínios:

1. fidelidade estrutural;
2. qualidade pedagógica;
3. aprendizagem;
4. qualidade operacional;
5. valor institucional;
6. qualidade das inferências.

Os quatro níveis de meta-avaliação — estudante, aula/unidade, implementação tecnológica e proposições do MAPES — permanecem distintos. Não foi criado escore agregado, limiar universal nem classificação institucional antes de validação.

## 5. Exemplo aplicado e piloto

O documento fundador contém exemplo completo do processo seguro de administração de medicamentos, com nós, relações, funções, relevância, tarefa cognitiva, ancoragens para Saúde, Engenharia, Administração e Direito e tarefa de transferência.

O documento fundador não contém protocolo de Neurovisão, cronograma T0–T3, número fixo de aulas, objetivos específicos de piloto ou alegação antecipada de comprovação. Neurovisão permanece apenas como exemplo ilustrativo fora do documento fundador e como backlog de pesquisa separado.

O backlog registra viabilidade, aceitabilidade, usabilidade, engajamento, aprendizagem, retenção, transferência, fidelidade, custos, equidade, precisão das inferências, resistência/aceitação docente e os momentos T0, T1, T2 e T3.

## 6. Termos, fontes e referências

- A busca no corpus final não encontrou formulações obsoletas que definam o MAPES como teoria.
- A busca não encontrou menção à fonte intermediária de conciliação nem atribuição acadêmica a ela.
- A busca não encontrou nomenclatura obsoleta de versão ou caminho fora das entradas históricas dos changelogs.
- A ordem dos autores foi preservada.
- A comparação automatizada das citações parentéticas autor–ano entre a versão anterior e a v0.10.0 encontrou **zero grupos removidos e zero grupos acrescentados** no documento fundador, no plano de pesquisa e na revisão de literatura. As listas APA correspondentes foram preservadas.
- Os arquivos históricos de referência, binários e fontes de trabalho permanecem no repositório como acervo não normativo e não foram reescritos para simular conteúdo contemporâneo.

## 7. Índices, âncoras e referências cruzadas

- Sumários gerados nos dois PDFs: aprovados.
- Numeração de capítulos e apêndices nos PDFs: aprovada, sem prefixo duplicado.
- Links relativos entre documentos: aprovados.
- Caminhos de versão em README, scripts de geração, metadados e documentação final: atualizados para v0.10.0 e formação v0.1.1.
- Referências cruzadas entre documento fundador, Core, manual, Perfil Institucional, glossário, formação e backlog: verificadas.

## 8. Decisões deliberadamente não convertidas em resultado validado

Não há decisão normativa da v0.10.0 identificada como ausente. Permanecem em aberto, por determinação do próprio plano:

1. elaboração futura do protocolo completo do piloto de Neurovisão;
2. validação dos instrumentos, indicadores, limiares e critérios interpretativos;
3. eventual estudo de um escore agregado de qualidade, vedado antes de validação;
4. teste empírico das proposições, condições de contorno, critérios de fidelidade e critérios de revisão/refutação.

Esses itens são agenda de pesquisa, não falhas de implementação documental.

## 9. Pendências que exigem decisão ou validação humana

1. aprovação integral da v0.10.0 pelos autores;
2. confirmação da declaração CRediT;
3. revisão externa independente e conferência editorial final das referências APA;
4. definição de licença, repositório de publicação e DOI;
5. importação de teste dos arquivos RDF na versão de Zotero adotada;
6. desenho metodológico, aprovação ética quando aplicável, instrumentos e critérios do futuro piloto;
7. validação empírica do framework, do Core, das inferências e dos seis domínios de qualidade.

Os hashes finais de cada arquivo constam em `MANIFEST-SHA256.txt`; o manifesto não inclui a si próprio.
