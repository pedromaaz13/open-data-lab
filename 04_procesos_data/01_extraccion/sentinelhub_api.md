# Extracción con Sentinel Hub API

API profesional que devuelve **imágenes ya procesadas** (true color, NDVI, NBR...) por AOI, con evalscripts. Free tier + pago.

## Conceptos clave

- Autenticación OAuth (client id/secret).
- Evalscript: define qué bandas/índice devuelve.
- Ideal para prototipos rápidos sin gestionar bandas a mano.

## Ejemplo

```python
from sentinelhub import SHConfig, SentinelHubRequest, DataCollection, MimeType, BBox, CRS
cfg = SHConfig(); cfg.sh_client_id='...'; cfg.sh_client_secret='...'   # desde .env
# request con un evalscript de NDVI sobre un BBox y fechas...
```

## Buenas prácticas

- Credenciales en `.env`.
- Vigila el consumo (processing units) en el free tier.
- Documenta el evalscript usado.

> Ver la referencia completa: `10_referencias/remote_sensing_satellite_data_sources.md`.
