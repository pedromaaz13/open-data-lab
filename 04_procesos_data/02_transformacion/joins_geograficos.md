# Joins geográficos

Unir datasets por relación espacial o por código territorial.

## Dos enfoques

1. **Join atributivo** por código (INE/NUTS): rápido y exacto si los códigos están normalizados.
2. **Spatial join** por geometría: cuando no hay código común.

## Ejemplo

```python
import geopandas as gpd
puntos = puntos.to_crs(areas.crs)
join = gpd.sjoin(puntos, areas, predicate='within')
```

## Buenas prácticas

- Homogeneiza CRS antes del spatial join.
- Verifica cardinalidad (1:1, 1:N).
- Prefiere join por código si está disponible.

## Errores comunes

- CRS distintos.
- Puntos en frontera asignados a varias áreas.
