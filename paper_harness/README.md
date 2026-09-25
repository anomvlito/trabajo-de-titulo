# paper_harness — manuscrito monolítico vs. harness multi-llamada (form199-v1)

Borrador en inglés para revisión interna. No contiene texto clínico, IDs de pacientes ni identidades de revisores.

## Estructura

```text
paper_harness/
├── main.tex                  documento principal (preámbulo, macros \pending y \todoauthor)
├── references.bib            BibTeX verificado (copia de referencias/references.bib)
├── secciones/                una sección IMRaD por archivo
│   ├── 00_resumen.tex … 07_declaraciones.tex
│   └── apendices/            A prompts, B pseudocódigo, C TRIPOD-LLM, D errores, E plan estadístico
│       └── prompts/          common.md y falla_01.md copiados del harness (sin datos de pacientes)
├── figuras/
│   ├── mermaid/              fuentes .mmd + mermaid-config.json (mismo estilo que el informe)
│   └── png/                  PNG renderizados que usa el .tex
├── referencias/
│   ├── pdf/                  papers descargados (uso local; no subir a un repo público)
│   ├── md/                   texto completo en markdown, con cabecera YAML
│   └── INDEX.md              ficha por paper y citas textuales con sección/página
├── scripts/cohort_aggregates.py   genera datos/cohort_aggregates.json desde el snapshot
├── datos/cohort_aggregates.json   solo agregados (sin IDs ni texto)
└── REVISION_INTERNA.md       hallazgos, afirmaciones no publicables, faltantes, plan clínico
```

## Compilar

```bash
cd paper_harness
tectonic -X compile main.tex          # genera main.pdf (tectonic ejecuta bibtex solo)
```

Regenerar un diagrama después de editar su `.mmd`:

```bash
cd figuras
npx -y @mermaid-js/mermaid-cli@11 -i mermaid/fig2_harness_flow.mmd -o png/fig2_harness_flow.png \
  -c mermaid/mermaid-config.json -b white -s 3
```

Recalcular los agregados (en el Mac que tiene el snapshot):

```bash
python3 scripts/cohort_aggregates.py
```

## Convenciones

- `\pending{...}` (naranja): cifra no medida. Solo se reemplaza con un valor que exista en un JSON de resultados.
- `\todoauthor{...}` (azul): decisión que corresponde al autor o al equipo clínico.
- Recuadros `RESULTS_PENDING`: figuras y tablas que se generan cuando existan las corridas.
- Cada cifra del texto tiene fuente: snapshot del 23-09-2026, código de `form199_v1` o `datos/cohort_aggregates.json`.
