# ADR_004 — PostgreSQL + PostGIS para geoespacial relacional

- **Estado:** aceptado
- **Fecha:** 2026-06-26

## Contexto

Los proyectos territoriales requieren joins espaciales, persistencia y consultas geográficas robustas.

## Opciones consideradas

1. PostGIS.
2. Solo GeoPandas en memoria.
3. BigQuery GIS desde el inicio.

## Decisión

Usar PostgreSQL + PostGIS como base geoespacial relacional, con GeoPandas para análisis en memoria.

## Motivo

PostGIS es el estándar geoespacial open source: índices espaciales, operaciones avanzadas y equivalencia con BigQuery GIS / Databricks Mosaic.

## Consecuencias

Análisis territorial escalable y reproducible vía Docker. GeoPandas para exploración ligera.

## Coste aproximado

open_source_self_hosted.

## Limitaciones

Requiere operar el servidor; tuning para rásteres grandes.
