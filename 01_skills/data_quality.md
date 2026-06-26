# Calidad de datos

## Para qué sirve

Garantizar que los datos son completos, válidos, únicos y consistentes antes de publicar.

## Conceptos principales

- Dimensiones de calidad (completitud, validez, unicidad, consistencia).
- Validación por esquema y por reglas de negocio.
- Tests automatizados en pipeline.
- Data contracts.

## Librerías útiles

- `pandera`, `great_expectations`, tests de `dbt`.

## Ejemplos de uso

```python
import pandera as pa
schema = pa.DataFrameSchema({
    'cod_ine': pa.Column(str, pa.Check.str_length(5, 5)),
    'precio_m2': pa.Column(float, pa.Check.gt(0)),
})
schema.validate(df)
```

## Errores comunes

- Validar solo al final, no en el pipeline.
- No versionar las reglas de calidad.
- Ignorar la cardinalidad en joins.

## Mini proyecto recomendado

Añadir una suite de validación pandera a un dataset processed del repo.

## Recursos para profundizar

- Docs de pandera y Great Expectations.
- Ver `00_documentacion/checklist_calidad_datos.md`.
