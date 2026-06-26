# Series temporales y forecasting

## Para qué sirve

Analizar y predecir evolución en el tiempo: precios, temperaturas, gasto público.

## Conceptos principales

- Tendencia, estacionalidad, ruido.
- Estacionariedad y diferenciación.
- ARIMA/SARIMA, suavizado exponencial.
- Prophet y modelos modernos.
- Backtesting y métricas de error.

## Librerías útiles

- `statsmodels`, `prophet`, `sktime`, `pmdarima`, `darts`.

## Ejemplos de uso

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing
fit = ExponentialSmoothing(serie, trend='add', seasonal='add', seasonal_periods=12).fit()
pred = fit.forecast(12)
```

## Errores comunes

- Validar con datos futuros que el modelo ya vio.
- Ignorar estacionalidad.
- Extrapolar sin intervalos de confianza.

## Mini proyecto recomendado

Forecast del índice de precios de vivienda por provincia a 12 meses con bandas de incertidumbre.

## Recursos para profundizar

- *Forecasting: Principles and Practice* (Hyndman).
- Docs de Prophet y sktime.
