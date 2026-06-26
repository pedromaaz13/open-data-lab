# ADR_002 — Filosofía: open source first, cloud when it adds value

- **Estado:** aceptado
- **Fecha:** 2026-06-26

## Contexto

Hay que fijar el principio rector de elección tecnológica para evitar sobre-ingeniería y costes innecesarios.

## Opciones consideradas

1. Open source first, cloud cuando aporte valor.
2. Cloud-native desde el inicio (BigQuery/Databricks).
3. Mix sin criterio explícito.

## Decisión

Adoptar 'open source first, cloud when it adds value' como principio rector.

## Motivo

Maximiza reproducibilidad y minimiza coste; separa stack local, pro open source y enterprise; demuestra criterio (saber cuándo NO escalar).

## Consecuencias

Stack base self-hosted; cloud documentado como evolución. Cada proyecto activa solo lo que necesita.

## Coste aproximado

gratis_local / open_source_self_hosted.

## Limitaciones

Self-hosting implica coste operativo; algunos servicios gestionados pueden ser más eficientes en tiempo.
