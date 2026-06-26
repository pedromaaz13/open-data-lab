# ADR_008 — Cloud solo si aporta valor

- **Estado:** aceptado
- **Fecha:** 2026-06-26

## Contexto

Hay que definir cuándo se justifica usar servicios cloud/enterprise frente a open source self-hosted.

## Opciones consideradas

1. Cloud solo ante volumen/concurrencia/despliegue/gobernanza.
2. Cloud-first por defecto.
3. Nunca cloud.

## Decisión

Adoptar cloud únicamente cuando el volumen, la concurrencia, el despliegue o la gobernanza lo justifiquen.

## Motivo

Coherente con la filosofía del laboratorio; evita coste y lock-in innecesarios; demuestra criterio profesional sobre cuándo escalar.

## Consecuencias

Se documentan equivalencias y disparadores de escalado (ver `stack_enterprise_cloud.md`). Servicios gestionados de pago bajo (Supabase, Render, MotherDuck) como puente.

## Coste aproximado

variable: free_tier → pago_profesional → enterprise.

## Limitaciones

Decisión caso a caso; requiere reevaluar costes al escalar.
