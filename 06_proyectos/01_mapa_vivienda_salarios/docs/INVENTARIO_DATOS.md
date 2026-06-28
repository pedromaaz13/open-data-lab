# Inventario de datos — Madrid por distritos

Estado de la investigación: qué fuentes y variables tenemos, y qué falta.
Nivel territorial: **21 distritos de la ciudad de Madrid**. Año: **2023** (INE Atlas).

## ✅ Fuentes que YA tenemos (descargadas, en `extract.py` y cargadas por `load_ine.py`)

| Fuente | Organismo | Qué aporta |
|---|---|---|
| Indicadores de renta media y mediana | INE Atlas (ADRH 2023) | renta bruta/neta, mediana |
| Distribución por fuente de ingresos | INE Atlas | % salario / pensiones / paro / otras |
| Índice de Gini y P80/P20 | INE Atlas | desigualdad |
| Indicadores demográficos | INE Atlas | edad, población, hogares, nacionalidad |
| Geometría de distritos (Shapefile) | Ayto. Madrid (Geoportal) | las formas para el mapa |

## ✅ Variables de estudio disponibles (22 columnas + geometría)

**Renta / ingresos**
- Renta neta media por hogar
- Renta neta media por persona
- Renta bruta media por hogar
- Renta bruta media por persona
- Media de la renta por unidad de consumo
- Mediana de la renta por unidad de consumo

**Desigualdad**
- Índice de Gini
- Distribución de la renta P80/P20

**Fuente de los ingresos (% sobre renta bruta)**
- Salario · Pensiones · Prestaciones por desempleo · Otras prestaciones · Otros ingresos

**Demografía**
- Población · Edad media · % menores de 18 · % de 65 y más
- % hogares unipersonales · Tamaño medio del hogar · % población española

**Geografía**
- Geometría (polígono) de cada distrito · Área

## 🧮 Variables que podemos DERIVAR (con lo que ya hay)

- **Peso de impuestos/cotizaciones** = (renta bruta − renta neta) / renta bruta
- **Brecha de renta** rico/pobre entre distritos
- Indicadores compuestos (vulnerabilidad) combinando renta + Gini + edad + pobreza

## ❌ Lo que FALTA (bloque vivienda — ver `PLAN_VIVIENDA.md`)

| Variable | Fuente candidata | Para qué |
|---|---|---|
| **Alquiler €/m²** | Sistema Estatal de Índices de Alquiler (Mº Vivienda) | Esfuerzo de alquiler (% del sueldo) |
| **Compra €/m²** | Mº Vivienda / Ayto. Madrid | Esfuerzo de compra (años de renta) |
| **Tipo de vivienda y m²** | INE · Censo 2021 | Superficie media, tipo, régimen (propiedad/alquiler) |
| **Antigüedad / m²** (alt.) | Catastro | Edad y tamaño de la edificación |

## ❓ Lo que NO podremos medir aún (limitaciones)

- Esfuerzo de vivienda **real**: falta alquiler/compra (las variables de arriba).
- Dato por **persona** (el Atlas es por hogar/distrito → cuidado con la falacia ecológica).
- Evolución temporal fina: por ahora solo año 2023 (el Atlas tiene serie; se podría ampliar).

## Resumen en una línea

Tenemos un **perfil socioeconómico completo por distrito** (renta, desigualdad, fuente de ingresos, demografía) + el **mapa**. Falta la capa de **vivienda** (alquiler/compra/tipo/m²) para cerrar el **esfuerzo real** y responder "¿dónde se vive mejor con el sueldo?".
