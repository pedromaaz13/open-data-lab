# Análisis geoespacial

## Para qué sirve

Analizar el territorio: mapas, uniones espaciales, indicadores por unidad administrativa y teledetección.

## Conceptos principales

- CRS y proyecciones (EPSG:4326, EPSG:25830).
- Geometrías (puntos, líneas, polígonos).
- Spatial joins y operaciones (buffer, intersect, dissolve).
- Indexación H3.
- Raster vs vector.

## Librerías útiles

- `geopandas`, `shapely`, `pyproj`, `h3`.
- `rasterio`, `rioxarray`, `xarray`.
- `keplergl`, `folium`, PostGIS.

## Ejemplos de uso

```python
import geopandas as gpd
muni = gpd.read_file('data/raw/municipios.gpkg')
incendios = gpd.read_file('data/raw/incendios.geojson')
join = gpd.sjoin(incendios.to_crs(muni.crs), muni, predicate='within')
conteo = join.groupby('cod_ine').size()
```

## Errores comunes

- Mezclar CRS distintos en un join.
- Calcular áreas en grados (lat/lon) en vez de en proyección métrica.
- Cargar rásteres enormes en memoria sin ventanas.

## Mini proyecto recomendado

Cruzar focos de incendio con municipios y calcular superficie afectada por NDVI.

## Recursos para profundizar

- *Geographic Data Science* (Rey, Arribas-Bel).
- Docs GeoPandas y PostGIS.
- Automating GIS (Helsinki).
