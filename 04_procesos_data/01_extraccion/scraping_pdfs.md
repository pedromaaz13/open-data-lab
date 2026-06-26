# Extracción de PDFs

Mucha información pública (boletines, subvenciones) vive en PDFs. Hay que extraerla con cuidado.

## Conceptos

- PDFs de texto vs escaneados (OCR).
- Tablas con líneas (lattice) vs sin líneas (stream).

## Herramientas

- `pdfplumber` para texto y tablas simples.
- `camelot` / `tabula` para tablas complejas.
- `pytesseract` para OCR de escaneados.

## Ejemplo

```python
import pdfplumber
with pdfplumber.open('data/raw/boletin.pdf') as pdf:
    tabla = pdf.pages[0].extract_table()
```

## Errores comunes

- Asumir estructura uniforme entre páginas.
- PDFs escaneados sin OCR.
- No validar los totales extraídos.
