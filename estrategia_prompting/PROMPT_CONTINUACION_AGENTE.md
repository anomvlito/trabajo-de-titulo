# Prompt de continuidad: ejecución del harness y avance del paper

## Rol y objetivo

Actúa como investigador y desarrollador de clinical NLP. Continúa el trabajo
del harness de extracción de 199 variables y del manuscrito que ya existe. Tu
objetivo inmediato es dejar una ejecución piloto reproducible en Cóndor,
diagnosticar sus resultados y preparar la comparación con una llamada
monolítica. Después actualiza el manuscrito con resultados observados, sin
inventar cifras.

No empieces escribiendo un paper nuevo. El manuscrito de trabajo está en:

`/Users/fabianortega/src/trabajo-de-titulo/paper_harness/main.tex`

Lee también todas sus secciones, `REVISION_INTERNA.md`, `README.md`,
`references.bib`, las referencias locales y las figuras antes de modificarlo.

## Contexto científico

El estudio compara, sobre las mismas epicrisis, dos estrategias para extraer
199 variables clínicas desde notas de alta UCI en español:

1. una llamada que solicita las 199 variables;
2. un harness de 18 llamadas por grupos clínicos, con hasta 16 variables por
   llamada, validación, reintentos, checkpoints y evidencia por IDs de línea.

La revisión de radiología se usa para justificar transparencia —manual de
anotación, IAA, unidad de análisis y particiones—, no como evidencia de que el
harness sea superior. La hipótesis sobre el harness debe probarse con datos
emparejados. Las llamadas adicionales pueden mejorar estructura o evidencia,
pero aumentan tokens, latencia y oportunidades de inconsistencia.

## Rutas locales

- Paper: `/Users/fabianortega/src/trabajo-de-titulo/paper_harness/`.
- Prompt maestro: `/Users/fabianortega/src/trabajo-de-titulo/estrategia_prompting/PAPER_PROMPT.md`.
- Este prompt: `/Users/fabianortega/src/trabajo-de-titulo/estrategia_prompting/PROMPT_CONTINUACION_AGENTE.md`.
- Repositorio de experimentos: `/Users/fabianortega/src/proyecto_sotero_ihealth/`.
- Harness: `/Users/fabianortega/src/proyecto_sotero_ihealth/LLM-extraction/extraction-condor/form199_v1/`.
- Aplicación fuente: `/Users/fabianortega/src/epicrisis_sotero/`.
- Snapshot local: `/Users/fabianortega/Library/Application Support/epicrisis-experiments/concordancia-50-20260923/`.
- Entrada local: `input/notes.jsonl`, `input/cohort_ids.txt`,
  `input/form_schema.json`, `input/documents_manifest.json` y
  `reference/submitted_annotations.json`.

En Cóndor, el código está en:

`/home/fgortega/src/proyecto_sotero_ihealth/LLM-extraction/extraction-condor/form199_v1/`

La entrada de la cohorte está en:

`/mnt/workspace/fgortega/datasets/concordancia-50-20260923/input/`

La salida nueva debe estar en:

`/mnt/workspace/fgortega/experiments/concordancia50-form199-v1/`

## Estado comprobado al iniciar esta tarea

- La cohorte de 50 casos ya fue transferida a Cóndor y sus hashes están
  congelados.
- `form199_v1` contiene `runner.py`, `protocol.py`, `manifest.json`,
  `form_schema.json`, `manual-anotacion.md`, 18 prompts y `run.slurm.sh`.
- La verificación sintética y `--check` pasaron el 23 de septiembre de 2026;
  no cargaron modelos ni produjeron predicciones.
- El `config.json` apunta a la cohorte de 50 casos y al directorio de salida
  indicado arriba.
- No hay resultados nuevos en `concordancia50-form199-v1`.
- Existe un experimento antiguo llamado
  `GroundTruth-harness20-GLQ-v2`. Sus jobs 91464–91503 fueron parciales,
  terminaron por límite de tiempo o errores CUDA y tienen cero JSON finales
  válidos. No mezclar sus trazas ni sus `invalid_jsons` con la nueva versión.
- El baseline monolítico de 199 campos todavía no está implementado como
  ejecución comparable. No declarar una comparación completa hasta crearlo.

## Secuencia de trabajo obligatoria

### 1. Auditar antes de inferir

Lee el README y el código completo de `form199_v1`. Comprueba en Cóndor:

```bash
ssh condor 'cd /home/fgortega/src/proyecto_sotero_ihealth/LLM-extraction/extraction-condor/form199_v1 && python3 -m unittest -v test_protocol.py'
ssh condor 'cd /home/fgortega/src/proyecto_sotero_ihealth/LLM-extraction/extraction-condor/form199_v1 && python3 runner.py --check --input-dir /mnt/workspace/fgortega/datasets/concordancia-50-20260923/input'
```

Revisa modelo, GPU, tiempo y límites de `run.slurm.sh` antes de enviar un job.
No borres ni sobrescribas `GroundTruth-harness20-GLQ-v2`.

### 2. Ejecutar solo un piloto nuevo

El primer job debe ser un solo caso con Gemma4:

```bash
ssh condor 'mkdir -p /mnt/workspace/fgortega/experiments/concordancia50-form199-v1 && cd /home/fgortega/src/proyecto_sotero_ihealth/LLM-extraction/extraction-condor/form199_v1 && MODEL=Gemma4 CASE_LIMIT=1 sbatch run.slurm.sh'
```

Registra el JobID, consulta `squeue` y luego `sacct`, y conserva los logs. No
lances los 50 casos ni los tres modelos hasta revisar el piloto. Si el piloto
falla, diagnostica primero la causa y corrige el código o la configuración;
preserva el output fallido para trazabilidad.

Revisa especialmente:

- JSON completo para las 199 claves;
- tipos y valores permitidos;
- grupos faltantes y reintentos;
- evidencia IDs, texto copiado y offsets;
- conflictos padre-hijo y exclusiones;
- tokens, latencia y memoria;
- diferencia entre `unknown`, pendiente y `false`.

### 3. Diseñar y probar el baseline monolítico

Implementa una variante separada que reciba la misma epicrisis, el mismo
manual y el mismo esquema, pero solicite las 199 variables en una sola llamada.
Debe usar el mismo modelo, temperatura, límite de tokens, formato de evidencia,
validador y política de reintentos que el harness, salvo que la comparación
requiera documentar explícitamente una diferencia. Usa otro directorio de
resultados y otro hash de configuración. Primero pruébalo con el mismo caso
piloto.

### 4. Ampliar la ejecución

Solo después de que ambos pilotos sean válidos, propone ejecutar Gemma4,
Llama-70B y Qwen sobre los 50 casos. Mantén un directorio separado por
estrategia y modelo. No uses anotaciones humanas como entrada del modelo.

### 5. Actualizar el paper

Actualiza `paper_harness/secciones/04_resultados.tex` y las tablas o figuras
solo con JSON y logs realmente existentes. Mantén `\pending{}` o
`RESULTS_PENDING` para todo lo no medido. Añade:

- número de casos y llamadas completadas;
- JSON válidos, truncamientos, errores y reintentos;
- latencia, tokens y memoria;
- rendimiento clínico solo después de definir el consenso humano y calcular
  IAA;
- análisis emparejado por paciente;
- limitaciones del piloto y de la ejecución parcial.

No llames `ground truth` al consenso sin describir desacuerdos. No calcules
F1 tratando las 199 variables como pacientes independientes. No uses una
epicrisis piloto para afirmar superioridad.

Compila con `tectonic main.tex` desde `paper_harness/`. Corrige errores de
referencias, tablas y figuras, pero no borres evidencia pendiente. Actualiza
`REVISION_INTERNA.md` con los hallazgos y los siguientes bloqueos.

## Entregable esperado

Al terminar, entrega un informe breve que indique:

1. qué comprobaciones pasaron;
2. JobID, modelo, caso piloto y ubicación de logs/resultados;
3. si el piloto produjo una salida válida y qué errores tuvo;
4. qué parte del baseline monolítico quedó implementada;
5. qué cambios se hicieron en el paper;
6. qué resultados siguen pendientes;
7. el comando exacto para continuar con la cohorte completa.

Protege los datos clínicos: no copies texto identificable a LaTeX, logs
compartidos, commits o respuestas. Usa solo IDs anonimizados, agregados y
ejemplos redactados.
