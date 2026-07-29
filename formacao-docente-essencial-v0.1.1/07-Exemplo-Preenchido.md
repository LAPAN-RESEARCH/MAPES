# Exemplo Didático Preenchido — Aula MAPES Essencial

> **Aviso:** este é um cenário fictício criado apenas para demonstrar o processo. As fontes A e B são simuladas e não devem ser utilizadas como conteúdo disciplinar real. Substitua-as por fontes autorizadas da sua área.

## 1. Identificação

- **Disciplina fictícia:** Análise de Processos e Riscos Aplicados
- **Aula:** Como localizar e priorizar pontos críticos de um processo
- **Público:** estudantes de graduação em área aplicada
- **Duração:** 90 minutos
- **Problema observado:** estudantes conhecem nomes de etapas, mas analisam falhas isoladamente e não consideram dependências ou feedback.

## 2. Fontes autorizadas simuladas

| ID | Fonte | Papel |
|---|---|---|
| A | Slides do professor, “Elementos de um processo” | vocabulário, sequência e exemplo |
| B | Texto do professor, “Análise de falhas” | relações, critérios e limites |
| C | Fonte de Contexto Transversal da disciplina | modelo comum de entrada, transformação, saída, controle e feedback |

**Conhecimento externo:** não autorizado.  
**Rastreabilidade:** fonte e slide/seção.  
**Lacunas:** devem ser apresentadas ao professor.

## 3. Fonte de Contexto Transversal — versão curta

### Pergunta central

Como representar um processo suficientemente bem para localizar falhas, explicar consequências e decidir onde intervir?

### Sistema e fronteira

A disciplina examina processos como combinações de entrada, transformação, saída, controle e feedback. Nesta unidade, fatores externos amplos e custos financeiros detalhados ficam fora da fronteira.

### Relações recorrentes

```text
Entrada --alimenta--> Transformação
Transformação --produz--> Saída
Controle --restringe/ajusta--> Transformação
Saída --é observada por--> Feedback
Feedback --informa--> Controle
```

### Vocabulário nuclear

- entrada;
- transformação;
- saída;
- controle;
- feedback;
- dependência;
- modo de falha;
- ponto crítico.

### Critérios comuns

- impacto sistêmico;
- propagação da falha;
- possibilidade de detecção;
- possibilidade de correção;
- qualidade da evidência disponível.

### Conexão com outras aulas

A aula recebe o conceito de processo da aula anterior e prepara a comparação de alternativas de intervenção da aula seguinte.

### Invariante

Os exemplos podem variar entre saúde, engenharia, Direito ou Administração, mas a análise deve explicitar fronteira, relações, critérios e incerteza.

## 4. Canvas MAPES Essencial

### 1. Sistema, problema ou decisão

**Pergunta organizadora:** Em qual ponto de um processo uma intervenção produziria maior redução de risco, considerando dependências e feedback?

**Fronteira:** processo focal entre a entrada inicial e o primeiro ciclo de feedback. Ficam fora custos de implementação e efeitos organizacionais de longo prazo.

### 2. Relações e funções indispensáveis

- a entrada condiciona o que pode ser transformado;
- a transformação produz a saída;
- o controle restringe ou ajusta a transformação;
- o feedback informa o controle;
- uma falha pode se propagar para etapas posteriores;
- detecção precoce pode limitar propagação.

### 3. Ação cognitiva do estudante

O estudante analisará um processo, comparará três pontos de falha e justificará uma prioridade de intervenção.

### 4. Entrada contextual

**Âncora:** um serviço de entrega fictício que recebe um pedido, separa um item, despacha, confirma o recebimento e corrige erros.

**Transição disciplinar:** substituir personagens e ações específicas pelas categorias entrada, transformação, saída, controle e feedback.

**Limite da analogia:** processos profissionais podem ter múltiplas saídas, controles distribuídos e consequências que não se reduzem à entrega de um produto.

### 5. Tarefa e evidência

**Produto:** mapa anotado e justificativa de até 300 palavras indicando o ponto prioritário de intervenção.

**Evidência:** uso correto das relações, consideração da propagação e comparação de alternativas.

### 6. Feedback, revisão e transferência

Os estudantes recebem um novo dado que altera a possibilidade de detecção. Eles revisam sua prioridade e, ao final, aplicam o modelo a um processo de outra área.

## 5. Blueprint/grafo da aula

### Nós

1. entrada;
2. transformação;
3. saída;
4. controle;
5. feedback;
6. falha de entrada;
7. falha de transformação;
8. falha de feedback.

### Relações tipadas

```text
Entrada --condiciona--> Transformação
Transformação --gera--> Saída
Controle --modula--> Transformação
Saída --gera evidência para--> Feedback
Feedback --ajusta--> Controle
Falha de entrada --propaga-se para--> Transformação
Falha de transformação --compromete--> Saída
Falha de feedback --impede correção de--> Controle
```

### Função e falha

| Elemento | Contribuição no sistema | Dependência | Quando falha |
|---|---|---|---|
| Entrada | fornece condição inicial | qualidade e completude | erro se propaga |
| Transformação | converte entrada em saída | entrada e controle | saída inadequada |
| Controle | mantém critérios | informação e regra | variação não corrigida |
| Feedback | informa desempenho | observação da saída | correção tardia ou ausente |

### Relevância

- **nuclear:** entrada, transformação, saída, controle, feedback;
- **habilitador:** conceito de dependência e propagação;
- **contextual:** exemplo do serviço de entrega;
- **extensão:** modelagem quantitativa de risco.

## 6. Tarefa autêntica simulada

### Situação

Um processo fictício apresenta três problemas possíveis:

- a entrada chega incompleta;
- a transformação varia sem um controle claro;
- o feedback chega tarde.

A equipe só consegue implementar uma intervenção inicial.

### Papel do estudante

Atuar como analista responsável por recomendar uma prioridade provisória.

### Materiais

- grafo do processo;
- três descrições de falha;
- critérios de impacto, propagação, detecção e correção;
- trecho das fontes A e B.

### Produto

1. selecionar um ponto prioritário;
2. explicar a cadeia de consequências;
3. comparar a alternativa escolhida com pelo menos outra;
4. declarar que informação adicional poderia mudar a decisão.

### Fundamentos just-in-time

Após a primeira tentativa, o professor apresenta:

- diferença entre falha local e propagada;
- função do feedback;
- critérios de comparação.

### Scaffolds

- grafo parcialmente preenchido;
- checklist de relações;
- exemplo de justificativa incompleta para crítica;
- frase inicial: “Priorizo X porque sua relação com Y...”

### Critérios

1. uso de relações do grafo;
2. comparação de alternativas;
3. justificação da decisão e reconhecimento de incerteza.

### Transferência

Cada estudante escolhe uma variante:

- saúde: processo de cuidado;
- engenharia: sistema de controle;
- Direito: fluxo de análise de um caso;
- Administração: processo de atendimento.

A variante não altera os critérios.

## 7. Estrutura da aula de 90 minutos

| Tempo | Ação | Função MAPES |
|---:|---|---|
| 0–8 min | apresentar problema e primeira decisão | Taxonomia Acelerada |
| 8–18 min | tentativa individual e comparação em dupla | ativação e diagnóstico |
| 18–30 min | apresentar Blueprint/grafo | arquitetura |
| 30–42 min | discutir função, dependência e falha | Teleonomia |
| 42–55 min | fornecer fundamentos just-in-time | scaffolding |
| 55–70 min | revisar decisão com novo dado | feedback |
| 70–82 min | transferir para outra área | Ancoragem e transferência |
| 82–90 min | síntese e pergunta de saída | avaliação |

## 8. Exemplo de auditoria com IA

### Prompt resumido

> Audite as fontes A, B e C. Não gere a aula. Identifique cobertura, conflitos, lacunas, sistema, relações e três opções de tarefa. Use rastreabilidade.

### Saída simulada da auditoria

- **Cobertura suficiente:** categorias de processo e relações básicas — Fonte A, slides simulados 3–8; Fonte C, seção “Relações recorrentes”.
- **Cobertura parcial:** critérios de priorização — Fonte B menciona impacto e detecção, mas não define pesos.
- **Lacuna:** não há regra para escolher quando critérios entram em conflito.
- **Pergunta ao professor:** a tarefa deve exigir decisão qualitativa ou haverá uma matriz de pesos?
- **Inferência a validar:** tratar atraso de feedback como falha distinta do controle.

### Correções docentes

1. manter decisão qualitativa, sem pesos;
2. definir feedback tardio como informação insuficiente para controle, não como controle defeituoso;
3. remover linguagem de “otimização”, ausente nas fontes.

### Gate

> Auditoria aprovada com as correções acima. Pode gerar um roteiro de dez slides e cinco questões formativas.

## 9. Roteiro resumido de slides gerado e revisado

1. pergunta organizadora;
2. cenário inicial;
3. primeira decisão;
4. sistema e fronteira;
5. grafo do processo;
6. função de controle e feedback;
7. propagação de falhas;
8. critérios de comparação;
9. revisão da decisão;
10. transferência e síntese.

**Alteração docente principal:** o caso foi movido do slide 8 para o slide 2, para que a tarefa organize a exposição.

## 10. Avaliação da aprendizagem

### Diagnóstico

Indicar, no grafo incompleto, onde começaria a investigar e por quê.

### Formativa

Revisar a prioridade após receber novo dado sobre detecção.

### Final

Entregar mapa anotado e justificativa.

### Transferência

Aplicar o modelo a um processo de outra área e indicar uma relação que precisaria ser modificada.

### Experiência do estudante

1. O grafo ajudou a acompanhar a aula?
2. Em que momento a tarefa ficou mais clara?
3. Que apoio faltou?
4. Que elemento poderia ser removido?

## 11. Meta-avaliação docente esperada

- O mapa foi usado na justificativa ou apenas reproduzido?
- Estudantes compararam alternativas?
- O exemplo familiar facilitou entrada sem limitar transferência?
- O novo dado produziu revisão real?
- O roteiro de slides ficou mais curto?
- A IA reduziu preparação ou exigiu correções extensas?

## 12. Como adaptar este exemplo

Substitua:

- o processo genérico pelo sistema real;
- as fontes simuladas por fontes autorizadas;
- as relações abstratas por relações disciplinares;
- os critérios genéricos por critérios válidos no domínio;
- as variantes de transferência por situações plausíveis da formação.

Preserve o fluxo:

```text
fontes → contexto transversal → auditoria → Canvas → tarefa → produção → revisão → avaliação
```
