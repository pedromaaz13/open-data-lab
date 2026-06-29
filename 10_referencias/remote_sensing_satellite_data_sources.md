# Remote Sensing, satélite y computer vision para Open Data Lab

> Documento de referencia para `open-data-lab`.
>
> Ruta sugerida:
>
> `10_referencias/remote_sensing_satellite_data_sources.md`
>
> También puede servir como base para:
>
> `12_learning_tracks/04_satellite_remote_sensing/README.md`

---

## 0. Objetivo de esta línea de trabajo

Esta línea dentro de `open-data-lab` busca aprender a trabajar con datos satelitales, GIS, teledetección, APIs geoespaciales, imágenes raster, análisis medioambiental y computer vision aplicada a problemas sociales, climáticos y territoriales.

El objetivo no es empezar directamente con modelos complejos, sino avanzar por niveles:

```txt
Exploración visual
↓
Búsqueda de escenas por API
↓
Descarga / lectura cloud-native
↓
Procesamiento raster/vector
↓
Cálculo de índices
↓
Cruce con datos sociales/económicos
↓
Visualización avanzada
↓
Modelos predictivos / computer vision
↓
Artículo, dashboard o data app
```

Esta línea cubre:

- computer vision;
- análisis satelital;
- daños en infraestructuras;
- calor extremo;
- incendios;
- vegetación;
- calidad del aire;
- sequía;
- movimientos del terreno;
- inundaciones;
- terremotos;
- contaminación atmosférica;
- nubes de gas;
- análisis histórico y actual.

---

# 1. Primer proyecto satelital recomendado

El primer proyecto satelital que haría en `open-data-lab` sería:

> **Calor y desigualdad en Madrid: temperatura superficial, vegetación y renta por barrios/municipios.**

## Por qué este proyecto

Es el mejor primer caso porque conecta varias líneas del laboratorio:

- vivienda;
- renta;
- desigualdad;
- calor extremo;
- islas de calor urbanas;
- vegetación;
- datos satelitales;
- GIS;
- Python;
- storytelling;
- producto de datos.

Además, es un proyecto suficientemente técnico para demostrar valor profesional, pero no tan complejo como empezar directamente con daños en infraestructuras, SAR avanzado o modelos de computer vision.

## Pregunta principal

> ¿Qué zonas de Madrid acumulan más calor superficial y cómo se relaciona ese calor con renta, vegetación, densidad urbana y vulnerabilidad social?

## Subpreguntas

```txt
1. ¿Qué barrios o municipios tienen mayor temperatura superficial?
2. ¿Qué relación hay entre temperatura superficial y renta?
3. ¿Las zonas con menos vegetación tienen mayor exposición al calor?
4. ¿Dónde coinciden calor, baja renta y población vulnerable?
5. ¿Qué zonas deberían priorizarse para adaptación climática urbana?
```

## Datos necesarios

```txt
Landsat 8/9 térmico
Sentinel-2 vegetación
INE Atlas de Renta
AEMET temperaturas
Geometrías de barrios / municipios
OSM zonas verdes, carreteras, edificios
Población por edad
```

## Variables base

```txt
codigo_barrio / codigo_municipio
nombre_barrio / nombre_municipio
geometria
renta_media_hogar
renta_media_persona
poblacion_total
poblacion_mayor_65
temperatura_superficial
ndvi
ndbi
porcentaje_zona_verde
densidad_poblacion
superficie_urbanizada
```

## Variables derivadas

```txt
LST = Land Surface Temperature
NDVI = índice de vegetación
NDBI = índice de urbanización
anomalía_temperatura
percentil_calor
percentil_baja_renta
percentil_baja_vegetacion
indice_vulnerabilidad_climatica
```

## Métricas

```txt
temperatura_media_superficial
temperatura_maxima_superficial
NDVI_medio
% vegetación
% superficie artificial
población vulnerable expuesta
correlación renta-temperatura
correlación NDVI-temperatura
ranking de barrios vulnerables
```

## Visualizaciones

```txt
Mapa de temperatura superficial
Mapa NDVI
Mapa de vulnerabilidad climática
Scatter renta vs temperatura
Scatter vegetación vs temperatura
Ranking barrios/municipios
Dashboard Streamlit
Mapa Kepler.gl
Artículo Quarto tipo data storytelling
```

## Carpeta sugerida

```txt
06_proyectos/08_calor_islas_urbanas_satellite/
```

---

# 2. Fuentes principales por tipo de acceso

## 2.1 Open source / gratuito / registro gratuito

| Fuente | Registro | Coste | API | Uso principal |
|---|---:|---:|---:|---|
| Copernicus Data Space | Sí | Gratis base | Sí | Sentinel-1/2/3/5P |
| Copernicus Browser | Sí | Gratis | Visual/API indirecta | Exploración visual |
| STAC API | Depende | Gratis | Sí | Búsqueda de escenas |
| openEO | Sí | Gratis con límites | Sí | Procesamiento cloud |
| NASA Earthdata | Sí | Gratis | Sí | MODIS, VIIRS, clima |
| NASA FIRMS | Sí para API key | Gratis | Sí | Incendios activos |
| USGS EarthExplorer | Sí | Gratis | Sí | Landsat histórico |
| Microsoft Planetary Computer | Sí | Gratis / condiciones | Sí | STAC, cloud-native geo |
| Google Earth Engine | Sí | Gratis con condiciones | Sí | Procesamiento masivo |
| OpenAerialMap | No/Sí | Gratis | Sí | Imágenes aéreas abiertas |
| OpenStreetMap | No | Gratis | Sí | Edificios, carreteras, zonas verdes |
| OpenAQ | Sí/No | Gratis con límites | Sí | Calidad del aire |
| AEMET OpenData | Sí | Gratis | Sí | Meteorología España |
| MITECO | No/Sí | Gratis | Depende | Agua, aire, incendios |
| EGMS | Sí | Gratis | Descarga/API | Movimiento del terreno |

---

## 2.2 Free tier / pago opcional / profesional

| Fuente | Registro | Coste | API | Uso principal |
|---|---:|---:|---:|---|
| Sentinel Hub | Sí | Free tier + pago | Sí | Imágenes procesadas |
| Mapbox | Sí | Free tier + pago | Sí | Mapas web, tiles, geocoding |
| CARTO | Sí | Comercial / trial | Sí | Geospatial analytics |
| Planet | Sí | Pago | Sí | Alta frecuencia / alta resolución |
| Maxar | Sí | Pago enterprise | Sí según contrato | Muy alta resolución |
| Airbus | Sí | Pago enterprise | Sí según contrato | Muy alta resolución |
| BlackSky | Sí | Pago enterprise | Sí según contrato | Monitorización frecuente |

---

# 3. Copernicus Data Space: fuente principal europea

Copernicus Data Space debería ser la fuente principal para empezar porque centraliza el acceso a datos Sentinel y servicios de búsqueda, descarga, visualización y procesamiento.

## Qué usar dentro de Copernicus

### A. Copernicus Browser

Para empezar visualmente.

Sirve para:

- buscar imágenes Sentinel por zona y fecha;
- ver nubosidad;
- comparar fechas;
- previsualizar bandas;
- hacer índices tipo NDVI o NBR;
- exportar imágenes.

Útil para exploración manual antes de automatizar.

### B. STAC API

STAC significa `SpatioTemporal Asset Catalog`. Es una especificación JSON para describir datos geoespaciales por espacio, tiempo y assets.

Con STAC puedes hacer:

```txt
buscar imágenes Sentinel-2
filtrar por bbox
filtrar por fecha
filtrar por nubosidad
obtener URLs de bandas
descargar o leer COGs
```

Librerías Python:

```txt
pystac-client
odc-stac
stackstac
rasterio
rioxarray
xarray
geopandas
```

### C. openEO

Muy bueno si quieres procesar en la nube sin bajarte escenas enormes.

Sirve para:

- crear datacubes;
- filtrar zona/fecha;
- calcular NDVI;
- hacer composites temporales;
- procesar Sentinel sin descargar todo localmente;
- exportar resultados.

Ideal para proyectos más serios de Copernicus.

### D. Sentinel Hub

Más orientado a producto/API profesional.

Sirve para:

- pedir imágenes procesadas por API;
- generar true color, false color, NDVI, NBR, etc.;
- descargar recortes por AOI;
- usar evalscripts;
- evitar gestionar todas las bandas manualmente.

Puede tener costes si haces uso intensivo, pero es muy bueno para prototipos profesionales.

---

# 4. Satélites y sensores por agencia / programa

## 4.1 Europa — Copernicus / ESA

### Sentinel-1

Tipo:

```txt
Radar SAR
Microondas
Funciona de noche
Atraviesa nubes
```

Usos:

```txt
inundaciones
movimientos del terreno
subsidencia
deslizamientos
terremotos
deformación del suelo
humedad del suelo
daños por desastre
infraestructuras
detección de agua
```

Datos necesarios para análisis:

```txt
Sentinel-1 GRD
Sentinel-1 SLC
polarización VV/VH
fecha pre-evento
fecha post-evento
órbita ascendente/descendente
ángulo de incidencia
AOI
```

Proyectos:

```txt
10_inundaciones_sentinel1
12_movimientos_terreno_egms
13_damage_assessment_cv
```

---

### Sentinel-2

Tipo:

```txt
Óptico multiespectral
13 bandas
10m / 20m / 60m
Visible + NIR + SWIR
```

Es el satélite más útil para empezar.

Usos:

```txt
NDVI
vegetación
incendios
NBR
sequía
agua
crecimiento urbano
clasificación de suelo
detección de cambios
computer vision multibanda
```

Bandas clave:

```txt
B02 Blue
B03 Green
B04 Red
B08 NIR
B11 SWIR
B12 SWIR
```

Índices:

```txt
NDVI = (NIR - RED) / (NIR + RED)
NBR = (NIR - SWIR) / (NIR + SWIR)
NDWI = índice de agua
NDBI = índice urbano
```

Proyectos:

```txt
08_calor_islas_urbanas_satellite
09_incendios_ndvi_nbr
13_damage_assessment_cv
```

---

### Sentinel-3

Tipo:

```txt
Óptico / térmico / oceanografía
Escala regional/global
```

Usos:

```txt
temperatura superficial
océanos
color del agua
incendios
vegetación global
clima
```

No empezaría por aquí, pero es útil para escala grande.

---

### Sentinel-5P

Tipo:

```txt
Atmósfera
Contaminantes
Gases
```

Usos:

```txt
NO2
SO2
CO
O3
CH4
aerosoles
formaldehído
contaminación urbana
nubes de gas
episodios industriales
calidad del aire
```

Proyecto posible:

> Cómo cambia la contaminación del aire en Madrid antes/durante/después de episodios concretos.

Proyectos:

```txt
11_calidad_aire_sentinel5p
contaminacion_urbana_madrid
nubes_gas_eventos_industriales
```

---

## 4.2 NASA / NOAA / USGS

### Landsat 5 / 7 / 8 / 9

Tipo:

```txt
Óptico + térmico
Serie histórica larga
Resolución media
```

Landsat es clave porque tiene una serie histórica muy larga. Es especialmente útil para estudiar cambios desde los años 80/90.

Usos:

```txt
evolución urbana histórica
temperatura superficial terrestre
islas de calor
cambios de uso del suelo
sequía
vegetación
incendios
```

Especialmente útil para:

```txt
análisis histórico de años
comparativas 1990-2000-2010-2020
LST urbana
```

Proyectos:

```txt
08_calor_islas_urbanas_satellite
expansion_urbana_madrid
evolucion_vegetacion_historica
```

---

### MODIS

Tipo:

```txt
Resolución más baja
Alta frecuencia temporal
Serie histórica
```

Usos:

```txt
vegetación global
temperatura
incendios
aerosoles
cobertura nieve
clima
```

Útil cuando importa más la serie temporal que el detalle espacial.

---

### VIIRS

Tipo:

```txt
Observación global
Alta frecuencia
Incendios y luces nocturnas
```

Usos:

```txt
incendios activos
luces nocturnas
actividad humana
eventos extremos
```

Proyecto:

```txt
14_firms_incendios_activos
```

---

### NASA FIRMS

Tipo:

```txt
Incendios activos
Anomalías térmicas
MODIS / VIIRS
```

Usos:

```txt
focos activos
cronología de incendios
detección casi real-time
cruce con perímetros y vegetación
```

Variables:

```txt
latitude
longitude
acq_date
acq_time
satellite
instrument
confidence
frp
brightness
```

---

# 5. Otras fuentes de imágenes satelitales y geoespaciales

## 5.1 NASA Earthdata

Fuente enorme para datos de observación de la Tierra.

Útil para:

```txt
incendios activos
temperatura
cobertura nubosa
aerosoles
clima global
vegetación
océanos
nieve
atmósfera
```

---

## 5.2 USGS EarthExplorer / Landsat

Muy útil para:

```txt
evolución urbana desde los años 80/90
temperatura superficial
cambios de uso del suelo
sequía
vegetación
incendios
```

Landsat 8/9 tiene bandas térmicas muy útiles para estudiar islas de calor urbanas.

---

## 5.3 Google Earth Engine

Muy potente para procesar sin descargar.

Ventajas:

```txt
no descargas todo
procesas en la nube
muy bueno para prototipos
miles de datasets listos
API Python y JavaScript
```

Desventajas:

```txt
depende de plataforma
uso comercial puede tener condiciones/coste
menos control local
```

---

## 5.4 Microsoft Planetary Computer

Muy bueno para Python + STAC + notebooks.

Tiene datos tipo:

```txt
Sentinel
Landsat
MODIS
NAIP
DEM
clima
land cover
```

Lo usaría mucho para aprender STAC y cloud-native geospatial.

---

## 5.5 OpenAerialMap

Más orientado a imágenes aéreas abiertas.

Útil para:

```txt
alta resolución
zonas concretas
mapeo humanitario
post-desastre
```

---

# 6. Datos por fenómeno de análisis

## 6.1 Vegetación

Fuentes:

```txt
Sentinel-2
Landsat
MODIS
Copernicus Land
Google Earth Engine
Microsoft Planetary Computer
```

Variables:

```txt
B04 Red
B08 NIR
B11 SWIR
fecha
nubosidad
AOI
uso del suelo
```

Índices:

```txt
NDVI
EVI
SAVI
NDWI
```

Preguntas:

```txt
¿Dónde se ha perdido vegetación?
¿Cómo se recupera una zona tras un incendio?
¿Qué barrios tienen menos cobertura vegetal?
¿Dónde aumenta el estrés hídrico?
```

---

## 6.2 Incendios

Fuentes:

```txt
Sentinel-2
NASA FIRMS
MODIS
VIIRS
MITECO incendios
Copernicus EMS
```

Variables:

```txt
NDVI pre/post
NBR pre/post
dNBR
focos activos
perímetro incendio
fecha inicio
fecha fin
superficie afectada
```

Preguntas:

```txt
¿Cuánta vegetación se perdió?
¿Qué severidad tuvo el incendio?
¿Cómo evoluciona la recuperación?
¿Qué infraestructuras estaban cerca?
```

---

## 6.3 Temperatura / calor urbano

Fuentes:

```txt
Landsat 8/9 térmico
Sentinel-3
AEMET
Copernicus Climate
Google Earth Engine
```

Variables:

```txt
banda térmica
temperatura máxima AEMET
temperatura mínima AEMET
LST
NDVI
NDBI
renta
edad
densidad
zonas verdes
```

Preguntas:

```txt
¿Dónde hay más isla de calor?
¿Coincide el calor con menor renta?
¿Qué zonas tienen baja vegetación y alta temperatura?
¿Qué población vulnerable queda expuesta?
```

---

## 6.4 Calidad del aire / contaminación

Fuentes:

```txt
Sentinel-5P
CAMS
OpenAQ
MITECO
Ayuntamiento de Madrid
AEMET
```

Variables:

```txt
NO2
PM2.5
PM10
O3
SO2
CO
viento
temperatura
tráfico
estación
fecha/hora
```

Preguntas:

```txt
¿Qué zonas respiran peor aire?
¿Cómo cambia el NO2 según tráfico y viento?
¿Coinciden estaciones de tierra y satélite?
¿Qué barrios tienen más exposición?
```

---

## 6.5 Gases / nubes contaminantes

Fuentes:

```txt
Sentinel-5P
CAMS
NASA Earthdata
NOAA
```

Variables:

```txt
NO2
SO2
CO
CH4
O3
aerosoles
dirección viento
altura columna
fecha/hora
```

Preguntas:

```txt
¿Se detectan episodios anómalos de gases?
¿Cómo se mueve una nube contaminante?
¿Qué zonas quedan bajo una pluma de contaminación?
```

---

## 6.6 Inundaciones

Fuentes:

```txt
Sentinel-1
Sentinel-2
AEMET precipitación
Copernicus EMS
OSM
DEM
```

Variables:

```txt
backscatter pre/post
máscara de agua
precipitación acumulada
ríos
pendiente
edificios
carreteras
población
```

Preguntas:

```txt
¿Qué superficie se inundó?
¿Qué infraestructuras quedaron afectadas?
¿Qué población estaba expuesta?
```

---

## 6.7 Movimientos del terreno / subsidencia

Fuentes:

```txt
Sentinel-1
EGMS
geología
OSM infraestructuras
CNIG
```

Variables:

```txt
velocidad mm/año
desplazamiento acumulado
serie temporal
coordenadas
calidad de punto
infraestructuras cercanas
```

Preguntas:

```txt
¿Qué zonas se hunden o deforman?
¿Hay infraestructuras críticas expuestas?
¿Qué municipios tienen mayor subsidencia?
```

---

## 6.8 Terremotos y daños

Fuentes:

```txt
IGN catálogo sísmico
USGS Earthquake API
EMSC
Sentinel-1
Sentinel-2
Copernicus EMS
OpenStreetMap
xBD / xView2
QuakeSet
```

Variables:

```txt
magnitud
profundidad
epicentro
fecha
intensidad
edificios
carreteras
imágenes pre/post
máscaras de daño
```

Preguntas:

```txt
¿Dónde ocurrió el terremoto?
¿Qué población/infraestructura estaba expuesta?
¿Puede observarse daño pre/post con satélite?
```

---

# 7. Calidad del aire y atmósfera

## 7.1 Sentinel-5P

Para contaminantes atmosféricos desde satélite:

```txt
NO2
SO2
CO
ozono
aerosoles
metano
```

Bueno para:

- ver contaminación urbana;
- comparar antes/después de confinamientos/eventos;
- mapas regionales;
- calidad del aire a escala amplia;
- nubes de gas.

---

## 7.2 Copernicus Atmosphere Monitoring Service — CAMS

CAMS da modelos y reanálisis de atmósfera/calidad del aire.

Útil para:

```txt
NO2
PM2.5
PM10
ozono
polvo
aerosoles
predicción calidad aire
```

---

## 7.3 OpenAQ

OpenAQ ofrece una API global de calidad del aire. Sirve más para datos de estaciones en tierra, complementando satélite.

Proyecto potente:

> ¿Coinciden las mediciones de estaciones urbanas con la señal satelital de contaminación?

---

## 7.4 AEMET / MITECO / Comunidad de Madrid

Para España, mejor combinar:

```txt
MITECO calidad del aire
AEMET meteorología
red autonómica de calidad del aire
Sentinel-5P
CAMS
```

---

# 8. Datasets históricos y actuales

## 8.1 Por qué necesitamos histórico y dato actual

Para hacer análisis serio no basta con una imagen aislada. Necesitamos:

```txt
datos actuales
+
datos históricos
+
contexto territorial
+
variables sociales/económicas
```

### Dato actual

Sirve para:

```txt
diagnóstico reciente
eventos extremos
incendios activos
calor actual
contaminación actual
monitorización
```

### Dato histórico

Sirve para:

```txt
tendencias
comparativa interanual
anomalías
predicción
modelos temporales
antes/después
impacto acumulado
```

---

## 8.2 Datasets históricos recomendados

| Fenómeno | Fuente histórica | Uso |
|---|---|---|
| Urbanización | Landsat histórico | crecimiento urbano |
| Vegetación | Landsat / MODIS / Sentinel-2 | pérdida/recuperación vegetal |
| Incendios | NASA FIRMS / MITECO | frecuencia y severidad |
| Calor | Landsat térmico / AEMET | islas de calor y olas |
| Calidad aire | MITECO / estaciones / OpenAQ | exposición histórica |
| Contaminantes atmosféricos | Sentinel-5P / CAMS | NO2, aerosoles, gases |
| Agua/sequía | MITECO / AEMET / Copernicus | estrés hídrico |
| Movimientos terreno | EGMS / Sentinel-1 | subsidencia acumulada |
| Terremotos | IGN / USGS / EMSC | actividad sísmica |
| Daños desastre | xBD / xView2 / Copernicus EMS | entrenamiento CV |

---

# 9. Datasets etiquetados para computer vision

Para entrenar modelos no basta con descargar imágenes. Hace falta:

```txt
imagen
+
label / máscara / bounding box / clase / daño
```

## 9.1 EuroSAT

Uso:

```txt
clasificación de parches Sentinel-2
land cover
CNNs básicas
transfer learning
```

Nivel:

```txt
Inicial
```

---

## 9.2 BigEarthNet

Uso:

```txt
clasificación multietiqueta
Sentinel-2
land cover
benchmark serio
```

Nivel:

```txt
Intermedio
```

---

## 9.3 SEN12MS

Uso:

```txt
Sentinel-1 + Sentinel-2
SAR + óptico
clasificación
segmentación
fusión de sensores
```

Nivel:

```txt
Intermedio / avanzado
```

---

## 9.4 xBD / xView2

Uso:

```txt
detección de edificios
clasificación de daños
before/after
desastres naturales
huracanes
terremotos
inundaciones
incendios
```

Nivel:

```txt
Avanzado
```

---

## 9.5 SpaceNet

Uso:

```txt
detección de edificios
detección de carreteras
segmentación urbana
alta resolución
```

Nivel:

```txt
Avanzado
```

---

## 9.6 QuakeSet

Uso:

```txt
terremotos
Sentinel-1
SAR
daños/severidad
monitorización post-desastre
```

Nivel:

```txt
Avanzado
```

---

## 9.7 TorchGeo

TorchGeo es una librería útil para trabajar con datasets geoespaciales en PyTorch.

Sirve para:

```txt
cargar datasets remote sensing
entrenar modelos
usar benchmarks
hacer segmentación
hacer clasificación
```

Para `open-data-lab`, TorchGeo debería entrar en fase avanzada.

---

# 10. APIs principales

## 10.1 APIs abiertas / oficiales

| API | Registro | Coste | Uso |
|---|---:|---:|---|
| Copernicus STAC | Sí | Gratis | búsqueda de productos |
| Copernicus OData | Sí | Gratis | descarga de productos |
| openEO | Sí | Gratis con límites | procesamiento cloud |
| NASA Earthdata API | Sí | Gratis | datos NASA |
| NASA FIRMS API | Sí | Gratis | incendios |
| USGS M2M API | Sí | Gratis | Landsat |
| OpenAQ API | Sí/No | Gratis | calidad aire |
| AEMET OpenData | Sí | Gratis | meteorología |
| USGS Earthquake API | No/Sí | Gratis | terremotos |
| OSM Overpass API | No | Gratis con límites | geometrías OSM |

---

## 10.2 APIs con free tier / pago

| API | Registro | Coste | Uso |
|---|---:|---:|---|
| Sentinel Hub API | Sí | Free tier / pago | imágenes procesadas |
| Mapbox API | Sí | Free tier / pago | mapas/geocoding |
| CARTO APIs | Sí | Comercial/trial | geospatial analytics |
| Planet API | Sí | Pago | alta resolución |
| Maxar APIs | Sí | Pago | muy alta resolución |
| Google Earth Engine API | Sí | gratis con condiciones / comercial | procesamiento cloud |

---

# 11. Proyectos recomendados para Open Data Lab

## 11.1 Calor e islas de calor urbanas en Madrid

Carpeta:

```txt
06_proyectos/08_calor_islas_urbanas_satellite/
```

Pregunta:

> ¿Qué zonas de Madrid acumulan más calor y cómo se relaciona con renta, vegetación y densidad urbana?

Datos:

```txt
Landsat 8/9 térmico
Sentinel-2 vegetación
INE Atlas de Renta
AEMET temperaturas
Ayuntamiento / CNIG geometrías
OSM zonas verdes
```

Métricas:

```txt
LST
NDVI
NDBI
% vegetación
renta media
población mayor de 65
índice de vulnerabilidad climática
```

Visualización:

```txt
mapa LST
mapa NDVI
scatter renta vs temperatura
ranking barrios vulnerables
Kepler.gl / Streamlit
```

Nivel:

```txt
medio-alto
muy buen post de portfolio
```

---

## 11.2 Incendios: antes/después con NDVI/NBR

Carpeta:

```txt
06_proyectos/09_incendios_ndvi_nbr/
```

Pregunta:

> ¿Cuánta vegetación se perdió tras un incendio y cómo se recupera con el tiempo?

Datos:

```txt
Sentinel-2 L2A
perímetro de incendio
Copernicus Land
NASA FIRMS
MITECO incendios
```

Métricas:

```txt
NDVI pre/post
NBR pre/post
dNBR = severidad de incendio
superficie quemada
recuperación vegetal
```

Visualización:

```txt
before/after
mapa dNBR
serie temporal NDVI
clasificación severidad
```

Nivel:

```txt
muy bueno para portfolio geoespacial
```

---

## 11.3 Inundaciones con Sentinel-1

Carpeta:

```txt
06_proyectos/10_inundaciones_sentinel1/
```

Pregunta:

> ¿Qué superficie quedó inundada tras un episodio extremo?

Datos:

```txt
Sentinel-1 GRD antes/después
perímetro administrativo
DEM / pendientes
ríos
precipitación AEMET
```

Métricas:

```txt
cambio backscatter
máscara de inundación
superficie afectada
infraestructuras cercanas
población expuesta
```

Visualización:

```txt
mapa inundación
antes/después
infraestructuras afectadas
```

Nivel:

```txt
avanzado
muy potente
```

---

## 11.4 Movimientos terrestres / subsidencia

Carpeta:

```txt
06_proyectos/12_movimientos_terreno_egms/
```

Pregunta:

> ¿Qué zonas muestran deformación o hundimiento progresivo del terreno?

Datos:

```txt
Sentinel-1 InSAR
Copernicus EGMS
geología / infraestructuras
municipios
```

Fuente clave:

```txt
European Ground Motion Service (EGMS)
```

Métricas:

```txt
velocidad mm/año
desplazamiento acumulado
zonas de subsidencia
infraestructuras expuestas
```

Nivel:

```txt
avanzado
muy diferencial
```

---

## 11.5 Calidad del aire Madrid: estaciones vs satélite

Carpeta:

```txt
06_proyectos/11_calidad_aire_sentinel5p/
```

Pregunta:

> ¿Qué zonas respiran peor aire y cómo se relaciona con tráfico, renta y clima?

Datos:

```txt
MITECO calidad aire
Ayuntamiento Madrid estaciones
OpenAQ
Sentinel-5P NO2
AEMET viento/temperatura
OSM carreteras
```

Métricas:

```txt
NO2 medio
PM2.5 medio
días sobre umbral
anomalía contaminación
relación tráfico/renta
```

Visualización:

```txt
mapa estaciones
serie temporal
mapa satelital NO2
ranking zonas
```

Nivel:

```txt
muy bueno para data story + API
```

---

## 11.6 Daños por desastre en infraestructuras

Carpeta:

```txt
06_proyectos/13_damage_assessment_cv/
```

Pregunta:

> ¿Puede detectarse daño en infraestructuras comparando imágenes pre/post desastre?

Datos:

```txt
Sentinel-1
Sentinel-2
xBD / xView2
OpenStreetMap buildings/roads
Copernicus EMS
```

Técnicas:

```txt
change detection
semantic segmentation
building footprint detection
damage classification
SAR + optical fusion
```

Nivel:

```txt
avanzado / computer vision real
```

---

# 12. Stack Python para satélite + computer vision

## 12.1 Librerías recomendadas

```txt
pystac-client
planetary-computer
stackstac
odc-stac
rasterio
rioxarray
xarray
geopandas
shapely
pyproj
folium
leafmap
geemap
earthengine-api
sentinelhub
openeo
torch
torchvision
torchgeo
opencv-python
scikit-image
albumentations
segmentation-models-pytorch
```

## 12.2 Separación por requirements

No instalar todo desde el primer día.

### `requirements-geo.txt`

```txt
geopandas
shapely
pyproj
rasterio
rioxarray
xarray
contextily
osmnx
h3
leafmap
lonboard
```

### `requirements-remote-sensing.txt`

```txt
pystac-client
planetary-computer
stackstac
odc-stac
sentinelhub
openeo
eodag
earthengine-api
geemap
```

### `requirements-cv.txt`

```txt
torch
torchvision
torchgeo
opencv-python
scikit-image
albumentations
segmentation-models-pytorch
```

---

# 13. Qué añadir al repo

## 13.1 Nuevas carpetas de proyectos

```txt
06_proyectos/
├── 08_calor_islas_urbanas_satellite/
├── 09_incendios_ndvi_nbr/
├── 10_inundaciones_sentinel1/
├── 11_calidad_aire_sentinel5p/
├── 12_movimientos_terreno_egms/
└── 13_damage_assessment_cv/
```

## 13.2 Nueva documentación

```txt
04_procesos_data/01_extraccion/
├── copernicus_stac.md
├── sentinelhub_api.md
├── openeo.md
├── google_earth_engine.md
├── nasa_earthdata.md
├── usgs_landsat.md
└── openaq_api.md
```

## 13.3 Nuevo learning track

```txt
12_learning_tracks/04_satellite_remote_sensing/
├── README.md
├── sentinel_2_ndvi.md
├── sentinel_1_sar.md
├── sentinel_5p_air_quality.md
├── landsat_lst_heat.md
├── copernicus_stac.md
├── openeo_datacubes.md
├── rasterio_xarray.md
└── computer_vision_remote_sensing.md
```

---

# 14. Progresión recomendada de aprendizaje

## Nivel 1 — Sentinel-2 NDVI

Proyecto:

```txt
Vegetación e islas de calor en Madrid
```

Aprendes:

```txt
buscar escena
descargar bandas
recortar AOI
calcular NDVI
mapear
```

---

## Nivel 2 — Landsat LST

Proyecto:

```txt
Temperatura superficial por barrio/municipio
```

Aprendes:

```txt
bandas térmicas
land surface temperature
raster zonal statistics
cruce con renta
```

---

## Nivel 3 — Sentinel-1 inundaciones

Proyecto:

```txt
Detección de inundación antes/después
```

Aprendes:

```txt
SAR
backscatter
change detection
máscaras
```

---

## Nivel 4 — Sentinel-5P calidad aire

Proyecto:

```txt
NO2 y calidad del aire en Madrid
```

Aprendes:

```txt
atmósfera
grillas
series temporales
datos satélite + estaciones
```

---

## Nivel 5 — Computer vision

Proyecto:

```txt
Segmentación de edificios / daño post-desastre
```

Aprendes:

```txt
datasets etiquetados
patch extraction
CNN/U-Net
segmentation
before-after
```

---

# 15. Canales recomendados GIS / remote sensing

La imagen compartida recomienda estos canales GIS:

```txt
Esri
QGIS
John Nelson
Qiusheng Wu
Spatial Thoughts
CARTO
Sentinel Hub
Hans van der Kwast
Mundo GIS
MasterGIS
```

Para `open-data-lab`, priorizaría:

| Canal | Tema | Prioridad |
|---|---|---|
| Qiusheng Wu | Python geoespacial, geemap, leafmap, Google Earth Engine | Alta |
| Spatial Thoughts | Análisis espacial, QGIS, Python GIS | Alta |
| Sentinel Hub | Copernicus, Sentinel, APIs, remote sensing | Alta |
| CARTO | Mapas, analytics geoespacial, cloud GIS | Media / Alta |
| QGIS | Base GIS sólida open source | Alta |
| Esri | ArcGIS y GIS profesional | Media |
| John Nelson | Cartografía y diseño visual | Media |
| Hans van der Kwast | SIG y datos abiertos | Media |
| Mundo GIS | GIS práctico | Media |
| MasterGIS | Formación GIS | Media |

Prioridad personal para empezar:

```txt
1. Qiusheng Wu
2. Spatial Thoughts
3. Sentinel Hub
4. QGIS
5. CARTO
```

---

# 16. Checklist de implementación

```txt
[ ] Crear carpeta 12_learning_tracks/04_satellite_remote_sensing/
[ ] Añadir este documento a 10_referencias/
[ ] Crear requirements-remote-sensing.txt
[ ] Crear requirements-cv.txt
[ ] Crear proyecto 08_calor_islas_urbanas_satellite/
[ ] Crear notebook 01_exploracion_copernicus_browser.md
[ ] Crear notebook 02_stac_sentinel2_ndvi.ipynb
[ ] Crear notebook 03_landsat_lst_madrid.ipynb
[ ] Crear README con pregunta, fuentes y metodología
[ ] Añadir fuentes al catalogo_datasets.csv
[ ] Añadir APIs al catalogo_apis.csv
[ ] Añadir canales GIS a 10_referencias/
```

---

# 17. Resumen de decisión

La ruta recomendada para `open-data-lab` es:

```txt
1. Copernicus Browser para exploración visual.
2. STAC API con pystac-client para búsqueda programática.
3. Sentinel-2 NDVI para vegetación/incendios.
4. Landsat térmico para islas de calor.
5. AEMET / MITECO / OpenAQ para clima y calidad del aire.
6. Sentinel-1 para inundaciones y movimiento.
7. EGMS para subsidencia.
8. EuroSAT / SEN12MS / xBD / SpaceNet / QuakeSet para computer vision.
```

Primer proyecto satelital:

> **Calor y desigualdad en Madrid: temperatura superficial, vegetación y renta por barrios/municipios.**

Este proyecto es ideal porque une datos sociales, satélite, medioambiente, GIS, Python y storytelling en una investigación potente y útil.

Además queda perfecto para demostrar que el laboratorio no es solo BI o visualización, sino una plataforma personal para aprender extracción de datos, APIs, pipelines, geoespacial, teledetección, modelos y productos de datos.
