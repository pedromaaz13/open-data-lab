# Resolución de entidades

El mismo organismo o empresa aparece con nombres distintos. Resolverlo es clave en contratación/subvenciones.

## Conceptos

- Normalización de strings (mayúsculas, acentos, formas jurídicas SL/SA).
- Identificadores únicos (NIF/CIF) cuando existan.
- Fuzzy matching y blocking para escala.

## Herramientas

- `rapidfuzz` para similitud de cadenas.
- `recordlinkage` / `dedupe` para matching a escala.
- Diccionarios de normalización manual.

## Ejemplo

```python
from rapidfuzz import process, fuzz
match = process.extractOne('ACME S.L.', candidatos, scorer=fuzz.token_sort_ratio)
```

## Buenas prácticas

- Prioriza identificadores oficiales sobre nombres.
- Revisa manualmente los matches dudosos.
- Versiona el diccionario de equivalencias.
