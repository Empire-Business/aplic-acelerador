# Regras de Validação KDP

## Validações Obrigatórias (ERROS)

### Page Count
- **Mínimo**: 24 páginas
- **Regra**: PDFs com menos de 24 páginas são rejeitados pelo KDP
- **Erro**: `PDF_TOO_SHORT`

### Trim Size
- **Width**: entre 4" e 8.5"
- **Height**: entre 6" e 11.69"
- **Erro**: `TRIM_SIZE_INVALID`

### Margens
- **Sem bleed**: mínimo 0.25" (top, bottom, outside)
- **Com bleed**: mínimo 0.375" (top, bottom, outside)
- **Gutter**: mínimo 0.5" (para lombada)
- **Erro**: `MARGINS_TOO_SMALL`

### Font Size
- **Corpo do texto**: mínimo 10pt, recomendado 11pt
- **Erro**: `FONT_SIZE_TOO_SMALL`

### Embedding
- Fontes devem estar embedadas no PDF
- **Erro**: `FONTS_NOT_EMBEDDED`

## Validações Opcionais (AVISOS)

### Page Count Alto
- **Aviso**: acima de 828 páginas
- **Motivo**: pode ter limitações de distribuição
- **Warning**: `LARGE_PAGE_COUNT`

### Proporção Incomum
- **Aviso**: width/height ratio fora de 0.5-0.85
- **Warning**: `UNUSUAL_ASPECT_RATIO`

### Sem ISBN
- **Info**: ISBN não fornecido
- **Motivo**: ISBN é recomendado para distribuição ampliada
- **Warning**: `NO_ISBN`

### Margens Justas
- **Aviso**: margens muito próximas do mínimo
- **Warning**: `TIGHT_MARGINS`

## Checklist Final de Validação

```yaml
validations:
  - name: "Page count mínimo"
    check: "page_count >= 24"
    severity: "error"

  - name: "Trim size válido"
    check: "width >= 4 and width <= 8.5 and height >= 6 and height <= 11.69"
    severity: "error"

  - name: "Margens mínimas"
    check: "top >= 0.25 and bottom >= 0.25 and outside >= 0.25"
    severity: "error"

  - name: "Gutter adequado"
    check: "inside >= 0.5"
    severity: "error"

  - name: "Font size mínimo"
    check: "body_font_size >= 10"
    severity: "error"

  - name: "Capítulos em páginas ímpares"
    check: "chapters_start_on_odd"
    severity: "warning"

  - name: "TOC presente"
    check: "has_toc"
    severity: "warning"

  - name: "Front matter completo"
    check: "has_title_page and has_copyright"
    severity: "warning"

  - name: "Paginação presente"
    check: "has_page_numbers"
    severity: "warning"
```

## Mensagens de Erro

```python
ERROR_MESSAGES = {
    "PDF_TOO_SHORT": "O PDF tem apenas {n} páginas. O mínimo KDP é 24 páginas.",
    "TRIM_SIZE_INVALID": "O trim size {w}\" x {h}\" não é válido. Use entre 4-8.5\" de largura e 6-11.69\" de altura.",
    "MARGINS_TOO_SMALL": "As margens são muito pequenas. Mínimo KDP: 0.25\" (sem bleed) ou 0.375\" (com bleed).",
    "FONT_SIZE_TOO_SMALL": "O tamanho da fonte ({n}pt) é muito pequeno. Mínimo recomendado: 11pt.",
    "FONTS_NOT_EMBEDDED": "As fontes não estão embedadas no PDF.",
}

WARNING_MESSAGES = {
    "LARGE_PAGE_COUNT": "O PDF tem {n} páginas. Acima de 828 pode ter restrições de distribuição.",
    "UNUSUAL_ASPECT_RATIO": "A proporção do livro ({r}) é incomum.",
    "NO_ISBN": "ISBN não fornecido. Considere obter um ISBN para melhor distribuição.",
    "TIGHT_MARGINS": "As margens estão muito próximas do mínimo KDP.",
}
```
