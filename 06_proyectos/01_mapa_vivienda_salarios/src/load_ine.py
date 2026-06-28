"""Carga y limpieza de los ficheros del Atlas de Renta del INE (ADRH).

Formato del INE (CSV separado por ';', UTF-8 con BOM, formato 'largo'):

    Municipios | Distritos | Secciones | <indicador> | Periodo | Total

Cada fila = un territorio x un indicador x un año. La columna 'Total' es el valor
(separador de miles '.', decimal ',', y '.' a secas = sin dato).

Este módulo:
  - lee con el encoding correcto (utf-8-sig, arregla los símbolos raros),
  - filtra los DISTRITOS de la ciudad de Madrid (código de distrito 28079xx),
  - parsea los valores a número,
  - pivota los indicadores a columnas,
  - y une las distintas tablas por distrito.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

import config

COD_MADRID = "28079"  # código INE del municipio de Madrid

# Nombres oficiales de los 21 distritos de la ciudad de Madrid (por su número).
NOMBRES_DISTRITO = {
    "01": "Centro", "02": "Arganzuela", "03": "Retiro", "04": "Salamanca",
    "05": "Chamartín", "06": "Tetuán", "07": "Chamberí", "08": "Fuencarral-El Pardo",
    "09": "Moncloa-Aravaca", "10": "Latina", "11": "Carabanchel", "12": "Usera",
    "13": "Puente de Vallecas", "14": "Moratalaz", "15": "Ciudad Lineal",
    "16": "Hortaleza", "17": "Villaverde", "18": "Villa de Vallecas",
    "19": "Vicálvaro", "20": "San Blas-Canillejas", "21": "Barajas",
}

# Fichero (nombre limpio que descarga extract.py) -> prefijo para sus columnas.
FICHEROS = {
    "ine_renta_media_mediana.csv": "",          # núcleo: deja los nombres tal cual
    "ine_fuente_ingresos.csv": "ingresos_",
    "ine_gini_p80p20.csv": "",
    "ine_demografia.csv": "demo_",
}


def _to_num(x) -> float:
    """Convierte un valor del INE ('16.893', '0,312', '.') a float."""
    if pd.isna(x):
        return np.nan
    s = str(x).strip()
    if s in {".", "..", "", "-", "N/A"}:
        return np.nan
    s = s.replace(".", "").replace(",", ".")  # miles '.' y decimal ','
    try:
        return float(s)
    except ValueError:
        return np.nan


def leer_ine(path: str | Path) -> pd.DataFrame:
    """Lee un CSV del Atlas y normaliza los nombres de columna."""
    df = pd.read_csv(path, sep=";", encoding="utf-8-sig", dtype=str)
    df.columns = [c.strip() for c in df.columns]
    # columnas 0-2 = territorio; 3 = indicador; luego Periodo y Total
    df = df.rename(columns={df.columns[3]: "indicador", "Periodo": "periodo", "Total": "total"})
    return df


def distritos_madrid(path: str | Path, periodo: str = "2023", prefijo: str = "") -> pd.DataFrame:
    """Distritos de Madrid de un fichero, con los indicadores pivotados a columnas."""
    df = leer_ine(path)
    cod = df["Distritos"].str.extract(r"^\s*(\d+)")[0]
    es_mad = (
        df["Distritos"].notna()
        & df["Secciones"].isna()
        & cod.str.startswith(COD_MADRID, na=False)
    )
    d = df[es_mad].copy()
    d["cod_distrito"] = cod[es_mad]
    d["distrito"] = d["Distritos"].str.replace(r"^\s*\d+\s*", "", regex=True).str.strip()
    d["valor"] = d["total"].map(_to_num)
    d = d[d["periodo"] == periodo]

    piv = (
        d.pivot_table(index=["cod_distrito", "distrito"], columns="indicador",
                      values="valor", aggfunc="first")
        .reset_index()
    )
    piv.columns.name = None
    if prefijo:
        piv = piv.rename(columns={c: prefijo + c for c in piv.columns
                                  if c not in ("cod_distrito", "distrito")})
    return piv


def construir_madrid(raw_dir: str | Path | None = None, periodo: str = "2023") -> pd.DataFrame:
    """Une todas las tablas disponibles en data/raw/ en un único dataset por distrito."""
    raw = Path(raw_dir) if raw_dir else config.DATA_RAW
    base: pd.DataFrame | None = None
    for fichero, prefijo in FICHEROS.items():
        ruta = raw / fichero
        if not ruta.exists():
            print(f"(aviso) falta {fichero}, lo salto")
            continue
        piv = distritos_madrid(ruta, periodo=periodo, prefijo=prefijo)
        base = piv if base is None else base.merge(piv, on=["cod_distrito", "distrito"], how="outer")
    if base is None:
        raise FileNotFoundError(
            f"No hay ficheros del INE en {raw}. Ejecuta antes: python src/extract.py"
        )
    # Añade el nombre oficial del distrito (Centro, Salamanca, ...).
    base["num_distrito"] = base["cod_distrito"].str[5:7]
    base.insert(2, "nombre_distrito", base["num_distrito"].map(NOMBRES_DISTRITO))
    base = base.drop(columns="num_distrito")
    return base.sort_values("cod_distrito").reset_index(drop=True)


if __name__ == "__main__":
    df = construir_madrid()
    config.DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    out = config.DATA_PROCESSED / "madrid_distritos_ine.csv"
    df.to_csv(out, index=False)
    print(f"OK -> {out}  ({len(df)} distritos, {df.shape[1]} columnas)")
    print(df.head(25).to_string())
