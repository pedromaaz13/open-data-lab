# SQL analítico

## Para qué sirve

SQL es el lenguaje universal del dato. Aquí se usa para consultar DuckDB, Postgres y, por equivalencia, BigQuery/Snowflake.

## Conceptos principales

- SELECT, JOINs, agregaciones, GROUP BY, HAVING.
- Window functions (`ROW_NUMBER`, `RANK`, `LAG`, `SUM() OVER`).
- CTEs y subconsultas.
- CTAS y vistas materializadas.
- Modelado en SQL con dbt.

## Librerías útiles

- `duckdb` (analítica local sobre Parquet).
- `psycopg`/SQLAlchemy para Postgres.
- `sqlfluff` para linting.
- `dbt-core` para modelado.

## Ejemplos de uso

```sql
-- Top 5 provincias por ratio vivienda/salario con window function
WITH base AS (
    SELECT provincia, precio_m2 * 90 / salario_medio AS ratio_anios
    FROM 'data/processed/vivienda.parquet'
)
SELECT provincia, ratio_anios,
       RANK() OVER (ORDER BY ratio_anios DESC) AS ranking
FROM base
QUALIFY ranking <= 5;
```

## Errores comunes

- JOINs que multiplican filas (cardinalidad mal entendida).
- Olvidar `GROUP BY` de columnas no agregadas.
- Comparar NULLs con `=` en vez de `IS NULL`.
- No indexar en Postgres consultas frecuentes.

## Mini proyecto recomendado

Modelar un star schema simple de contratación pública en DuckDB con dbt y tests de calidad.

## Recursos para profundizar

- Documentación de DuckDB y dbt.
- *SQL for Data Scientists*.
- Mode SQL Tutorial.
