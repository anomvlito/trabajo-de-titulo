---
name: trabajo-de-titulo
description: Orquestador para cualquier trabajo sobre el informe o las bitácoras del Trabajo de Título de Fabián Ortega (PUC, Ing. Civil de Industrias, Diploma en Ingeniería en Tecnologías de Información). Usar SIEMPRE que se pida redactar, mejorar, revisar, auditar o entender documento_final/informe_titulo.tex, una bitácora, las competencias de perfil de egreso, o cualquier cifra que vaya a ese informe. Enruta a la sub-skill correspondiente.
---

# Trabajo de título de Fabián: orquestador

Este repo es administrativo (bitácoras, informe, propuesta). El contexto completo del proyecto,
calendario y convenciones vive en `/home/fabian/src/trabajo_de_titulo/CLAUDE.md`: léelo si no
está ya en contexto. Esta skill no lo repite, solo enruta al trabajo de redacción concreto.

## El ejemplo de referencia

`ejemplo_referencia/Guía de Confección - Trabajo de Título.docx` es el trabajo de título real de una
compañera de generación, con 15 comentarios de revisión de su profesor guía. Se usa como ejemplo
sobresaliente de cómo escribir este tipo de informe. Es contenido privado de otra persona: vive
solo en local, **no está en git** (ver `.gitignore`). El análisis completo, ya anonimizado
(estructura, lecciones distiladas, brechas contra nuestro informe actual), está en
`documentacion/analisis_ejemplo_referencia.md` (léelo antes de redactar o revisar contenido, ahí está
el detalle que las sub-skills solo resumen). No cites textualmente ni nombres el docx original al
escribir nada que vaya a git o a SIDING: usa solo el análisis ya anonimizado.

**Aviso de nombres duplicados**: existe otro archivo con el mismo nombre en la raíz del repo y en
`documentacion/`, de 45 KB, que es solo la plantilla vacía de la escuela, no el ejemplo de
referencia. No confundirlos (detalle en el análisis).

## Enrutamiento

| La tarea es... | Usar |
|---|---|
| Escribir, reescribir o mejorar una sección del informe (introducción, actividades, resultados, conclusiones); dudas de estilo, gramática o qué figura incluir | `tt-redaccion` |
| Revisar, auditar o escribir el capítulo "Competencias de perfil de egreso", o los "resultados esperados" que lo anticipan | `tt-competencias` |
| Verificar que una cifra, métrica o afirmación del informe tenga fuente verificable antes de darla por final | `tt-cifras` |
| Redactar o revisar una bitácora antes de enviarla a SIDING | `tt-bitacoras` |

## Regla del usuario: prioridad explícita

Fabián pidió explícitamente que el capítulo de **Competencias de perfil de egreso** sea la tarea
principal por sobre el resto del contenido ("como main tarea sobre lo demás, para que converse
adecuadamente con el trabajo de título"). Ante cualquier duda de dónde invertir el esfuerzo de
revisión o redacción, ese capítulo (y los "resultados esperados" que lo preparan en la
introducción) va primero. Usa `tt-competencias` con prioridad sobre las otras sub-skills cuando
se pida una revisión general del informe ("mejora el informe", "revísalo completo").

## Convenciones ya resueltas con Fabián (no volver a preguntar)

- Las 3 competencias declaradas en el informe ya están verificadas contra
  `bitacoras/*/competencias.md` (fuente correcta, ver `tt-competencias`) y calzan verbatim.
- El nombre del diploma en portada no necesita más verificación: las competencias del perfil
  disponible en el repo son suficientemente parecidas para orientar la redacción.
- Nombres propios en el informe: la comisión oficial (profesor guía, supervisor, representante de
  pregrado) se nombra con nombre completo y rol, en Agradecimientos y en el cuerpo; el resto de
  las personas mencionadas usa rol genérico, sin nombre. Detalle en `tt-redaccion`.
