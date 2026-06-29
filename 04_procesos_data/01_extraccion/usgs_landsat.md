# Extracción de Landsat (USGS)

Serie histórica larga (años 80 en adelante) con bandas térmicas — clave para temperatura superficial (LST) e islas de calor.

## Conceptos clave

- USGS EarthExplorer (web) y M2M API (programática, API key).
- Niveles: Collection 2 Level-2 (reflectancia/temperatura de superficie).
- Banda térmica (ST_B10 en L8/9) para LST.

## Ejemplo

```python
# Vía STAC (Planetary Computer o USGS) con pystac-client:
from pystac_client import Client
cat = Client.open('https://planetarycomputer.microsoft.com/api/stac/v1')
items = cat.search(collections=['landsat-c2-l2'], bbox=[-3.8,40.3,-3.6,40.5],
                   datetime='2023-07-01/2023-08-31', query={'eo:cloud_cover':{'lt':20}}).item_collection()
```

## Buenas prácticas

- Para LST usa Collection 2 Level-2 (ya corregida).
- Filtra nubosidad.
- Reproyecta a un CRS métrico para estadísticas zonales.

> Ver la referencia completa: `10_referencias/remote_sensing_satellite_data_sources.md`.
