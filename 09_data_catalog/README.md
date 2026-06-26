# 09 · Data catalog

Catálogos centrales del laboratorio en CSV (versionados). Registran qué datos,
APIs, organismos y proyectos existen, para no perder trazabilidad.

| Archivo | Contenido |
|---|---|
| `catalogo_datasets.csv` | Datasets concretos usados o candidatos |
| `catalogo_apis.csv` | APIs y endpoints |
| `catalogo_organismos.csv` | Organismos y portales |
| `catalogo_proyectos.csv` | Proyectos del laboratorio |

## Esquemas

**catalogo_datasets.csv**
```csv
id,nombre,organismo,tema,url,formato,frecuencia_actualizacion,nivel_geografico,fecha_consulta,licencia,estado,notas
```

**catalogo_apis.csv**
```csv
id,nombre_api,organismo,url_documentacion,autenticacion,formato_respuesta,limites_uso,ejemplo_endpoint,estado,notas
```

**catalogo_organismos.csv**
```csv
id,nombre,ambito,pais,url,temas,tipo_datos,api_disponible,notas
```

**catalogo_proyectos.csv**
```csv
id,nombre_proyecto,categoria,pregunta,estado,fuentes,notebook_principal,visualizacion,fecha_inicio,fecha_actualizacion,notas
```

## Mantenimiento

- Actualiza el catálogo cada vez que uses una fuente nueva.
- `estado`: candidato | en_uso | descartado.
- Mantén la trazabilidad (ver `00_documentacion/trazabilidad_fuentes.md`).
