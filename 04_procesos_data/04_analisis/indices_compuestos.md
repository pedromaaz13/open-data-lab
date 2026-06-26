# Índices compuestos

Combinar varias variables en un único indicador (vulnerabilidad, calidad de vida).

## Pasos

1. Selección de indicadores.
2. Normalización (min-max, z-score).
3. Ponderación (igual, experta, PCA).
4. Agregación (media, geométrica).
5. Análisis de sensibilidad.

## Ejemplo

```python
# min-max + media ponderada
norm = (df[cols] - df[cols].min()) / (df[cols].max() - df[cols].min())
df['indice'] = (norm * pesos).sum(axis=1)
```

## Buenas prácticas

- Documenta pesos y método.
- Haz análisis de sensibilidad (¿cambia el ranking si cambian los pesos?).
- Sigue el manual OECD/JRC de índices compuestos.
