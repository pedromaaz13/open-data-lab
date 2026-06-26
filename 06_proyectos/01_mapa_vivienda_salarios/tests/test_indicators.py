"""Tests de los indicadores de esfuerzo de vivienda.

Funciones puras: se testean con valores conocidos a mano, sin dependencias pesadas.
Estos tests son los que dan valor real al check de CI en cada push.
"""
import indicators as ind


def test_esfuerzo_alquiler_valor_conocido():
    # 15 €/m²/mes * 70 m² * 12 = 12.600 €/año; sobre 30.000 € = 42 %.
    assert ind.esfuerzo_alquiler_pct(15, 30000, 70) == 42.0


def test_esfuerzo_alquiler_sube_si_baja_la_renta():
    alto = ind.esfuerzo_alquiler_pct(15, 20000, 70)
    bajo = ind.esfuerzo_alquiler_pct(15, 40000, 70)
    assert alto > bajo


def test_esfuerzo_compra_valor_conocido():
    # 4000 €/m² * 90 m² = 360.000 €; sobre 30.000 €/año = 12 años.
    assert ind.esfuerzo_compra_anios(4000, 30000, 90) == 12.0


def test_esfuerzo_compra_escala_con_precio():
    assert ind.esfuerzo_compra_anios(6000, 30000, 90) > ind.esfuerzo_compra_anios(3000, 30000, 90)


def test_clasificacion_umbrales():
    assert ind.clasifica_esfuerzo_alquiler(25) == "holgado"
    assert ind.clasifica_esfuerzo_alquiler(30) == "ajustado"   # límite inferior incluido
    assert ind.clasifica_esfuerzo_alquiler(39.9) == "ajustado"
    assert ind.clasifica_esfuerzo_alquiler(40) == "apurado"    # límite superior incluido
    assert ind.clasifica_esfuerzo_alquiler(55) == "apurado"
