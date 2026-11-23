# Laboratório 1: Construindo Assistentes Especializados (Gems & Projects)

**Contexto:** Ao invés de colar normas e contratos repetidamente a cada conversa, criaremos assistentes de IA persistentes com memória técnica institucional.
**Objetivo:** Configurar um **Claude Project** ou uma **Gemini Gem** capaz de atuar como Fiscal de Qualidade de Obra e Auditor de Contratos da Track.

---

## 🛠️ O Desafio Passo a Passo

### Opção A: Criando um Claude Project (Base de Conhecimento com Arquivos)
1. No [Claude](https://claude.ai), crie um novo **Project** chamado: `Fiscal de Qualidade & Normas - Track`.
2. Adicione ao Project Knowledge o arquivo `dia-3/dados/base_conhecimento_mock_nbr.md`.
3. Configure o **System Prompt / Project Instructions** (use o modelo em `dia-3/prompts/prompts_dia3.md`).
4. Realize 2 testes de estresse:
   - *Teste 1:* "O encarregado quer desformar a lateral do pilar amanhã (com 24 horas de concretagem). Posso autorizar?"
   - *Teste 2:* "O concreto chegou com abatimento 40mm acima do especificado e o motorista quer adicionar água para homogeneizar. Qual a orientação?"

---

### Opção B: Criando uma Gemini Gem (Google Workspace)
1. No [Gemini](https://gemini.google.com), acesse o Gerenciador de Gems e clique em **Criar Gem**.
2. Nome da Gem: `Assessor de Notificações e Medições de Obra`.
3. Cole as instruções de sistema definindo a personalidade de um engenheiro rigoroso e especialista em contratos.
4. Teste a geração de uma notificação de retenção de 20% da medição de uma empreiteira por inconformidade de armadura sem espaçador.
