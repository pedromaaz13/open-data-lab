"""Indicadores de esfuerzo de vivienda (funciones puras). Ver proyecto 01."""
from __future__ import annotations


def esfuerzo_alquiler_pct(alquiler_eur_m2_mes, renta_hogar_anual, superficie_m2: float = 80.0):
    """% de la renta anual del hogar que se va en alquiler de una vivienda tipo."""
    return alquiler_eur_m2_mes * superficie_m2 * 12.0 / renta_hogar_anual * 100.0


def esfuerzo_compra_anios(precio_compra_eur_m2, renta_hogar_anual, superficie_m2: float = 100.0):
    """Años de renta íntegra del hogar para comprar una vivienda tipo."""
    return precio_compra_eur_m2 * superficie_m2 / renta_hogar_anual


def clasifica_esfuerzo_alquiler(pct: float, umbral_holgado: float = 30.0, umbral_apurado: float = 40.0) -> str:
    if pct < umbral_holgado:
        return "holgado"
    if pct < umbral_apurado:
        return "ajustado"
    return "apurado"
