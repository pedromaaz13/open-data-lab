# Extracción de APIs REST

Patrón estándar para consumir APIs oficiales (INE, Eurostat, World Bank...).

## Conceptos clave

- Endpoints, parámetros y paginación.
- Autenticación (API key, OAuth) vía variables de entorno.
- Rate limiting y reintentos con backoff.
- Formatos JSON / JSON-stat / CSV.

## Ejemplo

```python
import httpx, time
from pathlib import Path

def fetch(url, params, out: Path, retries=3):
    for i in range(retries):
        r = httpx.get(url, params=params, timeout=30)
        if r.status_code == 200:
            out.write_bytes(r.content)
            return
        time.sleep(2 ** i)
    raise RuntimeError(f'fallo: {url}')
```

## Buenas prácticas

- Guarda el crudo en `data/raw/` sin transformar.
- Registra fecha y parámetros para trazabilidad.
- Cachea para no repetir descargas.
- Nunca pongas credenciales en el código.

## Errores comunes

- Ignorar la paginación (datos incompletos).
- No respetar límites de la API.
- Parsear a mano formatos con cliente disponible.
