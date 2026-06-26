# Scraping de HTML

Extracción de webs sin API, de forma legal y educada. Ver también `01_skills/web_scraping.md`.

## Conceptos

- Selectores CSS/XPath.
- robots.txt y términos de uso.
- Páginas estáticas vs dinámicas (JS → Playwright).

## Ejemplo

```python
from bs4 import BeautifulSoup
import httpx
html = httpx.get(url, headers={'User-Agent': 'open-data-lab'}).text
soup = BeautifulSoup(html, 'lxml')
rows = [[td.get_text(strip=True) for td in tr.select('td')]
        for tr in soup.select('table.datos tr')]
```

## Buenas prácticas

- Verifica robots.txt y ToS antes de empezar.
- Pausas entre peticiones; User-Agent identificable.
- Selectores robustos, no atados a clases volátiles.

## Errores comunes

- Martillear el servidor.
- Scrapers frágiles que se rompen al menor cambio.
