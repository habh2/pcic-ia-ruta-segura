# Proyecto final

El proyecto aplica inteligencia artificial a un problema real y lo lleva hasta la forma de una
empresa de base tecnológica. Cada equipo entrega un repositorio con la estructura de esta
plantilla. La estructura es fija para que todos los equipos entreguen la misma información en el
mismo lugar, con los mismos nombres de archivo y de columna. Un revisor automático lee estos
archivos, así que un archivo con otro nombre o en otra carpeta cuenta como no entregado.

## Estructura

```
00_propuesta/propuesta.tex    Propuesta de proyecto, 4 páginas
00_propuesta/propuesta.docx   La misma propuesta para Word o LibreOffice
01_negocio/modelo_negocio.tex Modelo de negocio con el canvas, 5 páginas
01_negocio/modelo_negocio.docx
                              El mismo modelo de negocio para Word o LibreOffice
01_negocio/canvas.tex         Business Model Canvas, insertado en modelo_negocio.tex
01_negocio/validacion.tex     Resultados de la validación, 3 páginas más anexo
01_negocio/hipotesis.csv      Hipótesis del canvas, prueba, criterio y resultado
01_negocio/guion_entrevista.md
01_negocio/entrevistas.csv    Registro de entrevistas con clientes potenciales
01_negocio/metricas_landing.csv
                              Visitas y registros semanales de la landing page
02_finanzas/modelo_financiero.xlsx
03_articulo/articulo.tex      Artículo, 4 páginas, formato NeurIPS
03_articulo/referencias.bib
04_pitch/pitch.tex            Diapositivas del pitch
05_mvp/                       Código, datos y documentación del producto mínimo viable
06_ia/declaracion.md          Declaración de uso de IA generativa
06_ia/bitacoras.csv           Índice de conversaciones con IA generativa
06_ia/bitacoras/              Conversaciones exportadas, completas
07_revision/revision_par.md   Revisión del artículo de otro equipo
```

Cada `.tex`, salvo `canvas.tex`, se entrega también compilado, con el mismo nombre y extensión `.pdf`, en la misma
carpeta. La propuesta puede escribirse en LaTeX (`propuesta.tex`) o en Word o LibreOffice
(`propuesta.docx`). En los dos casos se entrega `00_propuesta/propuesta.pdf`. Lo mismo vale
para el modelo de negocio, que se entrega como `01_negocio/modelo_negocio.pdf`. En la versión de
Word, las instrucciones aparecen como comentarios al margen, y los números de tabla se actualizan
con clic derecho y "Actualizar campos" (F9). El pitch puede hacerse con otra herramienta si conserva el orden de las diapositivas y se
entrega como `04_pitch/pitch.pdf`.

## Entregas

| Semana | Entrega | Archivos |
|---|---|---|
| 10 | Propuesta | `00_propuesta/propuesta.pdf` |
| 11 | Modelo de negocio, versión 1 | `modelo_negocio.pdf`, `hipotesis.csv` y `guion_entrevista.md` en `01_negocio/`, landing page publicada |
| 12 | Modelo financiero, versión 1 | `02_finanzas/modelo_financiero.xlsx` |
| 13 | Borrador del artículo | `03_articulo/articulo.pdf` |
| 14 | Revisión entre pares y ensayo del pitch | `07_revision/revision_par.md` |
| 15 | Entrega final | Repositorio completo |
| 15 y 16 | Presentaciones | 5 minutos de pitch y 4 minutos de preguntas |

Las entregas intermedias reciben retroalimentación y no se califican por separado. La calificación
usa la entrega final, así que cada archivo puede mejorarse hasta la semana 15.

## Rúbrica

| Componente | Porcentaje | Qué se evalúa |
|---|---|---|
| Artículo | 30% | Pregunta e hipótesis claras, línea base y métrica, experimentos reproducibles, limitaciones, escritura, citas verificadas y revisión entregada a otro equipo |
| MVP | 30% | Instalación y ejecución con los comandos del README, datos documentados, resultados del artículo reproducibles con el código y demostración funcional |
| Negocio | 30% | Canvas completo, con cada bloque ligado a una hipótesis; modelo financiero con una fuente por supuesto, coherente con el canvas y el tamaño de mercado; pitch claro, con cifras iguales a las del Excel y del artículo; landing page publicada, con propuesta de valor clara y registro funcional |
| Validación | 10% | Al menos 10 entrevistas con personas reales, encuestas y métricas de la landing page; hipótesis con criterio de éxito fijado antes de probarlas; cambios en el canvas justificados por la evidencia |
| **Total** | **100%** | |

Las bitácoras de IA generativa son requisito para calificar. Un entregable producido con IA
generativa sin bitácora no se califica.

## Uso de IA generativa

Se permite usar IA generativa en todo el proyecto con estas reglas:

- Cada conversación se exporta completa a `06_ia/bitacoras/` y se registra en `06_ia/bitacoras.csv`.
- El equipo responde por todo lo que entrega. Cada cifra, cita y fragmento de código generado se
  verifica antes de usarlo.
- Una referencia inventada en el artículo descuenta puntos del artículo.
- Las entrevistas simuladas con un modelo de lenguaje sirven para practicar el guion. Solo las
  entrevistas con personas reales cuentan como evidencia en `entrevistas.csv`.
- La revisión entre pares la escribe el equipo revisor. La IA puede ayudar a redactar, con bitácora.

## Formato de los archivos de datos

- CSV en UTF-8, separados por comas, con la primera fila de encabezados tal como viene en la
  plantilla. No se agregan, quitan ni renombran columnas.
- Los campos de texto que contienen comas van entre comillas dobles.
- Las listas dentro de un campo se separan con punto y coma, por ejemplo `E01;E04`.
- La fila de ejemplo de cada CSV se borra antes de entregar.

## Lista de verificación de la entrega final

- [ ] `propuesta.pdf`, `modelo_negocio.pdf`, `validacion.pdf`, `articulo.pdf` y `pitch.pdf` compilados.
- [ ] `hipotesis.csv` con estado `validada` o `invalidada` en cada hipótesis probada.
- [ ] `entrevistas.csv` con al menos 10 entrevistas con personas reales.
- [ ] `metricas_landing.csv` con una fila por semana desde la publicación.
- [ ] La dirección de la landing page aparece en la diapositiva de validación del pitch.
- [ ] `modelo_financiero.xlsx` con todas las fuentes llenas y la hoja Resultados sin "Revisar" sin explicar.
- [ ] El artículo cabe en 4 páginas, sin contar referencias ni apéndices.
- [ ] `05_mvp/README.md` permite instalar y ejecutar el MVP en una máquina limpia.
- [ ] `05_mvp/DATA_CARD.md` completo.
- [ ] Las cifras del pitch coinciden con el Excel y con el artículo.
- [ ] `06_ia/` con declaración, índice y conversaciones completas.
- [ ] Filas de ejemplo borradas.
