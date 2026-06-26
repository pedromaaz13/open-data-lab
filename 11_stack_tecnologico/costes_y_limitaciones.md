# Costes y limitaciones

Clasificación de coste y límites prácticos de cada tecnología.

## Niveles de coste

```txt
gratis_local           todo en tu máquina, sin coste
open_source_self_hosted gratis el software, pagas el servidor/operación
free_tier              capa gratuita de un servicio gestionado
pago_bajo              decenas de € / mes
pago_profesional       cientos de € / mes
enterprise             miles de € / mes o licencias corporativas
```

## Recomendación para el repo

```txt
usar_ahora        stack base del laboratorio
documentar        relevante como referencia/evolución, no se usa aún
usar_si_aporta    se activa si el caso lo justifica
evitar_al_inicio  sobre-ingeniería para el objetivo actual
solo_enterprise   solo en contexto corporativo real
```

## Costes por capa

| Capa | Open source self-hosted | Cloud gestionado |
|---|---|---|
| Análisis local | 0 € (tu máquina) | — |
| Postgres/PostGIS | servidor (~5-20 €/mes VPS) | Supabase/Neon free tier → pago |
| Warehouse | DuckDB 0 € | BigQuery (pago por uso), Snowflake (alto) |
| Orquestación | Dagster self-hosted | Dagster Cloud / Composer |
| BI | Superset/Metabase self-hosted | Looker/Power BI (licencias) |
| Mapas | Kepler/MapLibre 0 € | Mapbox (free tier → pago) |
| Despliegue apps | — | Render/Fly.io free tier → pago bajo |

## Limitaciones a tener en cuenta

- **DuckDB:** single-node; no para alta concurrencia multiusuario.
- **PostGIS:** requiere operar el servidor; tuning para rásteres grandes.
- **Superset:** curva de configuración inicial.
- **Self-hosting:** ahorras licencia pero asumes mantenimiento y seguridad.
- **Free tiers cloud:** límites de cómputo/almacenamiento; vigilar costes al escalar.
- **Satélite:** volumen masivo; procesa por ventanas/tiles.

## Principio de coste

El coste no es solo la factura: incluye el **coste operativo** (tiempo de mantener,
monitorizar y depurar). A veces un servicio gestionado de pago bajo es más barato
que self-hostear en tiempo.
