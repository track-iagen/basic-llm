#!/usr/bin/env python3
"""
Track Document Design Style - Master PDF Generator
Compila todos os documentos do curso IAGen-basics em um único PDF
com capa escura, páginas internas claras, cartões no estilo do slide Track,
tipografia profissional e paleta extraída da identidade visual da Track.
"""

import os
import subprocess
import base64
import csv

BASE_DIR = "/home/fcfmc/Documents/track"
COURSE_DIR = os.path.join(BASE_DIR, "IAGen-basics")
OUTPUT_HTML = os.path.join(BASE_DIR, "IAGen_basics_manual.html")
OUTPUT_PDF = os.path.join(BASE_DIR, "IAGen_basics_manual.pdf")
LOGO_PATH = os.path.join(BASE_DIR, "assets", "track_logo.png")

with open(LOGO_PATH, "rb") as f:
    LOGO_B64 = base64.b64encode(f.read()).decode("utf-8")

def md_to_html(filepath):
    """Converte markdown para HTML estruturado usando pandoc."""
    cmd = ["pandoc", filepath, "-f", "markdown+pipe_tables", "-t", "html5"]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return res.stdout

def csv_to_html(filepath):
    """Converte CSV em tabela estilizada."""
    with open(filepath, mode="r", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if not rows:
        return ""
    html = ['<div class="table-container"><table class="track-table">']
    html.append("<thead><tr>")
    for col in rows[0]:
        html.append(f"<th>{col.replace('_', ' ')}</th>")
    html.append("</tr></thead><tbody>")
    for row in rows[1:]:
        html.append("<tr>")
        for val in row:
            html.append(f"<td>{val}</td>")
        html.append("</tr>")
    html.append("</tbody></table></div>")
    return "\n".join(html)

CSS_STYLES = f"""
/* ===================================================
   TRACK DOCUMENT DESIGN STYLE - MASTER STYLESHEET
   Paleta extraída dos slides Track:
   - Dark Slate Navy: #202730
   - Cyan Accent:     #5CE1E6
   - Light Cream:     #F1ECE6
   - Clean Card:      #FFFFFF / #FAFAF6
   =================================================== */

@page {{
    size: A4 portrait;
    margin-top: 20mm;
    margin-bottom: 20mm;
    margin-left: 16mm;
    margin-right: 16mm;
    background-color: #F1ECE6;
    
    @top-left {{
        content: "IAGen-basics • Manual de Capacitação Técnica";
        font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
        font-size: 8pt;
        font-weight: 500;
        color: #64748B;
        vertical-align: bottom;
        padding-bottom: 4mm;
        border-bottom: 2px solid #202730;
    }}
    
    @top-right {{
        content: "TRACK • Inovação e Tecnologia";
        font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
        font-size: 8pt;
        font-weight: 800;
        letter-spacing: 1.5px;
        color: #202730;
        vertical-align: bottom;
        padding-bottom: 4mm;
        border-bottom: 2px solid #5CE1E6;
    }}
    
    @bottom-left {{
        content: "Track Document Design Style";
        font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
        font-size: 8pt;
        font-weight: 600;
        color: #94A3B8;
        vertical-align: top;
        padding-top: 4mm;
        border-top: 1px solid #CBD5E1;
    }}
    
    @bottom-right {{
        content: "Página " counter(page) " de " counter(pages);
        font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif;
        font-size: 8pt;
        font-weight: bold;
        color: #202730;
        vertical-align: top;
        padding-top: 4mm;
        border-top: 1px solid #CBD5E1;
    }}
}}

@page :first {{
    margin: 0;
    background-color: #202730;
    @top-left {{ content: none; }}
    @top-right {{ content: none; }}
    @bottom-left {{ content: none; }}
    @bottom-right {{ content: none; }}
}}

@page dark-break {{
    margin: 0;
    background-color: #202730;
    @top-left {{ content: none; }}
    @top-right {{ content: none; }}
    @bottom-left {{ content: none; }}
    @bottom-right {{ content: none; }}
}}

* {{
    box-sizing: border-box;
}}

body {{
    font-family: 'Liberation Sans', 'DejaVu Sans', system-ui, -apple-system, sans-serif;
    color: #202730;
    background-color: #F1ECE6;
    line-height: 1.6;
    font-size: 10pt;
    margin: 0;
    padding: 0;
}}

/* ===================================================
   CAPA ESCURA (COVER PAGE)
   =================================================== */
.cover-page {{
    page: dark-break;
    height: 100vh;
    padding: 35mm 22mm 22mm 22mm;
    background-color: #202730;
    color: #FFFFFF;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-after: always;
    box-sizing: border-box;
}}

.cover-header {{
    border-bottom: 2px solid rgba(92, 225, 230, 0.35);
    padding-bottom: 12px;
}}

.cover-header .tagline {{
    font-size: 10pt;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #94A3B8;
    font-weight: 700;
}}

.cover-badge-top {{
    display: inline-block;
    background: rgba(92, 225, 230, 0.15);
    border: 1px solid #5CE1E6;
    color: #5CE1E6;
    padding: 5px 14px;
    border-radius: 9999px;
    font-size: 8.5pt;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 18px;
}}

.cover-title {{
    font-size: 42pt;
    font-weight: 800;
    line-height: 1.05;
    margin: 0 0 16px 0;
    letter-spacing: -0.5px;
    color: #FFFFFF;
}}

.cover-title .cyan {{
    color: #5CE1E6;
}}

.cover-subtitle {{
    font-size: 14pt;
    font-weight: 400;
    color: #E2E8F0;
    line-height: 1.45;
    margin: 0 0 28px 0;
    max-width: 90%;
}}

.cover-cards-grid {{
    display: flex;
    gap: 14px;
    margin-top: 10px;
}}

.cover-mini-card {{
    flex: 1;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(92, 225, 230, 0.25);
    border-radius: 12px;
    padding: 14px 16px;
}}

.cover-mini-card .num {{
    color: #5CE1E6;
    font-size: 9pt;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 4px;
}}

.cover-mini-card .desc {{
    color: #E2E8F0;
    font-size: 8.5pt;
    line-height: 1.35;
    font-weight: 600;
}}

.cover-footer {{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    padding-top: 18px;
}}

.cover-meta {{
    font-size: 8.5pt;
    color: #94A3B8;
    line-height: 1.5;
}}

.cover-logo img {{
    height: 42px;
    width: auto;
}}

/* ===================================================
   DIVISOR DE SEÇÃO ESCURO (SECTION BREAK)
   =================================================== */
.section-divider {{
    page: dark-break;
    height: 100vh;
    padding: 45mm 22mm 22mm 22mm;
    background-color: #202730;
    color: #FFFFFF;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    page-break-before: always;
    page-break-after: always;
    box-sizing: border-box;
}}

.section-tag {{
    font-size: 11pt;
    font-weight: 700;
    color: #5CE1E6;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    margin-bottom: 14px;
}}

.section-divider h1 {{
    font-size: 28pt;
    font-weight: 800;
    line-height: 1.2;
    margin: 0 0 18px 0;
    color: #FFFFFF;
    border: none;
    padding: 0;
}}

.section-divider p {{
    font-size: 12pt;
    color: #CBD5E1;
    line-height: 1.55;
    max-width: 90%;
    margin-bottom: 24px;
}}

.module-pill-list {{
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}}

.module-pill {{
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(92, 225, 230, 0.4);
    color: #E2E8F0;
    padding: 6px 14px;
    border-radius: 8px;
    font-size: 8.5pt;
    font-weight: 600;
}}

/* ===================================================
   PÁGINAS CLARAS DE CONTEÚDO (CARDS & TYPOGRAPHY)
   =================================================== */
.content-wrapper {{
    page-break-before: always;
    margin-bottom: 20px;
}}

.section-badge {{
    display: inline-block;
    background-color: #202730;
    color: #5CE1E6;
    font-size: 7.5pt;
    font-weight: 800;
    padding: 4px 10px;
    border-radius: 6px;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 12px;
}}

.card {{
    background-color: #FFFFFF;
    border-radius: 14px;
    padding: 20px 24px;
    margin-bottom: 18px;
    box-shadow: 0 3px 12px rgba(32, 39, 48, 0.04);
    border: 1px solid rgba(32, 39, 48, 0.08);
}}

h1, h2, h3, h4 {{
    color: #202730;
    font-weight: 800;
    break-after: avoid;
    page-break-after: avoid;
}}

h1 {{
    font-size: 17pt;
    border-bottom: 2.5px solid #5CE1E6;
    padding-bottom: 6px;
    margin-top: 0;
    margin-bottom: 16px;
}}

h2 {{
    font-size: 13pt;
    margin-top: 20px;
    margin-bottom: 12px;
    color: #202730;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

h3 {{
    font-size: 11pt;
    margin-top: 16px;
    margin-bottom: 8px;
    color: #1E293B;
}}

p {{
    margin-top: 0;
    margin-bottom: 12px;
    color: #334155;
    line-height: 1.55;
}}

ul, ol {{
    margin-top: 0;
    margin-bottom: 14px;
    padding-left: 22px;
    color: #334155;
}}

li {{
    margin-bottom: 5px;
    line-height: 1.5;
}}

strong {{
    color: #202730;
}}

/* ===================================================
   TABELAS NO ESTILO TRACK
   =================================================== */
.table-container {{
    margin: 14px 0;
    break-inside: avoid;
    page-break-inside: avoid;
}}

table, .track-table {{
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    margin: 14px 0;
    border-radius: 10px;
    overflow: hidden;
    background: #FFFFFF;
    border: 1px solid rgba(32, 39, 48, 0.12);
    font-size: 9pt;
    break-inside: avoid;
    page-break-inside: avoid;
}}

th {{
    background-color: #202730;
    color: #FFFFFF;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    font-size: 8pt;
    padding: 10px 12px;
    text-align: left;
    border-bottom: 2.5px solid #5CE1E6;
}}

td {{
    padding: 8px 12px;
    border-bottom: 1px solid #E2E8F0;
    color: #334155;
    line-height: 1.4;
}}

tr:nth-child(even) td {{
    background-color: #F8FAFC;
}}

tr:last-child td {{
    border-bottom: none;
}}

/* ===================================================
   BLOCOS DE CÓDIGO E PROMPTS
   =================================================== */
pre {{
    background-color: #1A222B;
    color: #F8FAFC;
    border-radius: 10px;
    padding: 14px 16px;
    font-family: 'Liberation Mono', 'DejaVu Sans Mono', monospace;
    font-size: 8.5pt;
    line-height: 1.45;
    border-left: 3.5px solid #5CE1E6;
    margin: 14px 0;
    white-space: pre-wrap;
    word-wrap: break-word;
    break-inside: avoid;
    page-break-inside: avoid;
}}

code {{
    font-family: 'Liberation Mono', 'DejaVu Sans Mono', monospace;
    font-size: 8.5pt;
    background-color: rgba(32, 39, 48, 0.08);
    color: #0F172A;
    padding: 2px 5px;
    border-radius: 4px;
}}

pre code {{
    background-color: transparent;
    color: inherit;
    padding: 0;
}}

blockquote {{
    background-color: #F4EFEB;
    border-left: 3.5px solid #5CE1E6;
    border-radius: 0 10px 10px 0;
    padding: 12px 18px;
    margin: 14px 0;
    color: #1E293B;
    break-inside: avoid;
    page-break-inside: avoid;
}}

blockquote p:last-child {{
    margin-bottom: 0;
}}
"""

def generate_pdf():
    print("Gerando manual completo do curso no Track Document Design Style...")
    
    sections = []
    
    # 1. CAPA ESCURA
    sections.append(f"""
    <div class="cover-page">
        <div class="cover-header">
            <div class="tagline">TRACK • Inovação e Tecnologia</div>
        </div>
        <div>
            <div class="cover-badge-top">PROGRAMA DE CAPACITAÇÃO EM IA</div>
            <h1 class="cover-title">IAGen-<span class="cyan">basics</span></h1>
            <p class="cover-subtitle">IA Generativa Aplicada à Automação de Escritório e Engenharia Civil</p>
            <div class="cover-cards-grid">
                <div class="cover-mini-card">
                    <div class="num">Módulo 01</div>
                    <div class="desc">Fundamentos, RTCC & RDO Automatizado</div>
                </div>
                <div class="cover-mini-card">
                    <div class="num">Módulo 02</div>
                    <div class="desc">Google Workspace, Sheets & Dashboards SVG</div>
                </div>
                <div class="cover-mini-card">
                    <div class="num">Módulo 03</div>
                    <div class="desc">Gems, Claude Projects & Mini-Apps Web</div>
                </div>
            </div>
        </div>
        <div class="cover-footer">
            <div class="cover-meta">
                <strong>Track Document Design Style</strong><br>
                12 Horas de Imersão • 3 Sessões de 4 Horas<br>
                Edição 2026.1 • Versão Consolidada
            </div>
            <div class="cover-logo">
                <img src="data:image/png;base64,{LOGO_B64}" alt="Track Logo">
            </div>
        </div>
    </div>
    """)
    
    # 2. SUMÁRIO / ÍNDICE EXECUTIVO
    sections.append(f"""
    <div class="content-wrapper">
        <div class="section-badge">Estrutura do Curso</div>
        <div class="card">
            <h1>Sumário Executivo do Programa</h1>
            <p>O <strong>IAGen-basics</strong> é um programa de imersão de 12 horas estruturado em três blocos operacionais de 4 horas cada, combinando fundamentação estratégica e sprints práticos ancorados na rotina técnica da Track.</p>
            
            <table class="track-table">
                <thead>
                    <tr>
                        <th style="width: 15%;">Encontro</th>
                        <th style="width: 45%;">Temas Centrais & Foco Técnico</th>
                        <th style="width: 40%;">Entregáveis & Ativos Operacionais</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Dia 1</strong></td>
                        <td>Fundamentos de LLMs (Claude vs Gemini vs ChatGPT), Modo Raciocínio, RTCC, Extração de relatos e Claude Artifacts.</td>
                        <td>Relatório Diário de Obra (RDO), Notificação NR-18 e Auditoria de Memorial Descritivo.</td>
                    </tr>
                    <tr>
                        <td><strong>Dia 2</strong></td>
                        <td>Integração Google Workspace (Docs/Sheets), fórmulas de Curva ABC, Dashboards vetoriais em SVG e Comunicação Multi-canal.</td>
                        <td>Planilha de desvios SINAPI reconciliada, Dashboard Executivo da Obra e Apresentação Executiva.</td>
                    </tr>
                    <tr>
                        <td><strong>Dia 3</strong></td>
                        <td>Assistentes persistentes (Gemini Gems vs Claude Projects), bases de conhecimento de NBRs e prototipagem de Mini-Apps em Artifacts.</td>
                        <td>Assistente "Fiscal de Qualidade Track" em Gem/Project e Calculadora de Concreto web interativa.</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    """)
    
    # 3. VISÃO GERAL (README)
    readme_html = md_to_html(os.path.join(COURSE_DIR, "README.md"))
    sections.append(f"""
    <div class="content-wrapper">
        <div class="section-badge">Apresentação & Metodologia</div>
        <div class="card">
            {readme_html}
        </div>
    </div>
    """)
    
    # 4. EMENTA COMPLETA
    ementa_html = md_to_html(os.path.join(COURSE_DIR, "ementa", "ementa_detalhada.md"))
    sections.append(f"""
    <div class="content-wrapper">
        <div class="section-badge">Plano Pedagógico</div>
        <div class="card">
            {ementa_html}
        </div>
    </div>
    """)
    
    # 5. CHECKLIST PRÉ-CURSO
    checklist_html = md_to_html(os.path.join(COURSE_DIR, "recursos", "checklist_preparacao.md"))
    sections.append(f"""
    <div class="content-wrapper">
        <div class="section-badge">Ambiente & Requisitos</div>
        <div class="card">
            {checklist_html}
        </div>
    </div>
    """)
    
    # ==========================================
    # DIA 1: DIVISOR + CONTEÚDOS
    # ==========================================
    sections.append(f"""
    <div class="section-divider">
        <div>
            <div class="section-tag">Módulo 01 • Encontro de 4 Horas</div>
            <h1>Dia 1: Fundamentos, Panorama e Engenharia de Prompts na Construção</h1>
            <p>Compreensão profunda das capacidades e restrições dos modelos de fronteira (Claude 3.5, Gemini 1.5/2.0 e ChatGPT), engenharia de prompts de alta precisão técnica e conversão de áudios brutos de obra em entregáveis formais.</p>
            <div class="module-pill-list">
                <span class="module-pill">Comparativo de LLMs</span>
                <span class="module-pill">Framework RTCC</span>
                <span class="module-pill">RDO Automatizado</span>
                <span class="module-pill">Claude Artifacts</span>
            </div>
        </div>
        <div class="cover-footer">
            <div class="cover-meta">
                Módulo Prático: 2 Sprints de Execução<br>
                Instrutor: Track Inovação e Tecnologia
            </div>
            <div class="cover-logo">
                <img src="data:image/png;base64,{LOGO_B64}" alt="Track Logo">
            </div>
        </div>
    </div>
    """)
    
    dia1_guia = md_to_html(os.path.join(COURSE_DIR, "dia-1", "guia_instrutor.md"))
    dia1_lab1 = md_to_html(os.path.join(COURSE_DIR, "dia-1", "exercicios", "lab1_rdo_transcricao.md"))
    with open(os.path.join(COURSE_DIR, "dia-1", "dados", "transcricao_obra_bruta.txt"), "r", encoding="utf-8") as f:
        transcricao_txt = f.read()
    dia1_lab2 = md_to_html(os.path.join(COURSE_DIR, "dia-1", "exercicios", "lab2_analise_edital_artifacts.md"))
    dia1_dados2 = md_to_html(os.path.join(COURSE_DIR, "dia-1", "dados", "trecho_memorial_descritivo.md"))
    dia1_prompts = md_to_html(os.path.join(COURSE_DIR, "dia-1", "prompts", "prompts_dia1.md"))
    
    sections.append(f"""
    <div class="content-wrapper">
        <div class="section-badge">Dia 1 • Roteiro do Facilitador</div>
        <div class="card">{dia1_guia}</div>
    </div>
    <div class="content-wrapper">
        <div class="section-badge">Dia 1 • Sprint Prático 1</div>
        <div class="card">{dia1_lab1}</div>
        <div class="card">
            <h2>Dados de Apoio: Relato Bruto de Canteiro (Transcrição)</h2>
            <pre><code>{transcricao_txt}</code></pre>
        </div>
    </div>
    <div class="content-wrapper">
        <div class="section-badge">Dia 1 • Sprint Prático 2</div>
        <div class="card">{dia1_lab2}</div>
        <div class="card">{dia1_dados2}</div>
    </div>
    <div class="content-wrapper">
        <div class="section-badge">Dia 1 • Ativo Operacional</div>
        <div class="card">{dia1_prompts}</div>
    </div>
    """)
    
    # ==========================================
    # DIA 2: DIVISOR + CONTEÚDOS
    # ==========================================
    sections.append(f"""
    <div class="section-divider">
        <div>
            <div class="section-tag">Módulo 02 • Encontro de 4 Horas</div>
            <h1>Dia 2: Documentos, Planilhas, Dashboards e Comunicação Multi-canal</h1>
            <p>Integração dos LLMs ao Google Workspace (Sheets, Docs, Slides), geração de fórmulas de orçamentação e Curva ABC, criação de dashboards vetoriais em SVG e comunicação em cascata para múltiplos interlocutores.</p>
            <div class="module-pill-list">
                <span class="module-pill">Google Sheets & Gemini</span>
                <span class="module-pill">Fórmulas & Análise SINAPI</span>
                <span class="module-pill">Dashboards Vetoriais em SVG</span>
                <span class="module-pill">E-mail & WhatsApp Executivo</span>
            </div>
        </div>
        <div class="cover-footer">
            <div class="cover-meta">
                Módulo Prático: 2 Sprints de Execução<br>
                Instrutor: Track Inovação e Tecnologia
            </div>
            <div class="cover-logo">
                <img src="data:image/png;base64,{LOGO_B64}" alt="Track Logo">
            </div>
        </div>
    </div>
    """)
    
    dia2_guia = md_to_html(os.path.join(COURSE_DIR, "dia-2", "guia_instrutor.md"))
    dia2_lab1 = md_to_html(os.path.join(COURSE_DIR, "dia-2", "exercicios", "lab1_planilhas_orcamento_sheets.md"))
    dia2_csv = csv_to_html(os.path.join(COURSE_DIR, "dia-2", "dados", "orcamento_obra_amostra.csv"))
    dia2_lab2 = md_to_html(os.path.join(COURSE_DIR, "dia-2", "exercicios", "lab2_dashboard_comunicacao_artifacts.md"))
    dia2_prompts = md_to_html(os.path.join(COURSE_DIR, "dia-2", "prompts", "prompts_dia2.md"))
    
    sections.append(f"""
    <div class="content-wrapper">
        <div class="section-badge">Dia 2 • Roteiro do Facilitador</div>
        <div class="card">{dia2_guia}</div>
    </div>
    <div class="content-wrapper">
        <div class="section-badge">Dia 2 • Sprint Prático 1</div>
        <div class="card">{dia2_lab1}</div>
        <div class="card">
            <h2>Dados de Apoio: Amostra Orçamentária de Obra (Base SINAPI)</h2>
            {dia2_csv}
        </div>
    </div>
    <div class="content-wrapper">
        <div class="section-badge">Dia 2 • Sprint Prático 2</div>
        <div class="card">{dia2_lab2}</div>
    </div>
    <div class="content-wrapper">
        <div class="section-badge">Dia 2 • Ativo Operacional</div>
        <div class="card">{dia2_prompts}</div>
    </div>
    """)
    
    # ==========================================
    # DIA 3: DIVISOR + CONTEÚDOS
    # ==========================================
    sections.append(f"""
    <div class="section-divider">
        <div>
            <div class="section-tag">Módulo 03 • Encontro de 4 Horas</div>
            <h1>Dia 3: Assistentes Especializados (Gems & Projects) e Mini-Apps Interativos</h1>
            <p>Criação de agentes personalizados com memória institucional perene (Gemini Gems e Claude Projects) abastecidos com normas e políticas da empresa, e prototipagem ágil de mini-aplicações web interativas com Claude Artifacts.</p>
            <div class="module-pill-list">
                <span class="module-pill">Gemini Gems Personalizadas</span>
                <span class="module-pill">Claude Projects Knowledge Base</span>
                <span class="module-pill">Diretrizes NBR 6118 / NR-18</span>
                <span class="module-pill">Mini-Apps Web Funcionais</span>
            </div>
        </div>
        <div class="cover-footer">
            <div class="cover-meta">
                Módulo Prático: 2 Sprints de Execução<br>
                Instrutor: Track Inovação e Tecnologia
            </div>
            <div class="cover-logo">
                <img src="data:image/png;base64,{LOGO_B64}" alt="Track Logo">
            </div>
        </div>
    </div>
    """)
    
    dia3_guia = md_to_html(os.path.join(COURSE_DIR, "dia-3", "guia_instrutor.md"))
    dia3_lab1 = md_to_html(os.path.join(COURSE_DIR, "dia-3", "exercicios", "lab1_criando_gems_e_projects.md"))
    dia3_dados1 = md_to_html(os.path.join(COURSE_DIR, "dia-3", "dados", "base_conhecimento_mock_nbr.md"))
    dia3_lab2 = md_to_html(os.path.join(COURSE_DIR, "dia-3", "exercicios", "lab2_mini_app_calculadora_concreto.md"))
    dia3_prompts = md_to_html(os.path.join(COURSE_DIR, "dia-3", "prompts", "prompts_dia3.md"))
    
    sections.append(f"""
    <div class="content-wrapper">
        <div class="section-badge">Dia 3 • Roteiro do Facilitador</div>
        <div class="card">{dia3_guia}</div>
    </div>
    <div class="content-wrapper">
        <div class="section-badge">Dia 3 • Sprint Prático 1</div>
        <div class="card">{dia3_lab1}</div>
        <div class="card">{dia3_dados1}</div>
    </div>
    <div class="content-wrapper">
        <div class="section-badge">Dia 3 • Sprint Prático 2</div>
        <div class="card">{dia3_lab2}</div>
    </div>
    <div class="content-wrapper">
        <div class="section-badge">Dia 3 • Ativo Operacional</div>
        <div class="card">{dia3_prompts}</div>
    </div>
    """)
    
    # 7. CONTRACAPA ESCURA
    sections.append(f"""
    <div class="cover-page">
        <div class="cover-header">
            <div class="tagline">TRACK • Inovação e Tecnologia</div>
        </div>
        <div>
            <div class="cover-badge-top">TRANSFORMAÇÃO DIGITAL</div>
            <h1 class="cover-title">Construindo o Futuro com <span class="cyan">Inteligência</span></h1>
            <p class="cover-subtitle">A adoção de Inteligência Artificial Generativa em engenharia civil e gestão corporativa transforma dados brutos em decisões ágeis, reduzindo retrabalho e elevando o padrão de conformidade técnica.</p>
        </div>
        <div class="cover-footer">
            <div class="cover-meta">
                <strong>Track Document Design Style</strong><br>
                Repositório Oficial: github.com/track-iagen/basic-llm<br>
                Todos os direitos reservados • 2026
            </div>
            <div class="cover-logo">
                <img src="data:image/png;base64,{LOGO_B64}" alt="Track Logo">
            </div>
        </div>
    </div>
    """)
    
    # MONTAGEM FINAL DO HTML
    full_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>IAGen-basics • Manual do Curso (Track Document Design Style)</title>
<style>
{CSS_STYLES}
</style>
</head>
<body>
{"".join(sections)}
</body>
</html>
"""
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"HTML compilado em: {OUTPUT_HTML}")
    
    print("Compilando PDF final via WeasyPrint...")
    cmd = ["/home/fcfmc/.local/bin/weasyprint", OUTPUT_HTML, OUTPUT_PDF]
    subprocess.run(cmd, check=True)
    print(f"PDF gerado com sucesso: {OUTPUT_PDF}")

if __name__ == "__main__":
    generate_pdf()
