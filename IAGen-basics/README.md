# IAGen-basics: IA Generativa Aplicada à Automação de Escritório e Engenharia Civil

Bem-vindo ao repositório do curso **IAGen-basics**, desenvolvido para capacitar equipes e profissionais em automação de processos, produtividade de escritório e fluxos técnicos de engenharia civil utilizando os principais modelos de linguagem (Claude, Gemini e ChatGPT).

---

## 📌 Visão Geral do Curso

- **Carga Horária:** 12 horas (3 encontros de 4 horas cada).
- **Foco Prático:** Hands-on orientado a casos reais da construção civil e rotinas corporativas.
- **Público-Alvo:** Engenheiros civis, gestores de obras, orçamentistas, coordenadores de projetos e equipe administrativa da Track.
- **Stack Principal:**
  - **Claude (Anthropic):** Artifacts, Projects, raciocínio avançado e geração de ferramentas interativas.
  - **Gemini (Google):** Ecossistema Google Workspace (Docs, Sheets, Slides), Gems, leitura de contextos massivos e multimodalidade.
  - **ChatGPT (OpenAI):** Comparativo, automação e suporte a tarefas ágeis.

---

## 🗓️ Estrutura dos 3 Dias

| Dia | Tema Principal | Foco Prático & Entregável |
| :--- | :--- | :--- |
| **Dia 1** | **Fundamentos, Panorama e Engenharia de Prompts na Construção** | Comparativo de modelos, técnicas de prompt técnico, extração de dados de campo e geração do primeiro RDO automatizado. |
| **Dia 2** | **Documentos, Planilhas, Dashboards e Comunicação Multi-canal** | Análise e fórmulas em Google Sheets, geração de relatórios formais, apresentações executivas e painéis visuais com Claude Artifacts. |
| **Dia 3** | **Assistentes Especializados (Gems & Projects) e Mini-Apps Interativos** | Criação de Gemini Gems e Claude Projects com base de conhecimento normativa, e desenvolvimento de ferramentas web interativas (calculadoras de obra em Artifacts). |

---

## 📂 Organização das Pastas

```text
IAGen-basics/
├── README.md                          # Este documento (visão geral)
├── ementa/
│   └── ementa_detalhada.md            # Ementa pedagógica completa e objetivos
├── dia-1/                             # Dia 1: Fundamentos e Prompts Técnicos
│   ├── guia_instrutor.md              # Roteiro do facilitador (minuto a minuto)
│   ├── exercicios/                    # Enunciados dos laboratórios práticos
│   ├── dados/                         # Datasets fictícios para simulação de obra
│   └── prompts/                       # Prompts e templates de referência
├── dia-2/                             # Dia 2: Workspace, Sheets, Dashboards e Comms
│   ├── guia_instrutor.md              # Roteiro do facilitador
│   ├── exercicios/                    # Laboratórios práticos
│   ├── dados/                         # Planilhas modelo, orçamentos e memórias
│   └── prompts/                       # Prompts e templates de referência
├── dia-3/                             # Dia 3: Gems, Projects e Mini-Apps
│   ├── guia_instrutor.md              # Roteiro do facilitador
│   ├── exercicios/                    # Laboratórios de criação de assistentes
│   ├── dados/                         # Normas técnicas mock e bases de conhecimento
│   └── prompts/                       # Instruções de sistema (System Prompts)
└── recursos/
    └── checklist_preparacao.md        # Checklist de preparação pré-curso
```

---

## 🎯 Metodologia de Ensino

Cada encontro de 4 horas segue a estratégia **Sprint de 4 Blocos**:

1. **Bloco 1 (45 min):** Conceituação & Demonstração Ao Vivo (ancorada em uma dor real de engenharia/escritório).
2. **Bloco 2 (55 min):** Sprint Prático Guiado (Laboratório assistido passo a passo).
3. **Intervalo (15 min):** Pausa cognitiva.
4. **Bloco 3 (75 min):** Sprint Desafio Autônomo (Resolução de problema em pares ou individual).
5. **Bloco 4 (50 min):** Apresentação, Validação dos Resultados e Salvamento do Ativo Operacional.

---

## 📋 Lista de Tarefas: Artefatos Pendentes (A Construir / A Localizar)

Acompanhamento do que já está pronto e dos artefatos complementares a serem construídos ou localizados antes da primeira turma:

### 1. 🎨 Slides & Apresentações
- [ ] **Deck de Slides - Dia 1:** Introdução aos LLMs, panorama dos players (Claude, Gemini, ChatGPT), modo Thinking, segurança/LGPD e engenharia de prompts.
- [ ] **Deck de Slides - Dia 2:** Integração com Google Workspace (Docs, Sheets, Slides), geração de dashboards em Artifacts e comunicação multi-canal.
- [ ] **Deck de Slides - Dia 3:** Agentes persistentes (Gems vs Projects), engenharia de System Prompts e prototipagem de web apps em Artifacts.

### 2. 🎙️ Mídias & Datasets Reais
- [x] Transcrição textual do relato de canteiro (`dia-1/dados/transcricao_obra_bruta.txt`).
- [ ] **Áudio real gravado (.mp3 / .wav):** Gravar áudio de ~2 minutos simulando o engenheiro residente no canteiro para teste de transcrição e multimodalidade direta com o Gemini.
- [x] Trecho de memorial descritivo em Markdown (`dia-1/dados/trecho_memorial_descritivo.md`).
- [ ] **PDF de Memorial Descritivo formatado:** Criar/localizar uma versão em PDF com carimbo técnico e formatação visual padrão de engenharia para testar extração de documentos escaneados/vetoriais.
- [x] Planilha orçamentária modelo em CSV (`dia-2/dados/orcamento_obra_amostra.csv`).
- [ ] **Planilha formatada (.xlsx / Google Sheets):** Modelo completo com abas de Curva ABC, cronograma físico-financeiro e formatação condicional pronta para clonagem pelos alunos.

### 3. 💻 Códigos de Referência dos Claude Artifacts
- [ ] **Código Modelo - Dashboard do Dia 2:** Arquivo HTML/Tailwind completo de referência do Dashboard Executivo da Alpha Tower para o instrutor ter como gabarito.
- [ ] **Código Modelo - Mini-App do Dia 3:** Aplicação interativa funcional pronta (Calculadora de Concreto e Consumo de Materiais em HTML/JS/Tailwind) para demonstração ao vivo.
- [ ] **Exemplo de Diagrama de Processo:** Arquivo com fluxograma vetorial de medição de obra renderizado em SVG puro pronto para consulta.

### 4. 🤖 Assistentes & Bases de Conhecimento
- [x] Base de conhecimento técnica mock em Markdown (`dia-3/dados/base_conhecimento_mock_nbr.md`).
- [ ] **Pacote de PDFs de Normas Técnicas para Claude Project:** Reunir trechos essenciais da NBR 6118, NBR 14931 e NR-18 para upload na base de conhecimento do projeto prático.
- [ ] **Instruções prontas para importação (Gems/Custom GPTs):** Exportar o `System Prompt` do Fiscal de Obra em formato padronizado com exemplos de Few-Shot.

### 5. 📝 Gestão & Fechamento
- [x] Checklist de preparação pré-curso (`recursos/checklist_preparacao.md`).
- [ ] **Formulário de Avaliação e Feedback:** Criar template de Google Forms para envio no final do 3º dia.
- [ ] **Modelo de Certificado:** Template de certificado de conclusão de 12 horas no Google Slides / Canva.
