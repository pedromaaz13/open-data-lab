# Streamlit

Apps de datos rápidas en Python puro. Ver `08_apps/streamlit/`.

## Cuándo

- Prototipos interactivos.
- Dashboards ligeros.
- Exploradores de datos.

## Ejemplo

```python
import streamlit as st, polars as pl
df = pl.read_parquet('data/processed/vivienda.parquet')
prov = st.selectbox('Provincia', df['provincia'].unique())
st.dataframe(df.filter(pl.col('provincia') == prov))
```

## Buenas prácticas

- Cachea cargas pesadas (`st.cache_data`).
- Despliega en Streamlit Community Cloud / Render.
- Separa lógica (`src/`) de la UI.
