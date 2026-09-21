---
name: tt-redaccion
description: Guía de redacción y estructura para documento_final/informe_titulo.tex, basada en un ejemplo de referencia sobresaliente (otro trabajo de título ya aprobado). Usar al escribir, reescribir o mejorar cualquier sección del informe, al revisar gramática o estilo, o al decidir qué figura incluir y dónde.
---

# Redacción del informe

Antes de escribir, lee `documentacion/analisis_ejemplo_referencia.md` si no lo has leído en esta
sesión: tiene la estructura completa del ejemplo de referencia y sus lecciones de revisión ya
distiladas. Esta skill resume las reglas operativas que salen de ahí.

## Estructura canónica (ya vigente en informe_titulo.tex, mantenerla)

Portada x2, Dedicatoria, Agradecimientos, Índices, Resumen, Abstract, luego:

1. **Introducción**: contexto institucional, rol del estudiante (obligatoria, ver abajo),
   objetivos (general + específicos), metodología, resultados esperados, preview de competencias.
2. **Actividades desempeñadas**: por línea de desarrollo, en orden cronológico/lógico.
3. **Resultados**: uno por categoría, cada uno con métrica o evidencia verificable
   (ver `tt-cifras`).
4. **Competencias de perfil de egreso**: capítulo dedicado, ver `tt-competencias` (es la
   prioridad del proyecto, por instrucción explícita de Fabián).
5. **Conclusiones**, Bibliografía, Anexos.

No agregues ni quites capítulos de este esqueleto sin que el usuario lo pida: ya está alineado
con el ejemplo y con el reglamento.

## Reglas de estilo, en orden de importancia

1. **Relato sobre lista.** El proceso de revisión del ejemplo de referencia valoró explícitamente
   la "habilidad para el relato" de su autora. Cuenta por qué pasó cada cosa (qué problema forzó
   qué decisión, qué se intentó primero y no funcionó) en vez de enumerar tareas completadas. El
   informe actual ya hace esto bien en "Desafíos encontrados" y en el capítulo de competencias:
   usarlo de referencia de tono para el resto.
2. **Concreto y verificable, siempre.** Cada afirmación de resultado debe poder trazarse a un
   número, un artefacto o un commit. "Se mejoró el rendimiento" no sirve; "se redujo el tiempo de
   respuesta en 30%" sí. Ver `tt-cifras` para el proceso de verificación.
3. **Sin guion largo (em dash).** Regla global del usuario, ya vigente en todo el informe: usar
   comas, dos puntos, paréntesis o guion normal.
4. **Cursiva para términos en inglés** (metodologías, herramientas, conceptos técnicos sin
   traducción establecida: `\textit{...}`). El informe actual ya lo hace bien
   (`\textit{harness}`, `\textit{ground truth}`, `\textit{clustering}`); mantenerlo en todo texto
   nuevo.
5. **Nombres propios: convención resuelta.** La comisión oficial (profesor guía, supervisor,
   representante de pregrado) se nombra con nombre completo y rol en Agradecimientos y en Rol del
   estudiante, igual que en el ejemplo de referencia. El resto de las personas mencionadas en el
   informe (equipo clínico, anotadores, hospital) usa rol genérico, sin nombre, según la
   convención del `CLAUDE.md` del proyecto. Agradecimientos personales (familia, amistades
   cercanas del proceso) sí pueden nombrarse, es una sección de tono personal.
6. **Cero cifras sin fuente verificable** (regla ya declarada en el `CLAUDE.md` del proyecto). Lo
   no obtenido se describe como "análisis en curso", nunca como un valor inventado o estimado.

## Figuras

- Cada figura necesita un caption que la ate explícitamente al argumento del párrafo que la
  precede, no un pie de foto decorativo. El ejemplo de referencia usa figuras de antes/después de
  UI para hacer tangible un cambio; nosotros tenemos un recurso equivalente sin usar.
- Antes de cerrar un capítulo, compara qué imágenes existen en disco contra cuáles están citadas
  en el `.tex`:
  ```
  grep -n includegraphics documento_final/informe_titulo.tex
  find documento_final -iname "*.png"
  ```
  Al 2026-09-21 hay 3 imágenes generadas y no usadas (`fig_arquitectura.png`,
  `imagenes_plataforma/matriz_de_avance.png`, `imagenes_plataforma/ Vista de anotación.png`,
  esta última con espacio inicial en el nombre, cuidado al referenciarla). Evalúa si alguna suma
  evidencia visual a un resultado antes de la versión final; si no, no las fuerces.

## Antes de dar una sección por lista

- ¿Cada afirmación de resultado tiene número o artefacto verificable?
- ¿El capítulo de competencias (o su preview en la intro) quedó tocado por este cambio? Si sí,
  pasar por `tt-competencias`.
- ¿Hay términos en inglés sin cursiva?
- ¿Algún nombre nuevo agregado es de la comisión oficial (nombre completo está bien) o de otra
  persona (debería ir como rol genérico)?
- Compilar con `latexmk -pdf` desde `documento_final/` y revisar que no queden warnings de
  referencias rotas.
