---
name: tt-cifras
description: Verificación de que toda cifra, métrica o afirmación numérica en documento_final/informe_titulo.tex tenga fuente rastreable (repo, panel, bot o bitácora). Usar antes de agregar cualquier número nuevo al informe, y como pasada final antes de considerar una versión "cerrada".
---

# Verificación de cifras

Regla del proyecto (`CLAUDE.md`): "Cero cifras sin fuente verificable en repos, panel o bot; lo no
obtenido se describe como 'análisis en curso', nunca como valor." Esta skill la vuelve un proceso
concreto en vez de un recordatorio abstracto.

## Proceso

1. **Listar las cifras del texto que estás por tocar o revisar.** Cualquier número: horas,
   porcentajes, cantidades de casos/archivos/pruebas, kappas, tiempos.
2. **Para cada una, identificar su fuente y poder nombrarla en una frase.** Las fuentes válidas en
   este proyecto son:
   - Un archivo de datos versionado, por ejemplo `documento_final/datos/irr_2026-09-15.tsv`
     (kappa, número de epicrisis solapadas, criterios).
   - Un repositorio de código (commits, líneas, pruebas): `epicrisis-sotero/*`,
     `proyecto_sotero_ihealth`.
   - El panel de administración de la plataforma (capturas o exportaciones).
   - Los reportes del bot de monitoreo (Telegram).
   - Las horas declaradas en `bitacoras/*/horas_totales.md`.
3. **Si no puedes nombrar la fuente en una frase, la cifra no va.** Reemplazar por "análisis en
   curso" o equivalente, nunca dejar un número sin respaldo ni inventar un rango plausible.
4. **Cifras que cambian con el tiempo** (el experimento de concordancia sigue en ejecución, por
   ejemplo) van con la fecha de corte explícita en el texto, como ya hace
   `informe_titulo.tex` ("al corte del 15 de septiembre de 2026..."). No las dejes como si fueran
   definitivas si el proceso sigue corriendo.

## Antes de cerrar una versión del informe

Repasa cada cifra del capítulo tocado contra su fuente una vez más, específicamente buscando:
- Números que se copiaron de una versión anterior del informe y podrían haber quedado
  desactualizados frente a una corrida más reciente.
- Resultados marcados como pendientes (por ejemplo, la corrida definitiva de los 3 modelos en
  ih-condor) que no se hayan colado como si ya estuvieran cerrados.
