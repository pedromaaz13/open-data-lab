# Comunidad de Madrid · renta vs coste de vivienda por municipios

Nivel 2 del análisis de vivienda (el nivel 1 es por barrios de la ciudad de Madrid,
proyecto `01_mapa_vivienda_salarios`). Aquí la unidad es el **municipio** de la CAM.

## Pregunta de investigación

¿En qué municipios de la Comunidad de Madrid se vive mejor con el sueldo y en cuáles
vas más apurado, cruzando renta del hogar con coste de la vivienda (alquiler y compra)?

## Indicadores

| Indicador | Definición | Vivienda tipo |
|---|---|---|
| Esfuerzo de alquiler (%) | % de la renta anual del hogar en alquiler | 80 m² |
| Esfuerzo de compra (años) | años de renta para comprar | 100 m² |

## Fuentes (reales)

| Dato | Fuente | Nivel |
|---|---|---|
| Renta del hogar | INE · Atlas de Renta (ADRH) | municipio |
| Precio de compra €/m² | Mº Vivienda | municipio |
| Alquiler €/m² | Mº Vivienda (índice de alquiler) | municipio |
| Geometría municipal | CNIG/IGN | municipio |

## Estado

✅ Pipeline probado con **datos sintéticos** de los ~30 municipios más poblados de la
CAM (nombres reales, cifras sintéticas). ⏳ Datos reales: ejecuta `src/extract.py` en
tu máquina (mismo procedimiento que el proyecto 01, ver su
`docs/COMO_DESCARGAR_DATOS_REALES.md`).

## Cómo reproducir

```bash
cd 06_proyectos/07_cam_municipios_renta_vivienda
python src/build_dataset.py --source synthetic
jupyter lab notebooks/01_cam_municipios_renta_vivienda.ipynb
pytest
```

## Diferencia con el proyecto 01

- Unidad territorial: **municipio** (no barrio).
- El **precio de compra por municipio** tiene mejor cobertura oficial que por barrio,
  así que aquí el esfuerzo de compra es especialmente fiable.
- Geometría: límites municipales del CNIG/IGN (no barrios del Ayto.).

## Limitaciones

- Demo con ~30 municipios; el Atlas del INE cubre los 179 de la CAM por código.
- Renta y precios provienen de fuentes distintas.
- Superficie "tipo" (80/100 m²) es una convención.
