# Stack enterprise / cloud

Documentado como **referencia profesional y evolución posible**, no como punto de
partida. Demuestra que el stack open source del laboratorio tiene equivalencia
directa con las herramientas que se usan en empresa.

## Equivalencias

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

## Perfil profesional cubierto

El laboratorio está alineado con un perfil de **Analytics Engineer / Data Analyst /
Modern BI Consultant**, con dominio de:

- Modern BI y semantic layers.
- Modelado de datos.
- BigQuery, GCP.
- Looker / LookML.
- Power BI.
- Databricks, Microsoft Fabric.
- SQL, Git, CI/CD.
- Dashboards y data products.
- IA aplicada a datos, agentes y workflows de análisis.

## Cuándo escalar a cloud

| Señal | Acción |
|---|---|
| Volumen > lo que maneja una máquina | Warehouse cloud (BigQuery/Snowflake) |
| Alta concurrencia multiusuario | Warehouse + BI gestionado |
| Necesidad de despliegue público | Supabase/Neon, Render/Fly.io, Vercel |
| Procesamiento satélite serio | Sentinel Hub / openEO cloud |
| Equipo y gobernanza corporativa | Looker/Power BI + capa semántica |

## Principio

Cloud cuando aporta valor real (volumen, concurrencia, despliegue, gobernanza), no
por defecto. El criterio profesional es saber **cuándo NO escalar**.
