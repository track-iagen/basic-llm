# Laboratório 1: Transformação de Áudio de Campo em RDO Formal e Alertas

**Contexto:** No dia a dia de obra, o engenheiro residente ou encarregado raramente tem tempo de redigir relatórios formais longos. O uso de notas de voz ou anotações rápidas é o padrão.
**Objetivo:** Utilizar Claude ou Gemini para transformar a transcrição bruta de um áudio de canteiro em 3 entregáveis estruturados.

---

## 📥 Dados de Entrada
Consulte o arquivo: `dia-1/dados/transcricao_obra_bruta.txt`.

---

## 🛠️ O Desafio (Passo a Passo)

Utilizando a técnica **RTCC (Papel, Tarefa, Contexto, Restrições)**, construa um prompt para gerar:

1. **Relatório Diário de Obra (RDO) Padronizado:**
   - Cabeçalho: Obra, Data, Condições Climáticas (manhã/tarde).
   - Efetivo: Próprios vs. Terceirizados por frente de serviço.
   - Atividades Concluídas e Métricas de Produção.
   - Ocorrências e Desvios de Cronograma com causas e impactos estimados.
2. **Notificação Formal de Segurança (NR-18):**
   - Redigir uma notificação formal de advertência destinada à diretoria da empreiteira "Souza & Filhos", mencionando a reincidência de trabalho em altura sem EPI e linha de vida, solicitando plano de ação em 24h sob pena de rescisão contratual.
3. **Resumo Executivo para WhatsApp:**
   - Mensagem curta em tópicos (bullet points) com emojis discretos, adequada para envio no grupo de gestores da Track e diretoria, destacando o atraso da usina de concreto e o alerta de aço para amanhã.

---

## 💡 Critérios de Avaliação
- O modelo inventou nomes ou dados não presentes no áudio?
- As unidades de medida e termos técnicos de engenharia civil foram preservados corretamente?
- O tom de voz variou adequadamente entre o RDO (técnico), a notificação (jurídico/rigoroso) e o WhatsApp (sintético/direto)?
