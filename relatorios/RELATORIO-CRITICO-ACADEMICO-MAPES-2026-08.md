# Relatório crítico-acadêmico do framework MAPES

**Data:** 1º de agosto de 2026  
**Escopo:** análise documental do repositório `edu-mapes-framework`  
**Objeto:** consistência conceitual, rigor metodológico, fundamentação teórica, governança documental, ética e prioridades de desenvolvimento

## 1. Visão geral

O repositório apresenta o MAPES — Método de Aprendizagem por Estruturação Sistêmica — como um framework educacional abrangente, organizado por documentos conceituais, normativos, operacionais, institucionais e de pesquisa. A arquitetura documental inclui uma formulação fundacional do método, manual de implementação, especificação do MAPES Core, glossário normativo, perfil institucional, registro de decisões, plano de pesquisa, revisão sistematizada da literatura, relatório de garantia da qualidade e materiais de formação docente.

A principal virtude do conjunto é a tentativa explícita de separar definição conceitual, regras normativas, implementação, governança e agenda de validação. Essa separação reduz a ambiguidade típica de propostas educacionais que misturam fundamentos, procedimentos e alegações de eficácia. O repositório também demonstra consciência epistemológica ao reconhecer que o MAPES ainda não foi validado empiricamente como sistema integrado e ao tratar suas formulações como passíveis de teste, revisão e refutação.

Entretanto, a maturidade documental não deve ser confundida com evidência de efetividade. O material disponível sustenta a existência de um programa de pesquisa e desenvolvimento metodologicamente estruturado, mas não sustenta, por si só, afirmações sobre impacto em aprendizagem, permanência, equidade, desempenho docente ou eficiência institucional. Esses efeitos permanecem como hipóteses e objetivos de investigação.

A organização geral também é prejudicada por redundâncias entre documentos canônicos e por sobreposição entre materiais de formação, templates, prompts e artefatos específicos de aplicação. Além disso, permanece na raiz do repositório um plano histórico de trabalho cuja própria redação determina que ele deveria ser eliminado após a consolidação do MAPES. Sua permanência contradiz o estado unificado atual do framework e cria risco de interpretação histórica indevida.

## 2. Redundâncias e problemas de arquitetura documental

### 2.1 Redundâncias entre documentos canônicos

O documento fundacional, o manual de implementação, a especificação do MAPES Core, o glossário e o registro de decisões repetem definições, componentes, níveis de implementação, critérios de qualidade, princípios de governança e requisitos de rastreabilidade. Parte dessa repetição é funcional, pois diferentes públicos necessitam de diferentes graus de detalhe. Contudo, o repositório não dispõe de um mecanismo suficientemente claro para identificar qual documento é a fonte normativa primária de cada conceito.

A ausência de uma fonte canônica única e estruturada aumenta o risco de divergência semântica. Por exemplo, definições de construtos, componentes do Core, níveis de implementação e domínios de qualidade aparecem em múltiplos arquivos. Uma alteração em apenas um deles pode gerar versões inconsistentes sem que o problema seja detectado por revisão humana comum.

Recomenda-se transformar os elementos normativos centrais em uma fonte estruturada e versionada — por exemplo, YAML, JSON ou TOML — da qual glossário, tabelas, matrizes e trechos repetitivos possam ser gerados. Os documentos narrativos permaneceriam necessários, mas deixariam de ser autoridades concorrentes.

### 2.2 Redundâncias operacionais

Os materiais de formação docente incluem templates, prompts, auditorias, gates, fluxos de trabalho e instrumentos de apoio que reproduzem parcialmente o conteúdo do manual e do MAPES Core. Há valor pedagógico na tradução de conceitos abstratos para procedimentos concretos, mas a fronteira entre especificação do método e material instrucional não está plenamente controlada.

O problema se acentua quando materiais específicos de uma disciplina ou de um agente de IA são mantidos próximos a componentes reutilizáveis do framework. Um prompt operacional pode incorporar decisões contextuais legítimas, mas não deve adquirir autoridade normativa sobre o MAPES. O próprio material de integração reconhece a necessidade de evitar duplicação documental; a estrutura do repositório deve aplicar esse princípio de modo mais rigoroso.

### 2.3 Artefato histórico incompatível com o estado atual

O arquivo `conciliation-plan.md` permanece na raiz do repositório, embora seu próprio conteúdo determine que a proposta intermediária deveria ser incorporada, eliminada e não tratada como fonte separada após a consolidação. A manutenção desse arquivo constitui uma falha de conteúdo e de governança documental.

O problema não é apenas terminológico. Sua presença sugere que existem versões conceitualmente concorrentes, quando o estado vigente é um MAPES único. Além disso, o relatório de QA ainda registra uma verificação relacionada à antiga etapa histórica, reforçando uma distinção que não deve integrar a documentação atual.

A correção prioritária é remover o arquivo da árvore principal ou, caso exista necessidade legal de preservação, transferi-lo para um histórico não normativo claramente segregado, sem referências nos documentos vigentes. O relatório de QA deve ser atualizado para avaliar apenas a coerência interna do MAPES atual.

## 3. Rigor metodológico

O plano de pesquisa é um dos componentes mais fortes do repositório. Ele apresenta problema, objetivos, perguntas de pesquisa, fases de desenvolvimento, participantes, métodos mistos, instrumentos propostos, análise quantitativa e qualitativa, estratégias de implementação, riscos e critérios para uma versão estável. A abordagem demonstra compreensão de que um framework educacional complexo requer desenvolvimento iterativo, validação de construtos, avaliação de implementação e investigação de resultados.

A proposição de estudos mistos, análises de validade, medidas de fidelidade, avaliação dos processos de implementação e atenção a inferência causal é metodologicamente adequada. Também é positiva a distinção entre implementação essencial, expandida e institucional, pois permite estudar dose, fidelidade e adaptação sem tratar o método como uma intervenção monolítica.

Apesar disso, o conteúdo é predominantemente prospectivo. Não foram identificados, no material analisado, protocolos preregistrados, bancos de dados de estudos concluídos, instrumentos validados, resultados de análises psicométricas, relatórios de ensaios, pareceres éticos ou sínteses empíricas que permitam avaliar a efetividade do framework. Não verificável a partir do conteúdo fornecido do repositório.

A revisão da literatura é corretamente descrita como revisão sistematizada de escopo, não como revisão sistemática plena. O documento reconhece ausência de registro prévio, dupla triagem independente, arquivo completo de deduplicação e outros controles. Essa transparência é adequada, mas limita a força inferencial da revisão. O corpus de referências apoia a plausibilidade teórica dos componentes, porém não demonstra a superioridade ou a originalidade empírica do arranjo integrado.

Para elevar o rigor, o repositório deveria incluir protocolo reproduzível de busca e seleção, estratégia completa por base, datas de execução, exportações bibliográficas, registros de deduplicação, fluxograma PRISMA, extração padronizada e avaliação crítica da qualidade dos estudos. A agenda empírica também precisa distinguir claramente estudos de desenvolvimento, validade, implementação, eficácia e efetividade.

## 4. Fundamentação teórica e relação com a literatura

O MAPES articula aprendizagem sistêmica, teleonomia, taxonomias de aprendizagem, ancoragem contextual, metacognição, avaliação, governança e desenho instrucional. A amplitude é intelectualmente produtiva, mas eleva a carga de demonstração: quanto mais componentes são reunidos, maior a necessidade de explicitar os mecanismos causais e a contribuição incremental de cada elemento.

A documentação demonstra consciência desse problema ao tratar a originalidade como questão a ser demonstrada, não presumida. Essa postura deve ser preservada. A contribuição científica potencial do MAPES não está necessariamente em cada componente isolado, muitos dos quais possuem antecedentes consolidados, mas na arquitetura de integração, rastreabilidade e governança que os articula.

Essa hipótese de contribuição precisa ser submetida a testes discriminantes. O framework deve demonstrar que seus construtos não são apenas novos nomes para dimensões já cobertas por desenho reverso, alinhamento construtivo, aprendizagem baseada em problemas, design-based research, avaliação autêntica, ciência da implementação ou melhoria contínua. Também é necessário testar se a combinação produz ganhos mensuráveis acima de intervenções mais simples.

Uma estratégia adequada seria construir uma matriz comparativa de construtos, mecanismos, artefatos, decisões e resultados esperados em relação a frameworks adjacentes. Posteriormente, estudos de ablação poderiam avaliar quais componentes são necessários, suficientes ou redundantes. Sem esse tipo de comparação, a coerência interna pode ser demonstrada, mas a contribuição específica permanece parcialmente indeterminada.

## 5. Recomendações priorizadas

1. **Prioridade crítica — remover referências históricas incompatíveis com o MAPES atual.** Excluir `conciliation-plan.md` da documentação vigente e revisar o relatório de QA para eliminar a antiga distinção histórica.

2. **Prioridade crítica — instituir uma fonte normativa única.** Consolidar construtos, definições, níveis, componentes, domínios de qualidade e regras do Core em formato estruturado, com geração automática dos trechos derivados.

3. **Prioridade alta — publicar um mapa de autoridade documental.** Indicar, para cada arquivo, sua finalidade, público, status, autoridade normativa, dependências e relação com versões anteriores.

4. **Prioridade alta — tornar a revisão de literatura reproduzível.** Registrar protocolo, bases, estratégias completas, exportações, deduplicação, seleção, extração, avaliação crítica e fluxo PRISMA.

5. **Prioridade alta — separar programa de pesquisa de evidência disponível.** Criar uma página de estado da evidência que diferencie hipóteses, estudos planejados, estudos em andamento, resultados preliminares e resultados publicados.

6. **Prioridade alta — desenvolver e validar instrumentos.** Publicar versões, manuais de aplicação, evidências de validade, precisão, invariância, sensibilidade à mudança e critérios interpretativos.

7. **Prioridade média — formalizar o desenho de pesquisa baseado em design.** Definir ciclos, critérios de mudança, registros de decisão, dados utilizados, participação dos atores e regras para estabilização do framework.

8. **Prioridade média — testar validade discriminante e contribuição incremental.** Comparar o MAPES com frameworks adjacentes e conduzir estudos de componentes ou ablação.

9. **Prioridade média — reduzir duplicação nos materiais de formação.** Manter templates e prompts como aplicações derivadas, com links para as normas canônicas em vez de reproduzi-las integralmente.

10. **Prioridade média — fortalecer publicação e preservação.** Definir licença, política de citação, DOI por versão estável, changelog semântico, política de depreciação e arquivamento de artefatos não normativos.

## 6. Ética, direitos e governança

A documentação ética é conceitualmente forte. O plano de pesquisa e o perfil institucional abordam proteção de dados, LGPD, controle de acesso, retenção, contestação, revisão humana, riscos, equidade e direitos dos participantes. O MAPES Core incorpora risco e direitos como dimensões da decisão educacional, o que evita tratar ética como apêndice administrativo.

Todavia, princípios normativos não equivalem a capacidade operacional. Não foram identificados pacotes completos de consentimento, modelos de avaliação de impacto, procedimentos de resposta a incidentes, matriz de responsabilidades, termos de governança de dados, critérios de anonimização, planos de auditoria ou pareceres de comitês de ética. Não verificável a partir do conteúdo fornecido do repositório.

Recomenda-se criar um pacote ético-operacional versionado, com modelos adaptáveis e separação clara entre requisitos institucionais, requisitos de pesquisa e boas práticas recomendadas. Para aplicações com sistemas automatizados, devem ser documentados os limites de uso, revisão humana, contestabilidade, rastreabilidade das decisões, monitoramento de vieses e proibição de decisões de alto impacto baseadas exclusivamente em modelos automatizados.

## 7. Síntese final

O repositório MAPES apresenta um framework conceitualmente ambicioso, com documentação acima da média para um projeto educacional em desenvolvimento. Seus pontos fortes são a explicitação de decisões, a separação entre níveis de implementação, a especificação do Core, a integração entre qualidade, risco e direitos, a postura falibilista e a existência de uma agenda de pesquisa abrangente.

As fragilidades principais são a ausência de validação empírica do sistema integrado, a natureza ainda limitada da revisão de literatura, a inexistência verificável de instrumentos validados, a redundância entre documentos e a permanência de um artefato histórico que contradiz a unificação atual do framework.

O MAPES deve, portanto, ser apresentado como framework documentado e programa de pesquisa em processo de validação, não como método de eficácia já demonstrada. A próxima etapa de maturidade não depende de ampliar a retórica ou multiplicar artefatos, mas de reduzir ambiguidade normativa, tornar a revisão reproduzível, operacionalizar ética e governança, validar instrumentos e produzir evidência empírica comparativa. Com essas correções, o projeto poderá converter uma arquitetura conceitual promissora em contribuição científica e institucional verificável.
