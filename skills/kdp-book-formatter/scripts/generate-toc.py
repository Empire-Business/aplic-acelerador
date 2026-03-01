#!/usr/bin/env python3
"""
KDP TOC Generator
Gera índice (Table of Contents) para livros KDP.
"""

import sys
import argparse
import re
from pathlib import Path


def extract_chapter_title(markdown_content):
    """
    Extrai o título do capítulo do Markdown.
    Assume que o primeiro H1 é o título.
    """
    match = re.search(r'^#\s+(.+)$', markdown_content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "Sem título"


def count_words(markdown_content):
    """
    Conta palavras em um texto Markdown.
    """
    # Remover blocos de código
    content = re.sub(r'```.*?```', '', markdown_content, flags=re.DOTALL)
    # Remover links e imagens
    content = re.sub(r'\[.*?\]\(.*?\)', '', content)
    content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
    # Contar palavras
    words = re.findall(r'\b\w+\b', content)
    return len(words)


def estimate_pages(word_count, trim_size="6x9"):
    """
    Estima número de páginas baseado em word count e trim size.
    """
    # Baseline: 300 palavras/página para 6x9, 11pt
    baseline = 300

    # Multiplicadores por trim size
    multipliers = {
        "5x8": 0.85,
        "5.25x8": 0.88,
        "5.5x8.5": 0.92,
        "6x9": 1.0,
        "7x10": 1.15,
        "8x10": 1.3,
    }

    mult = multipliers.get(trim_size, 1.0)
    words_per_page = baseline * mult

    return max(1, round(word_count / words_per_page))


def generate_toc(chapters_dir, trim_size="6x9", front_matter_pages=5):
    """
    Gera índice completo do livro.

    Args:
        chapters_dir: Diretório com os capítulos (ou glob pattern)
        trim_size: Trim size do livro
        front_matter_pages: Número de páginas de front matter

    Returns:
        Dict com entradas do TOC e HTML
    """
    chapters_dir = Path(chapters_dir)

    if chapters_dir.is_dir():
        chapter_files = sorted(chapters_dir.glob("*.md"))
    else:
        # Tratar como glob pattern
        import glob
        chapter_files = sorted(Path(f) for f in glob.glob(str(chapters_dir)))

    toc_entries = []
    current_page = front_matter_pages + 1
    total_words = 0

    for i, chapter_file in enumerate(chapter_files, 1):
        content = chapter_file.read_text(encoding='utf-8')
        title = extract_chapter_title(content)
        words = count_words(content)
        pages = estimate_pages(words, trim_size)

        total_words += words

        toc_entries.append({
            "number": i,
            "title": title,
            "page": current_page,
            "words": words,
            "file": chapter_file.name
        })

        current_page += pages

    # Gerar HTML do TOC
    html = '<div class="toc-page page">\n'
    html += '  <h1>Conteúdo</h1>\n'
    html += '  <div class="toc-entries">\n'

    for entry in toc_entries:
        html += f'''    <div class="toc-entry">
      <span class="title">{entry["title"]}</span>
      <span class="leaders"></span>
      <span class="page-number">{entry["page"]}</span>
    </div>\n'''

    html += '  </div>\n'
    html += '</div>\n'

    return {
        "entries": toc_entries,
        "html": html,
        "total_words": total_words,
        "estimated_total_pages": current_page - 1
    }


def main():
    parser = argparse.ArgumentParser(description="Gera índice para livro KDP")
    parser.add_argument("chapters", help="Diretório ou glob pattern dos capítulos")
    parser.add_argument("--trim", default="6x9", help="Trim size (default: 6x9)")
    parser.add_argument("--front-pages", type=int, default=5,
                       help="Páginas de front matter (default: 5)")
    parser.add_argument("--output", help="Salvar TOC em arquivo")
    parser.add_argument("--html", action="store_true", help="Gerar HTML")
    args = parser.parse_args()

    toc = generate_toc(args.chapters, args.trim, args.front_pages)

    print(f"\n{'='*60}")
    print(f"Índice Gerado")
    print(f"{'='*60}")
    print(f"\nTrim Size: {args.trim}")
    print(f"Capítulos: {len(toc['entries'])}")
    print(f"Palavras totais: {toc['total_words']:,}")
    print(f"Páginas estimadas: {toc['estimated_total_pages']}\n")

    for entry in toc['entries']:
        print(f"  Capítulo {entry['number']:2d}: {entry['title']}")
        print(f"    → Página {entry['page']}, {entry['words']:,} palavras")

    if args.html:
        print(f"\n{'='*60}")
        print("HTML do TOC:")
        print(f"{'='*60}\n")
        print(toc['html'])

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if args.html:
            output_path.write_text(toc['html'], encoding='utf-8')
            print(f"\n✓ HTML salvo em: {output_path}")
        else:
            # Salvar como texto simples
            lines = []
            for entry in toc['entries']:
                lines.append(f"{entry['title']} ............ {entry['page']}")
            output_path.write_text('\n'.join(lines), encoding='utf-8')
            print(f"\n✓ TOC salvo em: {output_path}")


if __name__ == "__main__":
    main()
