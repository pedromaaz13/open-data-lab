"""Tests del pipeline (datos sintéticos + transformación).

Requieren numpy/pandas; si no están instalados, se omiten con skip (para no romper
un CI mínimo). En el CI del laboratorio se instalan, así que sí se ejecutan.
"""
import pytest

pytest.importorskip("numpy")
pytest.importorskip("pandas")

from synthetic import generar_barrios  # noqa: E402
from transform import add_indicators, resumen_por_distrito  # noqa: E402


def test_genera_131_barrios():
    df = generar_barrios()
    assert len(df) == 131
    assert df["cod_barrio"].is_unique


def test_synthetic_es_determinista():
    a = generar_barrios(seed=42)
    b = generar_barrios(seed=42)
    assert a.equals(b)


def test_add_indicators_crea_columnas_y_rangos():
    df = add_indicators(generar_barrios())
    for col in ["esfuerzo_alquiler_pct", "esfuerzo_compra_anios", "clasificacion_alquiler"]:
        assert col in df.columns
    # Esfuerzos siempre positivos y finitos.
    assert (df["esfuerzo_alquiler_pct"] > 0).all()
    assert (df["esfuerzo_compra_anios"] > 0).all()
    # Clasificación dentro del dominio esperado.
    assert set(df["clasificacion_alquiler"]).issubset({"holgado", "ajustado", "apurado"})


def test_add_indicators_falla_si_faltan_columnas():
    import pandas as pd

    with pytest.raises(ValueError):
        add_indicators(pd.DataFrame({"barrio": ["x"]}))


def test_resumen_por_distrito_tiene_21_filas():
    df = add_indicators(generar_barrios())
    resumen = resumen_por_distrito(df)
    assert len(resumen) == 21
