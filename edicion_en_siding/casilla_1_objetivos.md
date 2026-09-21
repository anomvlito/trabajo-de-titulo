Objetivo General:
Implementar un sistema de software clínico que integre modelos de lenguaje para la extracción automatizada de información desde registros médicos de pacientes en Unidades de Cuidados Intensivos (UCI), y evaluar su desempeño mediante coeficientes de concordancia frente a un conjunto de referencia anotado por humanos.

Metodología y Objetivos Específicos:
El trabajo se divide en tres áreas de desarrollo:
- Área 1 (Plataforma de anotación clínica): Desarrollo de una herramienta de anotación clínica para generar el ground truth, respaldada por una base de datos PostgreSQL consultable mediante una API propia y una interfaz web segura para el equipo de anotadores.
- Área 2 (Protección de datos e infraestructura en producción): Diseño e implementación de un mecanismo de anonimización de epicrisis reales, validación de la migración de la base de datos a un servicio administrado en la nube como entorno de respaldo, y despliegue de monitoreo y respaldos verificados (réplica horaria) para operar de forma confiable una plataforma que hoy corre sobre un servidor local.
- Área 3 (Extracción automática con modelos de lenguaje): Evaluación de modelos de lenguaje de código abierto en su capacidad de extraer variables clínicas desde epicrisis reales, con foco en las comorbilidades de pacientes críticos, exigiendo evidencia textual verificable para cada valor extraído. Incluye el diseño de un procedimiento de extracción por dominios clínicos (harness), la medición de la confiabilidad del conjunto de referencia mediante un experimento de concordancia entre anotadores, y la comparación del desempeño de los modelos contra ese estándar de referencia humano.

Resultados Esperados:
Un sistema integral funcional que permita la extracción de texto clínico, la construcción de un conjunto de referencia confiable con medidas de concordancia entre anotadores, y la evaluación rigurosa de modelos de lenguaje ajustados a las necesidades reales de gestión de pacientes críticos, con foco exploratorio en la extracción de información sobre comorbilidades.
