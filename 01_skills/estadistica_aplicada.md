# Estadística aplicada

## Para qué sirve

Fundamento para que los análisis sean rigurosos: describir, inferir y no engañarse (ni engañar).

## Conceptos principales

- Descriptiva: media, mediana, percentiles, dispersión.
- Distribuciones y normalidad.
- Inferencia: intervalos de confianza, contraste de hipótesis, p-valores.
- Correlación vs causalidad.
- Regresión lineal y logística.
- Sesgos comunes (selección, supervivencia, ecológico).

## Librerías útiles

- `scipy.stats`, `statsmodels`, `numpy`, `pingouin`.

## Ejemplos de uso

```python
import statsmodels.formula.api as smf
model = smf.ols('precio_m2 ~ salario_medio + densidad', data=df).fit()
print(model.summary())
```

## Errores comunes

- Interpretar correlación como causa.
- p-hacking y comparaciones múltiples sin corregir.
- Ignorar el tamaño del efecto frente a la significancia.
- Falacia ecológica.

## Mini proyecto recomendado

Analizar si existe relación significativa entre temperatura extrema y renta media por municipio.

## Recursos para profundizar

- *Statistics Done Wrong* (Reinhart).
- *Think Stats* (Downey).
- StatQuest (YouTube).
