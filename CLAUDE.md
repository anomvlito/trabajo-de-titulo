# Trabajo de Título de Fabián Ortega — contexto del repo

Repo administrativo del Trabajo de Título (PUC, Ing. Civil de Industrias, Diploma en Ingeniería en Tecnologías de Información). El código del proyecto vive en otros repos (epicrisis-sotero/*,
proyecto_sotero_ihealth); aquí viven bitácoras, informe, propuesta y documentación.

## Calendario crítico (fuentes: ficha SIDING + correo DIPRE semana 18, ver
`documentacion/correo_dipre_semana18_2026-09-16.md`)

| Hito | Fecha | Regla |
|---|---|---|
| Entrega borrador al profesor guía | 23-09-2026 | Se envía A TRAVÉS DE SIDING, no por correo |
| Informe a la comisión | ≥1 semana antes de la defensa | Tras aprobación del profesor (~2 semanas de corrección) |
| Defensa | ANTES del 14-10-2026 | El 14-10 es el límite de semana 22, no la fecha; coordinar con la comisión cuanto antes |
| Incumplir plazos | — | Causal de reprobación |

Comisión: Denis Parra (Profesor TT, DCC), Marcelo Andia (Supervisor, iHealth),
Javier Pereda (Representante Pregrado, Ing. Eléctrica).

## Rutas clave

- `documento_final/informe_titulo.tex` → PDF del informe (compilar: `latexmk -pdf`).
  Figuras mermaid: editar `.mmd` y regenerar con `mmdc` (config en `mermaid-config.json`).
- `documento_final/datos/irr_2026-09-15.tsv` → tabla kappa completa del experimento
  (κ promedio 0,72, 43 epicrisis solapadas, 222 criterios).
- `bitacoras/` → carpetas espejo de SIDING; `bitacoras/PLAN_BITACORAS.md` es la guía
  del formato, el estado por bitácora y el calendario.

## Convenciones de las bitácoras y del informe

- Tono mesurado, voz pasiva impersonal ("se implementó"); sin autobombo, sin guiones largos.
- Sin códigos HU-XXX ni jerga cruda en lo que va a SIDING o al informe; los códigos y
  hashes viven en los `anclaje.md` (respaldo interno).
- Personas sin nombre en bitácoras e informe: se usan roles (los nombres solo en portada).
- Cero cifras sin fuente verificable en repos, panel o bot; lo no obtenido se describe
  como "análisis en curso", nunca como valor.
- Las bitácoras en SIDING no se pueden editar después de enviadas.

## Estado al 16-09-2026

- Bitácoras 1-8 enviadas; la 9 (80 h, 6 actividades) editada y lista para enviar.
- Informe: 27 páginas, sin placeholders; falta solo la corrida definitiva de los
  3 modelos en ih-condor (va en la versión final, post revisión del profesor).
