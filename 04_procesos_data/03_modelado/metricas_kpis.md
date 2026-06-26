# Métricas y KPIs

Definir métricas de forma explícita, una sola vez, para que sean consistentes.

## Buenas prácticas

- Documenta fórmula y unidades.
- Define la métrica en la capa semántica, no en cada dashboard.
- Distingue medida base (importe) de métrica derivada (importe medio).

## Ejemplos

| Métrica | Fórmula | Unidad |
|---|---|---|
| Gasto total | SUM(importe) | € |
| Importe medio | AVG(importe) | € |
| Ratio vivienda/salario | precio_m2 * 90 / salario | años |
| Esfuerzo | cuota / renta | % |

## Antipatrón

Definir la misma métrica de formas distintas en cada gráfico → números que no cuadran.
