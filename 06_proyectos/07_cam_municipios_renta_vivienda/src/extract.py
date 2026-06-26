"""Extracción de datos REALES por municipio (ejecutar en tu máquina, con red).

Ver la guía del proyecto 01 (docs/COMO_DESCARGAR_DATOS_REALES.md): el procedimiento
es el mismo, pero a nivel de MUNICIPIO en vez de barrio.

  - Renta: INE Atlas de Renta, indicador por municipio (179 municipios de la CAM).
  - Compra: Mo Vivienda, precio EUR/m2 por municipio (buena cobertura).
  - Alquiler: Mo Vivienda, indice de alquiler por municipio.
  - Geometria: CNIG/IGN, limites municipales (filtrar provincia 28).

TODO: verificar los IDs de tabla del INE y las URLs de descarga al ejecutar.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

import config


def _guardar_raw(contenido: bytes, nombre: str) -> Path:
    config.DATA_RAW.mkdir(parents=True, exist_ok=True)
    destino = config.DATA_RAW / f"{date.today().isoformat()}_{nombre}"
    destino.write_bytes(contenido)
    return destino


def descargar_renta_ine_municipios(timeout: int = 60) -> Path:
    import httpx
    url = "https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/PLACEHOLDER.csv"  # TODO
    r = httpx.get(url, timeout=timeout, headers={"User-Agent": "open-data-lab"})
    r.raise_for_status()
    return _guardar_raw(r.content, "ine_atlas_renta_cam_municipios.csv")


def descargar_precio_vivienda_municipios(timeout: int = 60) -> Path:
    import httpx
    url = "https://www.mivau.gob.es/PLACEHOLDER.csv"  # TODO
    r = httpx.get(url, timeout=timeout, headers={"User-Agent": "open-data-lab"})
    r.raise_for_status()
    return _guardar_raw(r.content, "mivau_precio_vivienda_municipios.csv")


if __name__ == "__main__":
    for k, v in config.FUENTES.items():
        print(f"{k}: {v['organismo']} — {v['dataset']} ({v['url']})")
