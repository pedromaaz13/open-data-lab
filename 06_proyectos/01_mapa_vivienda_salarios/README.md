# Mapa de vivienda y salarios

## Pregunta de investigación

¿Cuántos años de salario medio cuesta comprar una vivienda en cada provincia/municipio español y cómo ha evolucionado?

## Contexto

El acceso a la vivienda es uno de los principales problemas sociales en España. Cruzar precio de la vivienda con salarios permite medir el esfuerzo real de acceso por territorio.

## Fuentes de datos previstas

- Precio del m² (Mº Vivienda / INE IPV).
- Salario medio (INE / AEAT).
- Límites administrativos (CNIG/IGN).

## Metodología

1. Extraer precios y salarios por territorio.
2. Normalizar códigos INE.
3. Calcular ratio = precio_m2 * 90 / salario_medio (años).
4. Unir con geometrías y mapear.

## Métricas principales

- Ratio años de salario por vivienda de 90 m².
- Variación interanual.
- Esfuerzo de acceso (% renta).

## Visualizaciones previstas

- Mapa coroplético (Kepler.gl / Folium).
- Series temporales por provincia.
- Ranking de provincias.

## Posibles modelos o simulaciones

- Forecast del ratio a 12-24 meses.
- Clustering de provincias por perfil de esfuerzo.

## Limitaciones

- Precios y salarios con metodologías y coberturas distintas.
- Granularidad municipal parcial.

## Próximos pasos

- Definir extractores en `src/`.
- Construir dataset processed.
- Notebook de análisis y mapa.

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
