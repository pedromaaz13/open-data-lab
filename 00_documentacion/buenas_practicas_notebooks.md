# Buenas prácticas con notebooks

Los notebooks son para **explorar y narrar**, no para esconder lógica crítica.

## Principios

1. **Un notebook, un objetivo.** Si crece demasiado, divídelo o mueve lógica a `src/`.
2. **Ejecución lineal.** Debe correr de arriba a abajo con *Restart & Run All*.
3. **Celdas idempotentes.** Re-ejecutar no debe romper el estado.
4. **Imports y configuración al principio.**
5. **Markdown abundante:** explica el qué y el porqué, no solo el cómo.

## Estructura recomendada

```txt
1. Título + objetivo + pregunta
2. Imports y configuración
3. Carga de datos (desde data/processed o desde extractores)
4. Exploración / análisis
5. Visualizaciones
6. Conclusiones y limitaciones
```

## Reproducibilidad

- Fija semillas: `np.random.seed(42)`.
- No dependas de variables de estado de celdas borradas.
- Limpia outputs antes de commitear (o usa `nbstripout` / `jupytext`).
- Versiona en paralelo con `jupytext` (`.py:percent`) si quieres diffs limpios en git.

## Lógica reutilizable

- Funciones que se usan en >1 notebook → muévelas a `src/`.
- Los notebooks importan de `src`, no copian/pegan código.

## Antipatrones a evitar

- Celdas ejecutadas fuera de orden.
- Rutas absolutas locales (`/Users/yo/...`). Usa rutas relativas.
- Credenciales en el notebook. Usa `.env` + `python-dotenv`.
- Notebooks de 2000 celdas sin estructura.
