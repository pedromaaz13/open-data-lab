# Plan — Notebook de análisis socioeconómico de Madrid por distritos

Objetivo: un notebook (`notebooks/03_madrid_distritos_analisis.ipynb`) que recorra
**todas** las variables disponibles como **casos de estudio**, cada uno con su
**visualización** (gráfico o mapa) y su **conclusión**. Usa los datos reales del INE
(ya cargados con `load_ine.py`) y la geometría de distritos (mapas con `maps.py`).

> Reutiliza lo ya hecho: `load_ine.construir_madrid()` para los datos y
> `maps.mapa_folium` / `maps.mapa_choropleth` para los mapas. Cada caso = 1 sección.

## Estructura del notebook

```txt
0. Setup (sys.path, cargar datos, comprobar ficheros)
1..N  Casos de estudio (uno por bloque)
F. Ficha de conclusiones (resumen de hallazgos)
```

## Casos de estudio (con datos que YA tenemos)

| # | Caso de estudio | Variable(s) | Visual | Conclusión esperada |
|---|---|---|---|---|
| 1 | Renta por distrito | Renta neta media por hogar | Mapa + ranking | Brecha norte/sur de la ciudad |
| 2 | Renta vs desigualdad | Renta + Índice de Gini | Scatter | ¿Los ricos son más desiguales? (sí, +0,69) |
| 3 | ¿De qué se vive? | % salario / pensiones / paro | Barras apiladas | Distritos de sueldo vs de pensión |
| 4 | Peso de impuestos *(derivada)* | (bruta − neta)/bruta | Mapa + ranking | Dónde "se queda" más IRPF efectivo |
| 5 | Envejecimiento | % ≥65, edad media | Mapa | Distritos envejecidos vs jóvenes |
| 6 | Cómo se habita | % hogares unipersonales, tamaño del hogar | Mapa/barras | Dónde se vive solo / en familia |
| 7 | Población extranjera | % población española (inverso) | Mapa | Distribución de la población migrante |
| 8 | Brecha rico/pobre *(derivada)* | ratio renta máx/mín, P80/P20 | Barras | Magnitud de la desigualdad territorial |
| 9 | Índice de vulnerabilidad *(derivada, compuesta)* | renta⁻¹ + Gini + %≥65 + %prestaciones | Mapa + ranking | Distritos más vulnerables |
| 10 | Mapa de correlaciones | todas | Heatmap | Qué variables van juntas |
| 11 | Perfiles de distrito *(opcional, ML)* | varias (clustering K-Means) | Mapa de clusters | Tipos de distrito (p. ej. "centro rico", "periferia joven") |

## Variables derivadas (cómo se calculan)

- **Peso de impuestos (%)** = `(renta_bruta_hogar − renta_neta_hogar) / renta_bruta_hogar * 100`
- **Brecha rico/pobre** = `renta_neta_hogar.max() / renta_neta_hogar.min()` (y P80/P20 ya viene del INE)
- **Índice de vulnerabilidad (0–100)** — índice compuesto (ver
  `04_procesos_data/04_analisis/indices_compuestos.md`):
  1. Normalizar 0–1 cada componente (min–max), orientado a "más = más vulnerable":
     - renta baja → `1 − norm(renta_neta_hogar)`
     - desigualdad → `norm(Gini)`
     - envejecimiento → `norm(% ≥65)`
     - dependencia de prestaciones → `norm(% pensiones + % paro)`
  2. Media (pesos iguales por defecto; documentar si se cambian) × 100.
  3. Análisis de sensibilidad: ver si el ranking cambia al variar los pesos.

## Cómo se presentan las conclusiones

- Cada sección termina con una **celda markdown de "Conclusión"** (1–3 frases).
- Al final, una **ficha resumen** con los hallazgos clave y sus limitaciones.
- Honestidad: correlación ≠ causalidad; dato por distrito (no por persona).

## Siguiente bloque (lo que FALTA — vivienda)

Cuando cerremos el análisis socioeconómico, añadimos vivienda (ver `PLAN_VIVIENDA.md`):

1. **Alquiler €/m²** → Sistema Estatal de Índices de Alquiler (Mº Vivienda) — **oficial, primero**.
2. **Compra €/m²** → Mº Vivienda / Ayto. Madrid.
3. **Tipo y m²** → INE Censo 2021.

### Sobre Idealista / Fotocasa (datos no oficiales)

- Idealista tiene **API** pero con **acceso restringido** (hay que **solicitar permiso**,
  con límites de llamadas y condiciones de uso). No es "scrapear su base entera".
- Regla del laboratorio (ver `01_skills/web_scraping.md`): **fuentes oficiales primero**;
  portales privados **solo con su API y permiso**, respetando sus términos de uso (ToS) y
  la legalidad. Nada de scraping masivo sin autorización.
- Plan responsable: (1) usar el índice **oficial** de alquiler; (2) si hace falta más
  detalle, **solicitar acceso a la API de Idealista** y documentar la fuente y su licencia.

## Checklist

- [ ] 1. Renta (mapa + ranking)
- [ ] 2. Renta vs Gini
- [ ] 3. Fuente de ingresos
- [ ] 4. Peso de impuestos (derivada)
- [ ] 5. Envejecimiento
- [ ] 6. Hogares / tamaño
- [ ] 7. Población extranjera
- [ ] 8. Brecha rico/pobre (derivada)
- [ ] 9. Índice de vulnerabilidad (derivada compuesta)
- [ ] 10. Heatmap de correlaciones
- [ ] 11. Clustering de distritos (opcional)
- [ ] F. Ficha de conclusiones
