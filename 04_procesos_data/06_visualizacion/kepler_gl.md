# Kepler.gl

Herramienta clave del laboratorio para mapas geoespaciales interactivos.

## Qué ofrece

- Mapas de puntos, arcos, hexágonos (H3), heatmaps.
- Animación temporal.
- Exportación a HTML autónomo.

## Ejemplo

```python
from keplergl import KeplerGl
m = KeplerGl(height=600)
m.add_data(data=gdf, name='municipios')
m.save_to_html(file_name='outputs/mapa.html')
```

## Buenas prácticas

- Datos en EPSG:4326 (lat/lon) para Kepler.
- Exporta el HTML a `08_apps/mapas_html/` o `outputs/`.
- Guarda la config del mapa para reproducir.
