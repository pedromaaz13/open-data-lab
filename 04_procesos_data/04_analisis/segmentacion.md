# Segmentación

Agrupar entidades (municipios, organismos) en perfiles homogéneos.

## Métodos

- Reglas de negocio (cuantiles, umbrales).
- Clustering (K-Means, jerárquico) — ver `05_prediccion_simulacion/clustering.md`.

## Ejemplo

```python
import polars as pl
df = df.with_columns(
    pl.col('renta').qcut(4, labels=['Q1','Q2','Q3','Q4']).alias('cuartil_renta')
)
```

## Buenas prácticas

- Escala variables antes de clustering.
- Interpreta y nombra los segmentos.
- Valida la estabilidad de los grupos.
