# Flujo de trabajo de un data project

Flujo operativo concreto, mapeado a carpetas del repo.

```txt
1. Crear proyecto desde template      → cp -r 07_templates/... 06_proyectos/NN_nombre
2. Definir pregunta y fuentes         → README.md del proyecto
3. Escribir extractores               → src/extract_*.py  →  data/raw/
4. Limpiar y transformar              → src/transform_*.py →  data/interim → processed
5. Modelar (opcional dbt)             → modelos SQL sobre DuckDB/Postgres
6. Analizar                           → notebooks/
7. Validar calidad                    → pandera / Great Expectations / checklist
8. Visualizar                         → outputs/ (mapas, gráficos), Streamlit/Superset
9. Redactar informe                   → reports/ (Quarto / Markdown)
10. Actualizar catálogos              → 09_data_catalog/*.csv
11. Commit + push                     → CI valida lint y tests
```

## Convenciones de nombres

- Scripts: `extract_<fuente>.py`, `transform_<dominio>.py`, `build_<output>.py`.
- Notebooks: `NN_descripcion.ipynb` (numerados por orden de ejecución).
- Datos: `data/processed/<dominio>_<grano>.parquet`.

## Separación raw / interim / processed

- **raw:** tal cual viene de la fuente. Nunca se edita a mano.
- **interim:** pasos intermedios de limpieza (pueden borrarse y regenerarse).
- **processed:** dataset final, limpio, tipado y listo para análisis.

## Reglas de oro

1. Si no está en un script, no ha pasado (nada de pasos manuales no documentados).
2. El crudo es sagrado: se conserva intacto.
3. Todo dataset publicado tiene diccionario de datos y trazabilidad de fuente.
