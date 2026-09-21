# Bitácoras — para qué son y cómo se registran

> Actualizado el 25-08-2026, sincronizado directamente contra las pantallas de SIDING.
> Único formato: carpetas `.md`. No hay archivos `.yaml` (se probaron y se eliminaron).

## 1. Lo que dicen los documentos oficiales

**Reglamento del Trabajo de Título vf2024**, único párrafo sobre el tema: el estudiante
debe subir a SIDING *"cada dos semanas un breve reporte a su profesor, señalando las
actividades realizadas durante ese período y una estimación de las horas dedicadas a esas
actividades"*.

**Procedimiento administrativo TT**: "Bitácora cada 2 semanas en SIDING".

Eso es todo. **No hay mínimo de horas por reporte ni número obligatorio de reportes.** Se
registran las horas realmente trabajadas.

El "mínimo 80 horas / 8 reportes" que aparece en
`documentacion/faq_siding_trabajo_de_titulo.md` es un resumen no oficial y no debe usarse
como criterio.

## 2. Para qué sirven realmente

1. **Insumo del informe.** Las descripciones de actividad son el borrador en bruto del
   desarrollo del informe.
2. **Mantener al profesor guía al tanto** del avance entre reuniones.

La comisión también las lee en la defensa.

## 3. Estructura del formulario en SIDING

Una bitácora tiene N actividades. Cada actividad guarda solo:

- `Nombre Actividad`
- `Horas de Dedicación`
- `Descripción Actividad`
- `Competencias` (multi-selección entre las 3 declaradas en el TT-1)

**No hay campo de fechas ni campo de evidencia separado.** SIDING calcula el "Total Horas
Dedicación" sumando las actividades. **Una vez enviada, la bitácora no se puede editar.**

URL: <https://intrawww.ing.puc.cl/siding/dirdoc/instrum_tit/trabajo_titulacion/inscripcion/alumno/index.phtml>
(Procesos Pregrado → CICLO 2 → Trabajo Título → Inscripción / Seguimiento Trabajo Título)

## 4. Estructura de carpetas en este repo

Una carpeta por bitácora, mismo esquema en todas (1 y 2 son formato antiguo heredado, sin
subcarpetas, porque son de antes de que este esquema existiera y ya están enviadas):

```
bitacora_N/
  actividad_1/
    nombre_actividad.md
    horas_dedicacion.md
    descripcion_actividad.md
    competencias.md        # una línea "- <texto oficial completo>" por competencia
  actividad_2/
    ...
  horas_totales.md         # suma de todas las actividades, debe cuadrar
  nota_cobertura.md        # de dónde sale el contenido, para uso interno
```

Las tres competencias del perfil de egreso (TT-1), texto oficial completo:

- Desarrollar soluciones innovadoras basadas en conocimientos avanzados de Ingeniería de
  Computación.
- Aplicar diversos métodos de análisis de datos para la comprensión de los fenómenos
  abordados.
- Investigar sobre nuevas tecnologías de información existentes en la industria y facilitar
  su adopción dentro de las organizaciones.

## 5. Estado real, sincronizado contra SIDING el 25-08-2026

| Bitácora | Actividades | Horas | Estado |
|---|---|---|---|
| 1 | 1 | 40 | Enviada |
| 2 | 1 | 42 | Enviada |
| 3 | 3 (20+10+15) | 45 | Enviada |
| 4 | 3 (14+10+16) | 40 | Enviada |
| 5 | 6 (10+14+16+16+15+9) | 80 | Enviada |
| 6 | 3 (12+51+17) | 80 | Enviada |
| 7 | 5 (16+14+10+30+12) | 82 | Enviada |
| 8 | 8 (12+8+10+12+10+6+12+14) | 84 | Enviada |
| 9 | 6 (14+12+14+14+12+14) | 80 | Cargada en SIDING el 14-09-2026 |

Las bitácoras 5 a 8 en este repo son la transcripción exacta de lo que hay hoy en las
pantallas de SIDING (algunas actividades fueron fusionadas y algunas horas ajustadas a mano
directamente ahí, no solo lo generado originalmente en el repo). Si vuelves a editar algo en
SIDING, este repo queda desactualizado hasta que se sincronice de nuevo.

**Bitácora 2, inconsistencia ya enviada e irreversible:** el nombre de actividad dice
"Formación técnica en IA y configuración del entorno HPC", pero la descripción real
publicada en SIDING trata de otra cosa: el diseño del experimento LLM-driven con ~300
registros de ground truth, y la gestión de un incidente de producción de mayo 2026 (un
pipeline sobrescribió la base de datos exponiendo PII; se aplicaron tres correcciones de
emergencia: anonimización de 434 ocurrencias, reparación del renderizador frontend y
migración idempotente de base de datos). No se puede editar. Dejar constancia para el
informe y para la defensa, por si preguntan.

## 6. Plazos SIDING (verificados en pantalla el 25-08-2026)

| Bitácora | Fecha Plazo | Estado del plazo | Estado del envío |
|---|---|---|---|
| 5 | 22-07-2026 | Vencido | Enviada |
| 6 | 05-08-2026 | Vencido | Enviada |
| 7 | 19-08-2026 | Vencido | Enviada |
| 8 | 02-09-2026 | No vencido | No enviada, quedan días |

Las 7 primeras bitácoras están enviadas. Solo falta la 8, que puede esperar a más cerca del
02-09 para incorporar el resto de la semana en curso antes de mandarla.

## 7. Calendario oficial del TT (según ficha de inscripción en SIDING, capturado el 14-09-2026)

| Hito | Fecha oficial |
|---|---|
| Inicio | 13-05-2026 |
| Término esperado | 16-09-2026 |
| Entrega de borrador | 23-09-2026 |
| Defensa estimada | 14-10-2026 |

Comisión: Denis Parra Santander (Profesor de Trabajo de Título, DCC), Marcelo Andia
Kohnenkampf (Supervisor, iHealth), Javier Pereda Torres (Representante Pregrado,
Ingeniería Eléctrica).
