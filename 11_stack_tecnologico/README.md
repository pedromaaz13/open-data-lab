# 11 · Stack tecnológico

El cerebro de arquitectura del laboratorio. Documenta **qué herramientas usar, por
qué, cuánto cuestan y cuándo escalar a cloud**.

## Filosofía

**Open source first. Cloud when it adds value.**

No se trata de usar la tecnología más grande, sino la **arquitectura adecuada para
cada problema**.

## Documentos clave

| Archivo | Contenido |
|---|---|
| `stack_recomendado.md` | Stack principal por fase |
| `matriz_tecnologias.csv` | Clasificación de cada tech por coste y recomendación |
| `matriz_decision_herramientas.md` | Cómo elegir herramienta según el caso |
| `costes_y_limitaciones.md` | Costes y límites por tecnología |
| `arquitectura_referencia.md` | Arquitectura pro open source de referencia |
| `stack_local.md` | Capa local (análisis y prototipos) |
| `stack_pro_open_source.md` | Capa pro open source (pipelines, BI, mapas) |
| `stack_enterprise_cloud.md` | Equivalencias enterprise/cloud |

## Subcarpetas por capa

```txt
01_extraccion_ingesta/      06_data_lake_lakehouse/      11_frontend_apps/
02_orquestacion/            07_modelado_semantico/       12_devops_cloud/
03_procesamiento_datos/     08_visualizacion_bi/         13_decision_records/
04_streaming_realtime/      09_geoespacial_satelite/
05_almacenamiento_bases_datos/  10_backend_apis/
```

## Las tres capas del stack

1. **Stack local** — análisis, notebooks y prototipos (Python, DuckDB, Parquet).
2. **Stack pro open source** — pipelines, modelado, dashboards y mapas (dbt, Dagster,
   Postgres/PostGIS, Superset, Kepler.gl).
3. **Stack enterprise/cloud** — referencia profesional y evolución posible (BigQuery,
   Databricks, Snowflake, Looker, Power BI).
