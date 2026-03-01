#!/usr/bin/env python3
"""
KDP HTML to PDF Converter
Converte HTML formatado para PDF compatível com KDP.
"""

import sys
import os
import argparse
import subprocess
from pathlib import Path


def convert_with_puppeteer(html_path, output_path, trim_size="6x9"):
    """
    Converte HTML para PDF usando Puppeteer (Node.js).
    """
    js_script = f"""
const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {{
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  const html = fs.readFileSync('{html_path}', 'utf8');
  await page.setContent(html, {{ waitUntil: 'networkidle0' }});

  await page.pdf({{
    path: '{output_path}',
    format: undefined,  // Usar @page CSS
    printBackground: true,
    margin: {{ top: 0, right: 0, bottom: 0, left: 0 }}
  }});

  await browser.close();
  console.log('PDF gerado: {output_path}');
}})();
"""

    script_path = Path("/tmp/kdp-pdf-generator.js")
    script_path.write_text(js_script)

    try:
        subprocess.run(["node", str(script_path)], check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def convert_with_weasyprint(html_path, output_path):
    """
    Converte HTML para PDF usando WeasyPrint (Python).
    """
    try:
        import weasyprint

        html = weasyprint.HTML(filename=html_path)
        html.write_pdf(output_path)
        return True
    except ImportError:
        return False


def generate_browser_instructions(html_path, output_path):
    """
    Gera instruções para conversão via navegador.
    """
    instructions = f"""
╔══════════════════════════════════════════════════════════════╗
║     CONVERSÃO HTML PARA PDF VIA NAVEGADOR                    ║
╚══════════════════════════════════════════════════════════════╝

Para converter o HTML em PDF KDP-ready:

1. Abra o arquivo no navegador:
   file://{html_path.absolute()}

2. Pressione Ctrl+P (Cmd+P no Mac) para imprimir

3. Configure as opções de impressão:
   ✓ Destino: Salvar como PDF
   ✓ Tamanho: Usar configurações da página (definido no CSS)
   ✓ Margens: Nenhuma (estão definidas no CSS)
   ✓ Fundos gráficos: Ativado

4. Clique em Salvar

5. Valide o PDF gerado com:
   python ~/.claude/skills/kdp-book-formatter/scripts/validate-pdf.py {output_path}

"""
    return instructions


def main():
    parser = argparse.ArgumentParser(description="Converte HTML para PDF KDP")
    parser.add_argument("html", help="Arquivo HTML de entrada")
    parser.add_argument("-o", "--output", default="output.pdf", help="Arquivo PDF de saída")
    parser.add_argument("--method", choices=["auto", "puppeteer", "weasyprint", "browser"],
                      default="auto", help="Método de conversão")
    args = parser.parse_args()

    html_path = Path(args.html).resolve()
    output_path = Path(args.output).resolve()

    if not html_path.exists():
        print(f"Erro: Arquivo HTML não encontrado: {html_path}")
        sys.exit(1)

    # Criar diretório de saída
    output_path.parent.mkdir(parents=True, exist_ok=True)

    method = args.method

    if method == "auto":
        # Tentar WeasyPrint primeiro
        if convert_with_weasyprint(html_path, output_path):
            print(f"✓ PDF gerado com WeasyPrint: {output_path}")
            sys.exit(0)

        # Tentar Puppeteer
        if convert_with_puppeteer(html_path, output_path):
            print(f"✓ PDF gerado com Puppeteer: {output_path}")
            sys.exit(0)

        # Se nenhum funcionar, mostrar instruções do navegador
        print("⚠ Nenhuma biblioteca de PDF encontrada.")
        print(generate_browser_instructions(html_path, output_path))
        sys.exit(1)

    elif method == "puppeteer":
        if not convert_with_puppeteer(html_path, output_path):
            print("✗ Erro ao converter com Puppeteer")
            print("Instale: npm install puppeteer")
            sys.exit(1)

    elif method == "weasyprint":
        if not convert_with_weasyprint(html_path, output_path):
            print("✗ Erro ao converter com WeasyPrint")
            print("Instale: pip install weasyprint")
            sys.exit(1)

    elif method == "browser":
        print(generate_browser_instructions(html_path, output_path))
        # Abrir no navegador
        import webbrowser
        webbrowser.open(f"file://{html_path}")


if __name__ == "__main__":
    main()
