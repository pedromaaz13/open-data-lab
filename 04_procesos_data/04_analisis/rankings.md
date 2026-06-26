# Rankings

Ordenaciones que comunican rápido, pero que hay que construir con cuidado.

## Conceptos

- Normalizar antes de rankear (per cápita, por superficie).
- Empates y sensibilidad del orden.
- Window functions para rankings (`RANK`, `ROW_NUMBER`).

## Ejemplo SQL

```sql
SELECT provincia, ratio,
       RANK() OVER (ORDER BY ratio DESC) AS pos
FROM tabla;
```

## Advertencias

- Un ranking sin contexto engaña.
- Cuidado con diferencias no significativas entre posiciones.
