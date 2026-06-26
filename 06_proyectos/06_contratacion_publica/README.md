# Contratación pública

## Pregunta de investigación

¿Existen patrones anómalos en la contratación pública (concentración, importes atípicos, adjudicatario único)?

## Contexto

La contratación pública (PLACSP) es un volumen enorme de gasto. El análisis de datos OCDS permite detectar patrones y aportar transparencia.

## Fuentes de datos previstas

- PLACSP (datos abiertos OCDS/ATOM).
- CPV (clasificación de contratos).
- Códigos INE / organismos.

## Metodología

1. Extraer adjudicaciones (OCDS).
2. Normalizar adjudicatarios y organismos.
3. Modelar en star schema (fct_contratos).
4. Detectar anomalías.

## Métricas principales

- Gasto total por organismo/CPV.
- % de procedimientos sin concurrencia.
- Concentración de adjudicatarios.

## Visualizaciones previstas

- Dashboard de gasto (Superset/Streamlit).
- Mapa por territorio.
- Detección de anomalías.

## Posibles modelos o simulaciones

- Isolation Forest sobre importes/plazos.
- Reglas de negocio (importes redondos, único oferente).

## Limitaciones

- Calidad de cumplimentación variable.
- Anomalía estadística ≠ irregularidad.

## Próximos pasos

- Extractor OCDS.
- Entity resolution.
- Modelo y detección de anomalías.

## Estructura

```txt
README.md
data/{raw,interim,processed}/
notebooks/
src/
outputs/
reports/
```

## Cómo reproducir

```bash
# 1. Crear/activar entorno (ver README raíz)
# 2. Ejecutar extractores
python src/extract.py
# 3. Transformar
python src/transform.py
# 4. Abrir notebooks/ y ejecutar de principio a fin
```

> Proyecto en construcción. Estructura y plan definidos; pendiente de implementación.
