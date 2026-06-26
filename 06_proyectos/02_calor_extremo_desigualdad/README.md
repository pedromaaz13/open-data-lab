# Calor extremo y desigualdad

## Pregunta de investigación

¿Las zonas con menor renta sufren más exposición al calor extremo?

## Contexto

El cambio climático intensifica las olas de calor. La exposición no es homogénea: depende de geografía, urbanismo y renta. Cruzar temperatura con renta revela desigualdad climática.

## Fuentes de datos previstas

- Series de temperatura (AEMET OpenData).
- Temperatura superficial (Copernicus / Landsat).
- Renta por municipio (INE Atlas de Renta).

## Metodología

1. Extraer temperaturas y días de calor extremo.
2. Calcular indicadores de exposición por municipio.
3. Cruzar con renta.
4. Analizar correlación y desigualdad.

## Métricas principales

- Días/año por encima de umbral de calor.
- Exposición media ponderada por población.
- Correlación calor-renta.

## Visualizaciones previstas

- Mapa de exposición al calor.
- Scatter calor vs renta.
- Islas de calor urbano (satélite).

## Posibles modelos o simulaciones

- Regresión exposición ~ renta + densidad.
- Índice de vulnerabilidad climática.

## Limitaciones

- Estaciones meteorológicas dispersas.
- Falacia ecológica con datos agregados.

## Próximos pasos

- Extractor AEMET.
- Procesado satélite (temperatura superficial).
- Análisis y mapa.

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
