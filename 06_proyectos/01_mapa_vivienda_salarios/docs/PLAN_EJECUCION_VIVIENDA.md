# Plan de ejecución — bloque vivienda (renta vs alquiler/compra)

Objetivo: cruzar la renta (ya la tenemos) con el **coste de la vivienda** para
responder *"¿qué supone ese gasto para cada renta?"* — esfuerzo de alquiler y de
compra, y el mapa de dónde se vive mejor o más apurado.

Trabajamos en **loop**: una iteración por fuente, siempre con el mismo método
(`00_documentacion/flujo_anadir_fuente_datos.md`):

```txt
buscar dataset → URL → documentar → extract.py → data/raw → loader → cruzar con renta → visual + conclusión → test → commit
```

> La lógica de los indicadores **ya existe** (`src/indicators.py`:
> `esfuerzo_alquiler_pct`, `esfuerzo_compra_anios`, `clasifica_esfuerzo_alquiler`).
> Solo hay que enchufar los datos reales.

## Iteración 1 — Alquiler €/m²  *(siguiente)*

- **Fuente:** Sistema Estatal de Índices de Alquiler de Vivienda (Mº Vivienda / MITMA).
- **Pasos:** localizar el dataset por distrito/sección de Madrid → copiar URL →
  añadir a `extract.py` (`vivienda_alquiler...`) → loader `load_vivienda.py` que
  filtra Madrid y deja `alquiler_eur_m2_mes` por distrito.
- **Cruce:** `esfuerzo_alquiler_pct(alquiler, renta_hogar, superficie)`.
- **Desbloquea:** % del sueldo en alquiler + clasificación (holgado/ajustado/apurado).

## Iteración 2 — Tipo de vivienda y m²  (Censo 2021)

- **Fuente:** INE · Censo de Población y Viviendas 2021 (superficie, tipo, régimen).
- **Desbloquea:** usar la **superficie real** (en vez de asumir 70/90 m²) y el
  **régimen de tenencia** (propiedad vs alquiler) por distrito.

## Iteración 3 — Compra €/m²

- **Fuente:** Mº Vivienda (precio de vivienda) / Ayto. Madrid. (La más difícil de
  cerrar oficial a nivel distrito; documentar limitaciones si solo hay municipio.)
- **Cruce:** `esfuerzo_compra_anios(precio, renta_hogar, superficie)`.
- **Desbloquea:** años de renta para comprar.

## Iteración 4 — Notebook 04: el esfuerzo real

- `notebooks/04_madrid_distritos_esfuerzo.ipynb`:
  - une renta (load_ine) + alquiler/compra (load_vivienda) por distrito,
  - calcula esfuerzo de alquiler (%) y de compra (años),
  - **mapa del esfuerzo** (Folium/Kepler) — dónde se vive apurado,
  - ranking, €/m² vs renta, y conclusiones,
  - tests del loader de vivienda.

## (Opcional) Iteración 5 — Idealista API

- Solo **con permiso** y vía su **API** (no scraping masivo). Respetar ToS.
- Aporta precios finos y descripción de inmuebles si las fuentes oficiales no bastan.

## Checklist del loop

- [ ] 1. Alquiler €/m² (extract + loader + cruce)
- [ ] 2. Tipo + m² (Censo 2021)
- [ ] 3. Compra €/m²
- [ ] 4. Notebook 04 — esfuerzo + mapa + conclusiones
- [ ] 5. (opcional) Idealista API con permiso
