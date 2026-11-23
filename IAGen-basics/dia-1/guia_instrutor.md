# Guia do Instrutor - Dia 1: Fundamentos, Panorama e Engenharia de Prompts na Construção

**Duração:** 4 horas (240 minutos)  
**Objetivo do Dia:** Desmistificar os modelos de IA generativa, dominar técnicas de prompting de alta precisão e criar os primeiros entregáveis profissionais a partir de dados brutos de campo.

---

## ⏱️ Cronograma Minuto a Minuto

### [00:00 - 00:45] Bloco 1: Abertura e o Novo Panorama das IAs (45 min)
* **00:00 - 00:10:** Boas-vindas, alinhamento de expectativas e contextualização na Track.
* **00:10 - 00:30:** O trio dominante: **Claude vs. Gemini vs. ChatGPT**.
  * Pontos fortes de cada um no contexto de escritório e canteiro de obras.
  * O que muda com janelas de contexto grandes (leitura de memoriais inteiros) e modo de raciocínio (*Thinking*).
  * Privacidade e segurança: quais dados não colar em modelos abertos.
* **00:30 - 00:45:** Demonstração ao vivo do instrutor:
  * Comparando a mesma instrução genérica vs. uma instrução estruturada de engenharia.

### [00:45 - 01:40] Bloco 2: Sprint Prático 1 - Engenharia de Prompts na Obra (55 min)
* **00:45 - 01:00:** Apresentação da fórmula **RTCC (Papel, Tarefa, Contexto e Restrições)** e técnicas de Few-Shot.
* **01:00 - 01:30:** **Laboratório 1 em Ação:**
  * Os participantes abrem o arquivo `dia-1/dados/transcricao_obra_bruta.txt`.
  * Desafio: Gerar um **Relatório Diário de Obra (RDO)** estruturado, listando clima, efetivo, atividades executadas, desvios de cronograma e inconformidades de segurança (NR-18).
* **01:30 - 01:40:** Compartilhamento de telas de 2 participantes e refinamento coletivo do prompt.

---

### [01:40 - 01:55] Intervalo de Café (15 min)

---

### [01:55 - 03:10] Bloco 3: Sprint Prático 2 - Análise de Documentos e Claude Artifacts (75 min)
* **01:55 - 02:15:** Apresentação dos **Claude Artifacts**:
  * O que são, quando aparecem e como interagir/editar o conteúdo gerado ao lado do chat.
* **02:15 - 02:55:** **Laboratório 2 em Ação:**
  * Uso de um trecho de edital/memorial descritivo (`dia-1/dados/trecho_memorial_descritivo.md`).
  * Desafio com Claude Artifacts:
    1. Identificar cláusulas críticas de penalidades e prazos de entrega.
    2. Gerar uma tabela comparativa (Matriz de Conformidade Técnica).
    3. Criar uma checklist interativa em formato Markdown dentro do Artifact.
* **02:55 - 03:10:** Análise de alucinações: como verificar fontes e restringir o modelo estritamente ao documento fornecido.

### [03:10 - 03:40] Bloco 4: Fechamento e Biblioteca de Prompts (30 min)
* **03:10 - 03:25:** Síntese dos aprendizados do dia e dúvidas frequentes.
* **03:25 - 03:40:** **Ativo do Dia:** Cada aluno salva seus melhores prompts no arquivo pessoal de biblioteca de prompts (`dia-1/prompts/prompts_dia1.md`).
