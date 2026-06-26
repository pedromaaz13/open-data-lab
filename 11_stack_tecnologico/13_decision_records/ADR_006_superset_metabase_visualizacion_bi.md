# ADR_006 — Superset y Metabase para visualización/BI

- **Estado:** aceptado
- **Fecha:** 2026-06-26

## Contexto

Se necesitan dashboards de BI open source self-hosted.

## Opciones consideradas

1. Superset.
2. Metabase.
3. Ambos.
4. Solo Power BI/Looker (enterprise).

## Decisión

Ofrecer ambos: Metabase para empezar rápido y usuarios no técnicos; Superset para dashboards potentes y SQL Lab.

## Motivo

Cubren distintos perfiles sin coste de licencia; equivalentes a Looker/Power BI/Tableau. Metabase es sencillo; Superset es potente.

## Consecuencias

Dashboards conectados a DuckDB/Postgres con modelos dbt. Power BI/Looker documentados como equivalencia enterprise.

## Coste aproximado

open_source_self_hosted.

## Limitaciones

Superset tiene configuración inicial costosa; gobernanza de métricas menos madura que Looker.
