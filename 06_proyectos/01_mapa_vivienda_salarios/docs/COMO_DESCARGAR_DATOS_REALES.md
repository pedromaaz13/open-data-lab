# Cómo traer los datos oficiales (paso a paso)

Guía para descargar los datos reales y sustituir los sintéticos. **Esto se hace en
tu ordenador** (en el entorno cloud del laboratorio la red a INE/Madrid está
bloqueada). No necesitas saber programar mucho: la mayoría es descargar ficheros.

> Regla de oro del laboratorio: el fichero que descargas se guarda **tal cual** en
> `data/raw/` y NO se toca a mano. La limpieza la hace el código.

---

## 0. Preparar tu máquina (una vez)

```bash
git clone https://github.com/pedromaaz13/open-data-lab.git
cd open-data-lab
python -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 1. Renta por barrio/distrito → INE (Atlas de Renta)

**Qué es:** el *Atlas de Distribución de Renta de los Hogares (ADRH)* del INE da la
**renta media por hogar y por persona** a nivel de municipio, distrito y sección
censal. Es la mejor fuente oficial de renta a escala pequeña.

**Dónde:**
- Página del Atlas: <https://www.ine.es/experimental/atlas/experimental_atlas.htm>
- Operación ADRH (tablas): busca en <https://www.ine.es> → "Atlas de distribución
  de renta de los hogares".

**Cómo descargar (opción fácil, sin código):**
1. Entra en la página del Atlas.
2. Selecciona **Madrid municipio (28079)** y el nivel **distritos** (o barrios/
   secciones).
3. Elige el indicador **"Renta neta media por hogar"** (y, si quieres, "por persona").
4. Pulsa **Descargar → CSV** (o Excel).
5. Guarda el fichero en `06_proyectos/01_mapa_vivienda_salarios/data/raw/`.

**Cómo descargar (opción con API, para automatizar):**
- El INE tiene una API JSON. El patrón es:
  `https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/{ID_TABLA}`
- El `{ID_TABLA}` lo ves en la URL de la tabla en la web del INE (aparece como
  `t=NNNNN`). Cópialo y úsalo en `src/extract.py` (función `descargar_renta_ine`,
  marcada con `TODO`).

---

## 2. Alquiler €/m² → Mº Vivienda / Ayuntamiento de Madrid

**Opción A — Sistema Estatal de Índices de Alquiler (Mº Vivienda):**
- <https://www.mivau.gob.es/vivienda/alquiler/indice-alquiler>
- Da precios de referencia del alquiler por zona/sección. Descarga el CSV de Madrid.

**Opción B — Ayuntamiento de Madrid (datos abiertos):**
- <https://datos.madrid.es> → buscador → "precio alquiler vivienda" o "vivienda".
- Descarga el CSV y guárdalo en `data/raw/`.

---

## 3. Compra €/m² → Ayuntamiento de Madrid / portales

- <https://datos.madrid.es> → buscar "precio vivienda" / "compraventa".
- Alternativa nacional por municipio (no barrio): Mº Vivienda, "Precio de vivienda".
- ⚠️ El precio de **compra por barrio** tiene cobertura oficial más débil que el de
  alquiler; si no lo encuentras por barrio, empieza solo con alquiler.

---

## 4. Geometría de los barrios (para el mapa) → Ayto. Madrid

- <https://datos.madrid.es> → buscar "barrios" o "distritos" → descarga el
  **GeoJSON** o Shapefile de barrios.
- Guárdalo como `data/raw/madrid_barrios.geojson`.

---

## 5. Unir todo y generar el dataset

Una vez tengas los CSV en `data/raw/`, hay que **unirlos por el código de barrio**
(`cod_barrio`) y calcular los indicadores. El esqueleto ya existe:

1. Abre `src/extract.py` y pega las URLs reales que verificaste (quita los `TODO`).
2. Crea una función que cargue los CSV de `data/raw/`, los una por `cod_barrio` y
   deje un DataFrame con estas columnas mínimas:
   `cod_distrito, distrito, cod_barrio, barrio, renta_hogar, alquiler_eur_m2_mes, precio_compra_eur_m2`
3. Pásalo por `transform.add_indicators(df)` y guárdalo:
   ```python
   df.to_csv("data/processed/madrid_barrios.csv", index=False)
   ```
4. En el notebook, cambia `SOURCE = 'real'` y ejecútalo entero.

> Truco: como el pipeline ya funciona con datos sintéticos que tienen exactamente
> esas columnas, solo tienes que conseguir que tus datos reales tengan **los mismos
> nombres de columna**. Lo demás (indicadores, gráficos, mapa) sale solo.

---

## 6. El punto delicado: los códigos de barrio

Para cruzar renta + vivienda + geometría, las tres fuentes tienen que compartir el
**mismo código de barrio**. En Madrid:
- El INE usa código de sección censal (agregable a distrito/barrio).
- El Ayto. usa su propio código de barrio (distrito 2 díg. + barrio).

Si los códigos no coinciden, hay que hacer una **tabla de equivalencias** una vez.
Es la parte que más cuesta de un proyecto de datos real — y la más importante para
que los números cuadren. (Ver `04_procesos_data/02_transformacion/joins_geograficos.md`.)

---

## ¿Y si quiero que Claude lo descargue por mí?

Tendrías que **abrir la red del entorno** al crear el entorno de Claude Code on the
web (permitir los dominios `*.ine.es` y `datos.madrid.es`). Documentación:
<https://code.claude.com/docs/en/claude-code-on-the-web>. Con la red abierta, el
mismo `src/extract.py` se ejecuta aquí y descargo yo.
