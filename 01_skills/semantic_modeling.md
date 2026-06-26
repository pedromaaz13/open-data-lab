# Modelado semántico

## Para qué sirve

Definir métricas y dimensiones de forma centralizada y reutilizable (la base del modern BI).

## Conceptos principales

- Capa semántica: métricas, dimensiones, joins definidos una vez.
- Modelo dimensional (hechos/dimensiones).
- Métricas consistentes entre dashboards.
- LookML/dbt Semantic Layer como referencia profesional.

## Librerías útiles

- `dbt-core`, dbt Semantic Layer / MetricFlow.
- Cube (open source) como alternativa.

## Ejemplos de uso

```yaml
# dbt metric (ejemplo conceptual)
metrics:
  - name: gasto_total
    type: sum
    sql: importe
    model: ref('fct_contratos')
    dimensions: [provincia, organismo, anio]
```

## Errores comunes

- Definir la misma métrica de 5 formas en 5 dashboards.
- Acoplar la lógica de negocio a la herramienta de BI.

## Mini proyecto recomendado

Definir 5 métricas de contratación pública en una capa semántica reutilizable.

## Recursos para profundizar

- dbt Semantic Layer docs.
- *The Unified Star Schema*.
- Cube docs.
