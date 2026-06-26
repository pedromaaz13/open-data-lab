"""Mapas del proyecto: coroplético estático (GeoPandas) e interactivo (Kepler.gl).

Dos escenarios:
  - DEMO (datos sintéticos): no tenemos los polígonos reales de los barrios, así que
    generamos una geometría ESQUEMÁTICA (una rejilla) para poder ver el mapa
    coloreado funcionando. NO es la forma real de Madrid.
  - REAL: cargas el GeoJSON oficial de barrios del Ayto. de Madrid y lo unes por
    `cod_barrio`. Entonces el mapa sale con la forma real y Kepler.gl funciona.
"""
from __future__ import annotations

from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import box


def geometria_esquematica(df, cols: int = 12) -> gpd.GeoDataFrame:
    """Crea una geometría de rejilla (un cuadrado por barrio) para la demo.

    Ordena por `cod_barrio` y coloca los barrios en una cuadrícula. Permite ver el
    coroplético con datos sintéticos. No tiene sentido geográfico real.
    """
    d = df.sort_values("cod_barrio").reset_index(drop=True)
    geoms = []
    for i in range(len(d)):
        fila, col = divmod(i, cols)
        geoms.append(box(col, -fila, col + 0.92, -fila + 0.92))
    return gpd.GeoDataFrame(d.copy(), geometry=geoms, crs=None)


def cargar_geometria_real(geojson_path: str | Path, df, on: str = "cod_barrio") -> gpd.GeoDataFrame:
    """Carga el GeoJSON real de barrios y le une los indicadores por código.

    El GeoJSON del Ayto. de Madrid trae el código de barrio en alguna columna
    (p. ej. 'COD_BAR' / 'codbarrio'); renómbrala a `cod_barrio` antes de unir.
    """
    barrios = gpd.read_file(geojson_path)
    if on not in barrios.columns:
        raise ValueError(
            f"El GeoJSON no tiene la columna '{on}'. Columnas: {list(barrios.columns)}. "
            "Renombra la columna de código de barrio a 'cod_barrio'."
        )
    return barrios.merge(df, on=on)


def mapa_choropleth(gdf: gpd.GeoDataFrame, columna: str = "esfuerzo_alquiler_pct",
                    titulo: str | None = None, cmap: str = "RdYlGn_r",
                    guardar: str | Path | None = None):
    """Dibuja un mapa coroplético estático con matplotlib. Devuelve (fig, ax)."""
    fig, ax = plt.subplots(figsize=(9, 9))
    gdf.plot(column=columna, cmap=cmap, legend=True, edgecolor="white", linewidth=0.4, ax=ax)
    ax.set_title(titulo or f"Madrid · {columna}")
    ax.set_axis_off()
    fig.tight_layout()
    if guardar:
        fig.savefig(guardar, dpi=110, bbox_inches="tight")
    return fig, ax


def mapa_kepler(gdf: gpd.GeoDataFrame, nombre: str = "barrios",
                guardar_html: str | Path | None = None):
    """Construye un mapa interactivo con Kepler.gl. Requiere `keplergl` y geometría real.

    Kepler necesita coordenadas geográficas (lat/lon, EPSG:4326), así que solo tiene
    sentido con la geometría REAL de los barrios, no con la rejilla esquemática.
    """
    try:
        from keplergl import KeplerGl
    except ImportError as e:  # keplergl no instalado
        raise ImportError(
            "Falta keplergl. Instala con: pip install keplergl  (y usa geometría real)."
        ) from e

    if gdf.crs is not None and gdf.crs.to_epsg() != 4326:
        gdf = gdf.to_crs(4326)

    m = KeplerGl(height=600)
    m.add_data(data=gdf, name=nombre)
    if guardar_html:
        m.save_to_html(file_name=str(guardar_html))
    return m
