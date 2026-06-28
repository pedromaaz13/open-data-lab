"""Tests del loader del INE (formato real del Atlas de Renta).

Usan un mock que replica el formato del INE (CSV ';', UTF-8 con BOM, formato largo).
Así el CI verifica que el parseo/filtrado/pivotado del dato real sigue funcionando.
"""
import numpy as np

import load_ine

MOCK = """Municipios;Distritos;Secciones;Indicadores de renta media y mediana;Periodo;Total
28079 Madrid;;;Renta neta media por persona;2023;17.000
;2807901 Madrid distrito 01 Centro;;Renta neta media por persona;2023;18.500
;2807901 Madrid distrito 01 Centro;;Renta neta media por hogar;2023;41.000
;2807917 Madrid distrito 17 Villaverde;;Renta neta media por persona;2023;11.500
;2807917 Madrid distrito 17 Villaverde;;Renta neta media por hogar;2023;28.000
;;2807901001 Una seccion censal;Renta neta media por persona;2023;19.000
;2800601 Alcobendas distrito 01;;Renta neta media por persona;2023;20.000
"""


def test_to_num_formato_ine():
    assert load_ine._to_num("16.893") == 16893.0   # separador de miles
    assert load_ine._to_num("33,5") == 33.5        # decimal con coma
    assert np.isnan(load_ine._to_num("."))         # sin dato
    assert np.isnan(load_ine._to_num(None))


def test_distritos_madrid_filtra_y_pivota(tmp_path):
    p = tmp_path / "ine_renta_media_mediana.csv"
    p.write_text(MOCK, encoding="utf-8-sig")
    out = load_ine.distritos_madrid(p)

    # Solo distritos de Madrid: Centro y Villaverde.
    # (excluidos: el municipio Madrid, la sección censal y el distrito de Alcobendas)
    assert len(out) == 2
    assert set(out["cod_distrito"]) == {"2807901", "2807917"}

    # Los indicadores se han pivotado a columnas.
    assert "Renta neta media por hogar" in out.columns
    assert "Renta neta media por persona" in out.columns

    centro = out[out["distrito"].str.contains("Centro")].iloc[0]
    assert centro["Renta neta media por persona"] == 18500.0
    assert centro["Renta neta media por hogar"] == 41000.0


def test_distritos_madrid_con_prefijo(tmp_path):
    p = tmp_path / "x.csv"
    p.write_text(MOCK, encoding="utf-8-sig")
    out = load_ine.distritos_madrid(p, prefijo="demo_")
    assert any(c.startswith("demo_") for c in out.columns)
    # las claves territoriales NO llevan prefijo
    assert "cod_distrito" in out.columns and "distrito" in out.columns
