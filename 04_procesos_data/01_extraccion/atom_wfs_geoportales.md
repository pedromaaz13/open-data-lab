# ATOM, WFS y geoportales

Geoportales españoles y europeos sirven datos vía servicios OGC (WFS/WMS) y feeds ATOM (INSPIRE).

## Conceptos

- WFS: descarga de features vectoriales.
- WMS: imágenes de mapa renderizadas.
- ATOM: feeds de descarga predefinida (INSPIRE).

## Ejemplo

```python
import geopandas as gpd
url = ('https://servicio/wfs?service=WFS&version=2.0.0&request=GetFeature'
       '&typeName=municipios&outputFormat=application/json')
gdf = gpd.read_file(url)
```

## Buenas prácticas

- Comprueba el CRS devuelto.
- Usa filtros (BBOX) para no descargar todo el país.
- Cachea los GeoJSON/GPKG resultantes.

## Errores comunes

- Olvidar el CRS.
- Descargar capas nacionales completas sin filtro.
