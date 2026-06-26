# 06 · Proyectos

Proyectos reproducibles completos. Cada uno es autocontenido y sigue la misma
estructura y metodología (ver `00_documentacion/`).

## Estructura de cada proyecto

```txt
NN_nombre/
├── README.md
├── data/
│   ├── raw/        crudo intacto (no versionado)
│   ├── interim/    intermedios (no versionado)
│   └── processed/  final en Parquet (no versionado)
├── notebooks/      análisis y narrativa
├── src/            extractores y transformadores reproducibles
├── outputs/        mapas, gráficos, exportaciones
└── reports/        informes y artículos
```

## Catálogo de proyectos

| Proyecto | Pregunta |
|---|---|
| `01_mapa_vivienda_salarios/` | ¿Cuánto cuesta la vivienda en años de salario por territorio? |
| `02_calor_extremo_desigualdad/` | ¿El calor extremo golpea más a las zonas con menos renta? |
| `03_sequia_embalses/` | ¿Cómo evoluciona la sequía a partir del estado de los embalses? |
| `04_incendios_ndvi_copernicus/` | ¿Qué superficie y vegetación afectan los incendios (NDVI/NBR)? |
| `05_subvenciones_publicas/` | ¿Cómo se distribuyen las subvenciones públicas? |
| `06_contratacion_publica/` | ¿Hay patrones anómalos en la contratación pública? |
| `07_cam_municipios_renta_vivienda/` | ¿Dónde se vive mejor/peor en la CAM por municipio? (nivel 2 del proyecto 01) |

## Cómo crear un proyecto nuevo

1. Copia la estructura desde `07_templates/`.
2. Rellena el README con la pregunta de investigación.
3. Registra fuentes en `09_data_catalog/`.
4. Sigue la metodología de `00_documentacion/`.
