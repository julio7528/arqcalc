# Roadmap do projeto

Documento vivo do andamento. Atualize o status, o trabalho concluído e o próximo passo previsto sempre que uma tarefa alterar o projeto ou avançar uma etapa. Os memorandos detalhados ficam em `project-context.md`; eventos e decisões sequenciais ficam em `decision-log.md`.

## Status

- **Concluída:** entregável realizado e evidência registrada.
- **Em andamento:** trabalho iniciado e ainda não finalizado.
- **Aguardando orientação:** entregável apresentado e depende de decisão/instrução do usuário.
- **Não iniciada:** ainda não começou.

## Estado atual

| Etapa | Status | Feito | Próximo trabalho |
| --- | --- | --- | --- |
| Fundação do processo e documentação | Concluída | Regras, fluxo de sete etapas, perfis de agentes, Skills, registros contínuos, arquitetura progressiva de especificações e guias README para iniciar o fluxo e localizar as instruções da aplicação. | Manter os guias e registros atualizados; definir comandos de execução da aplicação após a decisão tecnológica no Planejamento. |
| MVP do orquestrador progressivo | Concluída | CLI, schema, persistência SQLite, descoberta progressiva, requisitos com evidência confirmada, gates vinculados a hash, autorização específica de deploy, dry-run e suíte de 43 testes (21 de regressão e 22 de contratos); execução real do Codex continua desabilitada. | Aguardar orientação para iniciar o levantamento de requisitos pelo CLI ou priorizar a próxima fase do orquestrador. |
| Subsistema de contratos | Concluída | Schemas e templates versionados, três contratos operacionais, avaliação obrigatória no Planning, geração de contratos de produto por tarefa, revisão/aprovação por versão e hash, validação de execução/saídas/handoffs e migrações aditivas; 43 testes passaram. Reavaliação em UX/UI cria nova versão e invalida o gate de Planning até nova aprovação. | Usar a avaliação na Etapa 2 quando uma especificação for aprovada; reapreciar contratos após mudanças confirmadas de interface ou de origem. |
| 1. Levantamento de requisitos | Não iniciada | Bootstrap disponível; requisitos de produto ainda não foram levantados nem aprovados e nenhum gate foi concedido. | Quando o usuário orientar o início, seguir `specs/INIT.md`, conduzir o levantamento interativo e apresentar uma especificação baseada apenas em confirmações. |
| 2. Planejamento | Não iniciada | Nenhum plano técnico específico da landing page foi produzido. | Após a validação da Etapa 1, dividir o trabalho em tarefas, prioridades, dependências e decisões técnicas. |
| 3. UX / UI Design | Não iniciada | Nenhum wireframe ou layout de uma landing page foi produzido. | Após as etapas anteriores e orientação do usuário, definir navegação, wireframe e identidade visual. |
| 4. Desenvolvimento | Não iniciada | Nenhuma implementação de landing page foi realizada. | Após requisitos e design aprovados e orientação do usuário, implementar o escopo planejado. |
| 5. Testes e QA | Não iniciada | Nenhum teste de landing page foi executado. | Validar critérios, funcionamento, responsividade e acessibilidade após a implementação. |
| 6. Revisão e aprovação | Não iniciada | Nenhuma revisão de implementação ou aprovação de produto ocorreu. | Revisar a versão testada; corrigir achados e obter decisão do PO. |
| 7. Deploy | Não iniciada | Nenhuma publicação em produção foi realizada. | Publicar após aprovação do PO e orientação explícita do usuário; verificar e registrar o site publicado. |

**Próxima etapa elegível:** Etapa 1 — Levantamento de requisitos, quando o usuário orientar seu início. O subsistema de contratos está disponível para o Planejamento futuro; nenhuma avaliação ou especificação de produto foi criada nesta implementação.
