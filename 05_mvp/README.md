# GoIA

GoIA sugiere rutas a pie en la Ciudad de México que toman en cuenta la seguridad de cada calle, no solo el tiempo, y las compara con la ruta más rápida. Este repositorio contiene la página de presentación con pre-registro y un prototipo funcional de la app para la colonia Cuauhtémoc.

El sitio es estático y se publica en Firebase Hosting. No hay código de servidor: los correos del pre-registro se guardan desde el navegador en Firestore.

## Requisitos

- Node.js 18 o posterior y Firebase CLI 15 (`npm install -g firebase-tools`). Probado con Firebase CLI 15.37.0.
- Java 21 o posterior, que el emulador de Firestore necesita para correr en local.
- Un navegador actual con conexión a internet. El mapa de la app descarga Leaflet 1.9.4 desde unpkg y los mosaicos de OpenStreetMap. La página de presentación descarga el SDK de Firebase 13.4.0 desde gstatic.

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
└── web/
    ├── index.html           Página de presentación
    ├── app/index.html       Prototipo de la app
    └── assets/              Fuentes, imágenes y scripts compartidos
```

## Qué puedes probar en la app

- Buscar un destino o elegirlo en el mapa, y comparar la ruta GoIA con la más rápida.
- Caminar una ruta con indicaciones paso a paso (la caminata es simulada y va acelerada).
- Reportar algo en la calle. Si reportas durante la caminata, la ruta se recalcula para rodear el tramo.
- En el menú: tus reportes, la administración de comercios patrocinados y el modo técnico, que muestra el detalle de la búsqueda A*.

## Notas

- Abre las páginas a través del emulador o del sitio publicado, no haciendo doble clic en el archivo HTML. OpenStreetMap rechaza (error 403) los mosaicos que se piden sin un encabezado `Referer`, y un archivo abierto desde el disco no lo envía.
- Los correos del pre-registro se guardan en la colección `preregistros` de Firestore, con el correo como identificador del documento. Las reglas solo permiten crear un correo nuevo, válido y en minúsculas. Nadie puede leerlos, cambiarlos ni borrarlos desde la página. Para verlos o exportarlos, usa la consola de Firebase.
- La ubicación, la caminata, las zonas con reportes y los comercios son datos de ejemplo. Los reportes y los cambios a comercios que hagas en la app se guardan solo en tu navegador. Para borrarlos, usa "Restablecer datos de ejemplo" en el menú de la app.
