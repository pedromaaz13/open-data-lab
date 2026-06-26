# Normalización de códigos INE

Los códigos administrativos son la clave para cruzar datasets. Hay que normalizarlos siempre.

## Conceptos

- Código INE de municipio: **5 dígitos** (2 de provincia + 3 de municipio), con ceros a la izquierda.
- Provincia: 2 dígitos.
- NUTS: jerarquía europea (NUTS1/2/3).
- Equivalencias INE ↔ NUTS ↔ código postal (no 1:1).

## Problema típico

Excel/CSV comen los ceros a la izquierda: `01001` se convierte en `1001`.

## Ejemplo

```python
import polars as pl
df = df.with_columns(
    pl.col('cod_ine').cast(pl.Utf8).str.zfill(5)
)
```

## Buenas prácticas

- Carga los códigos siempre como string.
- Mantén una tabla maestra de municipios (CNIG/INE).
- Cuidado con fusiones/cambios de municipios entre años.
