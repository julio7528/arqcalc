# Bootstrap das especificações

Este documento é o ponto de entrada para iniciar ou retomar a descoberta de requisitos. Ele não contém requisitos de produto aprovados e não autoriza automaticamente a etapa seguinte.

## Estado inicial

- **Etapa atual:** 1 — Levantamento de requisitos.
- **Estado da etapa:** `NOT_STARTED`.
- **Especificações de produto aprovadas:** nenhuma.
- **Gates de aprovação:** nenhum concedido.
- **Próximas etapas:** `PENDING` até a conclusão da etapa anterior e autorização humana explícita.

O arquivo `SPEC-001.md` é um placeholder vazio preservado. Não o trate como briefing, requisito ou aprovação.

## Preparação da sessão

Antes de conversar sobre requisitos, leia nesta ordem ou confirme que estão atualizados:

1. `AGENTS.md` e `docs/` para as regras e o estado registrado do projeto.
2. `specs/README.md`, este arquivo e `specs/workflow.yaml`.
3. `plans/FLUXO-LANDING-PAGE.md` para o procedimento e os gates das sete etapas.
4. `.agents/skills/requirements-discovery/SKILL.md`.
5. Os perfis `.codex/agents/product_owner.toml` e `.codex/agents/analista-requisitos.toml`, quando a execução de agentes estiver disponível.

Confira o estado real e os artefatos existentes antes de retomar. Preserve conteúdo, decisões e aprovações anteriores. Se as ferramentas não puderem invocar os agentes ou a Skill, siga suas instruções diretamente e registre essa limitação quando pertinente.

## Execução da etapa 1

- Trabalhe somente no levantamento. Converse interativamente com o usuário para entender objetivo, público, conteúdo, funcionalidades, restrições, prioridades e critérios de sucesso.
- O Product Owner ajuda a esclarecer valor, objetivo e prioridades; o Analista de Requisitos transforma respostas confirmadas em requisitos claros e verificáveis.
- Separe fatos confirmados, decisões, sugestões e perguntas em aberto. Não converta silêncio, suposições ou recomendações de agentes em requisitos.
- Considere header, banner, catálogo, contato e rodapé somente quando forem pertinentes ao escopo confirmado.
- Preserve itens ainda sem resposta como perguntas em aberto. Não os apresente como requisitos aprovados.
- Só crie ou atualize um arquivo em `specs/generated/` quando houver informação confirmada suficiente para definir um objetivo, um escopo identificável e ao menos um requisito verificável. Caso contrário, continue a conversa sem gerar uma especificação incompleta.
- Atribua o próximo identificador `SPEC-NNN` livre, pesquisando a árvore inteira de `specs/`; `SPEC-001` já está reservado pelo placeholder existente. Use o [modelo](templates/SPEC-TEMPLATE.md).
- Gere especificações adicionais somente quando uma funcionalidade independente tiver escopo, objetivo e critérios próprios. Não crie uma especificação nova apenas porque o fluxo avançou.
- Apresente o briefing e a versão exata do artefato ao usuário. Enquanto houver revisão, mantenha o estado `IN_REVIEW`.

## Aprovação e autorização para avançar

Só registre uma especificação como `APPROVED` quando o usuário aprovar explicitamente a versão identificada. Registre a decisão no artefato e acrescente um novo `DEC-NNN` em `docs/decision-log.md`, incluindo especificação, versão, data/hora com fuso, evidência da resposta e alcance da autorização.

Aprovar o conteúdo e autorizar o início da etapa seguinte são decisões humanas; a resposta pode conter ambas, desde que isso esteja explícito. Atualize o gate em `workflow.yaml` com uma referência verificável ao registro, não apenas alterando um status. Se a pessoa aprovar o documento sem autorizar o avanço, mantenha a etapa seguinte bloqueada e aguarde orientação. Nunca fabrique identidade, data, aprovação ou evidência.

Após a validação e autorização, atualize os registros obrigatórios de `docs/` e então o estado do workflow. Apresente o entregável e pare. Não inicie planejamento, design, implementação, QA, revisão ou deploy nesta inicialização.

## Rastreabilidade das etapas seguintes

Planos e tarefas devem apontar para a especificação aprovada de origem. Wireframes e layouts, código ou tarefa de implementação, relatórios de QA, pareceres e registros de deploy também devem carregar ou referenciar o ID e a versão de origem. Mantenha cada artefato em seu local próprio, conforme `specs/README.md` e `workflow.yaml`.
