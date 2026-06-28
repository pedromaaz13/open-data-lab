# Plan de datos de vivienda — Madrid por distrito

Objetivo: cruzar lo que **ya tenemos** (renta) con el **coste de la vivienda**
(alquiler y compra) y las **características** (tipo de vivienda y m²) para sacar
análisis muy enriquecedor: dónde se vive mejor o más apurado con el sueldo, y cómo se
relacionan renta, precio y tamaño de la vivienda.

Sigue el método del laboratorio: `00_documentacion/flujo_anadir_fuente_datos.md`
(enlace → `config.py` → `extract.py` → `data/raw` → loader → notebook → test → commit).

## Lo que YA tenemos (no hay que buscar)

Del INE Atlas (en `load_ine.py`), por los 21 distritos de Madrid:
- **Renta neta** media (hogar y persona) ✅
- **Renta bruta** media (hogar y persona) ✅ ← los "ingresos brutos" que mencionas
- **Mediana** de la renta ✅
- Gini, % salario/pensiones, demografía ✅

## Lo que hay que conseguir (bloque vivienda)

| # | Dato | Fuente oficial candidata | Nivel | Dificultad | Qué aporta | Nombre destino |
|---|---|---|---|---|---|---|
| 1 | **Alquiler €/m²/mes** | Sistema Estatal de Índices de Alquiler (Mº Vivienda/MITMA) | sección censal → distrito | media | Esfuerzo de alquiler real | `vivienda_alquiler.csv` |
| 2 | **Tipo de vivienda y m²** | INE · Censo de Población y Viviendas 2021 | sección censal → distrito | media | Superficie media, tipo, régimen (propiedad/alquiler) | `censo_viviendas.csv` |
| 3 | **Compra €/m²** | Mº Vivienda (precio vivienda) / Ayto. Madrid | municipio/distrito | alta | Esfuerzo de compra real | `vivienda_compra.csv` |
| 4 | **m²/antigüedad** (alternativa) | Catastro (estadísticas catastrales) | municipio/distrito | media | Superficie y antigüedad de la edificación | `catastro_madrid.csv` |
| 5 | **Geometría distritos** | Ayto. Madrid (GeoJSON) | distrito | baja | El mapa | `distritos_madrid.geojson` |

> Realismo: a nivel **distrito**, el dato de vivienda es más escaso que la renta. El
> **alquiler** tiene buena cobertura sub-municipal (índice estatal); la **compra por
> distrito** es lo más difícil de encontrar oficial (puede que solo haya municipio, o
> fuentes no oficiales tipo Idealista/Fotocasa — se documentarían como tales).

## El análisis enriquecido que saldrá

Cruzando renta × vivienda × características:

- **Esfuerzo de alquiler** = alquiler anual / renta del hogar → % del sueldo en vivienda.
- **Esfuerzo de compra** = precio vivienda tipo / renta → años de renta para comprar.
- **€/m² vs renta** → ¿dónde la vivienda está más "cara" en relación al sueldo?
- **Tamaño vs precio** → ¿se paga más por menos m² en unos distritos que en otros?
- **Régimen de tenencia** → ¿distritos de propietarios vs de inquilinos?
- **Mapa del esfuerzo** → coroplético de "dónde se vive mejor con el sueldo".
- **Renta bruta vs neta** → peso de impuestos por distrito (ya tenemos ambas).

## Orden recomendado

1. **Geometría** (mapa) — rápido, usa la renta que ya hay. *Siguiente inmediato.*
2. **Alquiler** — el esfuerzo del día a día; mejor cobertura oficial sub-municipal.
3. **Tipo de vivienda y m²** (Censo 2021) — perfil de vivienda por distrito, muy rico.
4. **Compra** — el más difícil de cerrar oficial; se ataca al final.

## Flujo por cada fuente (recordatorio)

```txt
1. Buscar el dataset y copiar la URL directa de descarga
2. Documentar en config.py (FUENTES) y 09_data_catalog/
3. Añadir la URL a src/extract.py
4. python src/extract.py  ->  data/raw/
5. Loader que limpia y filtra Madrid (src/load_*.py)
6. Cruzar con la renta por cod_distrito en el notebook
7. Test del loader + commit (solo código)
```

## Checklist

- [ ] 5. Geometría de distritos (mapa)
- [ ] 1. Alquiler €/m²
- [ ] 2. Tipo de vivienda y m² (Censo 2021)
- [ ] 3. Compra €/m²
- [ ] 4. Catastro (m²/antigüedad) — opcional
- [ ] Cruce final renta × vivienda → esfuerzo + mapa + artículo
