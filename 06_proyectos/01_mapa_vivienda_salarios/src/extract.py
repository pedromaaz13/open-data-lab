"""Extracción de datos REALES (se ejecuta en tu máquina, donde hay red).

IMPORTANTE
----------
En el entorno remoto del laboratorio la salida a INE / datos.madrid.es está
bloqueada por política de red, así que estas funciones NO se ejecutan ahí. En tu
máquina local sí funcionan. Además, algunos identificadores de tabla (INE) y URLs
de dataset (Ayto Madrid) **debes verificarlos** la primera vez: los portales
cambian y aquí no he podido comprobarlos en vivo. Están marcados con TODO.

Estrategia recomendada:
  1. Renta por barrio  -> INE, Atlas de Distribución de Renta de los Hogares.
  2. Alquiler €/m²     -> Mº Vivienda (índice de alquiler) o Ayto Madrid.
  3. Compra €/m²       -> Ayto Madrid (precio de vivienda) o portal autonómico.
  4. Geometría barrios -> Ayto Madrid (GeoJSON de barrios).

Todo lo descargado se guarda intacto en data/raw/ con fecha de consulta.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

import config


def _guardar_raw(contenido: bytes, nombre: str) -> Path:
    """Guarda un fichero crudo en data/raw/ con la fecha de consulta en el nombre."""
    config.DATA_RAW.mkdir(parents=True, exist_ok=True)
    hoy = date.today().isoformat()
    destino = config.DATA_RAW / f"{hoy}_{nombre}"
    destino.write_bytes(contenido)
    return destino


def descargar_renta_ine(timeout: int = 60) -> Path:
    """Descarga la renta por barrio/distrito del Atlas de Renta del INE.

    El Atlas (ADRH) publica 'Renta neta media por hogar' y 'por persona' a nivel
    de sección censal, agregables a barrio y distrito. Para el municipio de Madrid
    (28079) hay descarga directa por unidad territorial.

    TODO: confirmar el ID de tabla / URL de descarga del Atlas para Madrid.
          Punto de partida: https://www.ine.es/experimental/atlas/experimental_atlas.htm
    """
    import httpx  # import perezoso: solo se necesita al ejecutar de verdad

    # TODO: sustituir por el endpoint/fichero real verificado.
    url = "https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/30824.csv"  # placeholder
    resp = httpx.get(url, timeout=timeout, headers={"User-Agent": "open-data-lab"})
    resp.raise_for_status()
    return _guardar_raw(resp.content, "ine_atlas_renta_madrid.csv")


def descargar_vivienda_madrid(timeout: int = 60) -> Path:
    """Descarga precios de alquiler y/o compra por barrio (Ayto Madrid / Mº Vivienda).

    TODO: confirmar el dataset concreto en https://datos.madrid.es (buscar
          'precio vivienda' / 'alquiler') o el Sistema Estatal de Índices de
          Alquiler del Ministerio de Vivienda.
    """
    import httpx

    url = "https://datos.madrid.es/egob/catalogo/PLACEHOLDER.csv"  # TODO real
    resp = httpx.get(url, timeout=timeout, headers={"User-Agent": "open-data-lab"})
    resp.raise_for_status()
    return _guardar_raw(resp.content, "madrid_vivienda.csv")


def descargar_barrios_geojson(timeout: int = 60) -> Path:
    """Descarga el GeoJSON de barrios de Madrid (límites administrativos).

    TODO: confirmar la URL del GeoJSON/Shapefile de barrios en datos.madrid.es.
    """
    import httpx

    url = "https://datos.madrid.es/egob/catalogo/BARRIOS_PLACEHOLDER.geojson"  # TODO
    resp = httpx.get(url, timeout=timeout, headers={"User-Agent": "open-data-lab"})
    resp.raise_for_status()
    return _guardar_raw(resp.content, "madrid_barrios.geojson")


if __name__ == "__main__":
    print("Descarga de datos reales (requiere red). Verifica los TODO de URLs.")
    print("Fuentes documentadas:")
    for clave, info in config.FUENTES.items():
        print(f"  - {clave}: {info['organismo']} — {info['dataset']} ({info['url']})")
