"""Transformación: a partir de los datos base de barrios calcula los indicadores.

Funciona igual con datos sintéticos o reales, siempre que el DataFrame de entrada
tenga las columnas base:
  renta_hogar, alquiler_eur_m2_mes, precio_compra_eur_m2
"""
from __future__ import annotations

import pandas as pd

import config
import indicators as ind


COLUMNAS_BASE = {
    "cod_barrio",
    "barrio",
    "renta_hogar",
    "alquiler_eur_m2_mes",
    "precio_compra_eur_m2",
}


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Añade columnas de esfuerzo de alquiler y de compra + clasificación.

    Lanza ValueError si faltan columnas base (validación temprana, fail-fast).
    """
    faltan = COLUMNAS_BASE - set(df.columns)
    if faltan:
        raise ValueError(f"Faltan columnas base para los indicadores: {sorted(faltan)}")

    out = df.copy()
    out["esfuerzo_alquiler_pct"] = ind.esfuerzo_alquiler_pct(
        out["alquiler_eur_m2_mes"], out["renta_hogar"], config.SUPERFICIE_ALQUILER_M2
    ).round(1)
    out["esfuerzo_compra_anios"] = ind.esfuerzo_compra_anios(
        out["precio_compra_eur_m2"], out["renta_hogar"], config.SUPERFICIE_COMPRA_M2
    ).round(1)
    out["clasificacion_alquiler"] = out["esfuerzo_alquiler_pct"].apply(
        lambda p: ind.clasifica_esfuerzo_alquiler(
            p, config.UMBRAL_ALQUILER_HOLGADO, config.UMBRAL_ALQUILER_APURADO
        )
    )
    return out


def resumen_por_distrito(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega los indicadores a nivel de distrito (media de barrios)."""
    cols = [
        "renta_hogar",
        "alquiler_eur_m2_mes",
        "precio_compra_eur_m2",
        "esfuerzo_alquiler_pct",
        "esfuerzo_compra_anios",
    ]
    g = (
        df.groupby(["cod_distrito", "distrito"], as_index=False)[cols]
        .mean(numeric_only=True)
        .round(1)
        .sort_values("esfuerzo_alquiler_pct", ascending=False)
    )
    return g
