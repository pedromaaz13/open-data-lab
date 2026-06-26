# Simulación Monte Carlo

Estimar resultados bajo incertidumbre simulando muchos escenarios aleatorios.

## Cuándo

- Propagar incertidumbre de parámetros.
- Estimar rangos plausibles, no un único número.

## Ejemplo

```python
import numpy as np
rng = np.random.default_rng(42)
sims = rng.normal(mu, sigma, size=(10000,))
p5, p95 = np.percentile(sims, [5, 95])
```

## Buenas prácticas

- Justifica las distribuciones de entrada.
- Fija la semilla para reproducibilidad.
- Reporta percentiles, no solo la media.
