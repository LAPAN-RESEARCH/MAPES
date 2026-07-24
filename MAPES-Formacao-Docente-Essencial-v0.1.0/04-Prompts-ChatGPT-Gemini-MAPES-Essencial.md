# Prompts para ChatGPT e Gemini — MAPES Essencial

**Objetivo:** apoiar o planejamento de uma aula sem substituir julgamento docente.  
**Princípios herdados do fluxo “Secretário-Geral”:** fontes autorizadas, anti-invenção, rastreabilidade, registro de lacunas e gate entre análise e produção.

---

# 1. Antes de usar

1. Abra uma conversa dedicada à aula.
2. Anexe ou cole somente materiais pertinentes.
3. Identifique cada fonte com um código: A, B, C.
4. Forneça a Fonte de Contexto Transversal.
5. Execute primeiro o prompt de auditoria.
6. Corrija a auditoria.
7. Autorize explicitamente a produção.
8. Gere um artefato por vez quando o conteúdo for complexo.
9. Faça revisão docente.

Não dependa de memória implícita da conversa para regras críticas. Repita fontes, escopo e restrições quando iniciar um novo artefato.

---

# 2. Prompt único — fluxo completo com gate docente

Copie e adapte:

```text
PAPEL
Atue como assistente de design educacional para uma aula de ensino superior baseada no MAPES Essencial. Você propõe alternativas e organiza informação, mas não é autoridade final. O professor valida conteúdo, objetivos, relações, gabaritos e uso em sala.

REGRA-MÃE
Não introduza conceitos, dados, exemplos, números, referências ou interpretações que não estejam explicitamente presentes nas fontes autorizadas. Quando algo necessário não estiver nas fontes, escreva “Lacuna nas fontes” e formule uma pergunta objetiva ao professor. Não complete silenciosamente.

FONTES AUTORIZADAS
- Fonte A: [arquivo e papel]
- Fonte B: [arquivo e papel]
- Fonte C: [Fonte de Contexto Transversal]

CONHECIMENTO EXTERNO
[não autorizado / autorizado apenas em seção separada de sugestões / autorizado com citação e validação]

CONTEXTO DA AULA
- Disciplina:
- Aula:
- Público:
- Duração:
- Resultado pretendido:
- Foco desejado pelo professor:

MAPES ESSENCIAL
A análise deve responder:
1. Qual sistema, problema ou decisão organiza a aula?
2. Quais relações e funções são indispensáveis?
3. O que o estudante fará com o conhecimento?
4. Qual entrada contextual é adequada?
5. Que tarefa ou produto demonstrará aprendizagem?
6. Como feedback, revisão e transferência ocorrerão?

ETAPA A — AUDITORIA
Produza somente:
1. cobertura claramente sustentada, com localização nas fontes;
2. conteúdo parcial ou ambíguo;
3. possíveis conflitos;
4. lacunas e perguntas ao professor;
5. proposta preliminar de sistema, fronteira, 5–9 elementos e relações tipadas;
6. funções, dependências e falhas sustentadas;
7. proposta provisória de relevância: nuclear, habilitadora, contextual ou extensão;
8. três opções de tarefa autêntica em nível de aplicação, análise, avaliação ou criação;
9. artefatos que podem ser gerados com segurança e artefatos que dependem de fonte adicional.

RASTREABILIDADE
Ao final de cada seção substantiva, indique as fontes e localizações usadas. Marque inferências como inferência.

GATE
Não produza notas, slides, questões, rubricas ou materiais finais. Termine perguntando se a Etapa A está aprovada. Só execute a Etapa B após autorização explícita do professor.

ETAPA B — APÓS APROVAÇÃO
Quando autorizado, produza somente o artefato solicitado, preserve rastreabilidade e inclua uma seção final “Pontos que exigem revisão docente”.
```

---

# 3. Prompt modular 1 — Auditoria de fontes

```text
Analise exclusivamente as fontes autorizadas abaixo para preparar uma aula MAPES Essencial.

Fontes:
[cole a lista e o papel de cada arquivo]

Contexto:
[disciplina, aula, público, duração e resultado pretendido]

Não gere materiais finais. Entregue uma tabela com:
- tópico ou relação;
- cobertura: completa, parcial, conflitante ou ausente;
- fonte e localização;
- implicação para a aula;
- pergunta objetiva ao professor, se necessária.

Depois proponha:
- sistema/problema e fronteira;
- 5–9 elementos;
- relações tipadas;
- funções e falhas sustentadas;
- itens nucleares, habilitadores, contextuais e de extensão.

Não use conhecimento externo. Marque qualquer inferência. Ao final, aguarde aprovação docente.
```

## Saída esperada

Uma auditoria curta, não uma aula. Se o modelo produzir conteúdo final, interrompa e reforce o gate.

---

# 4. Prompt modular 2 — Blueprint/grafo e Teleonomia

Use somente após validar as fontes.

```text
Com base exclusivamente nas fontes autorizadas e na auditoria aprovada, proponha um Blueprint funcional para a aula.

Entregue:
1. sistema e fronteira;
2. 5–9 nós, cada um com fonte;
3. relações tipadas e direcionadas quando aplicável;
4. função de cada elemento no nível analisado;
5. dependências, variações ou falhas;
6. classificação de relevância com justificativa;
7. representação textual do grafo;
8. três perguntas que obriguem o estudante a usar o grafo.

Restrições:
- não use linhas sem nome;
- não atribua intenção ao sistema;
- não acrescente relação ausente nas fontes;
- marque relações propostas pelo modelo como “inferência a validar”;
- use rastreabilidade por item.
```

---

# 5. Prompt modular 3 — Taxonomia Acelerada e tarefa autêntica

```text
Com base no Blueprint aprovado, crie três alternativas de tarefa autêntica para esta aula.

Cada alternativa deve incluir:
- situação e papel do estudante;
- decisão, explicação ou produto;
- relações do grafo mobilizadas;
- operação cognitiva dominante e justificativa além do verbo de Bloom;
- dados e restrições;
- fundamentos que podem ser fornecidos just-in-time;
- scaffolds para estudantes iniciantes;
- três critérios de avaliação;
- feedback formativo;
- variante de transferência;
- risco de o estudante acertar por reconhecimento superficial.

A tarefa deve aparecer cedo na aula e orientar a necessidade dos fundamentos. Não elimine conhecimentos básicos. Não use conteúdo fora das fontes autorizadas. Apresente as alternativas para decisão docente; não escolha por mim.
```

---

# 6. Prompt modular 4 — Ancoragem Contextual

```text
Proponha até três pontos de entrada para o conteúdo desta aula, usando apenas situações e repertórios sustentados pelas fontes ou informados pelo professor.

Para cada âncora, descreva:
1. conhecimento ou prática de partida;
2. correspondência com o conceito disciplinar;
3. vocabulário de transição;
4. limites da analogia;
5. formulação disciplinar de destino;
6. atividade de desancoragem;
7. tarefa de transferência para contexto diferente;
8. como manter os mesmos critérios de qualidade.

Não estereotipe estudantes por profissão, curso ou grupo. Se o repertório não estiver documentado, declare a incerteza.
```

---

# 7. Prompt modular 5 — Produção de artefato

Execute após a aprovação explícita da Etapa A e das decisões centrais.

```text
A Etapa A está aprovada com estas correções:
[cole correções]

Produza o seguinte artefato:
[notas de estudo / roteiro de slides / quiz / atividade prática / rubrica / guia de consulta]

Requisitos:
- público e duração: [inserir];
- use somente as fontes autorizadas;
- preserve os links existentes;
- organize o conteúdo pelo sistema, relações, funções e tarefa;
- inclua a tarefa autêntica no ponto definido;
- use linguagem acadêmica acessível;
- não crie número, referência ou exemplo ausente;
- ao final de cada seção substantiva, indique a rastreabilidade;
- termine com “Pontos que exigem revisão docente”.

Formato específico:
[descreva seções e extensão desejadas]
```

## Sugestões de artefatos simples

- notas de estudo de 2–4 páginas;
- roteiro de 8–12 slides;
- 5 questões com gabarito comentado;
- uma atividade prática;
- rubrica de três critérios;
- mapa textual com descrição acessível.

---

# 8. Prompt modular 6 — Auditoria da saída

```text
Atue como auditor crítico do artefato abaixo. Compare-o com as fontes autorizadas, o Canvas MAPES e a tarefa aprovada.

Verifique:
1. afirmações sem fonte;
2. relações inventadas ou deformadas;
3. finalismo indevido;
4. confusão entre relevância e complexidade cognitiva;
5. tarefas que apenas reproduzem texto;
6. desalinhamento entre objetivo, tarefa, critério e gabarito;
7. âncora que não conduz à abstração;
8. distratores incorretos ou ambíguos;
9. barreiras de acessibilidade;
10. conteúdo redundante ou sem função;
11. pontos que exigem julgamento docente.

Entregue uma tabela:
- trecho ou item;
- tipo de problema;
- fonte pertinente;
- gravidade: alta, média ou baixa;
- correção sugerida;
- decisão que deve permanecer humana.

Não reescreva tudo antes de apresentar o diagnóstico.
```

---

# 9. Prompt curto para verificar alinhamento

```text
Verifique o alinhamento entre estes quatro elementos:
1. resultado de aprendizagem;
2. tarefa do estudante;
3. evidência produzida;
4. critérios de avaliação.

Para cada desalinhamento, explique por que a evidência não permite julgar o resultado e proponha duas alternativas. Use somente as fontes e decisões fornecidas. Não altere o objetivo sem sinalizar.
```

---

# 10. Prompt curto para reduzir sobrecarga

```text
Revise este material para reduzir sobrecarga sem remover relações essenciais.

Classifique cada elemento como nuclear, habilitador, contextual ou extensão. Recomende:
- manter no fluxo principal;
- transformar em consulta;
- mover para outra aula;
- remover.

Justifique cada decisão em função da tarefa e do Blueprint. Não simplifique conceitos nucleares nem omita incertezas relevantes.
```

---

# 11. Revisão humana obrigatória

Aprovado pela IA não significa aprovado pelo professor. Antes do uso, confirme:

- [ ] fontes e localizações;
- [ ] precisão das relações;
- [ ] função e condições;
- [ ] tarefa e critérios;
- [ ] gabaritos;
- [ ] nível de desafio;
- [ ] linguagem;
- [ ] acessibilidade;
- [ ] vieses;
- [ ] dados pessoais e direitos de uso;
- [ ] versão final.

Para avaliações de alto impacto, faça revisão adicional e não use decisão automatizada exclusiva.
