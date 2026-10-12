# Registro de eventos e decisões

Registre eventos de trabalho e decisões relevantes em ordem sequencial usando identificadores `DEC-00X`. Não reutilize IDs nem apague entradas anteriores; corrija por meio de uma nova entrada que referencie a anterior. Cada registro deve explicar o contexto e o efeito no projeto.

## Registros

### DEC-001 — Fluxo de landing page em sete etapas

- **Registrado em:** 2026-10-11
- **Evento/decisão:** Adotado um fluxo sequencial com levantamento de requisitos, planejamento, UX/UI, desenvolvimento, QA, revisão/aprovação e deploy.
- **Contexto:** O usuário definiu que deseja executar o trabalho por etapas, revisar entregáveis e orientar o avanço.
- **Efeito:** O fluxo foi documentado em `plans/FLUXO-LANDING-PAGE.md`; as regras gerais ficam em `AGENTS.md`.

### DEC-002 — Papéis especializados como perfis de agente

- **Registrado em:** 2026-10-11
- **Evento/decisão:** Definidos oito perfis: Product Owner, Analista de Requisitos, UX Designer, UI Designer, Desenvolvedor Frontend, QA Tester, Tech Lead e DevOps.
- **Contexto:** O usuário solicitou responsabilidades específicas para os agentes que participam das etapas.
- **Efeito:** Os perfis TOML estão em `.codex/agents/`; cada arquivo descreve o comportamento do respectivo papel.

### DEC-003 — Skills organizadas por etapa do fluxo

- **Registrado em:** 2026-10-11
- **Evento/decisão:** Adotada uma Skill por etapa, com os agentes participantes, as instruções de trabalho, os entregáveis e o ponto de espera pela orientação do usuário.
- **Contexto:** O usuário aprovou o plano de preencher sete Skills alinhadas ao fluxo.
- **Efeito:** As Skills estão em `.agents/skills/`; a validação do `skill-creator` passou para as sete.

### DEC-004 — Registros contínuos em `docs/`

- **Registrado em:** 2026-10-11
- **Evento/decisão:** Criados `project-context.md`, `project-roadmap.md` e `decision-log.md`; sua atualização passa a ser obrigatória em toda tarefa que alterar o projeto.
- **Contexto:** O usuário pediu memorandos por feature, um roadmap vivo por etapa e registros sequenciais `DEC-00X` para acompanhar o trabalho e as decisões.
- **Efeito:** `AGENTS.md` agora exige consultar e atualizar esses registros antes de encerrar cada tarefa. A fundação atual foi documentada; o levantamento de requisitos da landing page permanece não iniciado.

### DEC-005 — Arquitetura progressiva de especificações

- **Registrado em:** 2026-10-11
- **Evento/decisão:** Inicializada a arquitetura de especificações de produto com descoberta incremental, rastreabilidade, ciclo de vida controlado e gates de aprovação humana.
- **Contexto:** O usuário solicitou que a descoberta comece sem requisitos previamente definidos, preserve artefatos por etapa em seus diretórios e registre aprovações antes de avançar.
- **Efeito:** Criados os artefatos em `specs/`; `AGENTS.md` e a Skill de levantamento apontam para o bootstrap. A Etapa 1 permanece `NOT_STARTED`, as demais `PENDING`, não há requisitos aprovados e nenhum gate está concedido. `specs/SPEC-001.md` permaneceu vazio e preservado.

### DEC-006 — MVP do orquestrador progressivo

- **Registrado em:** 2026-10-11
- **Evento/decisão:** Implementado um MVP local para avaliar e conduzir o workflow com especificações progressivas, estado persistente e aprovações humanas verificáveis.
- **Contexto:** A solicitação anexada pediu um ciclo determinístico de inspeção, avaliação, esclarecimento, execução controlada e validação, mantendo as etapas e os papéis já existentes como fonte de verdade.
- **Efeito:** Criados o pacote `orchestrator/`, a CLI, schema de workflow, configuração em dry-run, armazenamento SQLite e 20 testes. O bootstrap e os estados iniciais da landing page foram preservados; nenhuma especificação foi criada nem aprovada. A execução real do Codex permanece desabilitada; qualquer futuro deploy exige autorização explícita de escopo e versão.

### DEC-007 — Evidência obrigatória para requisito funcional verificável

- **Registrado em:** 2026-10-11
- **Evento/decisão:** Requisitos funcionais só contam como confirmados quando a linha contém uma descrição e uma evidência confirmada; referências ainda em formato de placeholder mantêm o requisito pendente.
- **Contexto:** A validação do MVP identificou que uma descrição de requisito sem origem registrada poderia ser tratada como suficiente para aprovar a especificação.
- **Efeito:** O resolvedor exige evidência não-placeholder para considerar o campo funcional completo; a coleta reutiliza somente requisitos com evidência. A suíte passou com 21 testes e `SPEC-001.md` continua vazio.

### DEC-008 — Contratos rastreáveis integrados ao orquestrador

- **Registrado em:** 2026-10-11
- **Evento/decisão:** Implementada uma camada de contratos operacionais e de produto com schemas, avaliação de Planning, geração por tarefa, revisão/aprovação humana vinculada a ID/versão/hash e validação integrada ao runtime.
- **Contexto:** A solicitação anexada definiu contratos reutilizáveis e verificáveis para entradas/saídas, escopo, dependências, resultados e handoffs, mantendo especificações, gates, autorizações e execução controlada existentes como fontes distintas.
- **Efeito:** Adicionados `contracts/` e `orchestrator/contracts/`; integrados `WorkflowEngine`, `StageController`, `DependencyValidator`, `QualityGate`, `ApprovalManager`, `StateManager`, `CodexExecutor` e a CLI. Planning exige a avaliação do Tech Lead mesmo quando não há contrato de produto. Revisões confirmadas em UX/UI podem criar versão nova e invalidam o gate de Planning até nova aprovação. As migrações SQLite são aditivas e preservam os registros existentes. `python -m compileall -q orchestrator tests` passou e `python -m unittest discover -s tests -v` passou com 43 testes. O estado do workflow, especificações e aprovações do projeto não foram resetados; nenhum processo Codex real nem deploy foi executado. Execução paralela, isolamento real de escopo e testes funcionais continuam fora do subsistema.

### DEC-009 — Guias de início do fluxo e da aplicação

- **Registrado em:** 2026-10-11
- **Evento/decisão:** Documentados os pontos de entrada para iniciar o fluxo de trabalho e para encontrar as futuras instruções de execução da aplicação.
- **Contexto:** O usuário pediu orientações claras para iniciar o trabalho do projeto e, separadamente, para iniciar a aplicação que será desenvolvida em `src/`.
- **Efeito:** `README.md` na raiz explica o fluxo no Codex e o uso básico do orquestrador; `src/README.md` reserva o guia de execução da aplicação. Comandos da aplicação permanecem pendentes da escolha e implementação da tecnologia no Planejamento. `AGENTS.md` orienta manter ambos atualizados.
