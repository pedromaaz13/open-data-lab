# Web scraping responsable

## Para qué sirve

Extraer datos de webs y PDFs cuando no hay API, de forma legal, educada y reproducible.

## Conceptos principales

- HTML, selectores CSS/XPath.
- robots.txt, términos de uso y rate limiting.
- Páginas dinámicas (JS) vs estáticas.
- Parsing de tablas y PDFs.

## Librerías útiles

- `requests`/`httpx`, `beautifulsoup4`, `lxml`.
- `playwright` para JS.
- `pdfplumber`, `camelot`, `tabula` para PDFs.

## Ejemplos de uso

```python
import httpx, time
from bs4 import BeautifulSoup
resp = httpx.get(url, headers={'User-Agent': 'open-data-lab'})
soup = BeautifulSoup(resp.text, 'lxml')
filas = [tr.get_text(strip=True) for tr in soup.select('table tr')]
time.sleep(1)  # ser educado con el servidor
```

## Errores comunes

- Ignorar robots.txt o términos de uso.
- Martillear el servidor sin pausas.
- Scrapers frágiles atados a clases CSS volátiles.
- No cachear las descargas.

## Mini proyecto recomendado

Scrapear una tabla pública (con permiso/licencia) y normalizarla a Parquet con trazabilidad.

## Recursos para profundizar

- Docs de BeautifulSoup y Playwright.
- Guías legales de scraping (respetar ToS).
