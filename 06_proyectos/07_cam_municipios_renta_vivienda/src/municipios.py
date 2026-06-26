"""Municipios principales de la Comunidad de Madrid (los de mayor población).

Código INE de municipio (5 dígitos, provincia 28) y nivel de renta base SOLO para
datos sintéticos realistas. Nombres oficiales; cifras de renta NO son reales.
Para el análisis real, el INE Atlas cubre los 179 municipios por código.
"""
from __future__ import annotations

# cod_ine: (nombre, base_renta_hogar_sintetica_eur)
MUNICIPIOS: dict[str, tuple[str, int]] = {
    "28079": ("Madrid", 38000),
    "28092": ("Móstoles", 32000),
    "28005": ("Alcalá de Henares", 31000),
    "28058": ("Fuenlabrada", 30000),
    "28074": ("Leganés", 33000),
    "28065": ("Getafe", 34000),
    "28007": ("Alcorcón", 34000),
    "28148": ("Torrejón de Ardoz", 31000),
    "28106": ("Parla", 27000),
    "28006": ("Alcobendas", 48000),
    "28127": ("Las Rozas de Madrid", 60000),
    "28134": ("San Sebastián de los Reyes", 42000),
    "28115": ("Pozuelo de Alarcón", 80000),
    "28049": ("Coslada", 31000),
    "28123": ("Rivas-Vaciamadrid", 41000),
    "28161": ("Valdemoro", 33000),
    "28080": ("Majadahonda", 58000),
    "28047": ("Collado Villalba", 33000),
    "28013": ("Aranjuez", 30000),
    "28014": ("Arganda del Rey", 31000),
    "28022": ("Boadilla del Monte", 62000),
    "28113": ("Pinto", 34000),
    "28045": ("Colmenar Viejo", 38000),
    "28900": ("Tres Cantos", 55000),
    "28133": ("San Fernando de Henares", 32000),
    "28061": ("Galapagar", 45000),
    "28171": ("Villaviciosa de Odón", 52000),
    "28085": ("Mejorada del Campo", 30000),
    "28092b": ("Navalcarnero", 32000),
    "28041": ("Ciempozuelos", 29000),
}
