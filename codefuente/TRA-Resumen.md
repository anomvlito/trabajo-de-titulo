# TRA
# Discusión sobre el Desarrollo y Pilotaje de la Plataforma de Donación de Órganos "Transplant"

[Image]


> Reunión de equipo multidisciplinario para revisar el estado actual de la plataforma "Transplant", identificar mejoras funcionales prioritarias, definir roles de usuario, resolver requerimientos legales para el pilotaje y explorar el uso avanzado de inteligencia artificial como catalizador del desarrollo.

---

## Automatización del Ingreso de Datos mediante PDF

La reunión abrió con una propuesta concreta de Speaker 1: en lugar de que el personal clínico ingrese campo por campo la información de un examen —como, por ejemplo, un resultado de pH 7.3—, se debería poder subir el documento PDF completo y que la aplicación auto-rellene los campos de forma automática. Speaker 2 amplió la idea señalando que el programa debería ser capaz de generar una tabla estructurada con datos como la **fecha, hematocrito y transaminasas**, extrayendo la información directamente del archivo.

Fabián confirmó la **viabilidad técnica** de la propuesta, aunque expresó una prevención importante: la variabilidad en el formato de ciertos documentos clínicos —en particular las **epicrisis**, donde cada profesional o institución usa su propio estilo— complica significativamente la estandarización del proceso de extracción. En contraste, Speaker 2 señaló que los **resultados de exámenes de laboratorio** sí mantienen un formato consistente y estandarizado en toda la red, incluso fuera de ella, lo que los convierte en el caso de uso más viable para comenzar.

Desde el punto de vista técnico, se mencionó el uso de **OCR (Reconocimiento Óptico de Caracteres)** y técnicas de inteligencia artificial para leer texto desde imágenes o fotografías de documentos. Sin embargo, Fabián advirtió que estas tecnologías pueden fallar, por lo que resulta indispensable que **una persona valide y etiquete** la información extraída antes de que quede registrada en la plataforma, garantizando la precisión clínica de los datos.

---

## Aspectos Legales y Estratégicos del Pilotaje

El equipo discutió en detalle los preparativos legales e institucionales previos al lanzamiento del piloto. En primer lugar, respecto al almacenamiento de datos, se concluyó que **Amazon Web Services (AWS)** es la opción preferida frente a los servidores locales de la universidad, por considerarse más segura y confiable. Como indicó Fabián: *"Uno paga por seguridad"*.

En el plano contractual, Speaker 2 informó que el **departamento legal del INF (UC)** exige la firma de un contrato formal que regule el uso de la plataforma "P100 Transplant" en el marco de la investigación del departamento de innovación. La relación jurídica se estructurará como una relación de **prestador de servicios externo**, lo que facilita la gestión de los derechos de autor de la UC y permite extender la **cláusula de confidencialidad** institucional al manejo de información sensible de pacientes.

Un segundo punto estratégico fue la incorporación del **Profesor Nigel (también referido como Meyem)** antes de iniciar el piloto virtual. Speaker 2 explicó que en proyectos anteriores de la facultad, las pruebas piloto han fallado recurrentemente porque no se coordinan bien los objetivos necesarios para avanzar de fase. El Profesor Nigel ha acompañado múltiples procesos de este tipo y puede aportar una perspectiva valiosa para evitar esos errores. Se determinó que su participación es parte del **comité de revisión del piloto**, por lo que su involucramiento es un paso obligatorio antes de la ejecución.

---

## Definición de Perfiles y Roles de Usuario

Esta fue una de las discusiones más extensas y con mayor tensión conceptual de la reunión. Fabián describió los perfiles de usuario existentes en la plataforma:

- **Médico general**: puede registrar sospechas de donantes con acceso restringido; no puede ver detalles de sospechas ajenas.
- **Médico intensivista (UCI)**: participa en la etapa de confirmación, completando la ficha clínica, el registro de muerte encefálica y la activación familiar; solo ve sospechas de su propio centro.
- **Procurador / Coordinador**: acceso amplio para la gestión integral del proceso.

El núcleo del debate giró en torno a quién debe tener la facultad de **ingresar datos clínicos** a la plataforma. Speaker 1 fue enfática: en el modelo de trabajo actual, el ingreso de información sensible es responsabilidad exclusiva de la **enfermera de procura local**, quien opera las 24 horas. El médico intensivista, por definición de su rol profesional —no por restricción legal—, no participa en la subida de datos, e históricamente ni siquiera ha tenido cuenta en plataformas como SIDO.

Speaker 2 planteó la posición contraria: dado que una sola enfermera de procura puede cubrir múltiples centros simultáneamente (como en el caso de El Salvador, San Borja y Sótero), ampliar las funciones a otros usuarios —como el intensivista— alivianarían una carga de trabajo insostenible. Su argumento fue que es preferible tener la función disponible en la plataforma aunque no se use, que no tenerla cuando eventualmente el modelo de trabajo cambie.

Tras el debate, se acordó una posición pragmática: **por ahora, el rol de ingreso de datos se mantendrá restringido a la enfermera de procura**, alineado al flujo de trabajo clínico vigente y a la realidad de la institución donde se realizará el piloto (UC). La expansión de roles se deja abierta como una decisión futura, condicionada a la consulta directa con los usuarios clave.

---

## Diseño de la Experiencia de Usuario (UX) y Flujos de la Aplicación

Speaker 1 planteó una mejora de alta prioridad para la usabilidad: al momento en que un profesional activa la "sospecha de donante", la plataforma debería mostrar de forma visible los **criterios que deben cumplirse**, específicamente los parámetros de la **Escala de Glasgow** (umbral: puntaje ≤ 7). La lógica es que el personal que realiza la pesquisa —frecuentemente técnicos en enfermería o enfermeras de UCI— puede no tener los criterios memorizados con precisión, lo que genera inseguridad a la hora de notificar. Un checklist informativo en pantalla daría confianza suficiente para que el usuario declare la sospecha sin titubear.

Se exploró incluso la posibilidad de que la selección interactiva de los componentes del Glasgow (apertura ocular, respuesta verbal, respuesta motora) gatille automáticamente la notificación cuando la suma sea inferior a 7, aunque se reconoció que esto requeriría pruebas con usuarios reales para evaluar si agrega fluidez o complejidad.

En cuanto a la **autenticación de usuarios**, se discutieron varias opciones. Fabián propuso un sistema de **tokens** digitales que funcionarían como llaves de acceso para autorizar la creación de nuevas cuentas, permitiendo además caracterizar el tipo de usuario desde el momento del registro. Como alternativa complementaria, se mencionó la integración con proveedores externos como **Google o Microsoft** para simplificar el inicio de sesión.

Para la **validación de identidad profesional**, Speaker 1 presentó el **Registro Nacional de Prestadores Individuales de la Supersalud**, una base de datos pública y de acceso abierto donde se puede buscar a cualquier profesional de la salud por nombre o RUT y verificar su acreditación, profesión y región. Fabián propuso que, durante el registro, los usuarios suban su certificado de este registro como prueba de credenciales. Sin embargo, Speaker 1 advirtió un riesgo de usabilidad real: en la práctica clínica, los profesionales no tienen a mano estos documentos, y exigir su búsqueda y carga podría generar una fricción que desincentive el uso de la herramienta.

Se reconoció que existe un **trade-off** entre seguridad e intuición de uso que deberá resolverse durante la fase de piloto, idealmente con retroalimentación directa de los usuarios finales. Un elemento adicional que justifica algún nivel de autenticación es la necesidad de generar **estadísticas confiables**: saber qué unidades y qué tipos de profesionales notifican más sospechas de donantes es un dato de valor para el sistema.

---

## Colaboración y Metodología de Trabajo

El equipo acordó una dinámica de trabajo flexible, basada en principios de **metodología ágil**: en lugar de reuniones semanales obligatorias, se priorizarán contactos breves —de 10 a 20 minutos— cuando surjan necesidades puntuales, ya sea vía Zoom o de forma presencial en el campus San Joaquín. Speaker 2 reiteró la apertura del equipo clínico para responder consultas del desarrollador con la mayor rapidez posible.

Se identificó como recurso valioso la **documentación original del proyecto Capstone**, descrita por Fabián como un archivo de aproximadamente **70 páginas** que contiene las historias de usuario, la descripción de cada componente del sistema y los detalles del desarrollo frontend y backend. Contar con este material permitiría hacer una comparativa del estado actual de la plataforma versus su concepción original. Speaker 2 confirmó tener acceso a carpetas con las entregas del Capstone y se comprometió a compartirlas.

Se identificó también la existencia del equipo **"Furi"**, que ya ha implementado soluciones similares tanto en el ámbito público como privado —aunque únicamente en la etapa de sospecha, sin abordar la coordinación avanzada—. El equipo consideró valioso establecer contacto con ellos para conocer sus desafíos y aprendizajes. Se acordó que este contacto puede iniciarse de forma exploratoria, sin comprometer aún el apoyo institucional formal de la **Comisión de Procura y Trasplante**, cuyo respaldo se preserva como una "carta" estratégica para una fase posterior de escalamiento.

---

## Uso Avanzado de la Inteligencia Artificial como Catalizador

La conversación derivó en una reflexión técnica sobre el valor real del profesional informático en la era de la IA. Fabián argumentó que el rol del ingeniero no desaparece, sino que se transforma: el valor está en **saber usar bien la IA**, lo que requiere una base sólida en estructuras de datos, patrones de diseño, seguridad y arquitectura de software. Sin este conocimiento, un profesional puede cometer errores de novato graves o producir código inconsistente, incluso usando las mejores herramientas disponibles. Con esa base, en cambio, un solo ingeniero puede alcanzar resultados equivalentes a los de un equipo de cinco personas.

Fabián describió la evolución del paradigma de la IA: se está transitando desde los simples **prompts** hacia los **loops**, en los que la IA itera soluciones de forma autónoma sin intervención humana constante, y hacia los **harnesses** (arneses), que son entornos configurados que dotan al modelo de contexto persistente, archivos de trabajo y reglas de comportamiento. Un ejemplo concreto mencionado fue el proyecto **Hermes**, un agente que aprende de sus propios errores registrándolos en un archivo estructurado (*"Formatted Marvel"*), volviéndose progresivamente más eficiente sin requerir reentrenamiento del modelo.

Entre las herramientas recomendadas para un flujo de trabajo avanzado, Fabián destacó: **Visual Studio Code** como editor principal, el uso de terminales (CLI) en lugar de interfaces de chat web para mayor control y eficiencia, el **Model Context Protocol (MCP)** para conectar modelos de IA con aplicaciones externas (correo, calendario, Notebook LM), y la práctica de mantener **bitácoras de contexto** para evitar que el código o los gráficos cambien arbitrariamente entre sesiones —un problema concreto que Speaker 1 había experimentado al trabajar con bases de datos Ómicas en R y ChatGPT—.

Un dato práctico relevante: los usuarios con **correo institucional UC** tienen acceso gratuito a **Google Gemini (Antigravity)**, herramienta que Fabián recomendó explorar. Asimismo, Fabián ofreció realizar una **sesión de capacitación técnica** con el equipo para enseñarles a usar estas herramientas de forma efectiva en sus tareas de investigación, análisis de datos y escritura académica.

---

## Tareas y Compromisos

### **@Speaker 2** *(Coordinador del proyecto)*
- [ ] Contactar al Profesor Nigel (Meyem) vía correo electrónico para solicitar su involucramiento formal en la revisión del plan de prueba piloto, previo a su lanzamiento - [TBD]
- [ ] Compartir con el equipo de desarrollo las carpetas de documentación y entregas del proyecto Capstone - [TBD]
- [ ] Gestionar la redacción y firma del contrato formal entre el departamento de innovación y Transplant, conforme a los requerimientos del departamento legal del INF (UC) - [TBD]

### **@Speaker 1 / @Speaker 2** *(Equipo clínico)*
- [ ] Recopilar y entregar al equipo de desarrollo archivos PDF de ejemplo de exámenes de laboratorio para testear la extracción y el llenado automático de datos - [TBD]
- [ ] Coordinar y realizar una entrevista con la enfermera de procura (Peña o Dani) para validar los roles de usuario y el flujo de trabajo clínico en la plataforma - [TBD]

### **@Fabián** *(Desarrollador)*
- [ ] Producir un video demo que muestre el funcionamiento actual de la aplicación para presentaciones institucionales - [TBD]
- [ ] Establecer contacto con el equipo "Furi" para entrevistarles y recabar información sobre sus desafíos, problemáticas y aprendizajes en la implementación de su solución - [TBD]
- [ ] Agendar y realizar una sesión técnica de capacitación con el equipo sobre el uso avanzado de herramientas de IA (Visual Studio Code, terminal/CLI, MCP) aplicadas a investigación y análisis de datos - [TBD]