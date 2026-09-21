# Análisis del ejemplo de referencia (trabajo de título de una compañera)

Este documento distila lecciones de redacción a partir de un trabajo de título ajeno, usado como
ejemplo sobresaliente: el borrador real de una compañera de generación, con los comentarios de
revisión de su profesor guía. El archivo original vive solo en local
(`ejemplo_referencia/`, fuera de git, ver `.gitignore`) porque es contenido privado de otra persona;
este documento guarda únicamente las lecciones generales, sin nombres ni citas textuales.

## Aclaración de nombres de archivo (importante)

Hay dos archivos distintos con el **mismo nombre** `Guía de Confección - Trabajo de Título.docx`
en este repo. No confundirlos:

| Ruta | Tamaño | Qué es |
|---|---|---|
| `ejemplo_referencia/Guía de Confección - Trabajo de Título.docx` (solo local, no está en git) | 866 KB | El trabajo real de la compañera, con 15 comentarios de revisión, 9 imágenes, 404 párrafos. Es el ejemplo de este documento. |
| `Guía de Confección - Trabajo de Título.docx` (raíz) y `documentacion/Guía de Confección - Trabajo de Título.docx` | 45 KB (idénticos entre sí) | La plantilla genérica y vacía de la escuela ("Título del Primer Capítulo", placeholders). No tiene contenido del ejemplo. |

## Contexto del ejemplo

Trabajo de título desarrollado en una empresa de software, sobre un problema real de rediseño de
un modelo de datos en un sistema en producción (migración de un modelo legado a uno unificado,
con rollout gradual a clientes). El paralelo con este proyecto no es el dominio (ahí no hay nada en
común), sino la forma: cómo se cuenta un proyecto técnico de varios meses, con desafíos de equipo
incluidos, para que evidencie las competencias de perfil de egreso.

## Estructura completa (tabla de contenidos)

```
Dedicatoria
AGRADECIMIENTOS
Índice general / de tablas / de figuras
RESUMEN (español) / ABSTRACT (inglés)
I. Introducción
  1.1 Estructura y áreas de la empresa
    1.1.1 (contexto de la empresa)
    1.1.2 (contexto del equipo)
    1.1.3 Rol de la estudiante
  1.2 Trabajo de título
    1.2.1 Objetivos (general + específicos)
    1.2.2 Resultados esperados
    1.2.3 Metodologías
    1.2.4 Competencias del perfil de egreso  (preview: enuncia las competencias)
II. Actividades desempeñadas
  2.1 Organización y planificación del desarrollo
  2.2 Diagnóstico del problema y análisis
  2.3 Diseño de la solución (con subsecciones a), b), c)... )
  2.4 Planificación y asignación de recursos
  2.5 Implementación técnica
  2.6 Desafíos encontrados
III. Resultados (una subsección por categoría de resultado, todas con métrica)
IV. Competencias de perfil de egreso  <- capítulo dedicado, el más importante
V. Conclusiones
BIBLIOGRAFÍA
ANEXOS (A: metodología aplicada en detalle; B: implementaciones técnicas en detalle)
```

Esta estructura es prácticamente idéntica a la de `documento_final/informe_titulo.tex` (que ya la
sigue). La diferencia no está en el esqueleto, sino en el contenido y la ejecución de cada parte.

## Lecciones del proceso de revisión, agrupadas por tema

Distiladas de los 15 comentarios de revisión entre la estudiante y su profesor guía, sin cita
textual ni atribución nominal.

### 1. El capítulo de competencias es la prioridad del revisor
El profesor guía pidió explícitamente, dos veces, que los "resultados esperados" y el enunciado de
competencias fueran más concretos: los resultados deben permitir, a través de su logro, verificar
que se tienen las competencias declaradas, y deben ser lo más concretos y verificables posible,
relacionables con la aplicación de esas competencias. También pidió que el enunciado mismo de las
competencias fuera más concreto, con una frase de transición explícita del tipo "en particular, las
competencias a evidenciar en este trabajo de título serán:".

Lección: los "resultados esperados" de la introducción y el capítulo de competencias deben leerse
como el mismo argumento contado dos veces. El texto que anuncia las competencias debe ser el
**oficial y textual**, no una paráfrasis.

### 2. Falta una sección para el lector no especialista
El profesor guía sugirió agregar una subsección breve y explícita sobre el rol de la estudiante en
el proyecto, justificándolo porque es útil para el contexto de un lector no especialista en la
comisión (el profesor DIPRE).

Lección: el informe lo lee gente que no domina el dominio técnico. Una subsección corta y explícita
sobre el rol del estudiante resuelve eso. (`informe_titulo.tex` ya tiene esta subsección, línea
141.)

### 3. Estilo narrativo, no lista de funcionalidades
El profesor guía elogió explícitamente la habilidad de la estudiante para el relato, y en otro
comentario reordenó qué contenido pertenecía a la introducción general versus a la descripción del
proyecto.

Lección: el informe premia el relato (por qué pasó cada cosa, qué se decidió y por qué) sobre el
listado seco de tareas. El orden de la información importa tanto como la información misma.

### 4. Precisión en el título y en las definiciones
Un comentario marcó una duda sobre el nombre exacto del título profesional en la portada.

Lección: verificar contra la fuente oficial el nombre exacto del título, el diploma y las
competencias. No asumir ni parafrasear.

### 5. Tipografía: cursiva para términos en inglés
El profesor guía pidió corregir varios términos en inglés que no estaban en cursiva.

Lección: todo término técnico en inglés (nombres de metodologías, herramientas, conceptos) va en
cursiva. `informe_titulo.tex` ya aplica esto de forma consistente (`\textit{harness}`,
`\textit{ground truth}`, `\textit{clustering}`), mantenerlo.

### 6. Nombrar colaboradores reales es aceptable y ayuda al relato, en ese informe
La estudiante preguntó a su profesor guía si debía nombrar a sus compañeros de equipo; él respondió
que no era necesario, pero que estaba de acuerdo en que hacerlo evitaba que el relato quedara plano.

Lección / tensión con este proyecto: en el ejemplo, tanto el profesor guía como un colaborador
técnico aparecen nombrados en agradecimientos y en el cuerpo del informe, con el visto bueno
explícito del profesor guía. **Esto contradice la convención declarada en el `CLAUDE.md` de este
repo** ("Personas sin nombre en bitácoras e informe: se usan roles, los nombres solo en portada"),
que `informe_titulo.tex` de hecho ya rompe hoy (nombra a Denis Parra, Marcelo Andia y Rafael
Kaempfer en Agradecimientos y en Rol del estudiante, líneas 86 y 143). Resuelto con Fabián: los
tres integrantes oficiales de la comisión (profesor guía, supervisor, representante de pregrado) sí
se nombran, con su rol completo, en agradecimientos y en el cuerpo del informe, igual que en el
ejemplo; la convención de "roles sin nombre" del `CLAUDE.md` aplica al resto de las personas
mencionadas (equipo clínico, anotadores, hospital), no a la comisión oficial. Ver `tt-redaccion`.

## El capítulo de competencias del ejemplo (el patrón a replicar)

Estructura exacta del capítulo dedicado a competencias:

1. Un párrafo de apertura que declara que las competencias se evidenciaron "no solo en el resultado
   final, sino en el proceso".
2. Una subsección por competencia, con el **texto oficial exacto de la competencia como título de
   la subsección**.
3. Dentro de cada subsección, 3 a 4 párrafos que conectan **decisiones técnicas concretas y
   nombradas** (no genéricas) con esa competencia específica: qué se diseñó, qué alternativa se
   descartó, qué métrica lo prueba.
4. Sin repetir evidencia entre subsecciones: cada competencia tiene su propio conjunto de hechos.

`informe_titulo.tex` (líneas 287-307) ya sigue esta misma forma para sus 3 competencias. La brecha
no es estructural, es de verificación de texto oficial (ver más abajo).

## Imágenes: cómo las usa el ejemplo

7 figuras, todas citadas explícitamente en el texto que las precede, nunca decorativas:
- Diagramas de flujo de planificación de tarjetas (equivalente a nuestros diagramas Mermaid de
  arquitectura/monitoreo).
- Capturas de pantalla del producto real, antes/después, para hacer tangible el cambio de UX (la
  figura del "antes y el después" se presenta explícitamente como el principal cambio visual de
  todo el trabajo).
- Diagramas explicativos del problema técnico.

Comparación con nuestras imágenes: `fig_arquitectura.png` (calidad visual comparable o superior a
las del ejemplo, con agrupación por capas y estilos de flecha diferenciados) **no está referenciada
en el `.tex`**; tampoco lo están `imagenes_plataforma/matriz_de_avance.png` ni
`imagenes_plataforma/ Vista de anotación.png`. El ejemplo usa el equivalente de "antes/después de
la UI"; nosotros tenemos material similar sin usar (matriz de avance del panel de administración,
vista de anotación sin censurar) que podría reforzar "Plataforma de anotación operativa" o
"Experimento de concordancia en ejecución" de la misma manera. Ver `tt-redaccion`.

## Brechas concretas detectadas en `documento_final/informe_titulo.tex` (al 2026-09-21)

1. ~~Competencia 3 no calza textualmente~~ **Descartado, era un falso positivo.** La comparación
   inicial se hizo contra `documentacion/Perfil Profesional industrial Computación.md`, que lista
   *todas* las competencias posibles del diploma (catálogo general), no las 3 que Fabián declaró
   en su inscripción TT-1. La fuente correcta es `bitacoras/*/competencias.md` (el campo
   "Competencias" de SIDING es "multi-selección entre las 3 declaradas en el TT-1", según
   `bitacoras/PLAN_BITACORAS.md`), y ahí las 9 bitácoras ya enviadas usan de forma consistente:
   "Investigar sobre nuevas tecnologías de información existentes en la industria y facilitar su
   adopción dentro de las organizaciones." Es exactamente el texto que ya está en
   `informe_titulo.tex` línea 179. Las 3 competencias del informe calzan verbatim con lo declarado.
   Lección para revisiones futuras: verificar competencias contra `bitacoras/*/competencias.md`,
   no contra los perfiles genéricos de carrera/diploma (esos sirven para contexto, no como fuente
   de verdad de lo declarado).
2. **Nombre del diploma en la portada ("Tecnologías de Información") vs. el título del único
   perfil de competencias disponible en el repo ("Computación").** Resuelto con Fabián: son
   diplomas distintos (el de la compañera del ejemplo es uno completamente aparte, "Ingeniería,
   Diseño e Innovación"; la comparación relevante era contra el perfil propio de Fabián, que sí
   corresponde). Las competencias listadas son suficientemente parecidas para orientar redacción;
   no vale la pena seguir indagando el nombre exacto del diploma más allá de esto.
3. **Nombres propios en el informe**: resuelto (ver lección 6 arriba). Comisión oficial con nombre
   completo y rol; el resto de las personas mencionadas, con rol genérico.
4. **Imágenes generadas sin usar** en el documento (`fig_arquitectura.png`,
   `matriz_de_avance.png`, `Vista de anotación.png`): evaluar si suman evidencia visual a algún
   resultado antes de la versión final.

Lo que ya está bien (no tocar sin razón): estructura de capítulos, subsección "Rol del estudiante",
capítulo dedicado de competencias con una subsección por competencia y evidencia concreta, cursiva
en términos en inglés, estilo narrativo con decisiones y aprendizajes (no solo lista de tareas), sin
guion largo.
