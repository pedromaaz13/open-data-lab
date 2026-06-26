# ADR_003 — DuckDB + Parquet como base analítica

- **Estado:** aceptado
- **Fecha:** 2026-06-26

## Contexto

Se necesita una capa analítica local, rápida y reproducible, sin servidor ni coste.

## Opciones consideradas

1. DuckDB + Parquet.
2. SQLite.
3. Postgres para todo.
4. BigQuery desde el inicio.

## Decisión

Usar DuckDB sobre ficheros Parquet/GeoParquet como base analítica por defecto.

## Motivo

DuckDB ejecuta SQL analítico sobre Parquet sin cargar todo en memoria, es embebido (sin servidor), rápido y con equivalencia directa a BigQuery/Snowflake.

## Consecuencias

Análisis reproducible y portable. Para persistencia/concurrencia se complementa con PostgreSQL.

## Coste aproximado

gratis_local.

## Limitaciones

Single-node; no apto para alta concurrencia multiusuario (ahí entra Postgres o cloud).
