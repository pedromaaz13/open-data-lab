# Correlaciones

Medir asociación entre variables, sin confundirla con causalidad.

## Conceptos

- Pearson (lineal) vs Spearman (monotónica).
- Matriz de correlaciones.
- Correlación ≠ causalidad.

## Ejemplo

```python
import pandas as pd
corr = df.to_pandas().corr(method='spearman')
```

## Advertencias

- Variables de confusión.
- Falacia ecológica con datos agregados.
- Correlaciones espurias en series temporales.
