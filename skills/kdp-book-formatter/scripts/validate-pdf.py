#!/usr/bin/env python3
"""
KDP PDF Validator
Valida PDFs contra requisitos de Amazon KDP.
"""

import sys
import argparse
from pathlib import Path


# Trim sizes válidos KDP
VALID_TRIM_SIZES = [
    (5, 8), (5.25, 8), (5.5, 8.5),
    (6, 9), (6.14, 9.21),  # 15.6cm x 23.39cm (A5 aprox)
    (7, 10), (8, 10), (8.5, 11), (8.25, 6), (8.25, 8.25)
]


def validate_pdf(pdf_path, expected_trim=None):
    """
    Valida um PDF contra requisitos KDP.

    Args:
        pdf_path: Caminho para o PDF
        expected_trim: Trim size esperado como (width, height) em polegadas

    Returns:
        Dict com resultado da validação
    """
    errors = []
    warnings = []

    try:
        # Tentar ler o PDF
        try:
            import pypdf
            with open(pdf_path, 'rb') as f:
                pdf_reader = pypdf.PdfReader(f)
                page_count = len(pdf_reader.pages)
                first_page = pdf_reader.pages[0]

                # Obter tamanho da página em points (1 point = 1/72 inch)
                page_size = first_page.mediabox
                width_pt = float(page_size.width)
                height_pt = float(page_size.height)

                # Converter para inches
                width_in = width_pt / 72
                height_in = height_pt / 72

        except ImportError:
            return {
                "valid": False,
                "errors": ["pypdf não está instalado. Instale: pip install pypdf"],
                "warnings": []
            }

        # Validação de page count
        if page_count < 24:
            errors.append(f"Page count ({page_count}) abaixo do mínimo KDP (24)")

        if page_count > 828:
            warnings.append(f"Page count ({page_count}) acima de 828 pode ter restrições")

        # Validação de trim size
        trim_valid = False
        for valid_w, valid_h in VALID_TRIM_SIZES:
            if abs(width_in - valid_w) < 0.1 and abs(height_in - valid_h) < 0.1:
                trim_valid = True
                break

        # Verificar se está dentro do range permitido
        if 4 <= width_in <= 8.5 and 6 <= height_in <= 11.69:
            trim_valid = True

        if not trim_valid:
            errors.append(f"Trim size {width_in:.2f}\" x {height_in:.2f}\" fora do range KDP (4-8.5\" x 6-11.69\")")

        # Verificar contra trim esperado
        if expected_trim:
            exp_w, exp_h = expected_trim
            if abs(width_in - exp_w) > 0.1 or abs(height_in - exp_h) > 0.1:
                warnings.append(f"Trim size atual ({width_in:.2f}\" x {height_in:.2f}\") difere do esperado ({exp_w}\" x {exp_h}\")")

        # Verificar orientação
        if width_in > height_in:
            warnings.append("PDF em orientação paisagem. KDP usa retrato.")

    except FileNotFoundError:
        errors.append(f"Arquivo não encontrado: {pdf_path}")
    except Exception as e:
        errors.append(f"Erro ao ler PDF: {str(e)}")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "page_count": page_count if 'page_count' in locals() else None,
        "trim_size": f"{width_in:.2f}\" x {height_in:.2f}\"" if 'width_in' in locals() else None
    }


def main():
    parser = argparse.ArgumentParser(description="Valida PDF contra requisitos KDP")
    parser.add_argument("pdf", help="Arquivo PDF para validar")
    parser.add_argument("--trim", help="Trim size esperado (ex: 6x9)")
    args = parser.parse_args()

    pdf_path = Path(args.pdf)

    if not pdf_path.exists():
        print(f"✗ Arquivo não encontrado: {pdf_path}")
        sys.exit(1)

    # Parse trim size
    expected_trim = None
    if args.trim:
        parts = args.trim.lower().replace('x', ' ').replace('"', '').split()
        if len(parts) == 2:
            try:
                expected_trim = (float(parts[0]), float(parts[1]))
            except ValueError:
                print(f"✗ Trim size inválido: {args.trim}")
                sys.exit(1)

    result = validate_pdf(pdf_path, expected_trim)

    print(f"\n{'='*60}")
    print(f"KDP PDF Validator")
    print(f"{'='*60}")
    print(f"\nArquivo: {pdf_path.name}")

    if result['trim_size']:
        print(f"Trim Size: {result['trim_size']}")
    if result['page_count']:
        print(f"Page Count: {result['page_count']}")

    print(f"\nStatus: {'✅ VALID' if result['valid'] else '❌ INVALID'}")

    if result['errors']:
        print(f"\n❌ Erros:")
        for error in result['errors']:
            print(f"   • {error}")

    if result['warnings']:
        print(f"\n⚠️ Avisos:")
        for warning in result['warnings']:
            print(f"   • {warning}")

    if result['valid']:
        print(f"\n✅ PDF está pronto para upload na Amazon KDP!")
    else:
        print(f"\n❌ Corrija os erros antes de fazer upload.")

    print(f"\n{'='*60}\n")

    sys.exit(0 if result['valid'] else 1)


if __name__ == "__main__":
    main()
