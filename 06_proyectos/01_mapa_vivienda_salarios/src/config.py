"""Configuración y parámetros del proyecto Madrid · renta vs vivienda.

Filosofía del laboratorio: parámetros explícitos y documentados, nada de
constantes mágicas escondidas en el código.
"""
from __future__ import annotations

from pathlib import Path

# --- Rutas (relativas a la raíz del proyecto, no absolutas) ---
PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_RAW = PROJECT_DIR / "data" / "raw"
DATA_INTERIM = PROJECT_DIR / "data" / "interim"
DATA_PROCESSED = PROJECT_DIR / "data" / "processed"
OUTPUTS = PROJECT_DIR / "outputs"

# --- Parámetros del análisis ---
# Superficie de la vivienda "tipo" para cada indicador (m²).
SUPERFICIE_ALQUILER_M2 = 70   # piso medio de alquiler
SUPERFICIE_COMPRA_M2 = 90     # vivienda media de compra

# Umbrales de esfuerzo de alquiler (% de la renta del hogar que se va en vivienda).
# Convención habitual: 30% es el límite de asequibilidad; >40% es sobreesfuerzo.
UMBRAL_ALQUILER_HOLGADO = 30.0
UMBRAL_ALQUILER_APURADO = 40.0

# Identificadores oficiales de Madrid (municipio).
COD_MUNICIPIO_MADRID = "28079"  # código INE del municipio de Madrid

# --- Fuentes oficiales (documentadas para el extractor real) ---
# OJO: los IDs de tabla y URLs exactas deben verificarse al ejecutar (la red de
# este entorno está restringida). Ver src/extract.py y el README del proyecto.
FUENTES = {
    "renta": {
        "organismo": "INE",
        "dataset": "Atlas de distribución de renta de los hogares (ADRH)",
        "nivel": "distrito / barrio / sección censal",
        "url": "https://www.ine.es/experimental/atlas/experimental_atlas.htm",
    },
    "alquiler": {
        "organismo": "Mº Vivienda / Ayto Madrid",
        "dataset": "Sistema estatal de índices de alquiler / precios de alquiler",
        "nivel": "distrito / barrio",
        "url": "https://www.mivau.gob.es",
    },
    "compra": {
        "organismo": "Ayto Madrid / Mº Vivienda",
        "dataset": "Precio de vivienda (€/m²)",
        "nivel": "distrito / barrio",
        "url": "https://datos.madrid.es",
    },
    "geometria": {
        "organismo": "Ayuntamiento de Madrid (Geoportal)",
        "dataset": "Distritos (límites administrativos) — Shapefile",
        "nivel": "distrito",
        "url": "https://geoportal.madrid.es/fsdescargas/IDEAM_WBGEOPORTAL/LIMITES_ADMINISTRATIVOS/Distritos/Distritos.zip",
    },
}
