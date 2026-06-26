# Validación de modelos

Garantizar que un modelo generaliza y no está sobreajustado.

## Técnicas

- Train/validation/test.
- Validación cruzada (k-fold; temporal para series).
- Métricas adecuadas al problema (RMSE, MAE, F1, ROC-AUC).

## Riesgos

- Data leakage.
- Overfitting.
- Métrica equivocada.

## Buenas prácticas

- Separa test antes de tocar nada.
- Para series temporales, valida hacia adelante.
- Reporta varias métricas y la incertidumbre.
