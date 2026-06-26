"""Los 21 distritos oficiales de la ciudad de Madrid.

Códigos de distrito municipales (01-21) y un nivel de renta base usado SOLO para
generar datos sintéticos realistas (ver src/synthetic.py). Los nombres de los
distritos son los oficiales; las cifras de `base_renta_hogar` son orientativas y
NO son datos reales.
"""
from __future__ import annotations

# cod_distrito: (nombre, base_renta_hogar_sintetica_eur)
# El orden de renta es plausible (centro/noroeste más alto, sur más bajo) pero
# las cifras son sintéticas para la demo, no estadística oficial.
DISTRITOS: dict[str, tuple[str, int]] = {
    "01": ("Centro", 38000),
    "02": ("Arganzuela", 41000),
    "03": ("Retiro", 49000),
    "04": ("Salamanca", 53000),
    "05": ("Chamartín", 55000),
    "06": ("Tetuán", 37000),
    "07": ("Chamberí", 51000),
    "08": ("Fuencarral-El Pardo", 43000),
    "09": ("Moncloa-Aravaca", 50000),
    "10": ("Latina", 32000),
    "11": ("Carabanchel", 30000),
    "12": ("Usera", 28000),
    "13": ("Puente de Vallecas", 28000),
    "14": ("Moratalaz", 35000),
    "15": ("Ciudad Lineal", 36000),
    "16": ("Hortaleza", 45000),
    "17": ("Villaverde", 27000),
    "18": ("Villa de Vallecas", 34000),
    "19": ("Vicálvaro", 33000),
    "20": ("San Blas-Canillejas", 33000),
    "21": ("Barajas", 44000),
}

# Número de barrios por distrito (los 131 barrios oficiales de Madrid).
N_BARRIOS_POR_DISTRITO: dict[str, int] = {
    "01": 6, "02": 7, "03": 6, "04": 6, "05": 6, "06": 6, "07": 6,
    "08": 8, "09": 7, "10": 7, "11": 7, "12": 7, "13": 6, "14": 6,
    "15": 9, "16": 8, "17": 5, "18": 3, "19": 2, "20": 8, "21": 5,
}

TOTAL_BARRIOS = sum(N_BARRIOS_POR_DISTRITO.values())
assert TOTAL_BARRIOS == 131, f"Madrid tiene 131 barrios, definidos {TOTAL_BARRIOS}"
