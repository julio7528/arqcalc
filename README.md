# ArqCalc

Repositório do projeto ArqCalc. O ambiente de trabalho está preparado, mas os requisitos e a tecnologia da aplicação ainda serão definidos durante o fluxo do projeto.

## Como iniciar o trabalho

Abra o repositório na raiz no Codex e solicite:

> Inicie somente a Etapa 1 — Levantamento de requisitos.

O Codex deve seguir [`AGENTS.md`](AGENTS.md), [`specs/INIT.md`](specs/INIT.md) e a Skill de [levantamento de requisitos](.agents/skills/requirements-discovery/SKILL.md). A conversa acontece em etapas: o usuário responde às perguntas, revisa o briefing e decide explicitamente se aprova e autoriza o Planejamento. Requisitos não confirmados ficam como perguntas em aberto.

O processo completo, os responsáveis e os entregáveis estão em [`plans/FLUXO-LANDING-PAGE.md`](plans/FLUXO-LANDING-PAGE.md). O estado atual de cada etapa está em [`docs/project-roadmap.md`](docs/project-roadmap.md); decisões e mudanças relevantes ficam em [`docs/decision-log.md`](docs/decision-log.md).

## Como usar o orquestrador

O orquestrador local registra respostas, especificações, aprovações e o estado do fluxo. Requer Python 3.11 ou superior. Na raiz do repositório:

```powershell
python -m pip install -r requirements.txt
python -m orchestrator status
python -m orchestrator discover
```

`discover` conduz a coleta interativa dos campos de requisitos ainda sem confirmação. Ele não inicia agentes independentes. A execução real do Codex permanece desabilitada e `run` opera em dry-run por padrão. Consulte [`orchestrator/README.md`](orchestrator/README.md) antes de usar os demais comandos de aprovação, avanço ou execução.

## Aplicação

O código da aplicação ficará em [`src/`](src/). As instruções para instalar, executar, testar e compilar a aplicação ficarão em [`src/README.md`](src/README.md) e serão completadas depois que o Planejamento definir a tecnologia e os comandos disponíveis.

## Estrutura principal

- `.codex/agents/` — perfis dos papéis do projeto.
- `.agents/skills/` — instruções reutilizáveis por etapa.
- `specs/` — requisitos confirmados e especificações do produto.
- `plans/` e `tasks/` — planejamento e tarefas.
- `contracts/` — contratos de execução e de produto.
- `docs/` — contexto, roadmap e registro de decisões.
- `orchestrator/` — ferramenta local para conduzir e registrar o fluxo.
- `src/` — código da aplicação.
