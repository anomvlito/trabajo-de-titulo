# Skills Index

One-line description of each available skill. Read this file to know what's available before deciding which skill(s) to load.

## Solvers & Orchestrators
- [exercise-solver](exercise-solver/SKILL.md) — Reads images from `{dir}/imagenes/`, solves each exercise, writes `{dir}/output/solution.tex` via `latex-writer`.
- [math-solver-style](math-solver-style/SKILL.md) — Estándar rector de estilo, flujo semántico en español y desarrollo continuo para todos los resolvedores.
- [skill-creator](skill-creator/SKILL.md) — Automatiza la creación y formateo de nuevas Agent Skills siguiendo la especificación estándar.

## LaTeX
- [latex-writer](latex-writer/SKILL.md) — Generates complete `.tex` documents from structured content. Called by `exercise-solver`. Delegates image embedding to `latex-illustrator`.
- [latex-illustrator](latex-illustrator/SKILL.md) — Inserts images into LaTeX (`\includegraphics`, figure environments, captions, relative paths).

## Math Tutors
- [tutor-calculus-1](tutor-calculus-1/SKILL.md) — Cálculo I: límites, derivadas, análisis gráfico, primitivas. Spivak + Stewart.
- [tutor-calculus-2](tutor-calculus-2/SKILL.md) — Cálculo II: técnicas de integración, series, geometría en R³. Spivak + Stewart.
- [tutor-calculus-3](tutor-calculus-3/SKILL.md) — Cálculo III: cálculo multivariable, integrales múltiples, cálculo vectorial.
- [tutor-ode](tutor-ode/SKILL.md) — EDO: ecuaciones de primer y segundo orden, transformadas de Laplace.
- [tutor-prob-stats](tutor-prob-stats/SKILL.md) — Probabilidad y Estadística: axiomas, distribuciones, inferencia, regresión. Ross + DeGroot + Devore.

## Reference
- [fe-handbook-ref](fe-handbook-ref/SKILL.md) — Recupera fórmulas del NCEES FE Reference Handbook (10.1) e integra páginas al documento LaTeX.

## Shared Resources
- [shared/notation-standard.md](shared/notation-standard.md) — Convenciones de notación matemática comunes a todos los tutores y `exercise-solver`.
