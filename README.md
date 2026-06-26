# Open Data Lab

Open source lab for public data, geospatial analysis, data science and civic storytelling.

> Laboratorio open source de datos públicos, análisis geoespacial, ciencia de datos
> aplicada, evidencia social y storytelling para investigar problemas sociales,
> económicos, medioambientales y territoriales con Python, APIs oficiales,
> notebooks, mapas y visualizaciones avanzadas.

## Visión

Este laboratorio nace para investigar problemas sociales, económicos, medioambientales
y territoriales usando datos públicos, fuentes oficiales, Python, notebooks
reproducibles, mapas interactivos, visualización avanzada y ciencia de datos aplicada.

## Filosofía

**Open source first. Cloud when it adds value.**

Este laboratorio no busca usar siempre la tecnología más grande, sino elegir la
arquitectura adecuada para cada problema: reproducible en local, profesional con
open source y escalable a cloud cuando el caso lo justifique.

Principios:

1. Priorizar herramientas open source.
2. Priorizar bajo coste.
3. Priorizar reproducibilidad.
4. Priorizar documentación clara.
5. Usar servicios de pago solo cuando aporten valor profesional real.
6. Separar claramente stack local, stack pro open source y stack enterprise/cloud.
7. No usar la tecnología más grande por defecto, sino la arquitectura adecuada para
   cada problema.

## Objetivos

- Practicar análisis de datos con casos reales.
- Reutilizar datos abiertos de organismos oficiales.
- Crear notebooks reproducibles.
- Construir mapas interactivos con Kepler.gl, GeoPandas, PostGIS y otras herramientas.
- Aprender estadística aplicada, ciencia de datos e investigación.
- Documentar procesos de extracción, transformación, análisis y visualización.
- Crear agentes/prompts especializados para acelerar el trabajo analítico.
- Desarrollar un portfolio profesional de Data Analyst / Analytics Engineer.
- Comparar tecnologías, costes y limitaciones.
- Diseñar arquitecturas data realistas y escalables.

## Áreas de trabajo

- Vivienda y salarios
- Coste de vida e inflación
- Medioambiente y clima
- Sequía, incendios y territorio
- Datos satelitales y Copernicus
- Contratación pública
- Subvenciones
- Memoria pública
- Geoespacial
- Visualización avanzada
- Ciencia de datos aplicada
- Storytelling con datos

## Stack principal

- Python
- JupyterLab
- DuckDB
- Parquet / GeoParquet
- PostgreSQL / PostGIS
- dbt Core
- Dagster
- Apache Superset
- Kepler.gl
- Streamlit
- FastAPI
- Docker Compose
- GitHub Actions

## Estructura del repositorio

```txt
open-data-lab/
├── 00_documentacion/      Metodología, buenas prácticas y calidad
├── 01_skills/             Skills técnicas (Python, SQL, geoespacial, ML...)
├── 02_agentes/            Prompts/agentes especializados por fase
├── 03_fuentes_oficiales/  Catálogo de organismos y APIs (ES / EU / global)
├── 04_procesos_data/      Extracción → transformación → modelado → análisis → viz
├── 05_notebooks/          Notebooks por temática
├── 06_proyectos/          Proyectos reproducibles completos
├── 07_templates/          Plantillas reutilizables
├── 08_apps/               Streamlit, FastAPI, dashboards, mapas
├── 09_data_catalog/       Catálogos de datasets, APIs, organismos y proyectos
├── 10_referencias/        Inspiración, librerías, cursos y recursos
└── 11_stack_tecnologico/  Stack, matrices de decisión, costes y ADRs
```

## Metodología

Cada proyecto debe tener:

1. Pregunta de investigación
2. Fuentes de datos
3. Extracción
4. Limpieza y transformación
5. Modelo de datos
6. Análisis exploratorio
7. Métricas
8. Visualizaciones
9. Conclusiones
10. Limitaciones
11. Cómo reproducir el análisis

## Arquitectura pro open source (referencia)

```txt
APIs oficiales / CSV / scraping / Copernicus
        ↓
Python extractors
        ↓
data/raw
        ↓
Polars / Pandas / DuckDB
        ↓
data/processed en Parquet / GeoParquet
        ↓
dbt Core
        ↓
DuckDB + PostgreSQL/PostGIS
        ↓
Dagster
        ↓
Superset / Metabase / Kepler.gl / Streamlit
        ↓
FastAPI opcional
        ↓
README + artículo + dashboard + mapa
```

## Cómo empezar

```bash
# 1. Clonar
git clone https://github.com/pedromaaz13/open-data-lab.git
cd open-data-lab

# 2. Entorno (uv recomendado, pip como alternativa)
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 3. Variables de entorno
cp .env.example .env

# 4. Levantar el stack open source por perfiles (opcional)
docker compose --profile core up
```

## Estado del proyecto

Repositorio en construcción. Ver [`roadmap.md`](roadmap.md) para las fases.

## Licencia

Pendiente de definir (se recomienda MIT para el código y CC-BY 4.0 para la
documentación). Los datos siguen las licencias de cada organismo emisor.
