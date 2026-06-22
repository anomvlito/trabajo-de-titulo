# Propuesta de Inscripción TT-1

Este documento contiene los campos listos para copiar y pegar en el formulario de inscripción (SIDING) del Trabajo de Título.

---

### 1. Datos Generales
- **Modalidad de Trabajo:** (Elegir: Internado Profesional o Investigación Aplicada)
- **Nombre Institucion/Empresa:** [Ingresar nombre del Hospital/Centro Clínico]
- **Nombre del trabajo de título:** Implementación de Software Clínico con IA para Gestión de Patologías en UCI

---

### 2. Objetivos, metodologías y resultados esperados
**Objetivo General:** 
Implementar un sistema de software clínico que integre inteligencia artificial para el análisis automatizado de registros médicos y la predicción de eventos clínicos en pacientes de UCI.

**Metodología y Objetivos Específicos:** 
El trabajo se divide en tres áreas de desarrollo consecutivas. 
- **Área 1: Software de Extracción (mayo – junio):** Desarrollo de una herramienta de anotación clínica para ground truth, respaldada por una base de datos consultable y expuesta mediante una API REST (FastAPI). Implementación de un front-end de evaluación para testear modelos LLM open-source.
- **Área 2: Análisis Predictivo con ML (junio – julio):** Generación de análisis predictivo sobre los campos extraídos para predecir outcomes clínicos (ej. mortalidad, shock séptico). Se compararán diversos algoritmos de clasificación tradicionales versus extracción semántica, aplicando técnicas de interpretabilidad clínica (valores SHAP).
- **Área 3: Modelo Transformer (julio – septiembre):** Estudio de arquitecturas orientadas a predicción de eventos clínicos (Delphi 2M, TFT, Foresight). Se realizará adaptación y fine-tuning del modelo sobre los datos reales de la UCI, finalizando con una validación rigurosa mediante métricas de desempeño (AUROC, precisión, recall, F1-score).

**Resultados Esperados:** 
Un sistema integral que permita la extracción de texto clínico, análisis predictivo interpretable y modelos avanzados de IA ajustados a las necesidades reales de gestión de pacientes en UCI.

---

### 3. Competencias del Perfil de Egreso
1. Desarrollar soluciones innovadoras basadas en conocimientos avanzados de Ingeniería de Computación.
2. Aplicar diversos métodos de análisis de datos para la comprensión de los fenómenos abordados.
3. Investigar sobre nuevas tecnologías de información existentes en la industria y facilitar su adopción dentro de las organizaciones.

---

### 4. Evidencias que demostrarán las competencias
**Evidencia para "Desarrollar soluciones innovadoras basadas en conocimientos avanzados de Ingeniería de Computación" (Vinculada al Área 1):** 
Diseño, arquitectura e implementación integral de la herramienta de software clínico (API REST, base de datos e interfaz), adaptada a la problemática, necesidades y limitaciones reales de la Unidad de Paciente Crítico para el manejo de *ground truth* y evaluación de modelos.

**Evidencia para "Aplicar diversos métodos de análisis de datos para la comprensión de los fenómenos abordados" (Vinculada al Área 2):** 
Desarrollo del modelo predictivo de *Machine Learning* para la predicción de eventos clínicos (ej. mortalidad, shock séptico), evaluando comparativamente algoritmos de clasificación y aplicando métodos de interpretabilidad (valores SHAP) sobre datos médicos reales.

**Evidencia para "Investigar sobre nuevas tecnologías de información existentes en la industria y facilitar su adopción dentro de las organizaciones" (Vinculada al Área 3):** 
Estudio profundo, adaptación y ejecución del proceso de *fine-tuning* sobre arquitecturas Transformer especializadas y de vanguardia (Delphi 2M, TFT, Foresight) orientadas a la predicción de secuencias y eventos en la UCI, facilitando la adopción de estas nuevas tecnologías en el entorno hospitalario.

### 5. Configuración de Tiempos (¡Atención: Caso de Excepción por Ramo Pendiente!)
Dado que debes un ramo (máx. 10 créditos no capstone), caes exactamente en la **Excepción 2** de DIPRE. Por lo tanto, debes llenar la sección de tiempos de la siguiente manera estricta:

- **N° de semanas de trabajo parcial:** 8 semanas (Durante este semestre, en paralelo con tu ramo).
- **N° de semanas de trabajo completo:** 10 semanas (Una vez que termine el semestre académico actual).
- **Fecha de inicio:** 04/05/2026
- **Fecha de término (18 semanas):** 07/09/2026
- **Fecha entrega borrador informe:** 14/09/2026
- **Fecha estimada de defensa:** 05/10/2026
- **¡Regla de Oro!:** Si por algún motivo repruebas ese ramo de 10 créditos que estás cursando, tu Trabajo de Título se reprobará automáticamente.

### 6. Checklists Finales antes de enviar en SIDING
- [ ] Adjuntar el **CV del Supervisor Externo** (Obligatorio en SIDING).
- [ ] Marcar **NO** en "Conflicto de Interés" (asumiendo que no hay familiares involucrados).
