"""Test de la unión geometría de distritos ↔ datos por distrito.

Requiere geopandas/shapely; si no están (p. ej. en un CI mínimo), se omite.
"""
import pytest

pytest.importorskip("geopandas")
pytest.importorskip("shapely")

import geopandas as gpd  # noqa: E402
import pandas as pd  # noqa: E402
from shapely.geometry import box  # noqa: E402

import maps  # noqa: E402


def _geo_mock() -> gpd.GeoDataFrame:
    # imita el shapefile del Ayto.: columna COD_DIS_TX con '01'..'21'
    filas = [{"COD_DIS_TX": f"{i:02d}", "geometry": box(i, 0, i + 1, 1)} for i in range(1, 22)]
    return gpd.GeoDataFrame(filas, geometry="geometry", crs="EPSG:25830")


def test_unir_distritos_madrid_casa_los_21():
    geo = _geo_mock()
    df = pd.DataFrame(
        {"cod_distrito": [f"28079{i:02d}" for i in range(1, 22)], "valor": list(range(21))}
    )
    gdf = maps.unir_distritos_madrid(geo, df)
    assert len(gdf) == 21
    assert gdf["valor"].notna().sum() == 21          # los 21 distritos quedan unidos
    assert gdf.crs is not None                        # conserva el CRS
    assert "geometry" in gdf.columns
