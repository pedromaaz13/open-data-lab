# Trazabilidad de fuentes

Cualquier dato del laboratorio debe poder rastrearse hasta su origen oficial.

## Qué registrar por fuente

| Campo | Ejemplo |
|---|---|
| Organismo | INE |
| Dataset | Índice de Precios de Vivienda |
| URL | https://www.ine.es/... |
| Endpoint/descarga | API JSON / CSV |
| Licencia | Reutilización con atribución |
| Formato | CSV / JSON / Parquet |
| Nivel geográfico | Provincia |
| Periodo | 2015-2024 |
| Fecha de consulta | 2026-06-26 |
| Hash/versión | sha256 del fichero raw |

## Dónde se registra

1. En `09_data_catalog/catalogo_datasets.csv` (catálogo central).
2. En el README del proyecto (sección *Fuentes de datos*).
3. En el diccionario de datos del dataset.

## Buenas prácticas

- Guarda el fichero raw exactamente como llegó.
- Anota la fecha de consulta: los portales cambian.
- Si la fuente no tiene API estable, documenta el procedimiento manual.
- Calcula un hash del raw para detectar cambios entre ejecuciones.

## Cadena de custodia del dato

```txt
Fuente oficial  →  raw (hash + fecha)  →  interim (script)  →  processed (script)
                                                              →  diccionario de datos
```
