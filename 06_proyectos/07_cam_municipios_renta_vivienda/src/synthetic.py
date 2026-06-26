"""Datos sintéticos realistas por municipio de la CAM (deterministas, semilla fija)."""
from __future__ import annotations

import numpy as np
import pandas as pd

from municipios import MUNICIPIOS


def generar_municipios(seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    filas = []
    for cod, (nombre, base_renta) in MUNICIPIOS.items():
        renta_hogar = float(np.clip(base_renta * (1 + rng.normal(0, 0.10)), 22000, 95000))
        renta_persona = renta_hogar / rng.uniform(2.3, 2.8)
        # Alquiler EUR/m2/mes: crece suave con la renta (mayor esfuerzo donde menos renta).
        alquiler = float(np.clip(7.0 + renta_hogar / 6000.0 + rng.normal(0, 0.5), 8.0, 20.0))
        # Compra EUR/m2: mejor cobertura oficial por municipio.
        compra = float(np.clip(900 + renta_hogar * 0.085 + rng.normal(0, 250), 1300, 7000))
        filas.append({
            "cod_ine": cod, "municipio": nombre,
            "renta_hogar": round(renta_hogar, 0), "renta_persona": round(renta_persona, 0),
            "alquiler_eur_m2_mes": round(alquiler, 2), "precio_compra_eur_m2": round(compra, 0),
        })
    return pd.DataFrame(filas)
