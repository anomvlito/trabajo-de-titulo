---
name: tt-bitacoras
description: Redacción y revisión de una bitácora antes de enviarla a SIDING. Usar al escribir una actividad nueva, revisar horas totales, o antes de marcar una bitácora como lista para envío (no se puede editar después de enviada).
---

# Bitácoras

Guía completa y actualizada: `bitacoras/PLAN_BITACORAS.md` (léelo si no está en contexto, es corto
y es la fuente de verdad de formato y estado por bitácora). Esta skill resume lo operativo.

## Antes de escribir

- **No hay mínimo de horas ni número obligatorio de reportes.** El "80 horas / 8 reportes" que
  aparece en `documentacion/faq_siding_trabajo_de_titulo.md` es un resumen no oficial: no lo uses
  como criterio para decidir cuánto reportar. Se registran las horas realmente trabajadas.
- Formato único: carpetas `.md`, sin YAML.

## Estructura de cada actividad

```
bitacora_N/
  actividad_M/
    nombre_actividad.md
    horas_dedicacion.md
    descripcion_actividad.md
    competencias.md
  horas_totales.md      # debe cuadrar con la suma de actividades
  nota_cobertura.md      # de dónde sale el contenido, uso interno
```

`competencias.md` es multi-selección entre las 3 competencias declaradas en el TT-1. Cópialas
**verbatim** desde una bitácora anterior ya enviada (`find bitacoras -name "competencias.md" -exec
cat {} \;` para verlas todas); no las parafrasees.

## Reglas de contenido (ya en el `CLAUDE.md` del proyecto, reforzadas aquí para bitácoras)

1. Tono mesurado, voz pasiva impersonal ("se implementó", no "yo implementé"). Sin autobombo. Sin
   guiones largos.
2. Sin códigos `HU-XXX` ni jerga cruda de los repos: eso vive solo en los `anclaje.md` internos,
   nunca en lo que va a SIDING.
3. Personas sin nombre: se usan roles ("el equipo médico", "el supervisor"). A diferencia del
   informe final, en bitácoras esta regla no tiene tensión conocida con ningún precedente: aplícala
   sin excepción.
4. Cero cifras sin fuente verificable (ver `tt-cifras`). Lo no obtenido es "análisis en curso".

## Antes de marcar como lista para enviar

Una bitácora enviada **no se puede editar nunca más**. Revisar, en este orden:
1. `horas_totales.md` cuadra exactamente con la suma de `horas_dedicacion.md` de cada actividad.
2. Cada actividad tiene sus 4 archivos y el texto de `competencias.md` es idéntico, carácter por
   carácter, al de una bitácora ya enviada.
3. Ningún nombre propio, código `HU-XXX` ni cifra sin fuente se coló en la descripción.
4. La descripción de cada actividad sirve como insumo directo para el informe final: si no
   alcanza ese estándar de claridad, vale la pena mejorarla antes de enviar, no después.
