#!/usr/bin/env python3
"""
KDP Margin Calculator
Calcula margens ideais para livros KDP baseado em page count e trim size.
"""

import sys
import json


# Trim sizes oficiais KDP
TRIM_SIZES = {
    "5x8": {"width": 5, "height": 8, "name": '5" x 8"'},
    "5.25x8": {"width": 5.25, "height": 8, "name": '5.25" x 8"'},
    "5.5x8.5": {"width": 5.5, "height": 8.5, "name": '5.5" x 8.5"'},
    "6x9": {"width": 6, "height": 9, "name": '6" x 9"'},
    "7x10": {"width": 7, "height": 10, "name": '7" x 10"'},
    "8x10": {"width": 8, "height": 10, "name": '8" x 10"'},
}


def get_gutter_margin(page_count):
    """
    Retorna a margem interna (gutter) baseado no número de páginas.
    Conforme requisitos KDP.
    """
    if page_count <= 150:
        return 0.5, "1/2"
    elif page_count <= 400:
        return 0.5625, "9/16"
    elif page_count <= 500:
        return 0.625, "5/8"
    elif page_count <= 600:
        return 0.6875, "11/16"
    elif page_count <= 700:
        return 0.75, "3/4"
    elif page_count <= 800:
        return 0.8125, "13/16"
    else:
        return 0.875, "7/8"


def calculate_margins(page_count, trim_size="6x9", has_bleed=False):
    """
    Calcula margens completas para um livro KDP.

    Args:
        page_count: Número de páginas estimado
        trim_size: Código do trim size (ex: "6x9")
        has_bleed: Se o livro tem elementos que vão até a borda

    Returns:
        Dict com todas as margens e CSS @page
    """
    min_margin = 0.375 if has_bleed else 0.25
    gutter, gutter_fraction = get_gutter_margin(page_count)

    trim = TRIM_SIZES.get(trim_size, TRIM_SIZES["6x9"])

    # Para livros muito largos, aumentar margem externa
    outside_margin = min_margin + 0.125 if trim["width"] >= 7 else min_margin

    margins = {
        "page_count": page_count,
        "trim_size": trim_size,
        "trim_dimensions": trim,
        "has_bleed": has_bleed,
        "margins": {
            "top": min_margin,
            "bottom": min_margin,
            "inside": gutter,
            "outside": outside_margin,
        },
        "gutter_fraction": gutter_fraction,
        "css": f"""@page {{
  size: {trim["width"]}in {trim["height"]}in;
  margin-top: {min_margin}in;
  margin-bottom: {min_margin}in;
  margin-left: {gutter}in;
  margin-right: {outside_margin}in;
}}

@page :left {{
  margin-left: {outside_margin}in;
  margin-right: {gutter}in;
}}

@page :right {{
  margin-left: {gutter}in;
  margin-right: {outside_margin}in;
}}"""
    }

    return margins


def main():
    if len(sys.argv) < 2:
        print("Uso: python calculate-margins.py <page_count> [trim_size] [has_bleed]")
        print("Exemplo: python calculate-margins.py 240 6x9 false")
        sys.exit(1)

    page_count = int(sys.argv[1])
    trim_size = sys.argv[2] if len(sys.argv) > 2 else "6x9"
    has_bleed = sys.argv[3].lower() == "true" if len(sys.argv) > 3 else False

    result = calculate_margins(page_count, trim_size, has_bleed)

    print(f"\n{'='*60}")
    print(f"KDP Margin Calculator")
    print(f"{'='*60}")
    print(f"\nTrim Size: {result['trim_dimensions']['name']}")
    print(f"Page Count: {page_count}")
    print(f"Bleed: {'Sim' if has_bleed else 'Não'}")
    print(f"\nMargens KDP:")
    print(f"  Top:    {result['margins']['top']:.4f}\"  (mínimo KDP: {'0.375' if has_bleed else '0.25'}\")")
    print(f"  Bottom: {result['margins']['bottom']:.4f}\"  (mínimo KDP: {'0.375' if has_bleed else '0.25'}\")")
    print(f"  Inside: {result['margins']['inside']:.4f}\"  (gutter: {result['gutter_fraction']}\")")
    print(f"  Outside: {result['margins']['outside']:.4f}\"  (mínimo KDP: {'0.375' if has_bleed else '0.25'}\")")
    print(f"\nCSS @page:")
    print(result["css"])
    print(f"{'='*60}\n")

    # Output JSON para uso programático
    if "--json" in sys.argv:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
