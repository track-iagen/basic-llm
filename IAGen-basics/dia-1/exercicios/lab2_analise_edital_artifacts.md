# Laboratório 2: Auditoria de Memorial Descritivo com Claude Artifacts

**Contexto:** Memoriais descritivos e cadernos de encargos de engenharia são repletos de requisitos técnicos e cláusulas punitivas que passam despercebidos.
**Objetivo:** Usar o Claude com foco na ativação e manipulação de **Claude Artifacts** para auditar especificações e criar uma matriz de conformidade técnica interativa.

---

## 📥 Dados de Entrada
Consulte o arquivo: `dia-1/dados/trecho_memorial_descritivo.md`.

---

## 🛠️ O Desafio (Passo a Passo)

1. **Ativação do Artifact no Claude:**
   - Abra o Claude ([claude.ai](https://claude.ai)).
   - Envie o texto do memorial junto a um prompt solicitando a auditoria técnica.
2. **Requisitos de Saída do Artifact:**
   - Solicite que a resposta seja gerada em um **Artifact do tipo Documento/Markdown**.
   - O Artifact deve conter:
     - **Tabela de Riscos Contratuais e Financeiros:** Prazos, multas diárias, limites e condições para aceitação de intempéries pluviométricas.
     - **Quadro de Parâmetros de Qualidade do Concreto:** $f_{ck}$, fator a/c, abatimento (*slump*) e regras de desforma.
     - **Checklist Interativo de Desforma:** Uma lista de verificação passo a passo para o fiscal de obra marcar antes de autorizar a retirada de escoras.
3. **Refinamento dentro do Artifact:**
   - Peça ao Claude para editar diretamente uma seção do Artifact gerado (ex: adicionar uma coluna com os artigos correspondentes da NBR 6118).

---

## 💡 Dica de Ouro
Observe como o Artifact cria um espaço de trabalho dedicado ao lado do chat, permitindo copiar, salvar como documento independente ou iterar sem poluir o histórico de mensagens!
