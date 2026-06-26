# Pandas, Polars y DuckDB

## Para qué sirve

Las tres herramientas de procesado tabular del laboratorio. Saber cuándo usar cada una según tamaño y caso.

## Conceptos principales

- Pandas: ecosistema amplio, ideal para EDA y datasets pequeños.
- Polars: rápido, lazy evaluation, paralelo, datasets medianos.
- DuckDB: SQL analítico sobre Parquet/CSV sin cargar todo en memoria.
- Interoperabilidad vía Arrow (zero-copy).

## Librerías útiles

- `pandas`, `polars`, `duckdb`, `pyarrow`.

## Ejemplos de uso

```python
import duckdb
# DuckDB consulta Parquet directamente, sin cargarlo entero
res = duckdb.sql('''
    SELECT provincia, AVG(precio_m2) AS p
    FROM 'data/processed/*.parquet'
    GROUP BY provincia
''').pl()  # devuelve un DataFrame Polars
```

## Errores comunes

- Cargar en Pandas un dataset que no cabe en memoria (usar DuckDB/Polars).
- Mezclar APIs sin necesidad.
- Ignorar el modo lazy de Polars (`scan_parquet` + `collect`).

## Mini proyecto recomendado

Comparar el mismo agregado en Pandas vs Polars vs DuckDB sobre un dataset de 5M filas y medir tiempos.

## Recursos para profundizar

- Docs de Polars, DuckDB y Arrow.
- Benchmarks h2oai db-benchmark.
