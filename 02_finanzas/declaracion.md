# Declaración de uso de IA generativa

Responder cada sección en uno o dos párrafos. El detalle de cada conversación va en
`bitacoras.csv` y el texto completo en `bitacoras/`.

## Herramientas

Durante el desarrollo del proyecto se utilizaron herramientas de inteligencia artificial generativa
 como Claude, Gemini y ChatGPT. Estas herramientas se emplearon como apoyo en las distintas etapas 
de elaboración de los entregables, principalmente para la consulta de información, revisión y mejora
 de redacción, apoyo en tareas de programación, análisis y organización de contenidos. 
Su utilización fue complementaria al trabajo realizado por los integrantes del equipo.

## Usos

Las herramientas de IA generativa se utilizaron para apoyar actividades de búsqueda y organización 
de información, redacción y corrección de textos, revisión de contenidos, resolución de dudas 
técnicas y apoyo en el desarrollo del código y los componentes del proyecto. También se utilizaron 
para explorar alternativas de implementación y mejorar la presentación de algunos entregables. 
No se utilizaron para realizar las entrevistas ni para generar las ideas originales del proyecto, 
ya que estas actividades fueron desarrolladas directamente por los integrantes del equipo.

## Verificación

Los resultados proporcionados por las herramientas de IA fueron considerados como sugerencias y no
 como información definitiva. El equipo realizó revisiones para comprobar la pertinencia y exactitud
 de los contenidos, contrastando las referencias con sus fuentes originales, revisando los
 procedimientos metodológicos y verificando los cálculos. En el caso del código, se realizaron 
pruebas para comprobar su funcionamiento y detectar posibles errores. Asimismo, los integrantes 
revisaron los resultados antes de incorporarlos a los entregables finales.

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

No se utilizó autocompletado mediante herramientas de IA integradas en los editores de código, 
como GitHub Copilot o Cursor.
