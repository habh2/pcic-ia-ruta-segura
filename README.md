# GoIA

GoIA sugiere rutas a pie en la Ciudad de México que toman en cuenta la seguridad de cada calle, no solo el tiempo, y las compara con la ruta más rápida. Este repositorio contiene la página de presentación con pre-registro y un prototipo funcional de la app para la colonia Cuauhtémoc.

## Requisitos

- Python 3.10 o posterior (probado con Python 3.10.5).
- Un navegador actual con conexión a internet. El mapa de la app descarga Leaflet 1.9.4 desde unpkg y los mosaicos de OpenStreetMap.

## Correr el proyecto

Desde la raíz del repositorio:

```bash
python -m venv .venv
```

Activa el entorno virtual.

En Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

Instala la dependencia (Flask 3.1.0) y arranca el servidor:

```bash
pip install -r web/requirements.txt
python web/server.py
```

Abre en el navegador:

| Dirección | Qué es |
|---|---|
| http://127.0.0.1:8000/ | Página de presentación con el formulario de pre-registro |
| http://127.0.0.1:8000/app/ | Prototipo de la app |

Para detener el servidor, presiona `Ctrl+C` en la terminal.

## Estructura

```
web/
├── server.py          Servidor Flask: sirve las dos páginas y guarda los pre-registros
├── requirements.txt
├── index.html         Página de presentación
├── app/index.html     Prototipo de la app
└── assets/            Fuentes, imágenes y scripts compartidos
```

## Qué puedes probar en la app

- Buscar un destino o elegirlo en el mapa, y comparar la ruta GoIA con la más rápida.
- Caminar una ruta con indicaciones paso a paso (la caminata es simulada y va acelerada).
- Reportar algo en la calle. Si reportas durante la caminata, la ruta se recalcula para rodear el tramo.
- En el menú: tus reportes, la administración de comercios patrocinados y el modo técnico, que muestra el detalle de la búsqueda A*.

## Notas

- Abre las páginas a través del servidor, no haciendo doble clic en el archivo HTML. OpenStreetMap rechaza (error 403) los mosaicos que se piden sin un encabezado `Referer`, y un archivo abierto desde el disco no lo envía.
- Los correos del pre-registro se guardan en `web/data/preregistros.csv`. La carpeta se crea al recibir el primer correo y git la ignora.
- La ubicación, la caminata, las zonas con reportes y los comercios son datos de ejemplo. Los reportes y los cambios a comercios que hagas en la app se guardan solo en tu navegador. Para borrarlos, usa "Restablecer datos de ejemplo" en el menú de la app.
- Si el puerto 8000 está ocupado, cambia `PORT` al inicio de `web/server.py`.
