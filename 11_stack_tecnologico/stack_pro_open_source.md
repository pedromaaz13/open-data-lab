# Stack pro open source

Capa profesional para pipelines, modelado, dashboards y mapas. Open source
self-hosted (con Docker Compose).

## Componentes

| Capa | Herramienta |
|---|---|
| Base de datos | PostgreSQL |
| Geoespacial | PostGIS |
| Transformación | dbt Core |
| Orquestación | Dagster |
| BI | Apache Superset / Metabase |
| Mapas | Kepler.gl / deck.gl / MapLibre |
| Apps | Streamlit |
| Backend | FastAPI |
| Almacenamiento objeto | MinIO (S3 local) |
| Observabilidad | Grafana |
| Entorno | Docker Compose |
| CI/CD | GitHub Actions |

## Cuándo activarlo

- Pipelines recurrentes con dependencias.
- Modelado serio (hechos/dimensiones, métricas reutilizables).
- Dashboards para compartir.
- Análisis geoespacial relacional.
- Apps y APIs de datos.

## Levantar por perfiles

```bash
docker compose --profile core up           # postgres + minio
docker compose --profile geo up            # postgis
docker compose --profile bi up             # superset + metabase
docker compose --profile orchestration up  # dagster
docker compose --profile observability up  # grafana
docker compose --profile full up           # todo
```

## Ventajas

- Capacidades profesionales sin coste de licencias.
- Equivalente directo al stack enterprise (ver `stack_enterprise_cloud.md`).
- Control total y portabilidad.

## Coste

Software gratis; pagas el servidor (VPS) y el coste operativo de mantenerlo.
