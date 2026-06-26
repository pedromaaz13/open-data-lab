"""Generación de datos sintéticos realistas para los 131 barrios de Madrid.

Sirve para desarrollar y validar TODO el pipeline (transformación, indicadores,
notebook, mapas) sin depender de la descarga real. Los datos NO son oficiales:
son plausibles y deterministas (semilla fija) para reproducibilidad.

Para datos reales, ver src/extract.py (se ejecuta en tu máquina, con red).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from distritos import DISTRITOS, N_BARRIOS_POR_DISTRITO


def generar_barrios(seed: int = 42) -> pd.DataFrame:
    """Devuelve un DataFrame con una fila por barrio y columnas base.

    Columnas:
      cod_distrito, distrito, cod_barrio, barrio,
      renta_hogar (€/año), renta_persona (€/año),
      alquiler_eur_m2_mes (€/m²/mes), precio_compra_eur_m2 (€/m²)

    El precio de la vivienda crece con la renta pero de forma *comprimida*: en los
    barrios de menor renta los precios no bajan tan rápido como los ingresos, lo
    que reproduce el fenómeno real de que el esfuerzo de vivienda puede ser alto
    también en la periferia.
    """
    rng = np.random.default_rng(seed)
    filas = []
    for cod_d, (nombre_d, base_renta) in DISTRITOS.items():
        for b in range(1, N_BARRIOS_POR_DISTRITO[cod_d] + 1):
            cod_barrio = f"{cod_d}{b:02d}"
            # Renta del barrio: base del distrito ± ruido (±15%).
            renta_hogar = base_renta * (1 + rng.normal(0, 0.15))
            renta_hogar = float(np.clip(renta_hogar, 18000, 90000))
            # Renta por persona ~ renta hogar / tamaño medio del hogar (~2.4).
            renta_persona = renta_hogar / rng.uniform(2.2, 2.7)

            # Alquiler €/m²/mes: crece con la renta pero de forma suave, de modo
            # que el esfuerzo (alquiler/renta) sea mayor en los barrios de menor
            # renta. Rango ~12-19 €/m², realista para Madrid.
            alquiler = 8.0 + renta_hogar / 5500.0 + rng.normal(0, 0.6)
            alquiler = float(np.clip(alquiler, 10.0, 21.0))

            # Compra €/m²: base + componente lineal en renta + ruido.
            compra = 1200 + renta_hogar * 0.09 + rng.normal(0, 250)
            compra = float(np.clip(compra, 1800, 8000))

            filas.append(
                {
                    "cod_distrito": cod_d,
                    "distrito": nombre_d,
                    "cod_barrio": cod_barrio,
                    "barrio": f"{nombre_d} · Barrio {b:02d}",
                    "renta_hogar": round(renta_hogar, 0),
                    "renta_persona": round(renta_persona, 0),
                    "alquiler_eur_m2_mes": round(alquiler, 2),
                    "precio_compra_eur_m2": round(compra, 0),
                }
            )
    df = pd.DataFrame(filas)
    return df
