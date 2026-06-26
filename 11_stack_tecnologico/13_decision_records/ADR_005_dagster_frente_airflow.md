# ADR_005 — Dagster frente a Airflow para orquestación

- **Estado:** aceptado
- **Fecha:** 2026-06-26

## Contexto

Se necesita orquestar pipelines con dependencias, trazabilidad y testabilidad.

## Opciones consideradas

1. Dagster.
2. Airflow.
3. Solo GitHub Actions/cron.

## Decisión

Usar Dagster como orquestador principal; GitHub Actions/cron para tareas simples.

## Motivo

Dagster es asset-centric (modela datos, no solo tareas), con lineage, tipado y testabilidad superiores; mejor DX para proyectos de datos modernos.

## Consecuencias

Pipelines como assets materializables con lineage. Airflow queda como equivalente si la organización ya lo usa.

## Coste aproximado

open_source_self_hosted.

## Limitaciones

Curva de aprendizaje; ecosistema menor que Airflow en integraciones legacy.
