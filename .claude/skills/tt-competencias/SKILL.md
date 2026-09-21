---
name: tt-competencias
description: Revisión y redacción del capítulo "Competencias de perfil de egreso" de documento_final/informe_titulo.tex y de los "resultados esperados" que lo anticipan en la introducción. Es la tarea principal del informe por instrucción explícita de Fabián. Usar al auditar, escribir o mejorar ese capítulo, o al verificar que el texto de las competencias declaradas sea el oficial.
---

# Competencias de perfil de egreso: la tarea principal

Fabián pidió explícitamente que este capítulo sea la prioridad sobre el resto del informe. Trátalo
como tal: si hay tiempo para revisar solo una parte del documento, es esta.

## Paso 1: verificar el texto oficial de las competencias

El texto de cada competencia debe ser **literal**, no una paráfrasis. La fuente autoritativa
**correcta** es `bitacoras/*/competencias.md` (o `bitacoras/*/actividad_*/competencias.md` en las
bitácoras con ese esquema): ese campo en SIDING es una "multi-selección entre las 3 declaradas en
el TT-1" (ver `bitacoras/PLAN_BITACORAS.md`), así que lo que aparece ahí, repetido de forma
consistente entre bitácoras, es lo que Fabián declaró al inscribir el trabajo. Para confirmar,
compara entre varias bitácoras (no te quedes con una sola) que el texto sea idéntico:
```
find bitacoras -name "competencias.md" -exec cat {} \; | sort -u
```

**No uses** `documentacion/Perfil Profesional Ingeniero Civil de Industrias.md` ni
`documentacion/Perfil Profesional industrial Computación.md` como fuente de verdad de lo
declarado: son el catálogo general de *todas* las competencias posibles de la carrera y el
diploma, de donde se elige un subconjunto al inscribir. Sirven solo como contexto de qué significa
cada competencia, no como el texto a citar en el informe. (Este proyecto ya cometió ese error una
vez: una primera revisión marcó la competencia 3 como "no oficial" comparándola contra el catálogo
general; al comparar contra `bitacoras/*/competencias.md` se confirmó que las 3 competencias del
informe calzan verbatim con lo declarado. Ver `documentacion/analisis_ejemplo_referencia.md`.)

El nombre del diploma en la portada ("Tecnologías de Información") y el título del perfil de
competencias disponible en el repo ("Computación") ya quedaron revisados con Fabián: no hace falta
seguir indagando esa diferencia, las competencias listadas son suficientemente parecidas para
orientar la redacción.

## Paso 2: el patrón del ejemplo de referencia para cada subsección

1. Título de la subsección = texto oficial exacto de la competencia (`\subsection*{...}` en el
   `.tex`, igual que ya está en `informe_titulo.tex` líneas 291, 297, 303).
2. 3 a 4 párrafos que conectan **decisiones técnicas concretas y nombradas** (qué se diseñó, qué
   alternativa se descartó, qué métrica lo demuestra) con esa competencia específica.
3. Sin reciclar la misma evidencia entre subsecciones: cada competencia necesita su propio
   conjunto de hechos, aunque vengan del mismo proyecto.
4. Un párrafo de cierre de capítulo que amarre las tres (o las que sean) competencias con el
   proceso completo, no solo el resultado final.

## Paso 3: coherencia con "resultados esperados"

Los "resultados esperados" de la introducción deben anticipar, aunque sea implícitamente, la
evidencia que el capítulo de competencias va a mostrar. Lección directa del proceso de revisión del
ejemplo de referencia: el logro de esos resultados debe permitir verificar que se tienen las
competencias de egreso declaradas, por lo que deben ser lo más concretos y verificables que sea
posible, y relacionables explícitamente con la aplicación de esas competencias. Si reescribes uno,
revisa el otro.

## Checklist antes de dar el capítulo por listo

- [ ] Las 3 competencias usan el texto oficial verbatim (contrastado contra
      `bitacoras/*/competencias.md`, no contra los perfiles genéricos).
- [ ] Cada subsección tiene evidencia propia, concreta y con número o artefacto verificable
      (usar `tt-cifras`).
- [ ] El párrafo de apertura y cierre conectan proceso, no solo resultado.
- [ ] Los "resultados esperados" de la introducción son consistentes con este capítulo.
