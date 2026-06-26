# Stack recomendado del Open Data Lab

## Filosofía

Open source first. Cloud when it adds value.

El objetivo no es usar la herramienta más compleja, sino elegir la herramienta
adecuada para cada fase del proyecto.

## Stack principal

| Fase | Herramienta principal | Alternativa | Motivo |
|---|---|---|---|
| Desarrollo | Python + JupyterLab | Quarto | análisis reproducible |
| Entorno | Docker Compose | uv / Poetry | reproducibilidad |
| Extracción | requests/httpx | Playwright | APIs y scraping controlado |
| Procesado | Polars/Pandas | Spark | datasets pequeños-medios |
| SQL local | DuckDB | SQLite | analítica local sobre Parquet |
| Formato datos | Parquet/GeoParquet | CSV | eficiente y reproducible |
| Base de datos | PostgreSQL | DuckDB | persistencia relacional |
| Geoespacial | PostGIS | GeoPandas | análisis territorial |
| Transformación | dbt Core | SQL scripts | modelado profesional |
| Orquestación | Dagster | Airflow | assets, lineage y pipelines |
| BI Open Source | Apache Superset | Metabase | dashboards profesionales |
| Mapas | Kepler.gl | deck.gl / QGIS | visualización geoespacial |
| App rápida | Streamlit | Dash | prototipos de datos |
| Backend | FastAPI | Flask | APIs de datos |
| Automatización | GitHub Actions | cron | ejecución programada |
| Observabilidad | Grafana | logs simples | métricas y monitorización |

## Stack no prioritario al inicio

No se usará inicialmente salvo que el caso lo justifique:

```txt
Kafka
Flink
Spark cluster
Databricks
Snowflake
BigQuery productivo
Airflow gestionado
Looker
Tableau
Power BI Service
```

**Motivo:** coste innecesario, complejidad operativa, dependencia cloud, no todos
los proyectos requieren escala enterprise. El objetivo inicial es un portfolio
reproducible y una arquitectura pro open source.

## Servicios de pago opcionales

| Servicio | Para qué | Cuándo usarlo |
|---|---|---|
| Supabase / Neon | Postgres gestionado | si se quiere desplegar una app |
| MotherDuck | DuckDB cloud | si se quiere compartir analítica DuckDB |
| Vercel | frontend | si se usa Next.js |
| Render / Fly.io / Railway | backend/apps | si se despliega FastAPI o Streamlit |
| Grafana Cloud | observabilidad | si no se quiere self-hostear Grafana |
| Metabase Cloud | BI gestionado | si se quiere evitar despliegue |
| Mapbox | mapas avanzados | si Kepler/MapLibre no basta |
| Sentinel Hub | datos satelitales | si Copernicus requiere procesamiento serio |
| BigQuery | warehouse cloud | si el volumen o concurrencia lo justifica |

## Equivalencias enterprise/cloud

| Stack open source del repo | Equivalente enterprise/cloud |
|---|---|
| DuckDB | BigQuery / Snowflake / Databricks SQL |
| PostgreSQL/PostGIS | BigQuery GIS / Databricks + Mosaic / Snowflake Geospatial |
| dbt Core | dbt Cloud / Dataform / workflows cloud |
| Dagster | Airflow / Cloud Composer / Azure Data Factory |
| Superset | Looker / Power BI / Tableau |
| Kepler.gl | deck.gl / CARTO / Mapbox |
| Streamlit | Power BI apps / Looker extensions / custom web apps |
| FastAPI | APIs internas / microservicios data |
| Parquet/GeoParquet | Delta Lake / Iceberg / BigLake |
| GitHub Actions | Azure DevOps / GitLab CI / Cloud Build |
