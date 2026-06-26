# Forecasting

Predicción de series temporales. Ver `01_skills/series_temporales_forecasting.md`.

## Métodos

- Suavizado exponencial (Holt-Winters).
- ARIMA/SARIMA.
- Prophet.
- Modelos ML (gradient boosting con lags).

## Ejemplo

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing
fit = ExponentialSmoothing(y, trend='add', seasonal='add', seasonal_periods=12).fit()
pred = fit.forecast(12)
```

## Buenas prácticas

- Backtesting con ventanas temporales.
- Reporta intervalos de incertidumbre.
- No extrapoles ciegamente.
