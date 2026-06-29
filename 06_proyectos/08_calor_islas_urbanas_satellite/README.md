# Calor y desigualdad en Madrid (satélite + renta)

Primer proyecto **satelital** del laboratorio. Cruza **temperatura superficial**
(Landsat térmico), **vegetación** (NDVI Sentinel-2) y **renta** (INE, que ya tenemos)
para responder dónde se concentra el calor urbano y a quién golpea más.

> Enlaza directo con el proyecto 01: reutiliza la **geometría de distritos** y la
> **renta real por distrito** ya cargadas (`load_ine.py`, `maps.py`).

## Pregunta de investigación

¿Qué zonas de Madrid acumulan más calor superficial y cómo se relaciona ese calor
con la **renta**, la **vegetación**, la **densidad urbana** y la **vulnerabilidad
social**? ¿La crisis climática urbana es también una cuestión de desigualdad?

## Subpreguntas (incluye tus ideas)

1. ¿Qué distritos/barrios tienen mayor **temperatura superficial** (LST)?
2. ¿El calor coincide con **menor renta**? (desigualdad climática)
3. ¿Las zonas con **menos vegetación** (NDVI) sufren más calor?
4. **Desertización del verde:** ¿qué zonas han **perdido vegetación** entre años?
5. **Infraestructura de refresco:** ¿los distritos calientes tienen **menos zonas
   verdes, fuentes y arbolado/sombra**? (datos OSM)
6. ¿Dónde coinciden **calor + baja renta + población mayor** (vulnerables)?
7. ¿Sube el **alquiler** en las zonas más frescas/verdes? (cuando tengamos alquiler)

## Datos

| Dato | Fuente | Estado |
|---|---|---|
| **LST** (temperatura superficial) | Landsat 8/9 C2 L2 (banda térmica `ST_B10`) | ⏳ vía STAC |
| **NDVI / vegetación** | Sentinel-2 L2A | ⏳ vía STAC |
| **NDBI** (urbanización) | Sentinel-2 / Landsat | ⏳ derivado |
| **Renta + demografía** | INE Atlas (proyecto 01) | ✅ ya disponible |
| **Geometría de distritos** | Ayto. Madrid | ✅ ya disponible |
| **Termómetro de aire** (validación) | AEMET (estaciones) | ⏳ |
| **Zonas verdes, fuentes, arbolado** | OpenStreetMap (osmnx) | ⏳ |
| **Alquiler €/m²** | Sistema Estatal Índices de Alquiler | ⏳ (bloque vivienda) |

## Variables y derivadas

```txt
LST_media / LST_max por distrito
anomalia_calor = LST_distrito − LST_media_ciudad
NDVI_medio · % zona verde · NDBI
cambio_NDVI (año A → año B)   → desertización del verde
densidad_fuentes / arbolado / parques (OSM)  → infraestructura de refresco
% poblacion >65 · renta (INE)
indice_vulnerabilidad_climatica = f(calor↑, vegetacion↓, renta↓, mayores↑)
```

## Metodología (pipeline)

```txt
1. AOI = distritos de Madrid (geometría ya disponible)
2. Buscar escenas de verano vía STAC (Landsat LST + Sentinel-2 NDVI), filtrar nubes
3. Calcular LST y NDVI (rioxarray/rasterio)
4. Estadísticas zonales por distrito (rasterstats / exactextract)
5. OSM (osmnx): parques, fuentes, arbolado → densidad por distrito
6. Unir con renta + demografía (load_ine del proyecto 01)
7. Índice de vulnerabilidad climática (normalizar + combinar)
8. Mapas (Folium/Kepler), scatter renta↔calor, ranking, conclusiones
```

## Visualizaciones previstas

- Mapa de **LST** (islas de calor) y mapa de **NDVI**.
- Scatter **renta vs temperatura** y **vegetación vs temperatura**.
- Mapa de **vulnerabilidad climática** (dónde priorizar adaptación).
- "Antes/después" de NDVI (desertización del verde).
- Ranking de distritos más calientes / más vulnerables.

## Stack

`requirements-geo.txt` + `requirements-remote-sensing.txt`:
`pystac-client`, `planetary-computer`, `rioxarray`, `rasterio`, `xarray`,
`rasterstats`, `geopandas`, `osmnx`, `folium`. (Ver
`10_referencias/remote_sensing_satellite_data_sources.md` y
`04_procesos_data/01_extraccion/usgs_landsat.md`.)

## Plan de ejecución (loop, como el de vivienda)

- [ ] 1. AOI + buscar escenas Landsat/Sentinel-2 (STAC) → `extract.py`
- [ ] 2. Calcular **NDVI** (Sentinel-2) por distrito (nivel 1)
- [ ] 3. Calcular **LST** (Landsat térmico) por distrito (nivel 2)
- [ ] 4. **OSM**: zonas verdes, fuentes, arbolado por distrito
- [ ] 5. Cruzar con renta + demografía → **índice de vulnerabilidad climática**
- [ ] 6. **Desertización**: cambio de NDVI entre dos veranos
- [ ] 7. Mapas + scatter + ranking + **artículo** de data storytelling
- [ ] 8. (si hay alquiler) ¿el frescor/verde encarece el alquiler?

## Limitaciones (honestidad)

- Rásteres = procesamiento más pesado; se ejecuta en tu máquina (con red).
- LST (satélite) ≠ temperatura del aire (AEMET); se complementan, no son lo mismo.
- "Sombras" reales requieren modelo 3D (altura de edificios/árboles) → fase avanzada;
  empezamos con proxies (NDVI, arbolado y zonas verdes OSM).
- Dato por distrito (no por persona).

## Estado

📋 **Planificado.** Pendiente de empezar el loop (tras cerrar el bloque vivienda del
proyecto 01). Reutilizará la renta y la geometría ya disponibles.
