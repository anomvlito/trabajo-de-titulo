---
name: deploy_workflow
description: Reglas de ramas, PRs, verificación y despliegue para Trasplan. Prioriza coordinación con documentación, GitHub Issues y Project 1 antes de mover código a producción.
---

# Flujo de Trabajo y Despliegue — Trasplan

Usa este skill cuando una tarea pase de documentación/HU a implementación, PR, cierre de issue o despliegue.

## Principio central

El Kanban de GitHub Projects es la vista operativa del trabajo:

https://github.com/orgs/trasplan2026/projects/1

Una HU no está lista para desarrollo si no está coordinada entre:

1. Markdown en `documentacion/historias-usuario/`.
2. Issue en `trasplan2026/documentacion`.
3. Item en Project 1.

## Ramas

- No trabajar directo en `main` para features o fixes relevantes.
- Usar ramas descriptivas:
  - `feat/HU-NNN-slug`
  - `fix/HU-NNN-slug`
  - `docs/HU-NNN-slug`
- Si se tocan varios subrepos (`backend`, `web`, `App`, `documentacion`), mantener nombres de rama coherentes cuando sea práctico.

## Antes del PR

Verificar según subrepo:

### Backend

```bash
cd backend
npm run build
npm test -- --runInBand
```

Si los tests completos son demasiado pesados, correr los tests relevantes y documentar por qué.

### Web

```bash
cd web
CI=true npm run build
```

Si la HU es visual o de flujo, probar en navegador o Playwright cuando sea posible.

### App

```bash
cd App
npm test
npm run lint
```

Solo si se tocó `App/`.

### Documentación

- Links relativos correctos.
- HU con estado actualizado.
- Issue URL registrada si existe.
- Project 1 actualizado.

## Pull Request

No abrir PR ni pushear sin autorización explícita del usuario.

Cuando se autorice:

1. Commits pequeños y descriptivos.
2. PR con referencia a HU e issue.
3. Incluir comandos de verificación ejecutados.
4. Incluir screenshots/video si la HU afecta UX.

## Cierre del issue y Project

Solo cerrar issue cuando:

- la implementación esté mergeada o el usuario indique cerrar;
- la HU Markdown esté actualizada;
- se hayan registrado tests/verificación;
- el item esté reflejado en Project 1.

Comandos:

```bash
gh issue comment <N> --repo trasplan2026/documentacion \
  --body "Verificación: <comandos>. Resultado: <resumen>."

gh issue close <N> --repo trasplan2026/documentacion \
  --comment "HU completada y verificada."
```

Si falta permiso de Projects:

```bash
gh auth refresh -s project -s read:project
```

## Despliegue

No asumir deploy automático. Revisar primero la documentación vigente:

- `documentacion/informe_deployment_aws_2026-06-18.md`
- `documentacion/aws_estado_actual_2026-06-18.md`
- guías en `documentacion/guias/` si existen.

No ejecutar deploy productivo sin confirmación explícita del usuario.

## Seguridad

- No imprimir `.env` ni secretos.
- No subir credenciales.
- No usar datos clínicos reales en screenshots o demos sin anonimización.
- Mantener human-in-the-loop para IA/OCR.
