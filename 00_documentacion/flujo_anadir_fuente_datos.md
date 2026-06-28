# Cómo añadir una fuente de datos (flujo del laboratorio)

Este es el **método estándar** del Open Data Lab para incorporar cualquier fuente de
datos nueva (INE, Ayuntamientos, Mº Vivienda, Eurostat...). Es el flujo que se sigue
en todos los proyectos, probado con la renta del INE en
`06_proyectos/01_mapa_vivienda_salarios`.

## Principio de oro

> **El código va al repo. Los datos NO.**
> Los datos se quedan en `data/raw/` (local, ignorado por git) y son **reproducibles**:
> cualquiera ejecuta el extractor y los vuelve a obtener. No se suben ficheros de datos
> al repositorio (engordan, caducan y dan errores de tamaño).

```txt
Fuente oficial → enlace de descarga → extractor (código) → data/raw → loader → data/processed → análisis
       (web)            (URL)            extract.py        (crudo)    load_*.py    (limpio)       (notebook)
```

## Los 7 pasos

### 1. Encontrar la fuente y el enlace EXACTO de descarga
- Localiza el dataset en el portal oficial (ver `03_fuentes_oficiales/`).
- Consigue la **URL directa de descarga** (no la página de inicio):
  clic derecho en el botón *Descargar* → **"Copiar dirección del enlace"**.
- Si no hay URL directa, anota el procedimiento de descarga manual.

### 2. Documentar la fuente
- Apúntala en `src/config.py` (diccionario `FUENTES`: organismo, dataset, URL).
- Regístrala en `09_data_catalog/` (`catalogo_datasets.csv` / `catalogo_apis.csv`).
- Anota fecha de consulta y licencia (ver `00_documentacion/trazabilidad_fuentes.md`).

### 3. Añadir la URL al extractor (`src/extract.py`)
- Mete el enlace en el diccionario de descargas con un **nombre de fichero limpio**:
  ```python
  URLS = {
      "ine_renta_media_mediana.csv": "https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/31097.csv?nocab=1",
      # nueva_fuente.csv: "https://...",
  }
  ```

### 4. Ejecutar el extractor → `data/raw/`
- En tu máquina (con internet):
  ```bash
  python src/extract.py
  ```
- Descarga los ficheros **crudos** a `data/raw/`. Ese crudo **no se toca a mano**.

### 5. Escribir el loader (`src/load_*.py`)
- Función que lee el crudo, **traduce** su formato al del proyecto y limpia:
  encoding correcto, parseo de números, filtros (p. ej. solo Madrid), pivotado.
- Salida a `data/processed/` (Parquet/CSV) o directa al notebook.
- Regla: si la lógica se reutiliza, va en `src/`, no copiada en cada notebook.

### 6. Analizar en el notebook
- El notebook **importa** el loader (no descarga nada): extraer una vez, analizar mil.
- Gráficos, mapas, métricas, y opcionalmente capa **DuckDB** para consultar con SQL.

### 7. Validar y subir (solo el código)
- Añade un **test** del loader (con un mock que imite el formato real).
- `git add` solo del **código** (extractor, loader, tests, notebook). Los datos los
  ignora `.gitignore`.
- Commit + push → el CI valida lint y tests.

## Checklist al añadir una fuente

- [ ] URL directa de descarga conseguida
- [ ] Fuente documentada en `config.py` + `09_data_catalog/`
- [ ] URL añadida a `src/extract.py`
- [ ] `python src/extract.py` descarga el crudo a `data/raw/`
- [ ] Loader que limpia y traduce el formato
- [ ] Notebook que importa el loader y analiza
- [ ] Test del loader (mock con el formato real)
- [ ] Commit del **código** (datos NO) + CI en verde

## Ejemplo real (referencia)

La renta del INE en `06_proyectos/01_mapa_vivienda_salarios`:
- `src/extract.py` → descarga 4 tablas del INE (URLs `jaxiT3`).
- `src/load_ine.py` → limpia el formato largo del INE, filtra los 21 distritos de Madrid.
- `tests/test_load_ine.py` → valida el parseo con un mock.
- `notebooks/02_madrid_distritos_ine_real.ipynb` → análisis real + DuckDB.
- Guía específica de descarga: `docs/COMO_DESCARGAR_DATOS_REALES.md`.
