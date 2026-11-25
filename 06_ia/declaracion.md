# Declaración de uso de IA generativa

Responder cada sección en uno o dos párrafos. El detalle de cada conversación va en
`bitacoras.csv` y el texto completo en `bitacoras/`.

## Herramientas

Herramientas usadas (por ejemplo, ChatGPT, Claude, Gemini, Copilot, Cursor) y para qué entregable
se usó cada una.

## Usos

Qué tareas se hicieron con apoyo de IA generativa: búsqueda de ideas, código, redacción,
traducción, análisis de datos, diseño de la landing page, práctica de entrevistas, entre otras.

## Verificación

Cómo verificó el equipo lo que produjo la IA: pruebas del código, revisión de cada referencia
contra su fuente, cálculo independiente de cifras, revisión de un integrante distinto.

## Errores encontrados

Ejemplos concretos de respuestas incorrectas, inventadas o descartadas, y cómo se detectaron.

- **Cobertura temporal de la fuente de la FGJ.** En la redacción del artículo, la IA citó el
  conjunto "Víctimas en carpetas de investigación FGJ" (portal de datos abiertos de la CDMX) como
  fuente de las cifras de 2025 y de enero a septiembre de 2026. Al abrir el enlace, la página solo
  menciona explícitamente datos hasta 2024: el archivo más reciente, "Víctimas en carpetas de
  investigación (acumulado)", cubre del 1 de enero de 2019 al 30 de septiembre de 2024, y ningún
  recurso menciona 2025 ni 2026. Las cifras de 2025 y 2026 provienen de Hoyo de Crimen, así que la
  cita a la FGJ no las respalda. Se corrigió el artículo para citar solo a Hoyo de Crimen en esas
  cifras y dejar la cita a la FGJ como origen del conjunto, con su cobertura real.
- **Velocidad de caminata sin fuente.** En la descripción del grafo, la IA fijó una velocidad de
  caminata de $v=1.4$ m/s sin citar ninguna fuente, y el valor no se usaba en ninguna otra parte del
  artículo. Un integrante lo detectó al revisar la sección de método. Se quitó el valor concreto y
  se dejó $v$ como un parámetro genérico (una velocidad de caminata constante).

## Autocompletado en el editor

Si se usó autocompletado (por ejemplo, Copilot en el editor), que no produce una conversación
exportable, declarar en qué archivos y en qué medida.
