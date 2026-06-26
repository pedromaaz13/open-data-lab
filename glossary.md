# Glosario

Términos clave usados en el Open Data Lab.

## Datos y formatos

- **Dato abierto (open data):** dato publicado bajo una licencia que permite su
  reutilización libre, normalmente por un organismo público.
- **Parquet:** formato columnar comprimido, eficiente para analítica.
- **GeoParquet:** Parquet con geometrías estandarizadas para datos geoespaciales.
- **GeoJSON / GPKG (GeoPackage):** formatos de intercambio geoespacial.
- **STAC (SpatioTemporal Asset Catalog):** estándar para catalogar imágenes satélite.
- **COG (Cloud Optimized GeoTIFF):** GeoTIFF optimizado para lectura parcial en cloud.

## Arquitectura data

- **ETL / ELT:** Extract-Transform-Load vs Extract-Load-Transform (transformar en
  el destino, patrón moderno con dbt).
- **Data lake:** almacenamiento de datos crudos a gran escala (p. ej. MinIO/S3).
- **Lakehouse:** combinación de lake + capacidades de warehouse (Delta, Iceberg).
- **Warehouse:** base analítica para consultas (DuckDB local, BigQuery cloud).
- **Capa semántica (semantic layer):** definición centralizada de métricas y
  dimensiones reutilizables por BI.
- **Lineage:** trazabilidad de cómo un dato fluye y se transforma.
- **Asset (Dagster):** objeto de datos versionable y materializable.

## Modelado

- **Modelo dimensional:** organización en hechos y dimensiones (Kimball).
- **Star schema:** esquema en estrella, una tabla de hechos rodeada de dimensiones.
- **Tabla de hechos:** eventos/medidas (ventas, contratos, mediciones).
- **Dimensión:** contexto descriptivo (tiempo, territorio, organismo).
- **KPI / métrica:** indicador cuantitativo de seguimiento.
- **Índice compuesto:** combinación ponderada de variables en un único indicador.

## Geoespacial

- **CRS (Coordinate Reference System):** sistema de referencia (p. ej. EPSG:4326,
  EPSG:25830 ETRS89 UTM30N para España).
- **PostGIS:** extensión geoespacial de PostgreSQL.
- **H3:** sistema de indexación geoespacial hexagonal de Uber.
- **NDVI:** índice de vegetación de diferencia normalizada (teledetección).
- **Spatial join:** unión de tablas por relación espacial.

## Calidad y reproducibilidad

- **Reproducibilidad:** capacidad de regenerar un resultado desde cero.
- **Trazabilidad:** poder reconstruir el origen de cada dato.
- **Data contract:** acuerdo sobre esquema y calidad de un dataset.
- **Great Expectations / pandera:** validación de calidad de datos.
- **ADR (Architecture Decision Record):** documento que registra una decisión técnica.

## Códigos administrativos (España)

- **Código INE:** identificador oficial de municipios/provincias/CCAA.
- **NUTS:** nomenclatura europea de unidades territoriales estadísticas.
- **CNAE:** clasificación nacional de actividades económicas.
- **CPV:** vocabulario común de contratación pública (UE).
