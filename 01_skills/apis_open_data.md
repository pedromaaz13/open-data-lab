# APIs de open data

## Para qué sirve

Consumir APIs oficiales (INE, Eurostat, World Bank, Copernicus...) de forma reproducible.

## Conceptos principales

- REST, parámetros, paginación, autenticación.
- Formatos JSON / CSV / GeoJSON.
- Rate limits y caché.
- Versionado de endpoints.

## Librerías útiles

- `requests`/`httpx`, `pandas`, `pyarrow`.
- Clientes específicos: `wbgapi` (World Bank), `eurostat`, `sentinelhub`, `pystac-client`.

## Ejemplos de uso

```python
import httpx
# Eurostat JSON-stat
url = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_hpi_q'
data = httpx.get(url, params={'format': 'JSON', 'geo': 'ES'}).json()
```

## Errores comunes

- No respetar límites de la API.
- No registrar la fecha de consulta.
- Parsear a mano formatos que ya tienen cliente.

## Mini proyecto recomendado

Crear un extractor genérico parametrizable para descargar series del INE a Parquet.

## Recursos para profundizar

- Documentación de cada API (ver `03_fuentes_oficiales/`).
- `pystac-client`, `wbgapi`.
