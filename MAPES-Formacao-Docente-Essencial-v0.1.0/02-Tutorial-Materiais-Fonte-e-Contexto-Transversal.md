# Tutorial — Seleção e Preparação de Materiais-Fonte e Contexto Transversal

**Finalidade:** preparar entradas confiáveis para o planejamento de uma aula MAPES Essencial e para uso com ChatGPT ou Gemini.  
**Fontes prioritárias:** artigos e slides.  
**Nível de exigência:** operacional; não substitui revisão sistemática nem avaliação formal da evidência.

---

## 1. Produto deste tutorial

Ao final, você terá quatro objetos:

1. **inventário de fontes autorizadas**;
2. **versões preparadas de artigos e slides**;
3. **Fonte de Contexto Transversal da disciplina**;
4. **registro de cobertura, conflito e lacunas**.

## 2. Passo 1 — Delimite a aula antes de procurar mais material

Registre em cinco linhas:

- tema da aula;
- sistema, problema ou decisão central;
- produto esperado do estudante;
- duração;
- lugar da aula na disciplina.

Não amplie a bibliografia antes de saber que decisão ela precisa sustentar. Um pacote menor e coerente é mais útil do que uma coleção extensa sem função definida.

## 3. Passo 2 — Reúna o conjunto inicial

Comece com:

- a apresentação usada ou planejada pelo professor;
- um artigo central que sustenta o núcleo conceitual;
- até dois artigos adicionais quando cobrem relações, controvérsias ou aplicações necessárias;
- o plano da disciplina ou uma breve descrição do conteúdo transversal.

Para cada item, responda:

- Que parte da aula esta fonte sustenta?
- É fonte de conteúdo, exemplo, contexto, método, imagem ou controvérsia?
- Que parte importante não está coberta?
- O professor aceita que esta fonte seja usada pela IA?

## 4. Passo 3 — Defina fontes autorizadas

Crie uma lista explícita. Exemplo:

```markdown
## Fontes autorizadas

- Fonte A — `Aula_03_slides.pdf`: estrutura e exemplos escolhidos pelo professor.
- Fonte B — `Artigo_principal.pdf`: conceitos e relações nucleares.
- Fonte C — `Contexto_Transversal.md`: sistema comum da disciplina e vocabulário.

## Uso externo

- Conhecimento externo: não autorizado.
- Sugestões externas: permitidas apenas em seção separada, marcadas como não incorporadas.
```

Ao usar IA, não confunda “arquivo anexado” com “fonte autorizada”. Declare o papel de cada arquivo.

## 5. Passo 4 — Prepare os slides

Slides frequentemente contêm fragmentos, imagens sem descrição e referências implícitas. Antes de gerar materiais:

### 5.1 Faça um inventário rápido

| Faixa de slides | Função | Problema identificado |
|---|---|---|
| 1–3 | abertura e objetivo | objetivo não observável |
| 4–9 | conceitos | sequência sem relações |
| 10–14 | exemplo | caso aparece tarde |
| 15–18 | síntese | sem tarefa de transferência |

### 5.2 Crie uma versão textual mínima

Use um arquivo Markdown:

```markdown
# Fonte A — Slides da aula

## Slide 1 — Título
[texto]

## Slide 2 — Problema
[texto]

**Descrição da figura:** [uma ou duas frases escritas pelo professor]

**Nota do professor:** [apenas quando necessária para compreender o slide]
```

Você não precisa transcrever elementos decorativos. Descreva figuras quando elas carregam relações ou dados essenciais.

### 5.3 Preserve localização

Mantenha o número do slide. A rastreabilidade permite que a IA e o professor indiquem: `Fonte A, slide 8`.

### 5.4 Separe o que é nuclear do que é extensão

Marque cada bloco:

- `[N]` nuclear;
- `[H]` habilitador;
- `[C]` contextual;
- `[E]` extensão.

Essa marcação é provisória e deve ser revista após a definição da tarefa.

## 6. Passo 5 — Prepare os artigos

Não é necessário resumir integralmente cada artigo. Crie uma ficha curta:

```markdown
# Fonte B — Artigo principal

**Referência completa:**

**Papel na aula:**

**Trechos prioritários:**
- p. X — definição central;
- p. Y — relação ou mecanismo;
- p. Z — exemplo, limite ou controvérsia.

**Conceitos nucleares:**

**Relações relevantes:**

**Limites para esta aula:**

**Figuras ou tabelas necessárias:**
```

Use páginas, seções, tabelas ou identificadores que permitam localizar a afirmação. Evite pedir à IA que “use o artigo” sem indicar o que o torna relevante.

## 7. Passo 6 — Faça uma checagem simples de adequação

A oficina não exige análise formal da evidência. Use apenas perguntas de suficiência:

- A fonte é reconhecida ou aceita pelo professor para esta aula?
- O conteúdo corresponde ao nível dos estudantes?
- A fonte sustenta a relação ou afirmação que será ensinada?
- A versão é suficientemente atual para o objetivo da aula?
- Existem conflitos com os slides ou com outra fonte?
- Há conteúdo que o professor considera obrigatório e não está documentado?

Quando a resposta for incerta, registre a incerteza. Não peça à IA para resolvê-la silenciosamente.

## 8. Passo 7 — Construa a Fonte de Contexto Transversal

### 8.1 O que ela é

É um documento comum a várias aulas que define o conteúdo-base da disciplina. Sua função é preservar continuidade. Ela pode ser usada pelo professor, pelos estudantes e por agentes de IA.

### 8.2 O que ela não é

- não é o plano de ensino completo;
- não é um repositório de todas as leituras;
- não é um resumo de cada aula;
- não deve impor a mesma âncora a todos os tópicos;
- não substitui as fontes específicas.

### 8.3 Estrutura recomendada

```markdown
# Fonte de Contexto Transversal — [Disciplina]

## 1. Pergunta ou problema central

## 2. Sistema e fronteira da disciplina

## 3. Componentes e relações que atravessam várias aulas

## 4. Vocabulário nuclear

## 5. Critérios comuns de análise, decisão ou qualidade

## 6. Como as aulas se conectam

## 7. Invariantes
[O que não deve mudar entre exemplos, públicos ou aulas]

## 8. Limites e exclusões

## 9. Fontes e versão
```

### 8.4 Procedimento de construção

1. Liste os temas de quatro a oito aulas próximas.
2. Circule os conceitos e relações que reaparecem.
3. Identifique o problema ou sistema que os conecta.
4. Escreva uma fronteira: o que a disciplina cobre e o que não cobre.
5. Selecione de cinco a doze termos nucleares.
6. Registre critérios comuns de decisão ou interpretação.
7. Descreva a relação da aula atual com a anterior e a posterior.
8. Cite as fontes usadas.
9. Mantenha o documento curto.
10. Revise quando uma aula revelar lacuna ou contradição.

### 8.5 Teste de qualidade

A Fonte de Contexto Transversal está adequada quando permite responder:

- Por que esta aula pertence à disciplina?
- Que conhecimento anterior ela mobiliza?
- Que relação prepara para aulas posteriores?
- Que conceitos devem permanecer invariáveis?
- Que exemplos podem mudar sem alterar o núcleo?

## 9. Passo 8 — Registre cobertura, conflitos e lacunas

Use três listas:

```markdown
## Cobertura suficiente
- [tópico] — Fonte A, slides 4–8; Fonte B, pp. 2–4.

## Possíveis conflitos
- [descrição] — Slides usam X; artigo usa Y. Professor deve decidir.

## O que está faltando
- [item] — necessário para [decisão/tarefa]. Solicitar [material ou esclarecimento].
```

O registro de lacunas não é falha. É um mecanismo de rigor.

## 10. Passo 9 — Execute a auditoria com IA

Use o Prompt 1 do arquivo `04-Prompts-ChatGPT-Gemini-MAPES-Essencial.md`.

A saída esperada deve conter:

- tópicos sustentados;
- tópicos apenas parciais;
- conflitos;
- lacunas;
- proposta inicial de sistema e relações;
- perguntas objetivas ao professor;
- rastreabilidade.

Não solicite ainda notas de aula, questões ou slides novos.

## 11. Passo 10 — Aprove antes de produzir

Revise a auditoria e escreva uma autorização explícita, por exemplo:

> A auditoria está aprovada com estas correções: [...]. Pode prosseguir para a produção, usando somente as fontes autorizadas e preservando a rastreabilidade.

Comentários vagos não equivalem a aprovação. Se ainda há dúvida sobre escopo ou conteúdo, permaneça na etapa de análise.

## 12. Passo 11 — Produza em lotes pequenos

Em vez de pedir todos os materiais ao mesmo tempo:

1. solicite primeiro o Canvas, o grafo e a tarefa;
2. valide;
3. solicite notas ou roteiro de slides;
4. valide;
5. solicite questões, rubrica e feedback;
6. faça uma revisão integrada.

Produção em lotes reduz propagação de erros.

## 13. Erros frequentes

### Fontes excessivas

Efeito: a IA combina documentos sem saber sua precedência.  
Correção: atribua função e prioridade.

### Slides tratados como texto completo

Efeito: lacunas são preenchidas por inferência.  
Correção: acrescente notas mínimas e descrição de figuras essenciais.

### Artigo anexado sem localização

Efeito: baixa rastreabilidade e seleção arbitrária.  
Correção: marque páginas ou seções prioritárias.

### Contexto transversal genérico

Efeito: frases institucionais sem utilidade para a aula.  
Correção: explicite sistema, relações, critérios e vínculos entre aulas.

### Geração antes da auditoria

Efeito: material extenso construído sobre escopo incorreto.  
Correção: use o gate análise → aprovação → produção.

### Confiança excessiva na fluência

Efeito: o professor revisa estilo, mas não relações e gabaritos.  
Correção: valide afirmação por afirmação nos pontos de maior impacto.

## 14. Checklist de conclusão

- [ ] A aula e seu produto foram delimitados.
- [ ] Cada fonte tem papel declarado.
- [ ] Slides essenciais foram textualizados ou descritos.
- [ ] Artigos têm trechos prioritários localizáveis.
- [ ] A Fonte de Contexto Transversal está disponível.
- [ ] Conteúdo nuclear, habilitador, contextual e de extensão foi distinguido.
- [ ] Conflitos e lacunas foram registrados.
- [ ] A IA executou uma auditoria antes da produção.
- [ ] O professor aprovou explicitamente o avanço.
- [ ] A produção foi revisada em lotes.
