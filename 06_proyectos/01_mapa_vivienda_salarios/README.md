# Madrid · renta vs coste de vivienda

## Pregunta de investigación

¿Dónde se vive mejor con el sueldo en Madrid y dónde más apurado, cruzando la
**renta** con el **coste de la vivienda** (alquiler y compra)? Como paso previo,
se construye además un **perfil socioeconómico** completo por distrito.

## Contexto

El acceso a la vivienda es el principal problema social en Madrid. El precio
absoluto (€/m²) no cuenta toda la historia: lo que importa es el **esfuerzo** — qué
parte del sueldo se va en vivienda. Un sitio caro puede ser más "asequible" que uno
barato si las rentas son mucho más altas, y al revés.

## Dos vías de trabajo

| Vía | Notebook | Datos | Estado |
|---|---|---|---|
| **Demo sintética por barrios** (prueba la maquinaria) | `01_madrid_barrios_renta_vivienda.ipynb` | sintéticos (131 barrios) | ✅ funciona sin red |
| **Análisis REAL por distrito** (renta + mapa + DuckDB) | `02_madrid_distritos_ine_real.ipynb` | **INE Atlas 2023** (real) | ✅ funcionando |
| **Análisis socioeconómico completo** (11 casos de estudio) | `03_madrid_distritos_analisis.ipynb` | **INE Atlas 2023** (real) | ✅ funcionando |

## Datos

| Dato | Fuente | Estado |
|---|---|---|
| Renta (neta/bruta/mediana), Gini, fuente de ingresos, demografía | INE · Atlas de Renta (ADRH 2023) | ✅ descargado y cargado |
| Geometría de los 21 distritos | Ayto. de Madrid (Geoportal) | ✅ descargado |
| Alquiler €/m² por distrito | Sistema Estatal de Índices de Alquiler | ⏳ siguiente |
| Compra €/m² por distrito | Mº Vivienda / Ayto. Madrid | ⏳ pendiente |
| Tipo de vivienda y m² | INE · Censo 2021 | ⏳ pendiente |

> Recuerda: los datos NO van al repo (se ignoran). Se descargan con
> `python src/extract.py` (reproducible). Ver `00_documentacion/flujo_anadir_fuente_datos.md`.

## Cómo reproducir

```bash
# desde la raíz del repo, con el entorno activado
cd 06_proyectos/01_mapa_vivienda_salarios

# 1. Descargar los datos reales del INE + geometría (a data/raw/)
python src/extract.py

# 2. Construir la tabla real de Madrid por distrito
python src/load_ine.py            # crea data/processed/madrid_distritos_ine.csv

# 3. Abrir los notebooks de análisis real
jupyter lab notebooks/02_madrid_distritos_ine_real.ipynb
jupyter lab notebooks/03_madrid_distritos_analisis.ipynb

# (alternativa sin red: demo sintética por barrios)
python src/build_dataset.py --source synthetic
jupyter lab notebooks/01_madrid_barrios_renta_vivienda.ipynb

# tests (14)
pytest
```

## Estructura

```txt
src/
  config.py          parámetros y fuentes (FUENTES)
  extract.py         descargador real (INE Atlas + geometría)
  load_ine.py        limpia el formato INE, filtra Madrid, une tablas por distrito
  maps.py            mapas: choropleth (matplotlib), Folium y Kepler.gl
  indicators.py      esfuerzo de alquiler/compra (funciones puras)
  distritos.py       21 distritos / 131 barrios (para la demo sintética)
  synthetic.py       datos sintéticos de barrios (demo)
  transform.py       indicadores sobre los barrios sintéticos
  build_dataset.py   CLI de la demo sintética
tests/               test_indicators, test_pipeline, test_load_ine, test_maps (14)
notebooks/           01 (sintético barrios), 02 (real distritos), 03 (análisis completo)
docs/                guías y planes (ver abajo)
data/  outputs/      no versionados
```

## Documentación del proyecto (`docs/`)

- `COMO_DESCARGAR_DATOS_REALES.md` — guía paso a paso de descarga del INE/Madrid.
- `INVENTARIO_DATOS.md` — qué variables tenemos / faltan.
- `PLAN_DATOS_REALES.md` — plan de las tablas del INE (hecho).
- `PLAN_ANALISIS_DISTRITOS.md` — plan del notebook 03 (11 casos de estudio).
- `PLAN_VIVIENDA.md` — fuentes del bloque vivienda.
- `PLAN_EJECUCION_VIVIENDA.md` — loop de ejecución del bloque vivienda.

## Indicadores de esfuerzo (`src/indicators.py`)

| Indicador | Definición | Vivienda tipo |
|---|---|---|
| Esfuerzo de alquiler (%) | alquiler anual / renta del hogar | 70 m² |
| Esfuerzo de compra (años) | precio vivienda / renta del hogar | 90 m² |

Clasificación de alquiler: `<30%` holgado · `30-40%` ajustado · `>40%` apurado.
*(La lógica ya existe; falta enchufar los datos reales de alquiler/compra.)*

## Hallazgos reales (INE 2023, por distrito)

- Brecha territorial: Chamartín (~79k €/hogar) casi duplica a Puente de Vallecas (~33k €).
- Los distritos de **mayor renta** son los **más desiguales** por dentro (renta↔Gini ≈ +0,69).
- En los distritos ricos, menos parte de la renta viene del salario (más del capital).

## Limitaciones

- Dato por **distrito**, no por persona (cuidado con la falacia ecológica).
- Año 2023; correlación ≠ causalidad.
- Falta la capa de vivienda para el esfuerzo **real** (en marcha).

## Próximos pasos

- [ ] Añadir **alquiler** €/m² (Sistema Estatal de Índices) → esfuerzo real.
- [ ] Añadir **compra** €/m² y **tipo/m²** (Censo 2021).
- [ ] Notebook 04: mapa del esfuerzo (dónde se vive más apurado).
- [ ] Artículo de data storytelling con los hallazgos.
