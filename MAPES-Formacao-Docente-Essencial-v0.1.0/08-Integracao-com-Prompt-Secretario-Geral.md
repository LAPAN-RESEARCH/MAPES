# Integração com o Prompt “Secretário-Geral”

## 1. Finalidade

O Prompt “Secretário-Geral” foi desenvolvido para coordenar fontes, decisões, notas de aula e artefatos da disciplina de Neurovisão. Este pacote de formação não o substitui. Ele prepara o docente para fornecer entradas mais claras e revisar suas saídas.

A adaptação genérica preserva cinco mecanismos:

1. fontes autorizadas;
2. anti-invenção;
3. rastreabilidade;
4. registro de lacunas;
5. gate entre auditoria e produção.

## 2. Correspondência entre produtos da oficina e o fluxo operacional

| Produto da formação | Campo ou função no Secretário-Geral |
|---|---|
| Briefing da aula | identificação, foco desejado e dados mínimos |
| Inventário de fontes | inputs recebidos e fontes autorizadas |
| Fonte de Contexto Transversal | Fonte de Contexto Comum da disciplina |
| Registro de cobertura | cobertura do conteúdo |
| Registro de conflitos | checagem de consistência |
| Registro de lacunas | “O que está faltando nas fontes” |
| Canvas MAPES Essencial | orientação pedagógica para a aula |
| Auditoria com IA | Etapa A — Registro Operacional |
| Aprovação explícita | gate A → B |
| Artefato produzido | Etapa B |
| Registro de IA | rastreabilidade, revisão e versão |
| Avaliação/meta-avaliação | avaliação da aula e revisão |

## 3. Fluxo recomendado

```text
Professor seleciona a aula
→ prepara fontes
→ cria/atualiza Contexto Transversal
→ preenche Canvas MAPES Essencial
→ envia inputs ao Secretário-Geral
→ recebe Etapa A
→ corrige e aprova
→ recebe Etapa B
→ revisa artefatos
→ aplica
→ registra resultados e modifica a versão
```

## 4. Elementos específicos que não devem ser generalizados automaticamente

O prompt original contém elementos fixos da Neurovisão, como olho humano, processamento visual, Tríade Funcional da Visão, classes do sistema visual e propedêutica neurofuncional. Em outra disciplina, esses elementos devem ser substituídos por uma Fonte de Contexto Transversal validada pelo docente.

Não faça substituição automática por analogia. O professor deve definir:

- o sistema central;
- os constructos disciplinares;
- o vocabulário normativo;
- critérios de validade;
- relações transversais;
- limites de contextualização.

## 5. Elementos reutilizáveis sem mudança conceitual

- regra-mãe anti-invenção;
- precedência das fontes;
- dados mínimos para iniciar;
- separação entre modo operacional e editorial;
- cobertura, conflito e lacunas;
- gate de aprovação;
- produção por artefato;
- rastreabilidade por seção;
- nomenclatura e versionamento;
- revisão docente.

## 6. Como preparar um mini-prompt para uma aula

```text
Aula/Título:
Professor:
Data:
Público e duração:
Resultado pretendido:
Fontes específicas:
Fonte de Contexto Transversal:
Foco desejado:
Conhecimento externo: autorizado/não autorizado
Artefato desejado após aprovação:
```

## 7. Gate adequado

A resposta “parece bom” pode ser ambígua. Use uma autorização clara:

> A Etapa A está aprovada com as correções registradas. Pode prosseguir para a Etapa B e produzir [artefato], usando somente as fontes autorizadas.

Se houver comentário sem autorização inequívoca, continue na Etapa A.

## 8. Evite duplicação documental

Não copie integralmente o Canvas, o briefing e o registro do Secretário-Geral em três arquivos diferentes. Uma implementação enxuta pode:

- usar o Briefing como mini-prompt;
- anexar a Fonte de Contexto Transversal;
- receber a Etapa A como registro de cobertura e lacunas;
- registrar no Template 5 apenas as correções e a decisão final.

## 9. Limite de responsabilidade

O Secretário-Geral organiza e gera. O docente continua responsável por:

- validade disciplinar;
- seleção e precedência de fontes;
- objetivos;
- equivalência entre grupos;
- avaliação;
- privacidade;
- acessibilidade;
- decisão de publicação e uso.
