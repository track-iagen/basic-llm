# Biblioteca de Prompts de Referência - Dia 2

Templates de prompts para análise de planilhas, geração de fórmulas e dashboards com Claude Artifacts.

---

## 1. Prompt: Análise Orçamentária e Fórmulas de Google Sheets

```markdown
Você é um Especialista em Engenharia de Custos e Orçamentação da Construção Civil.

Analise os dados da planilha orçamentária anexa no formato CSV e execute:
1. Calcule o Desvio Financeiro Total (Previsto vs. Realizado) indicando se há superávit ou déficit percentual.
2. Identifique os dois insumos com maior impacto negativo no orçamento e explique a causa provável com base nos status.
3. Forneça as fórmulas exatas para o Google Sheets para:
   a) Calcular a variação percentual na coluna J: =(H2*G2 - F2*E2)/(F2*E2)
   b) Usar a função QUERY para filtrar apenas os serviços que possuem a palavra "Atraso" ou "estouro".
4. Redija um parecer financeiro executivo de 2 parágrafos com tom institucional recomendando ações de contenção de custos.
```

---

## 2. Prompt: Dashboard Visual Interativo em Claude Artifacts (HTML/Tailwind)

```markdown
Gere um ARTIFACT contendo um dashboard executivo interativo em HTML único com Tailwind CSS para acompanhamento de obras.

Requisitos do Dashboard:
- Tema limpo, profissional (estilo engenharia civil / construção).
- Header com: "Track | Painel de Controle de Obra - Residencial Alpha Tower".
- 4 Cards de Métricas no topo:
  * Conclusão Físico-Financeira: 42% (com badge de status no prazo)
  * Custo Realizado: R$ 148.500,00 (+3.2% vs. previsto em amarelo)
  * Efetivo em Canteiro: 30 colaboradores (18 próprios / 12 terceiros)
  * Incidentes Críticos: 1 Alerta de Segurança (Badge vermelho de atenção)
- Seção de Progresso por Disciplina com barras de progresso coloridas.
- Tabela com os últimos registros do Diário de Obra e botões de ação para exportar.
```

---

## 3. Prompt: Comunicação em Cascata (E-mail + WhatsApp)

```markdown
Com base nas ocorrências de hoje (atraso na entrega do concreto pela usina e falta do aço de 10mm para amanhã):

Gere duas peças de comunicação:

PEÇA 1 - E-mail Formal de Cobrança:
- Destinatário: Gerência Comercial da Usina de Concreto.
- Assunto formal com número de pedido e obra.
- Notificação do atraso de 2h30 na entrega dos caminhões betoneira e prejuízo na junta de concretagem.
- Solicitação de garantia de pontualidade para a próxima etapa sob pena de retenção de pagamento.

PEÇA 2 - Mensagem Direta para WhatsApp da Diretoria:
- Máximo de 5 linhas.
- Uso de bullets e formatação em negrito para termos-chave.
- Resumo claro: o que foi concluído, o impacto do atraso e a ação tomada.
```
