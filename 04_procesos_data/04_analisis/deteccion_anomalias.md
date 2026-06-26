# Detección de anomalías

Identificar valores o patrones atípicos (p. ej. contratos sospechosos).

## Métodos

- Estadísticos: z-score, IQR, percentiles.
- ML: Isolation Forest, LOF.
- Reglas de negocio (importes redondos, adjudicatario único).

## Ejemplo

```python
from sklearn.ensemble import IsolationForest
flags = IsolationForest(contamination=0.01, random_state=42).fit_predict(X)
```

## Buenas prácticas

- Una anomalía estadística no implica irregularidad: contextualiza.
- Combina métodos automáticos con criterio experto.
- Documenta umbrales.
