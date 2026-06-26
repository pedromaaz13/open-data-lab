# Checklist de calidad de datos

Pasar antes de considerar un dataset "processed" y publicable.

## Completitud

- [ ] % de nulos por columna conocido y justificado
- [ ] Filas esperadas vs filas obtenidas (cobertura territorial/temporal)
- [ ] Sin pérdidas silenciosas en joins (validar cardinalidad)

## Validez

- [ ] Tipos correctos (fechas como fecha, numéricos como número)
- [ ] Rangos plausibles (edades 0-120, porcentajes 0-100, etc.)
- [ ] Códigos administrativos válidos (INE, NUTS, CNAE, CPV)
- [ ] CRS correcto y consistente en datos geoespaciales

## Unicidad

- [ ] Claves primarias sin duplicados
- [ ] Entidades resueltas (mismo organismo no aparece con 3 nombres)

## Consistencia

- [ ] Unidades homogéneas (€, miles de €, %, etc.)
- [ ] Mismos códigos entre tablas que se cruzan
- [ ] Totales cuadran con fuentes oficiales cuando existen

## Trazabilidad

- [ ] Cada columna tiene origen documentado
- [ ] Fecha de extracción registrada
- [ ] Transformaciones reproducibles desde raw

## Herramientas

- `pandera` para esquemas y validaciones en pipeline.
- `Great Expectations` para suites de expectativas más formales.
- Tests `dbt` (`not_null`, `unique`, `accepted_values`, `relationships`).

## Plantilla de reporte

Ver `07_templates/template_data_quality_report.md`.
