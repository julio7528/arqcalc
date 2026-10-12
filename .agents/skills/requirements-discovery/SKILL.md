---
name: requirements-discovery
description: Conduz o levantamento interativo de requisitos de uma landing page com PO, Analista de Requisitos, Codex e usuário; use antes do planejamento quando requisitos ainda precisam ser definidos.
---

# Levantamento de requisitos

Use esta Skill para executar somente a etapa 1 de `plans/FLUXO-LANDING-PAGE.md`.

1. Leia as regras de `AGENTS.md` e a etapa 1 do plano. Verifique se já existem requisitos ou decisões para preservar.
   Leia também `specs/README.md`, `specs/INIT.md` e `specs/workflow.yaml`; confirme que a etapa atual permite o levantamento e consulte as especificações existentes sem sobrescrevê-las.
2. Quando a delegação estiver disponível, envolva os perfis `product_owner` e `analista_requisitos`. O PO ajuda a esclarecer objetivo, público, valor e prioridades; o Analista converte as respostas em requisitos verificáveis. Trabalhe com ambos e com o usuário de forma interativa.
3. Pergunte sobre objetivos, público, conteúdo, funcionalidades, restrições e critérios de sucesso. Considere header, banner, catálogo, contato e rodapé quando pertinentes ao escopo. Faça perguntas para resolver incertezas; não invente requisitos nem transforme sugestões em decisões confirmadas.
4. Preserve incertezas como perguntas em aberto. Só crie ou atualize uma especificação em `specs/generated/` quando houver objetivo, escopo identificável e ao menos um requisito verificável confirmados; use `specs/templates/SPEC-TEMPLATE.md` e o próximo ID livre conforme `specs/README.md`.
5. Apresente o briefing e a versão exata para revisão. Peça aprovação explícita do usuário; registre a decisão no artefato e em `docs/decision-log.md` com evidência e referência cruzada. Não marque como `APPROVED`, não libere o próximo gate nem avance sem evidência e autorização explícitas. Atualize os registros obrigatórios em `docs/`.

**Entregável:** levantamento validado pelo usuário. Pare nesta etapa; não avance para planejamento, design ou implementação até receber orientação.
