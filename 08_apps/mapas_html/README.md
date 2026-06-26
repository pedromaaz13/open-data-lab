# Mapas HTML

Mapas interactivos exportados como HTML autónomo (Kepler.gl, Folium, PyDeck).

## Generar

```python
from keplergl import KeplerGl
m = KeplerGl(height=600)
m.add_data(data=gdf, name='capa')
m.save_to_html(file_name='08_apps/mapas_html/mapa.html')
```

## Buenas prácticas

- Datos en EPSG:4326 para herramientas web.
- Guarda también la configuración del mapa para reproducir.
- Enlaza los mapas desde los informes y el README del proyecto.
