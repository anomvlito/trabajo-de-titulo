# Skill: doc — Orquestador de Documentación Trasplan

Eres el responsable de mantener, crear y organizar la documentación de la plataforma Trasplan. Este skill define el mapa de carpetas, los templates, la metodología y las reglas para mantener sincronizadas las Historias de Usuario con GitHub Issues y el Project/Kanban.

Cuando el usuario invoque `/doc`, determina qué operación quiere realizar y ejecútala usando las reglas de este skill.

---

## Contexto del proyecto

**Trasplan** es una plataforma web y móvil para coordinar el proceso de procuramiento, donación y trasplante de órganos en Chile en tiempo real. Conecta médicos UCI, coordinadores locales, CORE Chile y equipos de procura.

- **Web:** React + Material UI v4 + Apollo Client v3 + TypeScript — `web/`
- **Backend:** Node.js + Express + Apollo Server v4 + Sequelize + TypeScript — `backend/`
- **App móvil moderna:** React Native CLI + TypeScript — `App/`
- **App móvil legacy:** Expo/React Native — `mobile/` (no tocar salvo instrucción explícita)
- **DB:** PostgreSQL
- **Infra:** AWS según documentación vigente

Rutas del proyecto:

- `/home/fabian/src/codefuente/web` — frontend web
- `/home/fabian/src/codefuente/backend` — backend GraphQL
- `/home/fabian/src/codefuente/App` — app móvil moderna
- `/home/fabian/src/codefuente/mobile` — app móvil legacy
- `/home/fabian/src/codefuente/documentacion` — repo de documentación

GitHub:

- Repo docs: `trasplan2026/documentacion`
- Project/Kanban: `https://github.com/orgs/trasplan2026/projects/1`
- Project owner: `trasplan2026`
- Project number: `1`

---

## Principio central: HU sincronizada o no existe

Toda Historia de Usuario accionable debe quedar coordinada en:

1. Archivo Markdown en `documentacion/historias-usuario/<actor>/HU-NNN-slug.md`.
2. Issue en `trasplan2026/documentacion`.
3. Item agregado al Project 1 de `trasplan2026`.

Si el Markdown existe pero el issue no, la HU está incompleta.
Si el issue existe pero no está en el Project 1, la HU no está visible en el Kanban.
Si el Project tiene una tarjeta sin Markdown, falta trazabilidad documental.

---

## Actores del sistema

| Slug | Actor | Rol |
|------|-------|-----|
| `medico` | Médico | Médico UCI o urgencia que detecta sospechas o participa en confirmación clínica |
| `coordinador` | Coordinador | Coordinador local o central que gestiona proceso, asignación y logística |
| `procurador` | Procurador | Equipo/enfermería de procura que registra y ejecuta etapas clínicas/logísticas |
| `admin` | Administrador | Gestiona usuarios, centros médicos y configuración del sistema |

---

## Mapa de carpetas

```text
documentacion/
├── README.md
├── arquitectura/
├── api/
├── features/
│   ├── README.md
│   ├── activas/
│   ├── en-desarrollo/
│   └── backlog/
├── historias-usuario/
│   ├── README.md
│   ├── medico/
│   ├── coordinador/
│   ├── procurador/
│   └── admin/
├── guias/
├── decisiones/
├── bitacora/
└── informe-tecnico/
```

---

## Reglas de escritura

### Idioma

Todo texto documental en español. Código, nombres de variables y APIs en inglés si el proyecto ya lo usa así.

### Nomenclatura

- Minúsculas con guiones: `confirmacion-muerte-encefalica.md`
- Historias de usuario: `HU-001-notificar-sospecha.md`
- ADRs: `ADR-001-graphql-sobre-rest.md`

### Numeración de HU

Las HU se numeran globalmente, no por actor.

Antes de crear una HU, buscar el número más alto en todas las subcarpetas:

```bash
find documentacion/historias-usuario -name 'HU-*.md' \
  | sed -E 's/.*HU-([0-9]+).*/\1/' \
  | sort -n \
  | tail -1
```

Usar el siguiente número con tres dígitos.

### Estados de HU

- `propuesta`: identificada, pendiente de validación.
- `aceptada`: aprobada para desarrollo.
- `en-desarrollo`: en implementación.
- `implementada`: deployada o mergeada y verificada.
- `descartada`: no se implementará, con razón documentada.

---

## Template: Historia de Usuario

```markdown
# HU-[NNN] — [Título corto]

**Tipo:** historia-usuario  
**Actor:** [medico | coordinador | procurador | admin]  
**Estado:** propuesta  
**Última actualización:** YYYY-MM-DD  
**Feature relacionada:** [Nombre de la feature](../../features/backlog/slug-feature.md)  
**Issue GitHub:** —  
**Project:** https://github.com/orgs/trasplan2026/projects/1  

## Historia

Como **[actor]**, quiero **[acción]** para **[beneficio]**.

## Contexto

Explicar de dónde surge la necesidad: reunión, entrevista clínica, bug observado, demo, etc.

## Criterios de aceptación

- [ ] Criterio verificable 1.
- [ ] Criterio verificable 2.
- [ ] Criterio verificable 3.

## Impacto sobre funcionalidades existentes

Revisar `documentacion/guias/matriz-regresion.md` antes de completar esta tabla.

| Funcionalidad existente | ¿Se toca? | Riesgo | Cómo se protege |
|---|---:|---|---|
| Funcionalidad 1 | Sí/No | Bajo/Medio/Alto | Test, build o verificación manual |

## Contratos que deben preservarse

- Contrato existente que no debe cambiar.
- Comportamiento anterior que debe seguir funcionando.

## No alcance

Esta HU no incluye:

- item fuera de alcance 1;
- item fuera de alcance 2;
- item fuera de alcance 3.

## Riesgo clínico/legal

Indicar si aplica. Para flujos sensibles, explicitar human-in-the-loop y que el sistema no reemplaza juicio clínico.

## Resolución técnica (propuesta)

> Esta sección es una propuesta al momento de crear la HU. Actualizar "Implementado en" cuando haya PR/commit real.

**Implementado en:** *pendiente*

## Código relacionado

Toda HU accionable debe identificar archivos concretos de implementación o declarar explícitamente que no toca código.

### Web (`web/`)

- `web/src/...` — componente, página, hook o test relevante.

### Backend (`backend/`)

- `backend/src/graphql/schemas/...` — schema GraphQL si aplica.
- `backend/src/graphql/resolvers/...` — resolver si aplica.
- `backend/src/models/...` — modelo Sequelize si aplica.
- `backend/src/policies/...` — autorización si aplica.

### App móvil (`App/`)

- `App/screens/...` o `App/graphql/...` si aplica.

### Base de datos

- Migraciones/modelos si aplica, o declarar “no requiere cambios”.

### Web (`web/`)

- Componente(s) a crear o modificar.
- Páginas/rutas afectadas.

### Backend (`backend/`)

- Query/Mutation GraphQL afectada.
- Resolver(s) involucrados.
- Modelos/policies si aplica.

### App móvil (`App/`)

- Pantallas o módulos afectados si aplica.

### Base de datos

- Tablas afectadas.
- Migraciones si aplica.

## Verificación esperada

- [ ] Build/test backend si aplica.
- [ ] Build/test web si aplica.
- [ ] Prueba visual/navegador si aplica.
- [ ] Issue agregado al Project 1.

## Pruebas de regresión

- [ ] Prueba existente o nueva que protege funcionalidades previas.
- [ ] Verificación manual si corresponde.

## Notas / contexto

Información adicional, restricciones, decisiones o links.
```

---

## Template: Feature

```markdown
# [Nombre de la Feature]

**Tipo:** feature  
**Estado:** [borrador | backlog | en-desarrollo | activa | deprecada]  
**Última actualización:** YYYY-MM-DD  
**Autor:** Fabián  

## Descripción

Qué hace esta feature y para qué sirve.

## Motivación

Qué problema resuelve en el flujo de procuramiento/donación.

## Alcance

Qué incluye y qué NO incluye.

## Comportamiento esperado

Paso a paso desde el punto de vista del usuario.

## Arquitectura técnica

### Backend

- Mutation/Query: `...`
- Resolver: `backend/src/graphql/resolvers/...`
- Modelo: `backend/src/models/...`

### Web

- Feature: `web/src/features/...`
- Componentes clave:

### App móvil

- Pantallas o navegación afectada si aplica.

### Base de datos

- Tabla(s):
- Campos relevantes:

## Casos límite

Lista de situaciones especiales y cómo se manejan.

## Contratos que deben preservarse

- Contrato funcional o técnico existente que esta feature no debe romper.
- APIs, inputs GraphQL, permisos, estados o pantallas que deben mantenerse compatibles.

## Pruebas de regresión

- [ ] Tests existentes que deben seguir pasando.
- [ ] Tests nuevos requeridos por la feature.
- [ ] Flujos manuales/navegador que deben verificarse.

## Pendientes / deuda técnica

- [ ] Item pendiente.
```

---

## Template: ADR

```markdown
# ADR-[NNN] — [Título de la decisión]

**Tipo:** adr  
**Estado:** [propuesto | aceptado | deprecado | reemplazado-por-ADR-xxx]  
**Fecha:** YYYY-MM-DD  
**Autor:** Fabián  

## Contexto

Situación que motivó la decisión.

## Decisión

Qué se decidió hacer.

## Alternativas consideradas

| Opción | Pros | Contras |
|--------|------|---------|
| Opción A | ... | ... |
| Opción B | ... | ... |

## Consecuencias

Qué implica esta decisión.

## Referencias

- Link a código relevante.
- Link a issue/PR si aplica.
```

---

## Operaciones del skill

### `/doc nueva-hu [actor] [titulo]`

Prerequisitos:

- `actor` debe ser uno de: `medico`, `coordinador`, `procurador`, `admin`.
- `gh` debe estar autenticado con acceso a `trasplan2026`.
- Para agregar al Project 1 se requieren scopes de GitHub Projects.

Pasos:

1. Buscar el mayor número HU existente.
2. Asignar el siguiente `HU-NNN`.
3. Crear slug del título: minúsculas, sin tildes si es práctico, espacios a guiones.
4. Crear carpeta del actor si no existe.
5. Crear o vincular una feature en `documentacion/features/` antes de crear el issue.
   - Si es funcionalidad de producto, crear `documentacion/features/backlog/<slug>.md` usando el template de feature.
   - Si la HU pertenece a una feature existente, enlazar esa feature en `Feature relacionada`.
   - Si la HU no toca producto/código, justificarlo explícitamente en `No alcance` y `Código relacionado`.
6. Inspeccionar el código real antes de finalizar la HU:
   - web: componentes/rutas/features/tests;
   - backend: schemas/resolvers/models/policies/migraciones;
   - App: pantallas/graphql/store si aplica.
7. Completar la sección `Código relacionado` con rutas reales o declarar “no requiere cambios” por capa.
8. Crear Markdown usando el template completo.
9. Validar que la HU contiene, antes de crear issue:
   - `Feature relacionada` con link real o justificación;
   - `## Código relacionado`;
   - `## No alcance`;
   - `## Impacto sobre funcionalidades existentes`;
   - `## Contratos que deben preservarse`;
   - `## Verificación esperada`;
   - `## Pruebas de regresión`;
   - referencias a archivos concretos cuando haya implementación.
10. Crear/asegurar labels base:

```bash
gh label create "historia-usuario" --repo trasplan2026/documentacion --color "0075ca" --force
gh label create "medico" --repo trasplan2026/documentacion --color "e4e669" --force
gh label create "coordinador" --repo trasplan2026/documentacion --color "d93f0b" --force
gh label create "procurador" --repo trasplan2026/documentacion --color "0e8a16" --force
gh label create "admin" --repo trasplan2026/documentacion --color "5319e7" --force
```

11. Crear issue:

```bash
ISSUE_URL=$(gh issue create \
  --repo trasplan2026/documentacion \
  --title "HU-NNN — <titulo>" \
  --body-file documentacion/historias-usuario/<actor>/HU-NNN-<slug>.md \
  --label "historia-usuario,<actor>")

echo "$ISSUE_URL"
```

12. Agregar issue al Project 1:

```bash
gh project item-add 1 --owner trasplan2026 --url "$ISSUE_URL"
```

13. Si el paso 12 falla por scopes, informar:

```bash
gh auth refresh -s project -s read:project
```

14. Actualizar la HU con `Issue GitHub: <url>` si el issue se creó correctamente.
15. Actualizar el body del issue si la HU cambió después de crearlo.
16. Reportar ruta del archivo, feature vinculada, issue URL y estado de agregado al Project.

Nunca afirmar que el Project fue actualizado si el comando falló.

### `/doc mejorar-hu [ruta]`

1. Leer la HU existente.
2. Asegurar que tenga: contexto, criterios verificables, no-alcance, riesgo clínico/legal y verificación esperada.
3. Asegurar que tenga `Feature relacionada` con link real a `documentacion/features/...`; si no existe, crear feature de backlog o justificar por qué no aplica.
4. Asegurar que tenga `## Código relacionado` con rutas reales por capa o declaración explícita de “no requiere cambios”.
5. Asegurar que tenga `## Impacto sobre funcionalidades existentes` usando `documentacion/guias/matriz-regresion.md`.
6. Asegurar que tenga `## Contratos que deben preservarse`.
7. Asegurar que tenga `## Pruebas de regresión` con tests/builds/verificaciones concretas.
8. Revisar el código real antes de escribir rutas; no inventar archivos.
9. No cambiar el número HU salvo que el usuario lo pida.
10. Si existe issue asociado, actualizar el body del issue para que GitHub Project no quede desfasado.
11. Si existe issue asociado, sugerir o aplicar comentario en GitHub solo con confirmación cuando sea un cambio semántico importante.

### `/doc nueva-feature [nombre]`

1. Preguntar estado inicial: backlog, en-desarrollo o activa.
2. Crear `documentacion/features/<estado>/<slug>.md` con template.
3. Poblar contexto inferible.
4. Reportar ruta.

### `/doc nuevo-adr [titulo]`

1. Buscar último `ADR-NNN`.
2. Crear `documentacion/decisiones/ADR-NNN-slug.md`.
3. Reportar ruta.

### `/doc listar`

Listar docs `.md` por carpeta, título y estado.

### `/doc buscar [termino]`

Buscar en `documentacion/**/*.md` y reportar matches con contexto.

### `/doc status`

Reportar:

- conteo de HUs por estado;
- HUs sin issue GitHub;
- HUs sin Project registrado;
- features por estado;
- documentos borrador.

### `/doc sync-project`

Auditar sincronía entre Markdown, Issues y Project 1:

1. Listar HUs Markdown.
2. Buscar `Issue GitHub:` en cada HU.
3. Consultar issues en `trasplan2026/documentacion`.
4. Detectar HUs sin issue.
5. Detectar issues `historia-usuario` sin Markdown.
6. Detectar fallos de acceso a Project y pedir `gh auth refresh -s project -s read:project` si aplica.

No crear ni cerrar nada sin confirmación explícita.

---

## HealthTech guardrails para documentación

Toda HU clínica sensible debe dejar claro:

- si es informativa o decisoria;
- si requiere validación humana;
- qué NO automatiza;
- qué datos se guardan y cuáles no;
- qué permisos backend deben protegerla;
- cómo se probará sin datos reales.
