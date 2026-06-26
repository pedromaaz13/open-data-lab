# Incendios y NDVI con Copernicus

## Pregunta de investigación

¿Qué superficie y qué vegetación afectan los grandes incendios, medido con índices satélite (NDVI/NBR)?

## Contexto

Los incendios forestales tienen impacto ambiental y social. La teledetección permite medir severidad (NBR) y recuperación de la vegetación (NDVI) de forma objetiva.

## Fuentes de datos previstas

- Sentinel-2 L2A (Copernicus Data Space, STAC).
- Focos de incendio (NASA FIRMS).
- Perímetros de incendio (EFFIS).

## Metodología

1. Localizar escenas pre/post incendio vía STAC.
2. Calcular NBR y dNBR (severidad).
3. Calcular NDVI y su evolución (recuperación).
4. Cruzar con municipios y usos del suelo.

## Métricas principales

- Superficie quemada (ha).
- Severidad (dNBR).
- Recuperación NDVI a 6/12 meses.

## Visualizaciones previstas

- Mapas raster de severidad.
- Series NDVI de recuperación.
- Mapa de superficie afectada por municipio.

## Posibles modelos o simulaciones

- Predicción de recuperación de vegetación.
- Clustering de severidad.

## Limitaciones

- Cobertura nubosa.
- Volumen de datos satélite.

## Próximos pasos

- Extractor STAC.
- Cálculo de índices con rioxarray.
- Cruce territorial y mapa.

## Estructura

```txt
README.md
data/{raw,interim,processed}/
notebooks/
src/
outputs/
reports/
```

## Cómo reproducir

```bash
# 1. Crear/activar entorno (ver README raíz)
# 2. Ejecutar extractores
python src/extract.py
# 3. Transformar
python src/transform.py
# 4. Abrir notebooks/ y ejecutar de principio a fin
```

> Proyecto en construcción. Estructura y plan definidos; pendiente de implementación.
