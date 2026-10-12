# Especificações de produto

Esta pasta guarda a fonte de verdade dos requisitos e do comportamento esperado do produto. A arquitetura é progressiva: os requisitos são descobertos em conversa, registrados conforme forem confirmados e revisados sem exigir que todo o produto esteja definido antes do início.

## Ponto de entrada

- Comece por [INIT.md](INIT.md) para carregar o contexto e conduzir a etapa 1.
- Consulte [workflow.yaml](workflow.yaml) para descobrir a etapa atual, responsáveis, entregáveis, dependências e gates.
- Use o processo de [FLUXO-LANDING-PAGE.md](../plans/FLUXO-LANDING-PAGE.md) junto com as regras de [AGENTS.md](../AGENTS.md).
- Crie especificações com o formato de [SPEC-TEMPLATE.md](templates/SPEC-TEMPLATE.md).

## Identificadores

- Cada especificação de produto recebe um identificador global e estável no formato `SPEC-NNN`, atribuído em ordem crescente.
- Antes de atribuir um ID, procure em toda a pasta `specs/`, inclusive em `generated/`, e nunca reutilize um ID encontrado em nome de arquivo ou conteúdo.
- O arquivo existente `SPEC-001.md` é vazio e deve ser preservado. Seu ID fica reservado; o próximo ID livre é `SPEC-002`.
- O nome de arquivo gerado segue `SPEC-NNN-slug.md`. Renomear o título não muda o ID.
- Requisitos funcionais, requisitos não funcionais e critérios de aceitação usam, respectivamente, `RF-NNN`, `RNF-NNN` e `CA-NNN`, únicos dentro da especificação.
- Decisões relacionadas apontam para o identificador sequencial `DEC-NNN` em `docs/decision-log.md`.

Uma especificação nova só é criada quando as confirmações do usuário já permitem registrar um objetivo, um escopo identificável e ao menos um requisito verificável. Se ainda não houver base suficiente, continue a conversa e mantenha as incertezas como perguntas; não preencha um documento com suposições.

## Versionamento e ciclo de vida

Cada documento mantém uma versão `MAJOR.MINOR.PATCH` e um dos estados a seguir:

| Estado | Uso |
| --- | --- |
| `DRAFT` | Conteúdo em elaboração; ainda não foi apresentado como versão final para aprovação. |
| `IN_REVIEW` | Versão identificada apresentada ao usuário para decisão. |
| `APPROVED` | Versão exata aprovada explicitamente pelo usuário, com evidência registrada. |

Aumente PATCH para correções editoriais sem alterar significado, MINOR para requisitos compatíveis adicionados e MAJOR para mudanças incompatíveis de escopo ou comportamento. Uma alteração em especificação aprovada cria uma nova versão em `DRAFT`; mantenha o histórico e solicite nova aprovação antes de usá-la como base de avanço.

A aprovação não é inferida de silêncio, de uma resposta ambígua, de uma decisão do agente PO ou de uma mudança isolada de estado. Para passar de `IN_REVIEW` a `APPROVED`, registre no próprio documento o ID e a versão aprovados, a decisão explícita do usuário, data/hora com fuso, referência ou evidência fiel da resposta e o `DEC-NNN` correspondente. O registro de decisão deve apontar para a mesma especificação e versão. O gate no workflow também precisa apontar para essa evidência. Um status sem esses registros não libera etapa alguma.

Os estados das etapas também têm transições controladas: a etapa atual começa quando o usuário pede seu início; uma etapa `PENDING` só começa após dependências concluídas e autorização explícita; um entregável apresentado aguarda orientação; e a etapa só é concluída depois que a evidência exigida pelo gate foi registrada. Mudanças solicitadas pelo usuário reabrem o trabalho na etapa atual. A conclusão de uma etapa nunca inicia a próxima automaticamente.

## Organização

| Local | Conteúdo |
| --- | --- |
| `INIT.md` | Procedimento de bootstrap para iniciar ou retomar o levantamento. |
| `workflow.yaml` | Estado, sequência, agentes, Skills, entregáveis, dependências e gates. |
| `templates/` | Modelos de especificações de produto. |
| `generated/` | Especificações progressivas geradas durante o trabalho. |
| `SPEC-001.md` | Arquivo legado vazio, preservado sem uso ou sobrescrita. |

`workflow.yaml` é uma configuração declarativa independente de executor. Uma sessão Codex pode seguir o procedimento agora; uma automação futura pode gerar documentos e atualizar estados, desde que mantenha a evidência humana e a rastreabilidade. Esta inicialização não instala nem implementa um motor de orquestração.

## Especificações e artefatos de etapa

Uma especificação descreve o que o produto deve fazer: objetivos, escopo, requisitos, restrições e critérios de aceitação. Ela não substitui os artefatos necessários para executar cada etapa.

- Planejamento cria planos e tarefas em `plans/` e `tasks/`.
- UX/UI cria wireframes, decisões de navegação e layouts no destino de design escolhido no planejamento, como Figma quando aplicável.
- Desenvolvimento cria ou altera arquivos de produto em `src/`.
- QA guarda evidências e relatórios em `tests/`.
- Contratos de interface e integração ficam em `contracts/`.
- Revisões, aprovações e registros de andamento ficam nos documentos pertinentes de `docs/`.

Todo artefato derivado deve apontar para o ID e a versão da especificação de origem, usando metadados, cabeçalho, tarefa relacionada ou referência rastreável equivalente. Alterações de código apontam essa origem na tarefa ou no registro da alteração; não é necessário inserir comentários artificiais no código. A especificação que inaugura um requisito é sua própria origem.

`contracts/` separa contratos operacionais reutilizáveis de contratos de produto ligados à especificação aprovada. O Tech Lead avalia sua necessidade durante Planning; nenhum contrato de produto é exigido antes dessa avaliação. Consulte [`contracts/README.md`](../contracts/README.md) para ciclo de vida, schemas e comandos.

Crie uma especificação adicional apenas quando o escopo aprovado justificar uma funcionalidade independente, com objetivo e critérios próprios. A entrada em outra etapa do fluxo, por si só, não justifica outro arquivo de especificação.

## Referências

- [Regras do projeto](../AGENTS.md)
- [Fluxo de trabalho](../plans/FLUXO-LANDING-PAGE.md)
- [Skill de levantamento de requisitos](../.agents/skills/requirements-discovery/SKILL.md)
- [Contexto e memorandos](../docs/project-context.md)
- [Roadmap](../docs/project-roadmap.md)
- [Registro de decisões](../docs/decision-log.md)
