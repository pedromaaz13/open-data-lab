# Tratamiento de fechas

Las fechas son fuente habitual de errores (formatos, zonas horarias, periodicidad).

## Conceptos

- Parsear formatos locales (`dd/mm/aaaa`).
- Periodicidad: diaria, mensual, trimestral.
- Zonas horarias y UTC.
- Resampling y alineación de series.

## Ejemplo

```python
import polars as pl
df = df.with_columns(
    pl.col('fecha').str.strptime(pl.Date, '%d/%m/%Y')
)
```

## Buenas prácticas

- Normaliza a ISO 8601 (`AAAA-MM-DD`).
- Documenta la zona horaria.
- Cuidado con trimestres y semanas ISO.

## Errores comunes

- Mezclar `%m/%d` y `%d/%m`.
- Ignorar cambios de hora.
