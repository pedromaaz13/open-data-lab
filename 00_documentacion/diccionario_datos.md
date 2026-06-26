# Diccionario de datos

Todo dataset publicado en `data/processed/` debe acompañarse de un diccionario.

## Qué documenta

Por cada variable/columna:

| Campo | Descripción |
|---|---|
| `columna` | Nombre técnico |
| `descripcion` | Qué representa en lenguaje natural |
| `tipo` | int / float / string / date / geometry |
| `unidad` | €, %, hab, km², etc. |
| `dominio` | Valores posibles o rango |
| `fuente` | Origen del dato |
| `transformacion` | Cómo se derivó (si aplica) |
| `nulos` | Tratamiento de ausentes |

## Ejemplo

| columna | descripcion | tipo | unidad | fuente |
|---|---|---|---|---|
| `cod_ine` | Código INE de municipio | string | - | INE |
| `precio_m2` | Precio medio vivienda | float | €/m² | Mº Vivienda |
| `salario_medio` | Salario bruto medio anual | float | € | INE (AEAT) |
| `ratio_anios` | Años de salario por vivienda 90m² | float | años | Derivado |

## Cómo crearlo

- Usa la plantilla `07_templates/template_diccionario_datos.md`.
- Guárdalo junto al dataset o en `reports/` del proyecto.
- Mantenlo sincronizado si el esquema cambia.
