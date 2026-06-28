# Plan de datos reales — Madrid por distritos

Objetivo: enriquecer el proyecto con datos **reales** del INE (Atlas de Distribución
de Renta de los Hogares, ADRH 2023) a nivel de **distrito de Madrid**, y luego añadir
la capa de **vivienda**.

> Todas las descargas van a `06_proyectos/01_mapa_vivienda_salarios/data/raw/`.
> Año: **2023**. Formato: **CSV separado por `;`** (UTF-8 con BOM). Territorio:
> **distritos de Madrid** (códigos que empiezan por `2807901`...`2807921`).

## Estado actual (lo que ya funciona)

✅ **Renta real montada y reproducible.** Las 4 tablas del INE se descargan solas con
`python src/extract.py` (URLs reales en `src/extract.py`), `src/load_ine.py` las limpia
y filtra los 21 distritos de Madrid, y el notebook `notebooks/02_madrid_distritos_ine_real.ipynb`
muestra el análisis real + una capa **DuckDB** (SQL sobre un fichero, sin servidor).

Hallazgo real (INE 2023): Chamartín es el distrito más rico (≈79k €/hogar) y Puente de
Vallecas el más pobre (≈33k €); los distritos de **mayor renta** son los **más
desiguales** por dentro (correlación renta↔Gini ≈ +0,69).

## Siguiente paso: el MAPA antes que la vivienda

Decisión: hacer el **mapa real** ahora, antes de la vivienda. Motivo:

| | Mapa real | Vivienda |
|---|---|---|
| Datos que necesita | 1 fichero (geometría distritos) | Buscar alquiler/compra oficial por distrito (más difícil) |
| Usa lo que ya tienes | ✅ Sí (la renta real) | Necesita datos nuevos |
| Recompensa | 🔥 Madrid de verdad coloreado por renta | Alta, pero más curro de búsqueda |

El mapa convierte la renta que ya tenemos en un mapa real de Madrid con un solo fichero
más: victoria rápida y muy visual. Luego vamos a por la vivienda (más caza de datos).

**Tarea (geometría de distritos):**
1. En `https://datos.madrid.es`, busca `distritos`.
2. Descarga el dataset de **Distritos** con **geometría** (GeoJSON o Shapefile .zip).
3. Guárdalo en `data/raw/` (p. ej. `distritos_madrid.geojson`).
4. Inspecciona y pega columnas + CRS:
   ```python
   import geopandas as gpd
   g = gpd.read_file("../data/raw/EL_FICHERO.geojson")   # o "...zip" si es shapefile
   print("filas:", len(g)); print("columnas:", g.columns.tolist()); print("CRS:", g.crs)
   print(g.drop(columns="geometry").head(25).to_string())
   ```
   Con eso se escribe la función que une geometría + renta y pinta el coroplético real
   (estático) y el mapa interactivo con **Kepler.gl**.

## Bloque A — INE Atlas (renta y sociedad)

Todas salen del mismo sitio: *Atlas de Renta → Resultados por municipios, distritos y
secciones → (tabla) → Madrid → distritos → 2023 → Descargar CSV (;)*.

| # | Tabla en el INE | Nombre destino (renómbralo así) | Qué aporta | Prioridad |
|---|---|---|---|---|
| 1 | **Indicadores de renta media y mediana** | `ine_renta_media_mediana.csv` | Renta media y **mediana** por hogar y por persona. El núcleo. | 🎯 **1º** |
| 2 | **Índice de Gini y Distribución P80/P20** | `ine_gini_p80p20.csv` | Desigualdad *dentro* de cada distrito | 2º |
| 3 | **Distribución por fuente de ingresos** | `ine_fuente_ingresos.csv` | % de renta de **salario** vs pensiones vs paro | 3º |
| 4 | **Indicadores demográficos** | `ine_demografia.csv` | % menores de 18 y mayores de 65 (edad) | 4º |
| 5 | **Población bajo umbrales de renta** | `ine_umbrales_pobreza.csv` | % de población pobre / vulnerable | 5º |

## Bloque B — Vivienda (otra fuente, más adelante)

| Dato | Fuente | Nombre destino |
|---|---|---|
| Alquiler €/m² por distrito | Mº Vivienda (índice de alquiler) / Ayto. Madrid | `vivienda_alquiler.csv` |
| Compra €/m² por distrito | Ayto. Madrid / portales | `vivienda_compra.csv` |
| Geometría de distritos/barrios | Ayto. Madrid (GeoJSON) | `madrid_distritos.geojson` |

## Flujo de trabajo (cómo lo montamos juntos)

```txt
1. Descargas la tabla 1 (renta) y la guardas como ine_renta_media_mediana.csv
2. Me pegas sus columnas (snippet de abajo)
3. Yo escribo el "loader" que traduce el formato del INE al del pipeline
4. Vemos Madrid con renta REAL (gráficos + mapa)
5. Repetimos con las tablas 2..5 (mismo formato → loaders rápidos)
6. Bloque B: añadimos vivienda y cruzamos -> esfuerzo real
```

Como todas las tablas del INE comparten formato, **en cuanto crackeemos la nº1 las
demás van rodadas.**

## Nota sobre el formato del INE (aprendido)

- Encoding correcto: **`utf-8-sig`** (no latin-1; si no, salen símbolos raros).
- Formato **largo**: cada fila es *territorio × indicador × año*; el valor está en `Total`
  (`16.893` = 16.893 € con `.` de miles; `.` a secas = sin dato). `src/load_ine.py` ya
  parsea esto y pivota los indicadores a columnas.

## Estado

- [x] 1. Renta media y mediana ✅
- [x] 2. Gini y P80/P20 ✅
- [x] 3. Fuente de ingresos ✅
- [x] 4. Demografía ✅
- [ ] 5. Umbrales de pobreza (opcional, mismo método)
- [ ] **Mapa**: geometría de distritos (GeoJSON Ayto. Madrid) → coroplético + Kepler.gl ← *siguiente*
- [ ] B. Vivienda (alquiler / compra por distrito) → esfuerzo real
