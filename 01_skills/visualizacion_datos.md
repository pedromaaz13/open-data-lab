# Visualización de datos

## Para qué sirve

Convertir análisis en gráficos que comunican con honestidad y claridad.

## Conceptos principales

- Gramática de gráficos (datos → estética → geometría).
- Elegir el gráfico según el mensaje.
- Color, escala y percepción.
- Gráficos estáticos vs interactivos.
- Accesibilidad (daltonismo, contraste).

## Librerías útiles

- `matplotlib`, `plotly`, `altair`, `seaborn`.
- `kepler.gl`, `folium`, `deck.gl` para mapas.

## Ejemplos de uso

```python
import altair as alt
alt.Chart(df).mark_bar().encode(
    x='provincia:N', y='ratio_anios:Q', color='ratio_anios:Q'
).properties(title='Años de salario por vivienda')
```

## Errores comunes

- Ejes truncados que engañan.
- Demasiada información en un gráfico.
- Paletas no aptas para daltónicos.
- Pie charts con muchas categorías.

## Mini proyecto recomendado

Recrear un gráfico de un medio de datos y mejorar su legibilidad y honestidad.

## Recursos para profundizar

- *The Visual Display of Quantitative Information* (Tufte).
- *Storytelling with Data*.
- Datawrapper Academy.
