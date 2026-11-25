# Modelo de negocio y validación

Esta carpeta conecta el canvas con la evidencia. Cada afirmación del canvas apunta a una hipótesis
de `hipotesis.csv`, y cada hipótesis apunta a las entrevistas o a las semanas de la landing page que
la prueban. La primera fila de datos de cada CSV es un ejemplo y se borra antes de entregar.

## Documentos

| Archivo | Entrega | Contenido |
|---|---|---|
| `modelo_negocio.tex` | Semana 11, se actualiza hasta la final | Canvas, perfil del cliente, canales y relación, competencia, tamaño de mercado e hipótesis con su prueba. Máximo 5 páginas, contando el canvas |
| `validacion.tex` | Final | Resultados de las hipótesis, landing page, cambios en el canvas y anexo con las entrevistas. Máximo 3 páginas más el anexo |
| `modelo_negocio.docx` | Semana 11 | Alternativa en Word o LibreOffice a `modelo_negocio.tex`, con el canvas como tabla. La tabla de hipótesis se copia de `hipotesis.csv` con el mismo texto |
| `canvas.tex` | — | Los nueve bloques del canvas. No se compila solo: `modelo_negocio.tex` lo inserta |

Las tablas de hipótesis, landing page y entrevistas se generan solas a partir de los CSV. Para
actualizarlas se editan los CSV y se compila cada documento dos veces:

```
pdflatex modelo_negocio.tex
pdflatex validacion.tex
```

Las cifras de tamaño de mercado son las mismas de la hoja Supuestos de `modelo_financiero.xlsx`.

`validacion.tex` no tiene versión en Word porque sus tablas se generan a partir de los CSV. Un
ejemplo completo de los dos documentos, con sus CSV, está en `Ejemplos/modelo_negocio_cvrp/`.

## hipotesis.csv

| Columna | Contenido | Valores permitidos |
|---|---|---|
| `id` | Identificador | `H1`, `H2`, ... |
| `bloque` | Bloque del canvas | `segmentos_clientes`, `propuesta_valor`, `canales`, `relacion_clientes`, `fuentes_ingresos`, `recursos_clave`, `actividades_clave`, `socios_clave`, `estructura_costos` |
| `hipotesis` | Afirmación falsable, con números cuando sea posible | Texto |
| `prueba` | Cómo se prueba | Texto (entrevistas, landing page, precio de competidores, ...) |
| `criterio_exito` | Resultado que valida la hipótesis, fijado **antes** de probarla | Texto con un umbral |
| `estado` | Resultado de la prueba | `pendiente`, `validada`, `invalidada` |
| `evidencia` | Entrevistas o semanas que la respaldan | Identificadores separados por `;`, por ejemplo `E01;E03;L2` |
| `cambio` | Qué cambió en el canvas por este resultado | Texto, vacío si nada cambió |

Las semanas de la landing page se citan como `L1`, `L2`, ... en el orden de `metricas_landing.csv`.

## entrevistas.csv

Las entrevistas son anónimas. No se registran nombres, teléfonos ni correos de las personas
entrevistadas. Antes de la entrevista se pide permiso para tomar notas.

| Columna | Contenido | Valores permitidos |
|---|---|---|
| `id` | Identificador | `E01`, `E02`, ... |
| `fecha` | Fecha de la entrevista | `AAAA-MM-DD` |
| `perfil` | Cargo y tipo de organización, sin nombres | Texto |
| `sector` | Sector | Texto, por ejemplo `salud`, `educacion`, `finanzas`, `gobierno`, `industria` |
| `canal` | Medio | `presencial`, `videollamada`, `telefono` |
| `duracion_min` | Duración | Entero, minutos |
| `hipotesis` | Hipótesis exploradas | Identificadores separados por `;` |
| `dolor_1a5` | Intensidad del dolor que describe la persona | 1 (ninguno) a 5 (urgente) |
| `paga_hoy` | ¿Gasta hoy dinero o tiempo en resolver el problema? | `si`, `no` |
| `pagaria` | ¿Dio una señal concreta de compra (precio, piloto, carta de intención)? | `si`, `no`, `no_sabe` |
| `referidos` | Contactos que la persona ofreció | Entero |
| `hallazgo` | Lo más importante que se aprendió | Texto |
| `cita` | Frase textual de la persona | Texto |

## metricas_landing.csv

| Columna | Contenido |
|---|---|
| `semana_inicio` | Lunes de la semana, `AAAA-MM-DD` |
| `visitas` | Visitantes únicos en la semana |
| `registros` | Correos o solicitudes registradas en la semana |
| `fuente_trafico` | De dónde llegaron las visitas |
| `cambio` | Qué cambió en la página esa semana (texto, precio, mensaje) |
