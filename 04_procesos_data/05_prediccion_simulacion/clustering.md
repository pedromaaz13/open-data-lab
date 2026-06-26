# Clustering

Agrupar entidades sin etiquetas previas.

## Métodos

- K-Means (esférico, hay que fijar k).
- Jerárquico (dendrograma).
- DBSCAN (densidad, detecta ruido).

## Ejemplo

```python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
X = StandardScaler().fit_transform(df[cols])
labels = KMeans(n_clusters=5, random_state=42).fit_predict(X)
```

## Buenas prácticas

- Escala siempre las features.
- Elige k con método del codo / silueta.
- Interpreta y nombra los clusters.
