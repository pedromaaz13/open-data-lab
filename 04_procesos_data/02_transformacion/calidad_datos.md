# Calidad de datos (en transformación)

Validar en el pipeline, no solo al final. Ver `01_skills/data_quality.md` y el checklist en docs.

## Validación con pandera

```python
import pandera as pa
schema = pa.DataFrameSchema({
    'cod_ine': pa.Column(str, pa.Check.str_length(5, 5)),
    'valor': pa.Column(float, pa.Check.ge(0)),
})
schema.validate(df)
```

## Dimensiones

- Completitud, validez, unicidad, consistencia.
- Cardinalidad de joins.
- Rangos plausibles.

## Buenas prácticas

- Reglas versionadas junto al código.
- Falla rápido si la calidad no se cumple.
- Genera un data quality report (ver template).
