# Extracción e ingesta

Obtener datos de fuentes externas hacia el laboratorio.

## Stack del laboratorio (open source)

requests/httpx, BeautifulSoup, Playwright, pystac-client, clientes de APIs (wbgapi, eurostat).

## Equivalencias enterprise/cloud

Airbyte, Fivetran, Cloud Functions, Azure Data Factory (ingesta gestionada).

## Notas

- APIs REST, ficheros, scraping y satélite (ver `04_procesos_data/01_extraccion/`).

## Filosofía

Open source first. Cloud when it adds value. Se elige la herramienta adecuada al
caso, no la más grande por defecto.
