---
name: kdp-book-formatter
description: Transforma livros em Markdown em PDFs profissionais prontos para publicação na Amazon KDP. Calcula margens automáticas, gera índice, valida conformidade.
version: 1.0.0
author: KDP Book Formatter
tags: [kdp, amazon, book, pdf, publishing, formatting, kindle]
argument-hint: [title] [author] --trim 6x9 --chapters "capitulos/*.md"
allowed-tools: Read, Write, Bash, Glob
---

# KDP Book Formatter

Skill especializada em transformar manuscritos em Markdown em PDFs profissionais compatíveis com Amazon Kindle Direct Publishing (KDP).

## Quando usar

- Diagramar livros para publicação na Amazon KDP
- Gerar PDF profissional pronto para upload
- Validar PDFs existentes contra requisitos KDP
- Calcular margens e configurações de layout
- Gerar índice (TOC) automaticamente
- Criar estrutura inicial de projeto de livro

## Comandos disponíveis

| Comando | Descrição |
|---------|-----------|
| `/kdp-book-formatter format` | Diagrama livro completo gerando PDF |
| `/kdp-book-formatter validate` | Valida PDF contra requisitos KDP |
| `/kdp-book-formatter preview` | Gera preview HTML no navegador |
| `/kdp-book-formatter margins` | Calcula margens ideais |
| `/kdp-book-formatter toc` | Gera índice automático |
| `/kdp-book-formatter template` | Cria estrutura de projeto |
| `/kdp-book-formatter guide` | Mostra guia completo |

---

## REQUISITOS KDP - CONHECIMENTO BASE

### Trim Sizes Oficiais

| Código | Dimensões | Uso |
|--------|-----------|-----|
| `5x8` | 5" × 8" | Romances compactos |
| `5.25x8` | 5.25" × 8" | Romances padrão |
| `5.5x8.5` | 5.5" × 8.5" | Ficção geral |
| `6x9` | 6" × 9" | Não-ficção (mais comum) |
| `7x10` | 7" × 10" | Livros técnicos |

### Cálculo de Gutter (Margem Interna)

```
function getGutterMargin(pageCount):
  if pageCount <= 150: return 0.5"
  if pageCount <= 400: return 0.5625"
  if pageCount <= 500: return 0.625"
  if pageCount <= 600: return 0.6875"
  if pageCount <= 700: return 0.75"
  if pageCount <= 800: return 0.8125"
  return 0.875"
```

### Margens Mínimas KDP

- **Sem bleed**: 0.25" (top, bottom, outside)
- **Com bleed**: 0.375" (top, bottom, outside)

### Font Sizes Padrão

- Corpo: 11pt
- Título capítulo (H1): 18pt
- Seções (H2): 16pt
- Subseções (H3): 14pt
- Copyright: 9pt

---

## WORKFLOW: FORMAT-BOOK

### 1. Coletar informações

Se o usuário não fornecer, pergunte:
- Título do livro (obrigatório)
- Nome do autor (obrigatório)
- Trim size (default: 6x9)
- Localização dos capítulos (default: capitulos/*.md)

### 2. Ler e parsear conteúdo

- Ler todos os arquivos Markdown
- Extrair títulos (primeiro H1)
- Contar palavras de cada capítulo
- Estimar páginas totais (baseline: 300 palavras/página para 6x9)

### 3. Calcular margens

Usar a função `getGutterMargin()` baseado no page count estimado.

### 4. Gerar HTML completo

Use o template HTML em `templates/book-template.html` e o CSS base em `resources/kdp-base.css`.

### 5. Gerar PDF

Use o script Python `scripts/html-to-pdf.py` ou instrua conversão via navegador.

---

## RECURSOS DA SKILL

### Templates

- `templates/book-template.html` - Estrutura HTML completa do livro
- `templates/config.yaml` - Template de configuração YAML
- `templates/non-fiction.yaml` - Config para não-ficção
- `templates/novel.yaml` - Config para romance
- `templates/anthology.yaml` - Config para antologia

### Resources

- `resources/kdp-base.css` - CSS base completo para KDP
- `resources/trim-sizes.yaml` - Dimensões oficiais
- `resources/validation-rules.md` - Regras de validação

### Scripts

- `scripts/html-to-pdf.py` - Converte HTML para PDF
- `scripts/calculate-margins.py` - Calcula margens
- `scripts/validate-pdf.py` - Valida PDF

### Additional resources

- Para referência completa de trim sizes, veja `resources/trim-sizes.yaml`
- Para CSS base, veja `resources/kdp-base.css`
- Para templates de projeto, veja `templates/`

---

## ESTRUTURA DE PROJETO RECOMENDADA

```
meu-livro/
├── capitulos/
│   ├── capitulo_01.md
│   ├── capitulo_02.md
│   └── ...
├── front-matter/
│   ├── dedicatória.md
│   └── prefacio.md
├── back-matter/
│   └── sobre-autor.md
└── config.yaml
```

### Formato de Capítulo (Markdown)

```markdown
# Capítulo 1

## Seção 1.1

Conteúdo da seção.

> "Uma citação inspiradora"

Mais texto...
```

---

## CHECKLIST DE VALIDAÇÃO

Antes de considerar o PDF pronto para KDP:

- [ ] Page count >= 24 páginas
- [ ] Trim size válido (4-8.5" width, 6-11.69" height)
- [ ] Margens atendem mínimo KDP
- [ ] Gutter adequado para page count
- [ ] Font size >= 11pt
- [ ] Capítulos em páginas ímpares
- [ ] TOC presente e correto
- [ ] Front matter completo
- [ ] Paginação presente

---

## EXEMPLO DE USO

```
Usuário: /kdp-book-formatter format "Meu Livro" "João Silva" --trim 6x9

Claude:
1. Lendo capítulos...
   ✓ capitulo_01.md (1,234 palavras)
   ✓ capitulo_02.md (1,567 palavras)

2. Total: 2,801 palavras ~ 10 páginas

3. Margens KDP para trim size 6x9:
   Top: 0.25", Bottom: 0.25", Inside: 0.5", Outside: 0.25"

4. Gerando HTML... ✓

5. Gerando PDF... ✓

6. PDF salvo em: ./output/meu-livro.pdf

✅ Livro pronto para upload na Amazon KDP!
```

---

## FONTES OFICIAIS KDP

- [Trim Size, Bleed, and Margins](https://kdp.amazon.com/help/topic/GVBQ3CMEQW3W2VL6)
- [Format Your Paperback](https://kdp.amazon.com/help/topic/G201834190)
- [Build Your Book](https://kdp.amazon.com/help/topic/G202145400)
- [Front/Back Matter](https://kdp.amazon.com/help/topic/GDDYZG2C7RVF5N9J)
