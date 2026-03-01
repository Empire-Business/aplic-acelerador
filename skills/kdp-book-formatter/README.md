# KDP Book Formatter - Claude Skill

Transforma livros em Markdown em PDFs profissionais prontos para publicação na Amazon KDP.

## Instalação

Esta skill já está instalada em `.claude/skills/kdp-book-formatter/`.

## Uso

### Comando principal

```
/kdp-book-formatter format "Título do Livro" "Nome do Autor" --trim 6x9
```

### Outros comandos

```
/kdp-book-formatter validate meulivro.pdf
/kdp-book-formatter preview
/kdp-book-formatter margins --pages 240 --trim 6x9
/kdp-book-formatter toc capitulos/*.md
/kdp-book-formatter template
/kdp-book-formatter guide
```

## Estrutura de Projeto

```
meu-livro/
├── capitulos/
│   ├── capitulo_01.md
│   ├── capitulo_02.md
│   └── ...
├── front-matter/
│   └── dedicatória.md
├── back-matter/
│   └── sobre-autor.md
└── config.yaml
```

## Scripts Python

A skill inclui scripts utilitários:

- `calculate-margins.py` - Calcula margens KDP
- `validate-pdf.py` - Valida PDFs
- `generate-toc.py` - Gera índice
- `html-to-pdf.py` - Converte HTML para PDF

## Trim Sizes Suportados

| Código | Dimensões | Uso |
|--------|-----------|-----|
| 5x8 | 5" × 8" | Romances compactos |
| 5.25x8 | 5.25" × 8" | Romances padrão |
| 5.5x8.5 | 5.5" × 8.5" | Ficção geral |
| 6x9 | 6" × 9" | Não-ficção (mais comum) |
| 7x10 | 7" × 10" | Livros técnicos |

## Fontes

- [Trim Size KDP](https://kdp.amazon.com/help/topic/GVBQ3CMEQW3W2VL6)
- [Format Your Paperback](https://kdp.amazon.com/help/topic/G201834190)
- [Build Your Book](https://kdp.amazon.com/help/topic/G202145400)
