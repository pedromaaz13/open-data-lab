# Sequía y embalses

## Pregunta de investigación

¿Cómo evoluciona la sequía en España a partir del estado de los embalses por cuenca?

## Contexto

El agua embalsada es un indicador directo de estrés hídrico. Su seguimiento temporal y por cuenca permite anticipar episodios de sequía.

## Fuentes de datos previstas

- Estado de los embalses (MITECO, boletín hidrológico).
- Cuencas hidrográficas (CNIG/MITECO).
- Precipitación (AEMET).

## Metodología

1. Extraer series de reserva por embalse/cuenca.
2. Normalizar respecto a capacidad.
3. Construir índice de sequía por cuenca.
4. Mapear evolución temporal.

## Métricas principales

- % de reserva sobre capacidad.
- Anomalía respecto a media histórica.
- Índice de sequía por cuenca.

## Visualizaciones previstas

- Mapa animado por cuenca (Kepler.gl).
- Series temporales de reserva.
- Comparativa interanual.

## Posibles modelos o simulaciones

- Forecast de reservas.
- Escenarios de sequía.

## Limitaciones

- Heterogeneidad entre confederaciones.
- Gestión humana del agua confunde la señal climática.

## Próximos pasos

- Extractor boletín hidrológico.
- Procesado por cuenca.
- Mapa temporal.

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
