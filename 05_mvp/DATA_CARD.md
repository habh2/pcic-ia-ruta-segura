# Ficha de datos

## Fuente

El proyecto usa dos conjuntos de datos, descargados una sola vez el 25 de noviembre de 2026. Los
experimentos y la app leen las copias locales de `data/` y no consultan los servicios en línea.

| Archivo | Fuente | Script de descarga |
|---|---|---|
| `data/incidentes_cuauhtemoc.csv` | API de Hoyo de Crimen, https://api.hoyodecrimen.com/ | `src/download_hoyodecrimen.py` |
| `data/cuauhtemoc.geojson` | API de Hoyo de Crimen, límite de la alcaldía Cuauhtémoc (`/api/v1/municipios/geojson`) | `src/download_hoyodecrimen.py` |
| `data/red_peatonal_cuauhtemoc.graphml` | OpenStreetMap, vía la Overpass API con OSMnx 2.0.7 | `src/download_osm.py` |

Hoyo de Crimen limpia y publica el conjunto "Víctimas en carpetas de investigación FGJ" de la
Fiscalía General de Justicia de la Ciudad de México, que se distribuye en
https://datos.cdmx.gob.mx/dataset/victimas-en-carpetas-de-investigacion-fgj. Los meses posteriores
a septiembre de 2024 no aparecen en los archivos CSV del portal, así que esos meses solo pueden
verificarse contra Hoyo de Crimen.

## Licencia

- Hoyo de Crimen: Creative Commons Atribución 4.0 Internacional (CC BY 4.0). Permite uso comercial
  con atribución, que debe enlazar a https://api.hoyodecrimen.com/. El conjunto original de la FGJ
  se publica con la licencia CC-BY-4.0-ESP.
- OpenStreetMap: Open Database License (ODbL) 1.0, © colaboradores de OpenStreetMap. Permite uso
  comercial con atribución. Una base de datos derivada que se distribuya públicamente, como la red
  con riesgo por arista que carga la app, debe ofrecerse con la misma licencia.

## Contenido

`incidentes_cuauhtemoc.csv`: 10,710 incidentes, uno por fila, del 1 de enero de 2019 al 30 de
septiembre de 2026.

| Columna | Tipo | Descripción |
|---|---|---|
| `delito` | texto | `ROBO A TRANSEUNTE C.V.` (con violencia, 7,141 incidentes) o `ROBO A TRANSEUNTE S.V.` (sin violencia, 3,569) |
| `fecha` | fecha, `AAAA-MM-DD` | Fecha del hecho |
| `hora` | hora, `HH:MM:SS` | Hora del hecho |
| `lat`, `lon` | real, grados (WGS 84) | Ubicación del hecho |
| `victimas` | entero | Número de víctimas registradas en el mismo incidente |

Incidentes por año: 2,273 (2019), 1,352 (2020), 1,311 (2021), 1,391 (2022), 1,279 (2023),
1,254 (2024), 1,132 (2025) y 718 (enero a septiembre de 2026).

`red_peatonal_cuauhtemoc.graphml`: red de calles caminables (`network_type="walk"` de OSMnx) dentro
de la alcaldía, con 10,463 nodos (esquinas y extremos de calle) y 15,966 tramos, 871.1 km en total.
OSMnx guarda cada tramo en los dos sentidos, por eso el archivo tiene 31,872 aristas dirigidas. Cada
arista lleva su longitud en metros (`length`). La red forma una sola componente conexa.

`cuauhtemoc.geojson`: polígono de la alcaldía Cuauhtémoc (clave geoestadística 9015).

`resultados/reportes_sinteticos.csv`: reportes de usuarios simulados, generados por
`src/route_experiment.py` con una semilla distinta en cada una de cinco ejecuciones. No provienen de
los incidentes de la FGJ. Cada ejecución tiene 60 reportes con columnas `semilla`, `tipo`, `lat` y
`lon`: 15 alrededor de una zona de riesgo alto (calle Francisco I. Madero, 19.43412, -99.14081),
15 alrededor de una zona de riesgo bajo (calle Toluca, colonia Roma Sur, 19.40983, -99.15768),
ambos grupos con dispersión normal de 60 m, y 30 reportes falsos repartidos al azar sobre la red en
proporción a la longitud de cada calle. Sirven para evaluar cómo responden las rutas a los reportes,
no para predecir delitos.

`web/assets/data/reportes_comunidad.json`: los reportes de la comunidad que muestra la app, generados
por `src/route_experiment.py` a partir de los 60 reportes sintéticos de la semilla 0. A cada uno se le
asignó al azar (semilla 0) uno de los cinco tipos de reporte de la app y una antigüedad de 0 a 44
días. La app solo muestra y toma en cuenta los que tienen menos de 30 días. Son datos de ejemplo,
no reportes de personas reales.

`web/assets/data/red_cuauhtemoc.json`: la red de calles que carga la app, generada por
`src/route_experiment.py`. Contiene las coordenadas de los nodos, cada calle una sola vez (15,906)
con su longitud, su riesgo base y su nombre, la geometría de las calles curvas, el límite de la
alcaldía, el ancho del núcleo y la altura de un reporte.

No hay variable objetivo en el sentido de un problema supervisado. Los incidentes de los años de
ajuste sirven para estimar el riesgo por calle, y los del año de prueba son los hechos contra los que
se mide la exposición de cada ruta.

## Recolección y preprocesamiento

1. Se descargaron los incidentes de los dos tipos de robo a transeúnte en un radio de 6 km alrededor
   del centro del rectángulo que envuelve la alcaldía, de enero de 2019 a septiembre de 2026. El
   punto del límite más lejano a ese centro está a 4.4 km, así que el círculo cubre toda la alcaldía.
   La API no tiene datos anteriores a 2019.
2. Se conservaron solo los incidentes dentro del polígono de la alcaldía.
3. La API devuelve una fila por víctima. Las filas con la misma fecha, hora, coordenadas y tipo de
   delito se unieron en un solo incidente, y la columna `victimas` cuenta cuántas eran.
4. La red de calles se descargó de OpenStreetMap con el polígono de la alcaldía y se conservó solo
   la componente conexa más grande.

5. El riesgo base de cada calle es la densidad media de los incidentes de ajuste a lo largo de la
   calle, estimada con un núcleo gaussiano de 50 m elegido con los incidentes de validación, y
   dividida entre la media de la red, de modo que 1 es una calle promedio.

Para verificar que los incidentes caen sobre la red, se midió la distancia de cada uno al tramo de
calle más cercano: mediana de 2.1 m, percentil 90 de 9.9 m, y 123 incidentes (1.1%) a más de 50 m.

## División

La división es temporal, para que el riesgo se estime con hechos anteriores a los que se usan para
evaluarlo:

| Parte | Periodo | Incidentes | Uso |
|---|---|---|---|
| Ajuste | 2021 a 2024 | 5,235 | Estimar el riesgo de cada calle |
| Validación | 2025 | 1,132 | Elegir el ancho del núcleo del estimador de riesgo |
| Prueba | enero a septiembre de 2026 | 718 | Medir la exposición de las rutas |

Los años 2019 y 2020 se excluyen: 2019 tiene casi el doble de incidentes que los años siguientes y
2020 coincide con la pandemia, así que mezclarlos con los demás combinaría dos niveles distintos de
delito. Ningún incidente de validación o prueba entra en la estimación del riesgo con la que se
evalúa, y la fecha separa las partes sin traslape.

## Sesgos y limitaciones

- Los datos son denuncias ante la Fiscalía. Los robos que no se denuncian no aparecen, y la tasa de
  denuncia puede variar entre colonias, horarios y grupos de personas, así que una calle sin
  registros no es necesariamente una calle segura.
- La ubicación es la que se registró en la carpeta de investigación. Puede ser aproximada, por
  ejemplo en una esquina cercana o en el lugar donde se denunció.
- Solo cubre la alcaldía Cuauhtémoc. El riesgo estimado no se puede usar en otras alcaldías.
- Solo cubre robo a transeúnte. Otros factores de seguridad para quien camina (iluminación,
  acoso, accidentes de tránsito) no están en los datos.
- OpenStreetMap puede tener calles faltantes, pasos peatonales sin trazar o tramos que ya no son
  transitables.
- El conjunto de la FGJ puede cambiar por actualizaciones retroactivas, así que una descarga
  posterior podría no coincidir exactamente con esta.

## Datos personales

Los incidentes no contienen nombres, edad, sexo ni datos de contacto de las víctimas: solo tipo de
delito, fecha, hora y coordenadas. La FGJ retiró en mayo de 2022 las columnas de calle por contener
información sensible. Las coordenadas de un hecho podrían, combinadas con otra información, señalar
un domicilio, así que la app no debe mostrar los incidentes uno por uno, solo el riesgo agregado por
calle.
OpenStreetMap no contiene datos personales.
