# GoIA

GoIA sugiere rutas a pie en la Ciudad de México que toman en cuenta la seguridad de cada calle, no solo el tiempo, y las compara con la ruta más rápida. Este repositorio contiene la página de presentación con pre-registro, un prototipo funcional de la app para la alcaldía Cuauhtémoc y el código en Python que estima el riesgo de cada calle y reproduce los resultados del artículo (`03_articulo/`).

El sitio es estático y se publica en Firebase Hosting. No hay código de servidor: los correos del pre-registro se guardan desde el navegador en Firestore.

## Requisitos

- Node.js 18 o posterior y Firebase CLI 15 (`npm install -g firebase-tools`). Probado con Firebase CLI 15.37.0.
- Java 21 o posterior, que el emulador de Firestore necesita para correr en local.
- Un navegador actual con conexión a internet. El mapa de la app descarga Leaflet 1.9.4 desde unpkg y los mosaicos de OpenStreetMap. La página de presentación descarga el SDK de Firebase 13.4.0 desde gstatic.

## Reproducir los resultados del artículo

Probado con Python 3.10.5 en Windows 11. Desde la carpeta `05_mvp/`:

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
.venv/Scripts/python src/route_experiment.py
```

En Linux o macOS, cambia `.venv/Scripts/python` por `.venv/bin/python`. El experimento tarda unos 35 minutos y escribe en `resultados/`:

| Archivo | Contenido |
|---|---|
| `seleccion_ancho.csv` | Log-verosimilitud media de los incidentes de 2025 para cada ancho del núcleo |
| `riesgo_aristas.csv` | Riesgo base de cada arista de la red |
| `reportes_sinteticos.csv` | Reportes sintéticos de cada semilla (zona alta, zona baja y falsos) |
| `rutas.csv` | Una fila por par origen-destino y método, con tiempo, incidentes de prueba y reportes cerca de la ruta |
| `resumen.csv` | Media y desviación estándar sobre las cinco semillas, de donde salen las Tablas 1 y 2 del artículo |

También regenera los datos que carga la app: `web/assets/data/red_cuauhtemoc.json`, la red de calles con riesgo, y `web/assets/data/reportes_comunidad.json`, los reportes de ejemplo de la comunidad.

Los datos ya vienen en `data/`, así que no hace falta descargarlos. Para volver a descargarlos (una sola vez, los resultados pueden cambiar si las fuentes se actualizan):

```bash
.venv/Scripts/python src/download_hoyodecrimen.py
.venv/Scripts/python src/download_osm.py
```

`download_hoyodecrimen.py` no verifica el certificado TLS de `api.hoyodecrimen.com`, porque la red donde se desarrolló intercepta TLS. La descripción completa de los datos está en `DATA_CARD.md`.

## Correr el proyecto en local

Desde la carpeta `05_mvp/`:

```bash
firebase emulators:start --only hosting,firestore
```

Abre en el navegador:

| Dirección | Qué es |
|---|---|
| http://127.0.0.1:8000/ | Página de presentación con el formulario de pre-registro |
| http://127.0.0.1:8000/app/ | Prototipo de la app |

En local, la página escribe en el emulador de Firestore (puerto 8080), no en la base real, y los correos de prueba se borran al detener el emulador. Para detenerlo, presiona `Ctrl+C` en la terminal.

## Publicar

```bash
firebase login
firebase deploy --only hosting,firestore
```

El sitio queda en https://rutasegura-d4afc.web.app.

## Estructura

```
05_mvp/
├── firebase.json            Configuración de Hosting, Firestore y los emuladores
├── firestore.rules          Reglas de seguridad de Firestore
├── firestore.indexes.json   Índices de Firestore
├── DATA_CARD.md             Documentación de los datos
├── requirements.txt         Dependencias de Python con versión fija
├── data/                    Incidentes, límite de la alcaldía y red de calles
├── src/
│   ├── download_hoyodecrimen.py   Descarga única de los incidentes
│   ├── download_osm.py            Descarga única de la red de calles
│   └── route_experiment.py        Riesgo por calle, experimento y datos de la app
├── resultados/              Resultados del experimento
└── web/
    ├── index.html           Página de presentación
    ├── app/index.html       Prototipo de la app
    └── assets/              Fuentes, imágenes, scripts y la red de calles (data/red_cuauhtemoc.json)
```

## Qué puedes probar en la app

- Buscar un destino o elegirlo en el mapa dentro de la alcaldía Cuauhtémoc, y comparar la ruta GoIA con la más rápida. La ruta GoIA es la de menos robos denunciados que tarda como máximo 20% más que la más rápida.
- Caminar una ruta con indicaciones paso a paso (la caminata es simulada y va acelerada).
- Ver en el mapa tus reportes (pines violetas con el ícono del tipo de reporte) y los de la comunidad (pines blancos que agrupan los reportes cercanos y muestran cuántos son). Los reportes de la comunidad son de ejemplo y cuentan solo si tienen menos de 30 días.
- Reportar algo en la calle. Si reportas durante la caminata, la ruta se recalcula para rodear el tramo.
- En el menú: tus reportes y la opción para restablecer los datos de ejemplo.

## Notas

- Abre las páginas a través del emulador o del sitio publicado, no haciendo doble clic en el archivo HTML. OpenStreetMap rechaza (error 403) los mosaicos que se piden sin un encabezado `Referer`, y un archivo abierto desde el disco no lo envía.
- Los correos del pre-registro se guardan en la colección `preregistros` de Firestore, con el correo como identificador del documento. Las reglas solo permiten crear un correo nuevo, válido y en minúsculas. Nadie puede leerlos, cambiarlos ni borrarlos desde la página. Para verlos o exportarlos, usa la consola de Firebase.
- El riesgo base de cada calle viene de los robos a transeúnte denunciados ante la FGJ entre 2021 y 2024. La app no muestra incidentes individuales ni un mapa de riesgo, solo la comparación entre rutas.
- La ubicación, la caminata y los comercios son datos de ejemplo. Los reportes que hagas en la app se guardan solo en tu navegador, y cada reporte cuenta durante 30 días. Para borrarlos, usa "Restablecer datos de ejemplo" en el menú de la app.
