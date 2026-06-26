# Arquitectura de referencia (pro open source)

Arquitectura principal del laboratorio. Reproducible en local, profesional con open
source y escalable a cloud cuando el caso lo justifique.

## Flujo de datos

```txt
APIs oficiales / CSV / scraping / Copernicus
        ↓
Python extractors  (src/extract_*.py)
        ↓
data/raw  (crudo intacto + trazabilidad)
        ↓
Polars / Pandas / DuckDB  (limpieza y transformación)
        ↓
data/processed en Parquet / GeoParquet
        ↓
dbt Core  (modelado dimensional + tests de calidad)
        ↓
DuckDB + PostgreSQL/PostGIS  (almacenamiento analítico y geoespacial)
        ↓
Dagster  (orquestación, lineage, materialización de assets)
        ↓
Superset / Metabase / Kepler.gl / Streamlit  (visualización)
        ↓
FastAPI opcional  (servir datos como API)
        ↓
README + artículo + dashboard + mapa  (entregables)
```

## Capas

1. **Ingesta:** extractores Python reproducibles → `data/raw`.
2. **Procesamiento:** Polars/Pandas/DuckDB → `data/processed` (Parquet/GeoParquet).
3. **Modelado:** dbt Core sobre DuckDB/Postgres (hechos y dimensiones + tests).
4. **Almacenamiento:** DuckDB (analítica), PostgreSQL/PostGIS (relacional/geo).
5. **Orquestación:** Dagster (assets, lineage) + GitHub Actions (programación).
6. **Visualización:** Superset/Metabase (BI), Kepler.gl (mapas), Streamlit (apps),
   Quarto (informes).
7. **Producto:** FastAPI opcional para servir resultados.
8. **Entrega:** README + artículo de storytelling + dashboard + mapa.

## Evolución a cloud (solo si aporta valor)

| Componente local | Evolución cloud |
|---|---|
| DuckDB | BigQuery / Snowflake / Databricks SQL |
| Postgres/PostGIS | Supabase/Neon → BigQuery GIS / Databricks Mosaic |
| dbt Core | dbt Cloud |
| Dagster | Dagster Cloud / Cloud Composer |
| Superset | Looker / Power BI |
| Parquet | Delta Lake / Iceberg |

## Principio

No todos los proyectos activan todas las capas. Cada proyecto usa **solo las piezas
que necesita**. El stack base existe; el proyecto decide qué encender.
