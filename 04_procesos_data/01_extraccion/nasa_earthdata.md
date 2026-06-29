# Extracción de NASA Earthdata

Acceso a MODIS/VIIRS, clima, temperatura, incendios y más. Requiere registro Earthdata gratuito.

## Conceptos clave

- CMR (Common Metadata Repository) para buscar.
- `earthaccess` (librería) simplifica login y descarga.
- FIRMS para incendios casi en tiempo real (API key aparte).

## Ejemplo

```python
import earthaccess
earthaccess.login()   # credenciales Earthdata
results = earthaccess.search_data(short_name='MOD13Q1', bounding_box=(-9,36,3,44),
                                  temporal=('2023-06-01','2023-09-30'))
files = earthaccess.download(results, 'data/raw/modis/')
```

## Buenas prácticas

- Guarda credenciales en `.env`, nunca en el código.
- Atención al volumen; filtra bbox y fechas.
- Documenta producto y versión (p. ej. MOD13Q1 v061).

> Ver la referencia completa: `10_referencias/remote_sensing_satellite_data_sources.md`.
