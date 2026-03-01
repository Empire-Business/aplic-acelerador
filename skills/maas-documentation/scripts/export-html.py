#!/usr/bin/env python3
"""
MAAS Documentation — HTML Exporter

Converte documentação MAAS em Markdown para HTML interativo com:
- Navegação lateral recolhível
- Diagramas Mermaid renderizados
- Modo claro/escuro
- Botão "Exportar PDF" (print dialog)

Usage:
    python export-html.py documento.md [output.html]

Author: MAAS Skill
Version: 1.0.0
"""

import argparse
import re
import sys
from pathlib import Path
from datetime import datetime


class MAASHTMLExporter:
    """Converte Markdown MAAS para HTML interativo."""

    def __init__(self, markdown_path: str, output_path: str = None):
        self.markdown_path = Path(markdown_path)
        self.output_path = Path(output_path) if output_path else self.markdown_path.with_suffix('.html')
        self.title = self.markdown_path.stem
        self.toc_items = []

    def read_markdown(self) -> str:
        """Lê o arquivo Markdown."""
        if not self.markdown_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {self.markdown_path}")
        return self.markdown_path.read_text(encoding='utf-8')

    def parse_toc(self, content: str) -> str:
        """Extrai cabeçalhos para o índice e adiciona IDs."""
        lines = content.split('\n')
        result = []
        section_counter = [0, 0, 0]  # h1, h2, h3

        for line in lines:
            # Match headings
            match = re.match(r'^(#{1,3})\s+(.+)$', line)
            if match:
                level = len(match.group(1))
                text = match.group(2).strip()
                section_counter[level - 1] += 1
                # Reset counters for deeper levels
                for i in range(level, 3):
                    section_counter[i] = 0

                # Create ID from text
                slug = re.sub(r'[^\w\s-]', '', text.lower())
                slug = re.sub(r'[\s_]+', '-', slug).strip('-')
                section_id = f"section-{slug}"

                # Add to TOC
                self.toc_items.append({
                    'level': level,
                    'text': text,
                    'id': section_id
                })

                # Replace line with anchored heading
                result.append(f'{match.group(1)} <span id="{section_id}">{text}</span>')
            else:
                result.append(line)

        return '\n'.join(result)

    def convert_markdown_to_html(self, content: str) -> str:
        """Converte Markdown básico para HTML."""
        html = content

        # Code blocks with language
        html = re.sub(
            r'```(\w*)\n(.*?)```',
            lambda m: self._code_block(m.group(2), m.group(1)),
            html,
            flags=re.DOTALL
        )

        # Inline code
        html = re.sub(r'`([^`]+)`', r'<code class="inline-code">\1</code>', html)

        # Bold
        html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', html)

        # Italic
        html = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', html)

        # Headings (já processados no parse_toc)
        html = re.sub(r'^###\s+<span id="([^"]+)">([^<]+)</span>$',
                      r'<h3 id="\1">\2</h3>', html, flags=re.MULTILINE)
        html = re.sub(r'^##\s+<span id="([^"]+)">([^<]+)</span>$',
                      r'<h2 id="\1">\2</h2>', html, flags=re.MULTILINE)
        html = re.sub(r'^#\s+<span id="([^"]+)">([^<]+)</span>$',
                      r'<h1 id="\1">\2</h1>', html, flags=re.MULTILINE)

        # Links
        html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', html)

        # Unordered lists
        html = self._convert_lists(html)

        # Tables
        html = self._convert_tables(html)

        # Blockquotes
        html = re.sub(r'^>\s+(.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)

        # Horizontal rules
        html = re.sub(r'^-{3,}$', r'<hr>', html, flags=re.MULTILINE)

        # Line breaks and paragraphs
        html = self._wrap_paragraphs(html)

        return html

    def _code_block(self, code: str, lang: str) -> str:
        """Formata bloco de código."""
        # Detect Mermaid
        if lang == 'mermaid':
            return f'<div class="mermaid">{code.strip()}</div>'

        # Outras linguagens
        lang_attr = f' data-language="{lang}"' if lang else ''
        return f'<pre class="code-block"{lang_attr}><code>{self._escape_html(code.strip())}</code></pre>'

    def _convert_lists(self, html: str) -> str:
        """Converte listas Markdown para HTML."""
        lines = html.split('\n')
        result = []
        in_ul = False
        in_ol = False

        for line in lines:
            # Unordered list
            if re.match(r'^[\*\-]\s+', line):
                if not in_ul:
                    result.append('<ul>')
                    in_ul = True
                content = re.sub(r'^[\*\-]\s+', '', line)
                result.append(f'<li>{content}</li>')
            elif re.match(r'^\d+\.\s+', line):
                if in_ul:
                    result.append('</ul>')
                    in_ul = False
                if not in_ol:
                    result.append('<ol>')
                    in_ol = True
                content = re.sub(r'^\d+\.\s+', '', line)
                result.append(f'<li>{content}</li>')
            else:
                if in_ul:
                    result.append('</ul>')
                    in_ul = False
                if in_ol:
                    result.append('</ol>')
                    in_ol = False
                result.append(line)

        if in_ul:
            result.append('</ul>')
        if in_ol:
            result.append('</ol>')

        return '\n'.join(result)

    def _convert_tables(self, html: str) -> str:
        """Converte tabelas Markdown para HTML."""
        lines = html.split('\n')
        result = []
        in_table = False
        in_header = False

        for line in lines:
            if line.startswith('|') and line.endswith('|'):
                if not in_table:
                    result.append('<table>')
                    in_table = True
                    in_header = True
                    result.append('<thead>')
                    result.append('<tr>')

                cells = [cell.strip() for cell in line.split('|')[1:-1]]

                for cell in cells:
                    if not re.match(r'^:?-+:?$', cell):  # Not separator
                        tag = 'th' if in_header else 'td'
                        result.append(f'<{tag}>{cell}</{tag}>')

                if in_header:
                    result.append('</tr>')
                    result.append('</thead>')
                    result.append('<tbody>')
                    in_header = False
                else:
                    result.append('</tr>')
            else:
                if in_table:
                    if in_header:
                        result.append('</tr>')
                        result.append('</thead>')
                        result.append('<tbody>')
                        in_header = False
                    result.append('</tbody>')
                    result.append('</table>')
                    in_table = False
                result.append(line)

        if in_table:
            result.append('</tbody>')
            result.append('</table>')

        return '\n'.join(result)

    def _wrap_paragraphs(self, html: str) -> str:
        """Envolve texto em parágrafos."""
        lines = html.split('\n')
        result = []
        in_paragraph = False

        for line in lines:
            # Skip empty lines and block elements
            if not line.strip() or line.startswith('<'):
                if in_paragraph:
                    result.append('</p>')
                    in_paragraph = False
                result.append(line)
            else:
                if not in_paragraph:
                    result.append('<p>')
                    in_paragraph = True
                result.append(line + ' ')

        if in_paragraph:
            result.append('</p>')

        return '\n'.join(result)

    def _escape_html(self, text: str) -> str:
        """Escapa caracteres HTML."""
        return (text.replace('&', '&amp;')
                   .replace('<', '&lt;')
                   .replace('>', '&gt;')
                   .replace('"', '&quot;'))

    def generate_toc_html(self) -> str:
        """Gera HTML do índice lateral."""
        if not self.toc_items:
            return '<p class="toc-empty">Nenhuma seção encontrada</p>'

        html = ['<nav class="toc">']
        html.append('<h3>Índice</h3>')
        html.append('<ul class="toc-list">')

        for item in self.toc_items:
            indent = (item['level'] - 1) * 16
            html.append(f'<li class="toc-item toc-level-{item["level"]}" '
                       f'style="margin-left: {indent}px">')
            html.append(f'<a href="#{item["id"]}">{item["text"]}</a>')
            html.append('</li>')

        html.append('</ul>')
        html.append('</nav>')

        return '\n'.join(html)

    def generate_html(self, markdown_content: str) -> str:
        """Gera HTML completo."""
        # Parse and convert
        content_with_ids = self.parse_toc(markdown_content)
        body_content = self.convert_markdown_to_html(content_with_ids)
        toc_html = self.generate_toc_html()

        # HTML template
        html_template = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title} — MAAS Documentation</title>

    <!-- Mermaid.js para diagramas -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>

    <style>
        /* ===========================================
           CSS CUSTOM PROPERTIES
           =========================================== */
        :root {{
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --bg-tertiary: #334155;
            --text-primary: #f1f5f9;
            --text-secondary: #94a3b8;
            --accent: #3b82f6;
            --accent-hover: #2563eb;
            --border: #334155;
            --code-bg: #1e293b;
            --toc-bg: #1e293b;
            --success: #22c55e;
            --warning: #f59e0b;
        }}

        .light-mode {{
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --bg-tertiary: #e2e8f0;
            --text-primary: #1e293b;
            --text-secondary: #64748b;
            --accent: #2563eb;
            --accent-hover: #1d4ed8;
            --border: #e2e8f0;
            --code-bg: #f1f5f9;
            --toc-bg: #f8fafc;
        }}

        /* ===========================================
           BASE STYLES
           =========================================== */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.7;
            transition: background 0.3s, color 0.3s;
        }}

        /* ===========================================
           LAYOUT
           =========================================== */
        .container {{
            display: flex;
            min-height: 100vh;
        }}

        /* Sidebar / TOC */
        .sidebar {{
            width: 280px;
            background: var(--toc-bg);
            border-right: 1px solid var(--border);
            padding: 2rem 1rem;
            position: fixed;
            height: 100vh;
            overflow-y: auto;
            transition: transform 0.3s;
            z-index: 100;
        }}

        .sidebar.collapsed {{
            transform: translateX(-280px);
        }}

        .sidebar h3 {{
            font-size: 0.875rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-secondary);
            margin-bottom: 1rem;
        }}

        .toc-list {{
            list-style: none;
        }}

        .toc-item {{
            margin-bottom: 0.25rem;
        }}

        .toc-level-1 {{
            font-weight: 600;
        }}

        .toc-level-2 {{
            font-weight: 400;
            color: var(--text-secondary);
        }}

        .toc-level-3 {{
            font-weight: 400;
            font-size: 0.875rem;
            color: var(--text-secondary);
        }}

        .toc a {{
            color: var(--text-primary);
            text-decoration: none;
            display: block;
            padding: 0.375rem 0.5rem;
            border-radius: 0.375rem;
            transition: background 0.2s;
        }}

        .toc a:hover {{
            background: var(--bg-tertiary);
        }}

        /* Main content */
        .main {{
            flex: 1;
            margin-left: 280px;
            padding: 3rem 4rem;
            max-width: 900px;
        }}

        .main.expanded {{
            margin-left: 0;
        }}

        /* ===========================================
           HEADER
           =========================================== */
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 3rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--border);
        }}

        .header h1 {{
            font-size: 1.5rem;
            font-weight: 700;
        }}

        .header-actions {{
            display: flex;
            gap: 0.75rem;
        }}

        .btn {{
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            border: 1px solid var(--border);
            background: var(--bg-secondary);
            color: var(--text-primary);
            cursor: pointer;
            font-size: 0.875rem;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .btn:hover {{
            background: var(--bg-tertiary);
            border-color: var(--accent);
        }}

        .btn-primary {{
            background: var(--accent);
            border-color: var(--accent);
            color: white;
        }}

        .btn-primary:hover {{
            background: var(--accent-hover);
        }}

        /* ===========================================
           CONTENT STYLES
           =========================================== */
        h1 {{
            font-size: 2.25rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            line-height: 1.2;
        }}

        h2 {{
            font-size: 1.75rem;
            font-weight: 700;
            margin-top: 3rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid var(--border);
        }}

        h3 {{
            font-size: 1.25rem;
            font-weight: 600;
            margin-top: 2rem;
            margin-bottom: 0.75rem;
        }}

        p {{
            margin-bottom: 1rem;
        }}

        a {{
            color: var(--accent);
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        /* Code blocks */
        .code-block {{
            background: var(--code-bg);
            border: 1px solid var(--border);
            border-radius: 0.5rem;
            padding: 1rem;
            overflow-x: auto;
            margin: 1rem 0;
            font-size: 0.875rem;
            line-height: 1.5;
        }}

        .inline-code {{
            background: var(--code-bg);
            padding: 0.125rem 0.375rem;
            border-radius: 0.25rem;
            font-size: 0.875em;
            color: var(--accent);
        }}

        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5rem 0;
            font-size: 0.875rem;
        }}

        th, td {{
            padding: 0.75rem;
            text-align: left;
            border-bottom: 1px solid var(--border);
        }}

        th {{
            font-weight: 600;
            background: var(--bg-secondary);
        }}

        tr:hover {{
            background: var(--bg-secondary);
        }}

        /* Lists */
        ul, ol {{
            margin-left: 1.5rem;
            margin-bottom: 1rem;
        }}

        li {{
            margin-bottom: 0.375rem;
        }}

        /* Blockquote */
        blockquote {{
            border-left: 4px solid var(--accent);
            padding-left: 1rem;
            margin: 1.5rem 0;
            color: var(--text-secondary);
            font-style: italic;
        }}

        /* Horizontal rule */
        hr {{
            border: none;
            border-top: 1px solid var(--border);
            margin: 2rem 0;
        }}

        /* ===========================================
           MERMAID DIAGRAMS
           =========================================== */
        .mermaid {{
            background: var(--bg-secondary);
            border-radius: 0.5rem;
            padding: 1.5rem;
            margin: 1.5rem 0;
            text-align: center;
        }}

        /* ===========================================
           MOBILE
           =========================================== */
        .menu-toggle {{
            display: none;
            position: fixed;
            bottom: 1.5rem;
            right: 1.5rem;
            width: 3.5rem;
            height: 3.5rem;
            border-radius: 50%;
            background: var(--accent);
            color: white;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            z-index: 200;
            font-size: 1.5rem;
        }}

        @media (max-width: 768px) {{
            .sidebar {{
                transform: translateX(-280px);
            }}

            .sidebar.open {{
                transform: translateX(0);
            }}

            .main {{
                margin-left: 0;
                padding: 2rem 1.5rem;
            }}

            .menu-toggle {{
                display: flex;
                align-items: center;
                justify-content: center;
            }}

            .header {{
                flex-direction: column;
                gap: 1rem;
                align-items: flex-start;
            }}

            .header-actions {{
                width: 100%;
            }}

            .btn {{
                flex: 1;
                justify-content: center;
            }}
        }}

        /* ===========================================
           PRINT STYLES
           =========================================== */
        @media print {{
            .sidebar, .menu-toggle, .header-actions {{
                display: none;
            }}

            .main {{
                margin: 0;
                padding: 1rem;
                max-width: 100%;
            }}

            body {{
                background: white;
                color: black;
            }}

            a {{
                color: black;
                text-decoration: underline;
            }}

            .code-block {{
                border: 1px solid #ccc;
                page-break-inside: avoid;
            }}

            table {{
                page-break-inside: avoid;
            }}

            h1, h2, h3 {{
                page-break-after: avoid;
            }}
        }}
    </style>
</head>
<body>
    <!-- Menu Toggle (mobile) -->
    <button class="menu-toggle" onclick="toggleSidebar()" aria-label="Toggle menu">☰</button>

    <div class="container">
        <!-- Sidebar / TOC -->
        <aside class="sidebar" id="sidebar">
            {toc_html}
        </aside>

        <!-- Main Content -->
        <main class="main" id="main">
            <header class="header">
                <h1>{self.title}</h1>
                <div class="header-actions">
                    <button class="btn" onclick="toggleTheme()">
                        <span id="theme-icon">🌙</span>
                        <span class="btn-text">Tema</span>
                    </button>
                    <button class="btn" onclick="toggleTOC()">
                        <span>☰</span>
                        <span class="btn-text">Índice</span>
                    </button>
                    <button class="btn btn-primary" onclick="exportPDF()">
                        <span>📄</span>
                        <span class="btn-text">Exportar PDF</span>
                    </button>
                </div>
            </header>

            <article class="content">
                {body_content}
            </article>

            <footer style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid var(--border); color: var(--text-secondary); font-size: 0.875rem;">
                <p>Gerado com <strong>MAAS Documentation Skill</strong> • {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
            </footer>
        </main>
    </div>

    <script>
        // ===========================================
        // MERMAID INITIALIZATION
        // ===========================================
        mermaid.initialize({{
            startOnLoad: true,
            theme: 'dark',
            themeVariables: {{
                primaryColor: '#3b82f6',
                primaryTextColor: '#f1f5f9',
                primaryBorderColor: '#3b82f6',
                lineColor: '#64748b',
                secondaryColor: '#1e293b',
                tertiaryColor: '#0f172a',
                background: '#0f172a',
                mainBkg: '#1e293b',
                nodeBorder: '#334155',
                clusterBkg: '#1e293b',
                clusterBorder: '#334155',
                titleColor: '#f1f5f9',
                edgeLabelBackground: '#1e293b',
            }}
        }});

        // ===========================================
        // THEME TOGGLE
        // ===========================================
        function toggleTheme() {{
            const body = document.body;
            const icon = document.getElementById('theme-icon');

            if (body.classList.contains('light-mode')) {{
                body.classList.remove('light-mode');
                icon.textContent = '🌙';
                mermaid.initialize({{ theme: 'dark' }});
                mermaid.init();
            }} else {{
                body.classList.add('light-mode');
                icon.textContent = '☀️';
                mermaid.initialize({{ theme: 'default' }});
                mermaid.init();
            }}
        }}

        // ===========================================
        // TOC TOGGLE
        // ===========================================
        function toggleTOC() {{
            const sidebar = document.getElementById('sidebar');
            const main = document.getElementById('main');

            sidebar.classList.toggle('collapsed');
            main.classList.toggle('expanded');
        }}

        // ===========================================
        // MOBILE MENU
        // ===========================================
        function toggleSidebar() {{
            const sidebar = document.getElementById('sidebar');
            sidebar.classList.toggle('open');
        }}

        // ===========================================
        // EXPORT PDF
        // ===========================================
        function exportPDF() {{
            // Close sidebar for cleaner print
            const sidebar = document.getElementById('sidebar');
            const wasCollapsed = sidebar.classList.contains('collapsed');

            sidebar.classList.add('collapsed');
            document.getElementById('main').classList.add('expanded');

            // Open print dialog
            window.print();

            // Restore state after print (user might cancel)
            setTimeout(() => {{
                if (!wasCollapsed) {{
                    sidebar.classList.remove('collapsed');
                    document.getElementById('main').classList.remove('expanded');
                }}
            }}, 100);
        }}

        // ===========================================
        // SMOOTH SCROLL WITH OFFSET
        // ===========================================
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    e.preventDefault();
                    const offsetTop = target.offsetTop - 20;
                    window.scrollTo({{
                        top: offsetTop,
                        behavior: 'smooth'
                    }});

                    // Close mobile menu
                    document.getElementById('sidebar').classList.remove('open');
                }}
            }});
        }});
    </script>
</body>
</html>'''

        return html_template

    def save_html(self, html_content: str):
        """Salva HTML no arquivo."""
        self.output_path.write_text(html_content, encoding='utf-8')
        return self.output_path

    def convert(self) -> Path:
        """Executa conversão completa."""
        print(f"📖 Lendo: {self.markdown_path}")
        markdown_content = self.read_markdown()

        print(f"🔄 Convertendo...")
        html_content = self.generate_html(markdown_content)

        print(f"💾 Salvando: {self.output_path}")
        self.save_html(html_content)

        print(f"✅ Sucesso! {len(self.toc_items)} seções encontradas.")
        print(f"📂 Abra: file://{self.output_path.absolute()}")

        return self.output_path


def main():
    """Ponto de entrada."""
    parser = argparse.ArgumentParser(
        description='Converte documentação MAAS Markdown para HTML interativo'
    )
    parser.add_argument('input', help='Arquivo Markdown de entrada')
    parser.add_argument('output', nargs='?', help='Arquivo HTML de saída (opcional)')
    parser.add_argument('-o', '--open', action='store_true', help='Abrir no browser após gerar')

    args = parser.parse_args()

    try:
        exporter = MAASHTMLExporter(args.input, args.output)
        output_path = exporter.convert()

        if args.open:
            import webbrowser
            webbrowser.open(f'file://{output_path.absolute()}')

        return 0
    except Exception as e:
        print(f"❌ Erro: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
