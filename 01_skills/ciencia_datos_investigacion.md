# Ciencia de datos para investigación

## Para qué sirve

Aplicar el método científico a problemas sociales y públicos con datos: hipótesis, evidencia, validación.

## Conceptos principales

- Diseño de la investigación y operacionalización de variables.
- Feature engineering desde datos públicos.
- Validación cruzada y data leakage.
- Reproducibilidad y revisión por pares.
- Comunicación de resultados.

## Librerías útiles

- `scikit-learn`, `statsmodels`, `pandas`, `polars`, `matplotlib`.

## Ejemplos de uso

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
scores = cross_val_score(RandomForestRegressor(random_state=42), X, y, cv=5)
print(scores.mean())
```

## Errores comunes

- Data leakage entre train y test.
- Sobreajustar a un dataset pequeño.
- Confundir predicción con explicación.

## Mini proyecto recomendado

Construir un índice de vulnerabilidad municipal y validar su robustez con distintos pesos.

## Recursos para profundizar

- *Doing Data Science*.
- Our World in Data (metodologías).
- Papers de ciencia social computacional.
