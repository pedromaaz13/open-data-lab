# Matriz de decisión de herramientas

Cómo elegir la herramienta adecuada según el caso, sin sobre-ingeniería.

## Procesamiento de datos: ¿Pandas, Polars, DuckDB o Spark?

| Situación | Elección |
|---|---|
| EDA rápido, dataset < 1M filas | Pandas |
| Dataset 1M-100M filas, en una máquina | Polars o DuckDB |
| SQL sobre Parquet sin cargar en memoria | DuckDB |
| Dataset > memoria, joins complejos | DuckDB (out-of-core) |
| Cientos de GB / TB, cluster necesario | Spark / Databricks (evitar al inicio) |

## Base de datos: ¿DuckDB o PostgreSQL?

| Situación | Elección |
|---|---|
| Analítica local sobre ficheros | DuckDB |
| Persistencia, concurrencia, app en producción | PostgreSQL |
| Análisis geoespacial relacional | PostgreSQL + PostGIS |
| Compartir analítica en cloud | MotherDuck (DuckDB) o Supabase/Neon (Postgres) |

## Orquestación: ¿cron, GitHub Actions, Dagster o Airflow?

| Situación | Elección |
|---|---|
| 1-2 tareas programadas simples | GitHub Actions / cron |
| Pipelines con dependencias, lineage, assets | Dagster |
| Ya existe Airflow en la organización | Airflow (equivalente) |

## BI: ¿Metabase, Superset, Looker o Power BI?

| Situación | Elección |
|---|---|
| Empezar rápido, usuarios no técnicos | Metabase |
| Dashboards potentes, SQL Lab | Superset |
| Capa semántica enterprise | Looker (cloud) |
| Ecosistema Microsoft | Power BI |

## Mapas: ¿Folium, Kepler.gl, deck.gl o Mapbox?

| Situación | Elección |
|---|---|
| Mapa simple y rápido | Folium |
| Exploración geoespacial potente | Kepler.gl |
| Millones de puntos / app a medida | deck.gl / MapLibre |
| Mapas base avanzados de pago | Mapbox |

## Regla de oro

Empieza por la solución **más simple que funcione**. Sube de nivel solo cuando el
volumen, la concurrencia o el despliegue lo justifiquen.
