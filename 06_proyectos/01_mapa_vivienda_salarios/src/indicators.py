"""Indicadores de esfuerzo de vivienda.

Funciones puras (operan sobre números o sobre columnas de pandas indistintamente,
porque solo usan aritmética). Esto permite testearlas sin dependencias pesadas y
reutilizarlas tanto sobre escalares como sobre un DataFrame.
"""
from __future__ import annotations


def esfuerzo_alquiler_pct(
    alquiler_eur_m2_mes,
    renta_hogar_anual,
    superficie_m2: float = 70.0,
):
    """% de la renta anual del hogar que se va en alquiler de una vivienda tipo.

    alquiler_anual = €/m²/mes * m² * 12
    esfuerzo (%)   = alquiler_anual / renta_hogar_anual * 100

    >>> round(esfuerzo_alquiler_pct(15, 30000, 70), 1)
    42.0
    """
    alquiler_anual = alquiler_eur_m2_mes * superficie_m2 * 12.0
    return alquiler_anual / renta_hogar_anual * 100.0


def esfuerzo_compra_anios(
    precio_compra_eur_m2,
    renta_hogar_anual,
    superficie_m2: float = 90.0,
):
    """Años de renta íntegra del hogar para comprar una vivienda tipo.

    precio_total = €/m² * m²
    años         = precio_total / renta_hogar_anual

    >>> round(esfuerzo_compra_anios(4000, 30000, 90), 1)
    12.0
    """
    precio_total = precio_compra_eur_m2 * superficie_m2
    return precio_total / renta_hogar_anual


def clasifica_esfuerzo_alquiler(
    pct: float,
    umbral_holgado: float = 30.0,
    umbral_apurado: float = 40.0,
) -> str:
    """Etiqueta cualitativa del esfuerzo de alquiler.

    - < umbral_holgado        -> 'holgado'
    - [holgado, apurado)      -> 'ajustado'
    - >= umbral_apurado       -> 'apurado'

    >>> clasifica_esfuerzo_alquiler(25)
    'holgado'
    >>> clasifica_esfuerzo_alquiler(35)
    'ajustado'
    >>> clasifica_esfuerzo_alquiler(45)
    'apurado'
    """
    if pct < umbral_holgado:
        return "holgado"
    if pct < umbral_apurado:
        return "ajustado"
    return "apurado"
