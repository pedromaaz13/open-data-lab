"""Descarga automática de los datos REALES del Atlas de Renta del INE (ADRH 2023).

Ejecuta esto en tu máquina (con internet):

    python src/extract.py

Descarga las tablas del INE a data/raw/ con nombres limpios. Son enlaces directos
de descarga del INE (jaxiT3). Cada tabla trae TODA la provincia de Madrid; el
filtrado a los distritos de la ciudad se hace luego en src/load_ine.py.
"""
from __future__ import annotations

from pathlib import Path

import httpx

import config

# Fichero destino en data/raw/ -> URL directa de descarga.
URLS: dict[str, str] = {
    # Renta y sociedad (INE Atlas de Renta, ADRH 2023 — tablas jaxiT3)
    "ine_renta_media_mediana.csv": "https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/31097.csv?nocab=1",
    "ine_fuente_ingresos.csv": "https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/31098.csv?nocab=1",
    "ine_gini_p80p20.csv": "https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/37727.csv?nocab=1",
    "ine_demografia.csv": "https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/31105.csv?nocab=1",
    # Geometría de los distritos (Geoportal del Ayto. de Madrid — Shapefile en .zip)
    "distritos_madrid.zip": "https://geoportal.madrid.es/fsdescargas/IDEAM_WBGEOPORTAL/LIMITES_ADMINISTRATIVOS/Distritos/Distritos.zip",
}


def descargar_todo(timeout: int = 90) -> list[Path]:
    """Descarga todas las tablas a data/raw/. Devuelve las rutas guardadas."""
    config.DATA_RAW.mkdir(parents=True, exist_ok=True)
    guardados = []
    for nombre, url in URLS.items():
        destino = config.DATA_RAW / nombre
        print(f"Descargando {nombre} ...", end=" ", flush=True)
        resp = httpx.get(url, timeout=timeout, follow_redirects=True,
                         headers={"User-Agent": "open-data-lab"})
        resp.raise_for_status()
        destino.write_bytes(resp.content)
        print(f"OK ({len(resp.content):,} bytes)")
        guardados.append(destino)
    return guardados


if __name__ == "__main__":
    rutas = descargar_todo()
    print(f"\nListo: {len(rutas)} ficheros en {config.DATA_RAW}")
