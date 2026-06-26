# Star schema

El esquema en estrella: una tabla de hechos central rodeada de dimensiones.

## Estructura

```txt
        dim_tiempo
            |
dim_territorio — FCT_CONTRATOS — dim_organismo
            |
        dim_cpv
```

## Ventajas

- Joins simples (hecho ↔ dimensión).
- Buen rendimiento analítico.
- Intuitivo para BI (Superset/Metabase/Looker).

## Ejemplo dbt

```sql
-- models/marts/fct_contratos.sql
select c.id, c.importe, d.cod_ine, t.anio, o.organismo_id
from {{ ref('stg_contratos') }} c
left join {{ ref('dim_territorio') }} d using (cod_ine)
left join {{ ref('dim_tiempo') }} t using (fecha)
```
