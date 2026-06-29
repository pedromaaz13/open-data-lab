# Extracción con openEO (Copernicus)

openEO procesa Sentinel **en la nube** (datacubes) sin descargar escenas enormes: filtras zona/fecha, calculas índices y bajas solo el resultado.

## Conceptos clave

- Datacube: vista espacio-tiempo-banda.
- Procesado server-side (NDVI, composites) → descargas el resultado.
- Backend: Copernicus Data Space (registro gratuito, con límites).

## Ejemplo

```python
import openeo
con = openeo.connect('https://openeo.dataspace.copernicus.eu').authenticate_oidc()
cube = con.load_collection('SENTINEL2_L2A', spatial_extent={'west':-3.8,'south':40.3,'east':-3.6,'north':40.5},
                           temporal_extent=['2023-07-01','2023-08-31'], bands=['B04','B08'])
ndvi = (cube.band('B08') - cube.band('B04')) / (cube.band('B08') + cube.band('B04'))
ndvi.max_time().download('outputs/ndvi.tiff')
```

## Buenas prácticas

- Filtra nubosidad y periodo para no procesar de más.
- Guarda el resultado en `data/processed/`, no la escena entera.
- Respeta las cuotas del backend gratuito.

> Ver la referencia completa: `10_referencias/remote_sensing_satellite_data_sources.md`.
