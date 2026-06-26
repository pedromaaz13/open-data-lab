"""Transformación: añade indicadores de esfuerzo por municipio."""
from __future__ import annotations

import pandas as pd

import config
import indicators as ind

COLUMNAS_BASE = {"cod_ine", "municipio", "renta_hogar", "alquiler_eur_m2_mes", "precio_compra_eur_m2"}


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    faltan = COLUMNAS_BASE - set(df.columns)
    if faltan:
        raise ValueError(f"Faltan columnas base: {sorted(faltan)}")
    out = df.copy()
    out["esfuerzo_alquiler_pct"] = ind.esfuerzo_alquiler_pct(
        out["alquiler_eur_m2_mes"], out["renta_hogar"], config.SUPERFICIE_ALQUILER_M2).round(1)
    out["esfuerzo_compra_anios"] = ind.esfuerzo_compra_anios(
        out["precio_compra_eur_m2"], out["renta_hogar"], config.SUPERFICIE_COMPRA_M2).round(1)
    out["clasificacion_alquiler"] = out["esfuerzo_alquiler_pct"].apply(
        lambda p: ind.clasifica_esfuerzo_alquiler(p, config.UMBRAL_ALQUILER_HOLGADO, config.UMBRAL_ALQUILER_APURADO))
    return out
