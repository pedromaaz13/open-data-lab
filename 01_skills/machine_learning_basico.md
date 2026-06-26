# Machine learning básico

## Para qué sirve

Modelos predictivos y de agrupación aplicados a datos públicos, con foco en interpretabilidad.

## Conceptos principales

- Supervisado (regresión, clasificación) vs no supervisado (clustering).
- Train/validation/test y validación cruzada.
- Métricas (RMSE, MAE, accuracy, F1, ROC-AUC).
- Overfitting y regularización.
- Interpretabilidad (coeficientes, SHAP, importancia).

## Librerías útiles

- `scikit-learn`, `xgboost`/`lightgbm`, `shap`.

## Ejemplos de uso

```python
from sklearn.cluster import KMeans
labels = KMeans(n_clusters=5, random_state=42).fit_predict(X_scaled)
df['cluster'] = labels
```

## Errores comunes

- No escalar features cuando el modelo lo requiere.
- Data leakage.
- Optimizar métrica equivocada para el problema.
- Usar ML donde basta una regla simple.

## Mini proyecto recomendado

Clustering de municipios por perfil socioeconómico e interpretar los grupos.

## Recursos para profundizar

- *Hands-On Machine Learning* (Géron).
- scikit-learn user guide.
- StatQuest.
