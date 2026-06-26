# Dashboards (Superset / Metabase)

Dashboards de BI sobre los modelos de datos del laboratorio.

## Opciones

- **Apache Superset**: dashboards potentes, SQL Lab, muchos tipos de gráfico.
- **Metabase**: más sencillo, ideal para empezar y para usuarios no técnicos.

## Levantar

```bash
docker compose --profile bi up
# Superset: http://localhost:8088   ·   Metabase: http://localhost:3000
```

## Buenas prácticas

- Conecta a DuckDB/Postgres con los modelos de dbt.
- Define métricas en la capa semántica, no en cada gráfico.
- Versiona la exportación de dashboards cuando sea posible.
