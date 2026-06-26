# Extracción satélite (STAC / Copernicus)

Búsqueda y descarga de imágenes satélite mediante catálogos STAC. Ver agente Copernicus.

## Conceptos

- STAC (catálogos, colecciones, items, assets).
- COG (Cloud Optimized GeoTIFF) y lectura por ventanas.
- Máscaras de nube (SCL en Sentinel-2).

## Ejemplo

```python
from pystac_client import Client
cat = Client.open('https://catalogue.dataspace.copernicus.eu/stac')
items = cat.search(collections=['SENTINEL-2'], bbox=[-9,42,-7,44],
                   datetime='2022-07-01/2022-08-31').item_collection()
```

## Buenas prácticas

- Filtra por cobertura de nube.
- Procesa por tiles/ventanas, no descargues todo.
- Documenta producto y nivel (L1C/L2A).

## Errores comunes

- Descargar escenas completas innecesarias.
- Ignorar máscaras de calidad.
