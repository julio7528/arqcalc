---
name: deploy-approved
description: Publica uma landing page aprovada e verifica o ambiente de produção; use apenas na etapa de deploy após aprovação do PO e orientação explícita do usuário.
---

# Deploy aprovado

Use esta Skill para executar somente a etapa 7 de `plans/FLUXO-LANDING-PAGE.md`.

1. Leia `AGENTS.md`, a etapa 7 do plano, o parecer de revisão e o registro de aprovação do PO.
2. Confirme que há aprovação explícita do PO e orientação explícita do usuário para publicar. Se alguma delas estiver ausente, não publique; informe o que falta e aguarde.
3. Inspecione a configuração de deploy existente e identifique a plataforma e o ambiente já usados. Quando a delegação estiver disponível, envolva `devops` e coordene com `desenvolvedor_frontend` conforme necessário. Não presuma provedor, domínio, credenciais ou configurações.
4. Siga o processo configurado no projeto. Proteja segredos; não os imprima nem os inclua em relatórios. Não crie infraestrutura ou serviços fora do escopo aprovado.
5. Após publicar, verifique o endereço publicado e os fluxos essenciais disponíveis. Registre versão, endereço, verificações, resultados e problemas observados.

**Entregável:** relatório do deploy com endereço, versão e resultado da verificação. Se houver falha, informe o estado observado e a ação necessária; não alegue sucesso sem evidência.
