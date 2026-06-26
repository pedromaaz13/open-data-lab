# Mapas interactivos

Opciones para mapas web según el caso.

## Herramientas

- **Folium** (Leaflet): mapas simples y rápidos.
- **Kepler.gl**: exploración geoespacial potente.
- **deck.gl / MapLibre**: apps a medida y gran volumen.
- **PyDeck**: deck.gl desde Python.

## Ejemplo Folium

```python
import folium
m = folium.Map(location=[40.4, -3.7], zoom_start=6)
folium.Choropleth(geo_data=geojson, data=df, columns=['cod_ine','valor'],
                  key_on='feature.properties.cod_ine').add_to(m)
```

## Buenas prácticas

- Elige la herramienta según volumen e interactividad.
- Exporta a HTML para compartir.
