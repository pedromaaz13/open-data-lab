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


def unir_distritos_madrid(geo, df, col_codigo_geo: str = "COD_DIS_TX") -> gpd.GeoDataFrame:
    """Une la geometría de los distritos de Madrid (Geoportal Ayto.) con un DataFrame.

    - `geo`: ruta al shapefile/zip de distritos, o un GeoDataFrame ya cargado.
    - `df`: tabla por distrito; debe tener `cod_distrito` (código INE de 7 dígitos,
      p. ej. '2807901'). La unión se hace por el número de distrito ('01'..'21').
    - `col_codigo_geo`: columna de código de distrito en la geometría (en el shapefile
      del Ayto. es 'COD_DIS_TX', con valores '01'..'21').

    Devuelve un GeoDataFrame con geometría + indicadores, listo para mapear.
    """
    g = gpd.read_file(geo) if not isinstance(geo, gpd.GeoDataFrame) else geo.copy()
    g["num_distrito"] = g[col_codigo_geo].astype(str).str.zfill(2)

    d = df.copy()
    d["num_distrito"] = d["cod_distrito"].astype(str).str[5:7]

    gdf = g.merge(d, on="num_distrito", how="left")
    return gpd.GeoDataFrame(gdf, geometry="geometry", crs=g.crs)


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


# Gradiente de color (estilo viridis) para Kepler: oscuro = bajo, claro = alto.
_COLOR_RANGE_VIRIDIS = {
    "name": "Viridis-6",
    "type": "sequential",
    "category": "Uber",
    "colors": ["#440154", "#414487", "#2a788e", "#22a884", "#7ad151", "#fde725"],
}


def _kepler_config(data_id: str, color_field: str, color_scale: str = "quantile") -> dict:
    """Config de Kepler.gl para colorear los polígonos por `color_field` (gradiente)."""
    return {
        "version": "v1",
        "config": {
            "visState": {
                "layers": [
                    {
                        "id": "capa_color",
                        "type": "geojson",
                        "config": {
                            "dataId": data_id,
                            "label": color_field,
                            "columns": {"geojson": "geometry"},
                            "isVisible": True,
                            "visConfig": {
                                "opacity": 0.8,
                                "stroked": True,
                                "filled": True,
                                "thickness": 0.5,
                                "colorRange": _COLOR_RANGE_VIRIDIS,
                            },
                            "colorField": {"name": color_field, "type": "real"},
                            "colorScale": color_scale,
                        },
                    }
                ]
            }
        },
    }


def mapa_folium(gdf: gpd.GeoDataFrame, columna: str,
                nombre_col: str = "nombre_distrito",
                guardar_html: str | Path | None = None):
    """Mapa interactivo con Folium (Leaflet): coroplético con **leyenda** y tooltip.

    Más sencillo y fiable que Kepler para colorear por un valor: siempre sale el
    gradiente y la barra de leyenda. Reproyecta a lat/lon (EPSG:4326).
    """
    import branca.colormap as bcm
    import folium

    g = gdf.to_crs(4326) if (gdf.crs is not None and gdf.crs.to_epsg() != 4326) else gdf.copy()
    vals = g[columna].dropna()
    cmap = bcm.linear.viridis.scale(float(vals.min()), float(vals.max()))
    cmap.caption = columna

    minx, miny, maxx, maxy = g.total_bounds
    m = folium.Map(location=[(miny + maxy) / 2, (minx + maxx) / 2],
                   zoom_start=11, tiles="cartodbpositron")

    def _style(feat):
        v = feat["properties"].get(columna)
        return {"fillColor": cmap(v) if v is not None else "#cccccc",
                "color": "white", "weight": 1, "fillOpacity": 0.85}

    folium.GeoJson(
        g, style_function=_style,
        tooltip=folium.GeoJsonTooltip(fields=[nombre_col, columna]),
    ).add_to(m)
    cmap.add_to(m)  # leyenda (barra de color)

    if guardar_html:
        m.save(str(guardar_html))
    return m


def mapa_kepler(gdf: gpd.GeoDataFrame, nombre: str = "datos",
                color_field: str | None = None, color_scale: str = "quantile",
                guardar_html: str | Path | None = None):
    """Mapa interactivo con Kepler.gl, coloreado por `color_field` si se indica.

    - `color_field`: columna por la que colorear (p. ej. 'Renta neta media por hogar').
      Si es None, Kepler pinta todo del mismo color (lo coloreas tú en el panel).
    - `color_scale`: 'quantile' (por defecto), 'quantize' u 'ordinal'.

    Requiere `keplergl` y geometría real (la reproyecta a lat/lon EPSG:4326).
    """
    try:
        from keplergl import KeplerGl
    except ImportError as e:  # keplergl no instalado
        raise ImportError(
            "Falta keplergl. Instala con: pip install keplergl"
        ) from e

    if gdf.crs is not None and gdf.crs.to_epsg() != 4326:
        gdf = gdf.to_crs(4326)

    if color_field:
        config = _kepler_config(nombre, color_field, color_scale)
        m = KeplerGl(height=600, data={nombre: gdf}, config=config)
    else:
        m = KeplerGl(height=600)
        m.add_data(data=gdf, name=nombre)

    if guardar_html:
        m.save_to_html(file_name=str(guardar_html))
    return m
