# Subvenciones públicas

## Pregunta de investigación

¿Cómo se distribuyen las subvenciones públicas por organismo, territorio y beneficiario?

## Contexto

La BDNS centraliza las ayudas públicas. Analizar su distribución aporta transparencia sobre el destino del dinero público.

## Fuentes de datos previstas

- BDNS (concesiones y convocatorias).
- Códigos INE (territorio).
- CNAE (sector).

## Metodología

1. Extraer concesiones de la BDNS.
2. Normalizar beneficiarios (entity resolution).
3. Modelar en star schema.
4. Analizar concentración y distribución.

## Métricas principales

- Importe total por organismo/territorio.
- Concentración (top beneficiarios, índice de Gini).
- Importe medio por convocatoria.

## Visualizaciones previstas

- Mapa de subvenciones por territorio.
- Treemap por sector.
- Ranking de beneficiarios.

## Posibles modelos o simulaciones

- Detección de anomalías en importes.
- Clustering de perfiles de ayuda.

## Limitaciones

- Normalización de beneficiarios compleja.
- Cobertura temporal parcial.

## Próximos pasos

- Extractor BDNS.
- Resolución de entidades.
- Modelo dimensional y dashboard.

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
