# Modelo dimensional

Metodología Kimball: organizar datos en hechos (medidas) y dimensiones (contexto) para analítica clara.

## Por qué

- Consultas y dashboards más simples y rápidos.
- Métricas consistentes.
- Fácil de entender por analistas.

## Conceptos

- Grano: el nivel de detalle de la tabla de hechos (1 fila = 1 contrato).
- Dimensiones conformadas: compartidas entre hechos (tiempo, territorio).
- Slowly Changing Dimensions (SCD).

## Buenas prácticas

- Define el grano antes de modelar.
- Reutiliza dimensiones (territorio, tiempo).
- Implementa con dbt sobre DuckDB/Postgres.
