# Stack local

Capa para análisis, notebooks y prototipos. Todo corre en tu máquina, sin coste y
con reproducibilidad total.

## Componentes

| Componente | Herramienta |
|---|---|
| Lenguaje | Python 3.11+ |
| Entorno | uv / Poetry / venv |
| Notebooks | JupyterLab |
| Procesamiento | Pandas, Polars, NumPy |
| SQL local | DuckDB |
| Formato | Parquet / GeoParquet |
| Geoespacial | GeoPandas, Shapely, rasterio, rioxarray |
| Visualización | Matplotlib, Plotly, Altair, Folium, Kepler.gl |
| Calidad | pandera, pytest |
| Tooling | ruff, black, sqlfluff, pre-commit |
| Publicación | Quarto |

## Cuándo basta el stack local

- Datasets que caben en una máquina (hasta decenas de millones de filas con DuckDB/Polars).
- Análisis exploratorio, prototipos, notebooks.
- Proyectos de portfolio reproducibles.

## Ventajas

- Coste cero.
- Reproducibilidad máxima.
- Sin dependencias de servicios externos.

## Cómo empezar

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```
