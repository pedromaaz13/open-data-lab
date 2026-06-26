# Matplotlib, Plotly y Altair

Las tres librerías de gráficos del laboratorio. Cuándo usar cada una.

## Cuándo

- **Matplotlib**: control total, figuras para informes/publicación.
- **Plotly**: interactividad, dashboards.
- **Altair**: gráficos declarativos (gramática de gráficos), exploración rápida.

## Ejemplo Altair

```python
import altair as alt
alt.Chart(df).mark_line().encode(x='fecha:T', y='precio:Q', color='provincia:N')
```

## Buenas prácticas

- Una idea por gráfico.
- Ejes honestos, fuente y unidades visibles.
- Paletas aptas para daltonismo.
