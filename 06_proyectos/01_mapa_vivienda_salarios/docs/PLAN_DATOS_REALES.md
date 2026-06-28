# Plan de datos reales — Madrid por distritos

Objetivo: enriquecer el proyecto con datos **reales** del INE (Atlas de Distribución
de Renta de los Hogares, ADRH 2023) a nivel de **distrito de Madrid**, y luego añadir
la capa de **vivienda**.

> Todas las descargas van a `06_proyectos/01_mapa_vivienda_salarios/data/raw/`.
> Renombra cada fichero al **nombre destino** de la tabla para que el código lo
> encuentre. Año: **2023**. Formato: **CSV separado por `;`**. Territorio:
> **distritos de Madrid** (códigos que empiezan por `2807901`...`2807921`).

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

## Snippet para inspeccionar cada CSV

```python
import pandas as pd
crudo = pd.read_csv("../data/raw/ine_renta_media_mediana.csv", sep=";", encoding="latin-1")
print(crudo.shape)
print(crudo.columns.tolist())
crudo.head(15)
```

## Estado

- [ ] 1. Renta media y mediana
- [ ] 2. Gini y P80/P20
- [ ] 3. Fuente de ingresos
- [ ] 4. Demografía
- [ ] 5. Umbrales de pobreza
- [ ] B. Vivienda (alquiler / compra / geometría)
