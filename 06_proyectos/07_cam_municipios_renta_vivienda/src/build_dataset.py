"""Construye el dataset de municipios de la CAM con indicadores.

    python src/build_dataset.py --source synthetic   (por defecto)
    python src/build_dataset.py --source real         (requiere extracción previa)
"""
from __future__ import annotations

import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
import config, transform


def construir(source: str = "synthetic") -> pd.DataFrame:
    if source == "synthetic":
        from synthetic import generar_municipios
        base = generar_municipios()
    elif source == "real":
        raise NotImplementedError("Ejecuta src/extract.py en tu máquina y une los CSV por cod_ine.")
    else:
        raise ValueError(f"source no válido: {source!r}")
    return transform.add_indicators(base)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--source", default="synthetic", choices=["synthetic", "real"])
    args = p.parse_args()
    df = construir(args.source)
    config.DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    out = config.DATA_PROCESSED / "cam_municipios.csv"
    df.to_csv(out, index=False)
    print(f"OK -> {out}  ({len(df)} municipios)")


if __name__ == "__main__":
    main()
