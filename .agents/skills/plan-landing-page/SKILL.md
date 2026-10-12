---
name: plan-landing-page
description: Converte requisitos validados de uma landing page em tarefas, prioridades, dependências e decisões técnicas; use na etapa de planejamento após a validação dos requisitos.
---

# Planejamento da landing page

Use esta Skill para executar somente a etapa 2 de `plans/FLUXO-LANDING-PAGE.md`.

1. Leia `AGENTS.md`, a etapa 2 do plano e os requisitos validados. Confirme que o usuário orientou o início do planejamento.
2. Inspecione o repositório para conhecer tecnologias, estrutura, convenções e integrações existentes antes de propor mudanças.
3. Quando a delegação estiver disponível, envolva `tech_lead`. Divida o escopo em tarefas priorizadas, identifique responsáveis adequados, dependências, riscos e ordem de execução. Avalie cada especificação/tarefa quanto à necessidade de contrato de produto e registre a justificativa em `plans/contract-assessment.yaml`, inclusive quando nenhum contrato adicional for necessário.
4. Gere contratos de produto em DRAFT somente a partir da especificação aprovada e dos artefatos de planejamento confirmados. Valide estrutura e rastreabilidade; registre campos pendentes e peça esclarecimento ao responsável adequado em vez de inventar interfaces ou decisões.
5. Proponha apenas decisões técnicas que o contexto justifique. Explique impactos e alternativas relevantes; destaque decisões que precisam da escolha do usuário. Não implemente código nem instale dependências nesta etapa.
6. Apresente plano, avaliação de contratos, rascunhos e perguntas ou decisões em aberto ao usuário.

**Entregável:** tarefas e prioridades, dependências, sequência de execução, decisões técnicas e riscos, mais a avaliação rastreável de contratos. Pare e aguarde orientação antes de iniciar UX/UI ou desenvolvimento.
