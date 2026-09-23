---
name: tt-compilar
description: Compilar documento_final/informe_titulo.tex a PDF sin dejar basura de LaTeX (.aux, .log, .lof, .lot, .out, .toc, .fls, .fdb_latexmk) en el working tree. Usar siempre que se compile el informe, en vez de invocar latexmk directo.
---

# Compilar el informe sin dejar basura

Fabián no quiere ver los archivos auxiliares de LaTeX sueltos en `documento_final/` después de
compilar. Esos archivos son regenerables, no van a git (están en `.gitignore`), y no aportan nada
fuera de una compilación en curso.

## Procedimiento

```bash
cd documento_final
latexmk -pdf -interaction=nonstopmode informe_titulo.tex
```

Revisar el resultado: si `latexmk` reporta error o hay `! ` / `Undefined` en `informe_titulo.log`,
diagnosticar ahí, con el `.log` todavía presente.

Si la compilación fue limpia, limpiar de inmediato:

```bash
latexmk -c
```

`latexmk -c` borra los intermedios (`.aux`, `.log`, `.lof`, `.lot`, `.out`, `.toc`, `.fls`,
`.fdb_latexmk`) y conserva `informe_titulo.pdf`. Nunca usar `latexmk -C` (mayúscula): esa variante
también borra el PDF.

Al terminar, `documento_final/` debe quedar solo con `informe_titulo.tex`, `informe_titulo.pdf`, y
las carpetas `figuras/` y `datos/`.

## Si hay que depurar un error de compilación

No limpiar hasta resolverlo: dejar el `.log` (y el resto) en el disco, revisar
`grep -i "undefined\|! " informe_titulo.log`, corregir el `.tex`, recompilar. Limpiar solo después
de una compilación exitosa.
