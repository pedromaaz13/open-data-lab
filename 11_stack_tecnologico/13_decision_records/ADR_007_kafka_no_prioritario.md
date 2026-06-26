# ADR_007 — Kafka y streaming no prioritarios al inicio

- **Estado:** aceptado
- **Fecha:** 2026-06-26

## Contexto

Hay que decidir si incluir streaming/tiempo real en el stack inicial.

## Opciones consideradas

1. Incluir Kafka/Flink desde el inicio.
2. Posponer streaming hasta que un caso lo justifique.

## Decisión

No incluir Kafka/Flink/streaming en el stack inicial; documentarlos como referencia.

## Motivo

Los proyectos de datos públicos son mayormente batch (actualizaciones diarias/semanales/mensuales). Streaming añade complejidad operativa sin valor para el objetivo actual.

## Consecuencias

Stack más simple y mantenible. Streaming se evaluará solo si aparece un caso real de tiempo real.

## Coste aproximado

evitar_al_inicio (open_source_self_hosted si se adopta).

## Limitaciones

No apto para casos de baja latencia/tiempo real mientras no se adopte.
