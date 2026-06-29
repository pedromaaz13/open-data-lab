# Extracción de calidad del aire (OpenAQ)

API global de **calidad del aire** de estaciones en tierra (NO2, PM2.5, PM10, O3...). Complementa la señal satélite de Sentinel-5P.

## Conceptos clave

- Estaciones (locations) → mediciones (measurements).
- Filtrado por país, ciudad, parámetro y fecha.
- v3 requiere API key gratuita.

## Ejemplo

```python
import httpx
h = {'X-API-Key': '...'}   # desde .env
r = httpx.get('https://api.openaq.org/v3/locations',
              params={'iso':'ES','parameter':'no2','limit':100}, headers=h)
data = r.json()
```

## Buenas prácticas

- API key en `.env`.
- Respeta los límites de peticiones.
- Cruza estaciones (tierra) con Sentinel-5P (satélite) para validar.

> Ver la referencia completa: `10_referencias/remote_sensing_satellite_data_sources.md`.
