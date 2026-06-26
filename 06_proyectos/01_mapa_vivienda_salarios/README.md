# Madrid · renta vs coste de vivienda por barrios

## Pregunta de investigación

¿En qué barrios y distritos de Madrid se vive mejor con el sueldo y en cuáles vas
más apurado, cruzando la **renta del hogar** con el **coste de la vivienda**
(alquiler y compra)?

## Contexto

El acceso a la vivienda es el principal problema social en Madrid. El precio
absoluto (€/m²) no cuenta toda la historia: lo que importa es el **esfuerzo**, es
decir, qué parte del sueldo se va en vivienda. Un barrio caro puede ser más
"asequible" que uno barato si las rentas son mucho más altas — y al revés.

## Indicadores

| Indicador | Definición | Vivienda tipo |
|---|---|---|
| **Esfuerzo de alquiler (%)** | % de la renta anual del hogar que se va en alquilar | 70 m² |
| **Esfuerzo de compra (años)** | años de renta íntegra del hogar para comprar | 90 m² |

Clasificación de alquiler: `<30%` holgado · `30-40%` ajustado · `>40%` apurado.

## Fuentes de datos previstas (reales)

| Dato | Fuente | Nivel |
|---|---|---|
| Renta media del hogar | INE · Atlas de Distribución de Renta de los Hogares (ADRH) | barrio / distrito / sección |
| Alquiler €/m² | Mº Vivienda (índice de alquiler) / Ayto. Madrid | barrio / distrito |
| Compra €/m² | Ayto. Madrid / Mº Vivienda | barrio / distrito |
| Geometría de barrios | Ayuntamiento de Madrid (GeoJSON) | barrio |

## Metodología

1. **Extracción** (`src/extract.py`) — descarga de INE y Ayto. Madrid a `data/raw/`.
2. **Transformación** (`src/transform.py`) — unión por código de barrio y cálculo
   de indicadores (`src/indicators.py`).
3. **Dataset** (`src/build_dataset.py`) — genera `data/processed/madrid_barrios.csv`.
4. **Análisis** (`notebooks/01_madrid_barrios_renta_vivienda.ipynb`) — rankings,
   scatter renta vs esfuerzo, agregados por distrito y mapa.

## Estado actual

✅ Pipeline completo y **probado con datos sintéticos** reproducibles (131 barrios,
21 distritos). El notebook se ejecuta de principio a fin y los indicadores tienen
tests (`tests/`). ⏳ Falta enchufar los datos **reales** (la red de este entorno
no permite descargar de INE/Madrid; se hace en tu máquina).

## Cómo reproducir

```bash
# Desde la raíz del repo, con el entorno activado (ver README raíz)
cd 06_proyectos/01_mapa_vivienda_salarios

# 1. Construir el dataset (demo sintética, funciona sin red)
python src/build_dataset.py --source synthetic

# 2. Abrir el notebook
jupyter lab notebooks/01_madrid_barrios_renta_vivienda.ipynb

# 3. Tests del pipeline e indicadores
pytest        # desde esta carpeta
```

### Para datos reales (en tu máquina, con red)

1. Edita `src/extract.py` y **verifica los `TODO`** (IDs de tabla del INE y URLs de
   datasets del Ayto. de Madrid — pueden cambiar).
2. Ejecuta los extractores; los crudos quedan en `data/raw/` con fecha.
3. Une renta + alquiler + compra por `cod_barrio`, aplica `transform.add_indicators`
   y guarda en `data/processed/`.
4. En el notebook, cambia `SOURCE = 'real'`.

## Estructura

```txt
src/        config, distritos, indicators, synthetic, transform, extract, build_dataset
tests/      test_indicators.py, test_pipeline.py
notebooks/  01_madrid_barrios_renta_vivienda.ipynb
data/       raw / interim / processed   (no versionado)
outputs/    gráficos y mapas            (no versionado)
```

## Limitaciones

- Renta y precios de vivienda provienen de fuentes distintas y con metodologías propias.
- La superficie "tipo" (70/90 m²) es una convención; cambiarla altera los valores.
- Falacia ecológica: el dato es por barrio, no por persona.
- Cobertura oficial del precio de **compra por barrio** más débil que la de alquiler.

## Próximos pasos

- [ ] Verificar y fijar los endpoints reales de INE y Ayto. Madrid.
- [ ] Añadir geometría de barrios y mapa coroplético / Kepler.gl.
- [ ] Extender a la Comunidad de Madrid por municipios.
- [ ] Artículo de data storytelling con los hallazgos reales.
