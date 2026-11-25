# Conversaciones con IA generativa

Cada conversación se guarda completa, un archivo por conversación, con el nombre
`AAAA-MM-DD_herramienta_tema.ext`, por ejemplo `2026-10-21_claude_guion-entrevista.md`.

Formatos aceptados, en orden de preferencia:

1. Exportación de la herramienta (Markdown, JSON o HTML).
2. Enlace público de la conversación, guardado en un archivo `.md` junto con el texto copiado.
3. PDF impreso desde el navegador.

Los agentes de código (por ejemplo, Claude Code o Cursor) guardan la sesión completa, que se
exporta igual que una conversación. Cada archivo de esta carpeta tiene una fila en `../bitacoras.csv`.

## Columnas de bitacoras.csv

| Columna | Contenido | Valores permitidos |
|---|---|---|
| `archivo` | Nombre del archivo en esta carpeta | Texto |
| `herramienta` | Herramienta usada | Texto |
| `fecha` | Fecha de la conversación | `AAAA-MM-DD` |
| `entregable` | Entregable al que contribuyó | `propuesta`, `negocio`, `finanzas`, `articulo`, `mvp`, `pitch`, `landing`, `revision` |
| `proposito` | Qué se buscaba | Texto |
| `verificacion` | Cómo se verificó el resultado | Texto |
| `descartado` | Qué se descartó y por qué | Texto, vacío si nada |
