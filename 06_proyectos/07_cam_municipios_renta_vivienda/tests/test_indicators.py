"""Tests de indicadores y pipeline (CAM municipios)."""
import pytest
import indicators as ind


def test_alquiler_valor_conocido():
    # 12 EUR/m2/mes * 80 m2 * 12 = 11520; sobre 30000 = 38.4 %.
    assert ind.esfuerzo_alquiler_pct(12, 30000, 80) == pytest.approx(38.4)


def test_compra_valor_conocido():
    # 3000 EUR/m2 * 100 m2 = 300000; sobre 30000/año = 10 años.
    assert ind.esfuerzo_compra_anios(3000, 30000, 100) == 10.0


def test_clasificacion():
    assert ind.clasifica_esfuerzo_alquiler(25) == "holgado"
    assert ind.clasifica_esfuerzo_alquiler(35) == "ajustado"
    assert ind.clasifica_esfuerzo_alquiler(45) == "apurado"


def test_pipeline_sintetico():
    pytest.importorskip("numpy"); pytest.importorskip("pandas")
    from synthetic import generar_municipios
    from transform import add_indicators
    df = add_indicators(generar_municipios())
    assert len(df) >= 25
    assert (df["esfuerzo_alquiler_pct"] > 0).all()
    assert set(df["clasificacion_alquiler"]).issubset({"holgado", "ajustado", "apurado"})
