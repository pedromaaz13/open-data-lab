# Tablas de hechos y dimensiones

Distinguir bien qué es un hecho y qué es una dimensión.

## Hechos

- Eventos o medidas: contratos, mediciones, transacciones.
- Contienen claves foráneas + métricas numéricas.
- Grano fino y muchas filas.

## Dimensiones

- Contexto descriptivo: tiempo, territorio, organismo, categoría.
- Pocas filas, muchos atributos.
- Se reutilizan entre hechos (conformadas).

## Ejemplos en el lab

- `fct_contratos`, `fct_subvenciones`, `fct_mediciones_clima`.
- `dim_territorio` (INE/NUTS), `dim_tiempo`, `dim_organismo`, `dim_cpv`.
