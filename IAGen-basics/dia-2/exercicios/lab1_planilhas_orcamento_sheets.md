# Laboratório 1: Análise Orçamentária e Automação no Google Sheets

**Contexto:** Desvios de custo e quantidade em relação à base SINAPI ou tabela orçada inicial ocorrem em quase todas as semanas de obra.
**Objetivo:** Usar o Gemini ou Claude para analisar dados orçamentários, criar fórmulas de reconciliação para o Google Sheets e gerar parecer de desvio orçamentário.

---

## 📥 Dados de Entrada
Consulte o arquivo: `dia-2/dados/orcamento_obra_amostra.csv`.

---

## 🛠️ O Desafio

1. **Análise de Variâncias:**
   - Calcule o Custo Total Previsto vs. Custo Total Realizado (até o momento).
   - Identifique os itens com maior variação de custo absoluto e variação percentual de preço unitário (inflação de insumo).
2. **Geração de Fórmulas para Google Sheets:**
   - Solicite ao modelo a fórmula para calcular a Variação Percentual ponderada no Google Sheets: `=(Realizado - Previsto) / Previsto`.
   - Peça uma fórmula com `QUERY` ou `FILTER` para listar automaticamente apenas os itens com status de atraso ou estouro de custo.
3. **Parecer Executivo para Gerência Financeira:**
   - Redija uma justificativa executiva formal de 2 parágrafos explicando os fatores de pressão de custo (ex: aumento do aço CA-50 e sobrepreço de concreto bombeado).
