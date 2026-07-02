# AGENTS.md — Trasplan

Este archivo define las reglas operativas para agentes de código y documentación que trabajen en este repo. Es la fuente portable para Hermes, Codex, Claude Code y otros agentes.

## Proyecto

Trasplan es una plataforma web y móvil para coordinar el proceso de procuramiento, donación y trasplante de órganos en Chile.

Subproyectos principales:

- `documentacion/`: centro de mando documental. Historias de usuario, features, ADRs, guías, bitácora e informes.
- `backend/`: API GraphQL Node.js + Express + Apollo Server + Sequelize + PostgreSQL.
- `web/`: panel web React + TypeScript + Material UI + Apollo Client.
- `App/`: app móvil React Native moderna.
- `mobile/`: app Expo/React Native legacy. No tocar salvo que la tarea lo pida explícitamente.

## Regla principal: docs + Kanban son la fuente de verdad

Toda Historia de Usuario accionable debe existir en tres lugares coordinados:

1. Archivo Markdown en `documentacion/historias-usuario/<actor>/HU-NNN-slug.md`.
2. Feature relacionada en `documentacion/features/<estado>/<slug>.md`, salvo que se justifique explícitamente que no aplica.
3. Issue del repo `trasplan2026/documentacion` agregado al Project/Kanban:
   `https://github.com/orgs/trasplan2026/projects/1`.

No basta con crear el Markdown. No basta con crear el issue. La HU debe estar conectada a feature, código real y Project 1.

Antes de implementar una funcionalidad clínica:

1. Leer la HU correspondiente.
2. Verificar si existe una feature/ADR relacionada.
3. Buscar HUs/features pasadas del mismo dominio.
4. Revisar `documentacion/guias/matriz-regresion.md`.
5. Revisar el código real que se tocará.
6. Confirmar alcance, no-alcance, contratos existentes y pruebas de regresión.
7. Recién entonces modificar código.

## Actores válidos para HUs

Usar estos actores y carpetas:

- `medico`: profesional clínico que detecta o participa en sospechas/confirmación.
- `coordinador`: coordinador local o central que gestiona el proceso.
- `procurador`: equipo de procura/enfermería de procura que ejecuta o registra etapas clínicas/logísticas.
- `admin`: administrador del sistema, usuarios, centros médicos y configuración.

## Flujo obligatorio para crear una HU

Usar la skill `.claude/skills/doc.md` como referencia operativa.

Checklist mínimo:

- [ ] Buscar el mayor `HU-NNN` existente en todas las carpetas de `documentacion/historias-usuario/`.
- [ ] Asignar el siguiente número global.
- [ ] Crear o vincular feature en `documentacion/features/`.
- [ ] Inspeccionar código real antes de escribir rutas de implementación.
- [ ] Crear Markdown con historia, criterios verificables, no-alcance, feature relacionada, código relacionado y propuesta técnica si aplica.
- [ ] Incluir rutas concretas de código por capa, o declarar explícitamente “no requiere cambios”.
- [ ] Incluir impacto sobre funcionalidades existentes usando `documentacion/guias/matriz-regresion.md`.
- [ ] Incluir contratos que deben preservarse.
- [ ] Incluir pruebas de regresión concretas.
- [ ] Crear issue en `trasplan2026/documentacion` con labels `historia-usuario` y actor.
- [ ] Agregar issue al Project 1 de `trasplan2026`.
- [ ] Registrar en la HU la URL del issue/proyecto si se dispone.
- [ ] Actualizar el body del issue si la HU se enriquece después de crearlo.

Si `gh project` falla por permisos, informar claramente al usuario que debe ejecutar:

```bash
gh auth refresh -s project -s read:project
```

No inventar URLs ni afirmar que un issue fue agregado al Project si el comando falló.

## HealthTech guardrails

Trasplan trabaja con flujos clínicos sensibles. Mantener estas reglas:

- IA/OCR solo como asistencia, no como decisión clínica automática.
- Preferir human-in-the-loop: una persona valida antes de guardar datos clínicos extraídos o sugeridos.
- No automatizar notificaciones/decisiones clínicas sin validación explícita del equipo clínico.
- No bloquear flujos clínicos por reglas nuevas sin aprobación y prueba con usuarios reales.
- Validar permisos en backend, no solo esconder botones en frontend.
- No exponer ni imprimir secretos, tokens, credenciales, connection strings ni datos sensibles.
- Usar datos demo/anonimizados para pruebas y videos.
- Documentar riesgos clínicos/legales en HUs cuando aplique.

## Reglas de implementación

No programar a ciegas:

- Leer archivos relevantes antes de editar.
- Buscar HUs/features relacionadas antes de tocar un dominio existente.
- Identificar qué funcionalidad anterior puede romperse.
- Preservar contratos explícitos de GraphQL, permisos, estados, navegación y datos existentes.
- Trazar símbolos a definición y usos.
- No inventar APIs, imports, modelos, campos GraphQL ni tablas.
- Tocar solo lo necesario.
- No mezclar proyectos externos ni copiar contenido de Epicrisis salvo como inspiración metodológica.

Backend (`backend/`):

- Revisar `backend/src/graphql/schemas/`, `backend/src/graphql/resolvers/`, `backend/src/models/`, `backend/src/policies/` y migraciones cuando aplique.
- Cambios de datos normalmente requieren: migración Sequelize, modelo, schema GraphQL, resolver, policy, tests/factory.
- No asumir que un control frontend es suficiente para seguridad.

Web (`web/`):

- Mantener estilo React/TypeScript/Material UI existente.
- Revisar `web/src/features/`, `web/src/routes.tsx`, `web/src/config/apollo.tsx` y componentes vecinos antes de editar.
- Para cambios visibles, validar en navegador o con build/tests.

App móvil (`App/`):

- Tocar solo si la HU lo pide.
- Revisar `App/screens/`, `App/graphql/`, navegación y store antes de editar.

`mobile/` legacy:

- No tocar salvo instrucción explícita.

## Verificación antes de declarar terminado

Ejecutar verificación real según alcance:

- Backend: `npm run build`; tests Jest relevantes si se toca lógica.
- Web: `CI=true npm run build`; tests/Playwright relevantes si se toca UI/flujo.
- App: lint/test/build correspondiente si se toca móvil.
- Docs: revisar rutas, links, numeración HU y estado.
- GitHub: confirmar URL del issue y que fue agregado al Project cuando esa era parte de la tarea.

No decir “listo” si solo se escribió un plan o un stub.

## Git y efectos externos

- No commitear, pushear, mergear ni cerrar issues sin instrucción explícita del usuario.
- Crear issues o modificar GitHub Projects es efecto externo: hacerlo solo cuando el usuario lo pida o confirme.
- Si hay cambios locales ajenos, no sobrescribirlos.

## Skills locales del proyecto

Claude-style skills viven en:

- `.claude/skills/doc.md`
- `.claude/skills/orchestrator.md`
- `.claude/skills/fullstack-implementer.md`
- `.claude/skills/deploy_workflow/SKILL.md`

Para Hermes/Codex, este `AGENTS.md` es el contrato común. Si se quiere convertir estas reglas en skills Hermes nativas, crear versiones bajo `~/.hermes/skills/trasplan-*` después de estabilizar el flujo.
