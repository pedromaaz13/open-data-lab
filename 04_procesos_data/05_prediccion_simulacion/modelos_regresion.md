# Modelos de regresión

Explicar o predecir una variable continua a partir de otras.

## Tipos

- Lineal (OLS) e interpretación de coeficientes.
- Regularizada (Ridge/Lasso).
- No lineal (árboles, gradient boosting).

## Ejemplo

```python
import statsmodels.formula.api as smf
m = smf.ols('precio ~ salario + densidad + costa', data=df).fit()
print(m.summary())
```

## Buenas prácticas

- Revisa supuestos (linealidad, homocedasticidad).
- Cuidado con multicolinealidad.
- Distingue explicación de predicción.
