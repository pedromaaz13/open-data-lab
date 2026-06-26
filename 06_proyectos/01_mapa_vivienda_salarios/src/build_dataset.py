"""Construye el dataset final de barrios de Madrid con indicadores.

Uso:
    python src/build_dataset.py --source synthetic   # demo reproducible (por defecto)
    python src/build_dataset.py --source real        # datos oficiales (requiere red)

Escribe data/processed/madrid_barrios.csv (y .parquet si pyarrow está disponible).
"""
from __future__ import annotations

import argparse
import os
import sys

# Permite ejecutar el script directamente: añade su carpeta (src/) al path.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pandas as pd

import config
import transform


def construir(source: str = "synthetic") -> pd.DataFrame:
    if source == "synthetic":
        from synthetic import generar_barrios

        base = generar_barrios()
    elif source == "real":
        raise NotImplementedError(
            "Para datos reales: ejecuta src/extract.py en tu máquina (con red), "
            "verifica los TODO de URLs/IDs y carga aquí los ficheros de data/raw/. "
            "Después aplica transform.add_indicators() sobre el DataFrame unido."
        )
    else:
        raise ValueError(f"source no válido: {source!r} (usa 'synthetic' o 'real')")

    return transform.add_indicators(base)


def main() -> None:
    parser = argparse.ArgumentParser(description="Construye el dataset de barrios de Madrid.")
    parser.add_argument("--source", default="synthetic", choices=["synthetic", "real"])
    args = parser.parse_args()

    df = construir(args.source)
    config.DATA_PROCESSED.mkdir(parents=True, exist_ok=True)

    csv_path = config.DATA_PROCESSED / "madrid_barrios.csv"
    df.to_csv(csv_path, index=False)
    print(f"OK -> {csv_path}  ({len(df)} barrios)")

    try:
        parquet_path = config.DATA_PROCESSED / "madrid_barrios.parquet"
        df.to_parquet(parquet_path, index=False)
        print(f"OK -> {parquet_path}")
    except Exception as e:  # pyarrow puede no estar instalado
        print(f"(parquet omitido: {e})")


if __name__ == "__main__":
    main()
