# Laboratório 2: Claude Artifacts como Mini-Aplicações Web Interativas

**Contexto:** O Claude Artifacts permite gerar aplicações web funcionais (HTML + JavaScript ou React + Tailwind CSS) que rodam instantaneamente no próprio navegador, sem exigir instalação de servidores ou conhecimento de código.
**Objetivo:** Construir uma ferramenta interativa de engenharia civil que qualquer membro da Track possa usar no navegador.

---

## 🛠️ O Desafio

Escolha um dos 3 mini-apps abaixo para criar com o Claude Artifacts:

### Opção 1: Calculadora de Volume de Concreto e Consumo de Materiais
* **Inputs Interativos:**
  * Tipo de elemento: Viga, Pilar, Sapata ou Laje.
  * Dimensões (Comprimento, Largura, Altura/Espessura em metros).
  * Traço de concreto ou FCK desejado.
  * % de perda estimada (ex: 5% a 10%).
* **Outputs Interativos:**
  * Volume total em $m^3$.
  * Quantidade estimada de sacos de cimento (50 kg), metros cúbicos de areia e brita.
  * Checklist interativo de liberação de concretagem.

---

### Opção 2: Simulador Dinâmico de BDI (Benefícios e Despesas Indiretas)
* **Inputs Interativos:**
  * Sliders para: Administração Central (%), Seguro/Garantia (%), Risco (%), Tributos PIS/COFINS/ISS (%), Lucro Desejado (%).
* **Outputs Interativos:**
  * Cálculo instantâneo do BDI conforme fórmula padrão do TCU.
  * Gráfico de composição visual dos custos.
  * Preço final de venda de um serviço com base no custo direto inserido.

---

### Opção 3: Visualizador de Cronograma / Linha do Tempo de Obra
* **Inputs:** Formulário para adicionar marcos da obra (Etapa, Data Início, Data Fim, Responsável, Status).
* **Outputs:** Linha do tempo visual colorida destacando o caminho crítico e alertas de atraso.
