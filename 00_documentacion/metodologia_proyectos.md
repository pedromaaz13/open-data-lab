# Metodología de proyectos de datos

Metodología end-to-end que sigue cada proyecto del laboratorio. Inspirada en CRISP-DM
y en la práctica del periodismo de datos riguroso.

## 1. Pregunta de investigación

- Una pregunta clara, concreta y respondible con datos.
- Define el sujeto, la métrica, el ámbito geográfico y el periodo.
- Ejemplo: *"¿Cuántos años de salario medio cuesta comprar una vivienda en cada
  provincia española y cómo ha evolucionado 2015-2024?"*

## 2. Fuentes de datos

- Identificar fuentes **oficiales** primero (ver `03_fuentes_oficiales/`).
- Anotar URL, organismo, licencia, formato y fecha de consulta.
- Registrar cada fuente en `09_data_catalog/catalogo_datasets.csv`.

## 3. Extracción

- Scripts reproducibles en `src/` (no descargas manuales sin documentar).
- Guardar el crudo intacto en `data/raw/` (read-only conceptual).
- Documentar parámetros de la petición (endpoint, filtros, fecha).

## 4. Limpieza y transformación

- Normalizar códigos (INE, NUTS, CNAE), fechas y tipos.
- Tratar nulos, duplicados y outliers de forma documentada.
- Output intermedio en `data/interim/`, final en `data/processed/` (Parquet).

## 5. Modelo de datos

- Definir hechos y dimensiones (ver `04_procesos_data/03_modelado/`).
- Cuando aplique, modelar con dbt Core sobre DuckDB/Postgres.

## 6. Análisis exploratorio

- Distribuciones, correlaciones, series temporales, comparativas territoriales.
- Documentar hallazgos y descartes (qué no funcionó también informa).

## 7. Métricas

- Definir métricas de forma explícita y reproducible.
- Documentar la fórmula y las unidades en el diccionario de datos.

## 8. Visualizaciones

- Elegir el gráfico/mapa adecuado al mensaje (ver `04_procesos_data/06_visualizacion/`).
- Mapas con Kepler.gl / GeoPandas; series con Plotly/Altair; informes con Quarto.

## 9. Conclusiones

- Responder la pregunta inicial con evidencia.
- Distinguir correlación de causalidad.

## 10. Limitaciones

- Calidad de los datos, cobertura, sesgos, supuestos del modelo.
- Lo que el análisis **no** puede afirmar.

## 11. Reproducibilidad

- Cualquiera debe poder regenerar el resultado: `requirements.txt`, scripts,
  semillas aleatorias fijadas, instrucciones en el README del proyecto.

## Checklist final

- [ ] Pregunta clara y respondida
- [ ] Fuentes oficiales documentadas y catalogadas
- [ ] Extracción reproducible
- [ ] Limpieza documentada
- [ ] Calidad validada (ver `checklist_calidad_datos.md`)
- [ ] Trazabilidad completa
- [ ] Limitaciones declaradas
- [ ] Reproducible de cero
