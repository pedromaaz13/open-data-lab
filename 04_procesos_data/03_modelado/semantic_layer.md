# Capa semántica

Centralizar métricas y dimensiones para que todo el BI use las mismas definiciones. Ver `01_skills/semantic_modeling.md`.

## Qué es

Una capa que define métricas, dimensiones y joins una vez, y los expone a todas las herramientas de visualización.

## Opciones

- **dbt Semantic Layer / MetricFlow** (recomendado con dbt Core).
- **Cube** (open source, headless BI).
- **LookML** (equivalente enterprise en Looker).

## Beneficio

- Consistencia: una sola definición de 'gasto total'.
- Reutilización entre Superset, Metabase, Streamlit.
- Gobernanza de métricas.
