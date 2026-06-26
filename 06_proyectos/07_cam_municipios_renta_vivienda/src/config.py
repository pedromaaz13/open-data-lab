"""Configuración del proyecto CAM · municipios."""
from __future__ import annotations
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_RAW = PROJECT_DIR / "data" / "raw"
DATA_PROCESSED = PROJECT_DIR / "data" / "processed"
OUTPUTS = PROJECT_DIR / "outputs"

SUPERFICIE_ALQUILER_M2 = 80   # vivienda media de alquiler (municipio)
SUPERFICIE_COMPRA_M2 = 100    # vivienda media de compra (municipio)
UMBRAL_ALQUILER_HOLGADO = 30.0
UMBRAL_ALQUILER_APURADO = 40.0

FUENTES = {
    "renta": {"organismo": "INE", "dataset": "Atlas de Renta (ADRH) por municipio",
              "url": "https://www.ine.es/experimental/atlas/experimental_atlas.htm"},
    "compra": {"organismo": "Mo Vivienda", "dataset": "Precio de vivienda EUR/m2 por municipio",
               "url": "https://www.mivau.gob.es"},
    "alquiler": {"organismo": "Mo Vivienda", "dataset": "Indice de alquiler por municipio",
                 "url": "https://www.mivau.gob.es/vivienda/alquiler/indice-alquiler"},
    "geometria": {"organismo": "CNIG/IGN", "dataset": "Limites municipales",
                  "url": "https://centrodedescargas.cnig.es"},
}
