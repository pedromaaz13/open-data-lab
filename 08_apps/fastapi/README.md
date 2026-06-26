# APIs con FastAPI

APIs de datos para servir resultados del laboratorio. Ver
`11_stack_tecnologico/10_backend_apis/`.

## Ejecutar

```bash
uvicorn main:app --reload
```

## Buenas prácticas

- Modelos de entrada/salida con Pydantic.
- Documentación automática en `/docs` (OpenAPI).
- Sirve datos desde DuckDB/Postgres, no recalcules en cada request.

## Ideas

- API de indicadores por municipio.
- Endpoint de búsqueda en el catálogo de datasets.
