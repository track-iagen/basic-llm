# Biblioteca de Prompts de Referência - Dia 1

Templates de prompts testados e validados para as práticas do Dia 1.

---

## 1. Prompt RTCC: Geração de RDO a partir de Relato Bruto

```markdown
Você é um Engenheiro Civil Sênior e Gerente de Obras experiente na gestão de obras residenciais e corporativas.

Sua tarefa é analisar o relato bruto de campo transcrito abaixo e convertê-lo em um Relatório Diário de Obra (RDO) técnico, formal e estruturado.

[DIRETRIZES DE FORMATAÇÃO]:
1. Cabeçalho estruturado com Data, Obra, Condições Climáticas e Temperatura.
2. Tabela de Efetivo separando mão de obra direta (própria) e subempreiteiros.
3. Seção "Produção e Avanço Físico" com quantitativos exatos mencionados.
4. Seção "Ocorrências e Desvios Críticos", destacando o atraso da usina de concreto e impactos no cronograma de desforma.
5. Seção "Segurança do Trabalho", reportando o flagrante de descumprimento de EPIs na periferia conforme diretrizes da NR-18.
6. Seção "Pendências e Suprimentos Críticos para o Próximo Dia".

[RESTRIÇÕES]:
- Não invente informações não mencionadas no áudio.
- Mantenha linguagem técnica estritamente profissional e objetiva.

[DADOS DE CAMPO]:
"""
{COLAR A TRANSCRIÇÃO AQUI}
"""
```

---

## 2. Prompt: Notificação Formal de Advertência de Segurança

```markdown
Você é o Gestor Jurídico e Operacional da Construtora.

Redija uma Notificação Extrajudicial de Advertência e Aplicação de Medida Corretiva de Segurança do Trabalho dirigida à diretoria da empreiteira "{NOME_EMPREITEIRA}".

[FATOS]:
- Reincidência na data de {DATA} de 2 ajudantes executando alvenaria na periferia do 4º pavimento sem o uso de cinto tipo paraquedista conectado à linha de vida.
- Ocorrência grave que infringe a NR-18 e as cláusulas de segurança do contrato de prestação de serviços.

[EXIGÊNCIAS]:
- Solicitar apresentação de plano de mitigação e reciclagem da equipe em até 24 horas úteis.
- Alertar que nova reincidência acarretará aplicação de multa contratual e rescisão motivada por justa causa.

Tom: Formal, austero, jurídico e irrefutável.
```

---

## 3. Prompt: Auditoria Técnica com Claude Artifacts

```markdown
Atue como Especialista em Auditoria e Contratos de Engenharia Civil.

Analise o trecho do memorial descritivo anexo e gere um ARTIFACT contendo:
1. Uma Matriz de Riscos e Penalidades em formato de tabela (Cláusula, Risco Identificado, Penalidade Contratual, Ação Preventiva da Construtora).
2. Uma Tabela de Parâmetros Técnicos Obrigatórios para o Concreto Estrutural.
3. Uma Lista de Verificação (Checklist de Fiscalização de Desforma) em formato Markdown pronto para impressão ou consulta em tablet no canteiro.

Restrinja sua análise unicamente aos itens presentes no documento fornecido.
```
