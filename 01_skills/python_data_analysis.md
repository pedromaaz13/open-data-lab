# Python para análisis de datos

## Para qué sirve

Base del laboratorio: manipular, analizar y automatizar datos con Python, el lenguaje estándar del ecosistema data.

## Conceptos principales

- Estructuras de datos (listas, dicts, sets) y comprensiones.
- Entornos virtuales y gestión de dependencias.
- Vectorización vs bucles.
- Funciones puras y código reutilizable en `src/`.
- Tipado y `pydantic` para validar entradas.

## Librerías útiles

- `pandas`, `polars`, `numpy` para datos.
- `requests`/`httpx` para APIs.
- `python-dotenv` para configuración.
- `pathlib` para rutas portables.

## Ejemplos de uso

```python
import polars as pl

df = pl.read_parquet('data/processed/vivienda.parquet')
resumen = (
    df.group_by('provincia')
      .agg(pl.col('precio_m2').mean().alias('precio_medio'))
      .sort('precio_medio', descending=True)
)
print(resumen.head())
```

## Errores comunes

- Usar rutas absolutas locales.
- Mutar DataFrames en sitios inesperados.
- Bucles donde cabría vectorización.
- No fijar versiones de dependencias.

## Mini proyecto recomendado

Construir un script que descargue un CSV del INE, lo limpie y guarde un Parquet reproducible.

## Recursos para profundizar

- *Python for Data Analysis* (Wes McKinney).
- Documentación de Polars y Pandas.
- Real Python (tutoriales).
