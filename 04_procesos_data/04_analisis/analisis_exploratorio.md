# Análisis exploratorio (EDA)

Primer contacto sistemático con los datos: distribuciones, relaciones, calidad.

## Qué mirar

- Distribución de cada variable (histograma, percentiles).
- Nulos y outliers.
- Relaciones entre variables.
- Patrones territoriales y temporales.

## Ejemplo

```python
df.describe()
df.select(pl.col('precio_m2').quantile(q) for q in [0.1,0.5,0.9])
```

## Buenas prácticas

- Documenta hallazgos y descartes.
- No saques conclusiones causales de un EDA.
- Usa visualización para detectar patrones.
