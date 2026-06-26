# Limpieza de datos

Pasos sistemáticos para convertir datos crudos en datos fiables.

## Checklist

- Tipos correctos (numéricos, fechas, categóricas).
- Nulos: detectar, entender y tratar (no borrar a ciegas).
- Duplicados: identificar la clave y deduplicar.
- Outliers: detectar y decidir (mantener/marcar/eliminar con criterio).
- Strings: trim, mayúsculas/acentos, normalización.

## Ejemplo

```python
import polars as pl
df = (pl.read_csv('data/raw/x.csv', separator=';')
        .with_columns(pl.col('importe').str.replace(',', '.').cast(pl.Float64))
        .drop_nulls('cod_ine')
        .unique(subset=['cod_ine', 'anio']))
df.write_parquet('data/processed/x.parquet')
```

## Buenas prácticas

- Documenta cada decisión no trivial.
- Mantén el raw intacto.
- Valida con pandera al final.
