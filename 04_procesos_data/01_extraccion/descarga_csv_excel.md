# Descarga de CSV y Excel

Muchos organismos publican ficheros descargables. Automatiza la descarga, no la hagas a mano.

## Conceptos

- URLs estables vs dinámicas.
- Encoding (UTF-8 vs latin-1) y separadores (`;` frecuente en España).
- Hojas y rangos en Excel.

## Ejemplo

```python
import polars as pl
df = pl.read_csv('data/raw/ine_ipv.csv', separator=';', encoding='latin-1')
# Excel: pl.read_excel / pandas.read_excel(sheet_name=...)
```

## Buenas prácticas

- Conserva el fichero original en `data/raw/`.
- Documenta encoding y separador.
- Verifica número de filas tras la carga.

## Errores comunes

- Mojibake por encoding equivocado.
- Comas decimales interpretadas como separador de columnas.
