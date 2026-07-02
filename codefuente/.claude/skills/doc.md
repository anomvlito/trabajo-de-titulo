# Skill: doc — Orquestador de Documentación Trasplan

Eres el responsable de mantener, crear y organizar la documentación de la plataforma Trasplan. Este skill define el mapa de carpetas, los templates, la metodología y las reglas de escritura.

Cuando el usuario invoque `/doc`, determina qué operación quiere realizar y ejecútala usando las reglas de este skill.

---

## Contexto del proyecto

**Trasplan** es una plataforma web y móvil para coordinar el proceso de procuramiento y trasplante de órganos en Chile en tiempo real. Conecta médicos UCI, coordinadores locales, CORE Chile y equipos de procura.

- **Web:** React 17 + Material-UI v4 + Apollo Client v3 + TypeScript — `web/`
- **Backend:** Node.js + Express + Apollo Server v4 + Sequelize + TypeScript — `backend/`
- **App móvil:** React Native CLI + TypeScript — `App/`
- **DB:** PostgreSQL en RDS AWS (`us-east-2`)
- **Storage:** S3 `trasplan-files-dev` + CloudFront

Rutas del proyecto:
- `/home/fabian/src/codefuente/web` — frontend web
- `/home/fabian/src/codefuente/backend` — backend GraphQL
- `/home/fabian/src/codefuente/documentacion` — este repo de documentación

Repo de documentación en GitHub: `trasplan2026/documentacion`
Proyecto GitHub: `https://github.com/orgs/trasplan2026/projects/1/views/1` (project number: 1, owner: trasplan2026)

---

## Actores del sistema

| Slug | Actor | Rol |
|------|-------|-----|
| `medico` | Médico | Médico UCI o de urgencia — inicia sospechas, confirma muerte encefálica |
| `coordinador` | Coordinador | Coordinador local o central (CORE) — gestiona asignación y logística |
| `procurador` | Procurador | Equipo quirúrgico de procura de órganos |
| `admin` | Administrador | Gestiona usuarios, centros médicos y configuración del sistema |

---

## Mapa de carpetas

```
documentacion/
│
├── README.md
├── arquitectura/
│   ├── vision-general.md
│   ├── backend.md
│   ├── frontend.md
│   ├── base-de-datos.md
│   └── infraestructura.md
│
├── api/
│   ├── graphql-queries.md
│   ├── graphql-mutations.md
│   └── autenticacion.md
│
├── features/
│   ├── README.md
│   ├── activas/
│   ├── en-desarrollo/
│   └── backlog/
│
├── historias-usuario/
│   ├── README.md
│   ├── medico/          ← HU-nnn-slug.md
│   ├── coordinador/     ← HU-nnn-slug.md
│   ├── procurador/      ← HU-nnn-slug.md
│   └── admin/           ← HU-nnn-slug.md
│
├── guias/
│   ├── onboarding.md
│   ├── deploy.md
│   └── uso-sistema.md
│
├── decisiones/
│   ├── README.md
│   └── ADR-nnn-slug.md
│
├── bitacora/
└── informe-tecnico/
```

---

## Metodología y reglas de escritura

### Idioma
Todo en **español**. Código en inglés como siempre.

### Nomenclatura de archivos
- Minúsculas con guiones: `confirmacion-muerte-encefalica.md`
- Historias de usuario: `HU-001-notificar-sospecha.md`
- ADRs: `ADR-001-graphql-sobre-rest.md`

### Numeración de HU
Las HU se numeran **globalmente** (no por actor). Antes de crear una HU, buscar el número más alto existente en todas las subcarpetas de `historias-usuario/` y usar el siguiente.

### Encabezado obligatorio
```
# Título del documento

**Tipo:** [arquitectura | feature | historia-usuario | guia | adr]
**Estado:** [borrador | activo | deprecado]
**Última actualización:** YYYY-MM-DD
**Autor:** Fabián
```

### Convenciones
- H2 para secciones principales, H3 para subsecciones
- Listas sobre párrafos largos
- Bloques de código con lenguaje explícito
- Sin emojis decorativos
- Máximo 80 palabras por párrafo

---

## Templates

### Template: Historia de Usuario

```markdown
# HU-[nnn] — [Título corto]

**Tipo:** historia-usuario
**Actor:** [medico | coordinador | procurador | admin]
**Estado:** [propuesta | aceptada | en-desarrollo | implementada | descartada]
**Última actualización:** YYYY-MM-DD
**Feature relacionada:** —

## Historia

Como **[actor]**, quiero **[acción]** para **[beneficio]**.

## Criterios de aceptación

- [ ] Criterio 1
- [ ] Criterio 2
- [ ] Criterio 3

## Resolución técnica (propuesta)

> Actualizar "Implementado en" una vez mergeado el PR.

**Implementado en:** *pendiente*

### Web (`web/`)
- Componente(s) a crear o modificar
- Páginas/rutas afectadas

### Backend (`backend/`)
- Query o Mutation GraphQL afectada
- Resolver(s) involucrados
- Modelos Sequelize afectados

### Base de datos
- Tablas afectadas
- Cambios de schema si aplica

## Notas / contexto

Información adicional, restricciones, decisiones de diseño.
```

---

### Template: Feature

```markdown
# [Nombre de la Feature]

**Tipo:** feature
**Estado:** [borrador | en-desarrollo | activa | deprecada]
**Última actualización:** YYYY-MM-DD
**Autor:** Fabián

## Descripción

Qué hace esta feature y para qué sirve.

## Motivación

Por qué se construyó, qué problema resuelve en el flujo de procuramiento.

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
- Página: `web/src/pages/...`
- Feature: `web/src/features/...`
- Componentes clave:

### Base de datos
- Tabla(s): 
- Campos relevantes:

## Casos límite

Lista de situaciones especiales y cómo se manejan.

## Pendientes / deuda técnica

- [ ] Item pendiente
```

---

### Template: ADR

```markdown
# ADR-[nnn] — [Título de la decisión]

**Tipo:** adr
**Estado:** [propuesto | aceptado | deprecado | reemplazado por ADR-xxx]
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

Qué implica esta decisión — positivo y negativo.

## Referencias

- Link a código relevante
- Link a issue/PR si aplica
```

---

## Operaciones del skill

### `/doc nueva-hu [actor] [título]`

**Prerequisito:** `gh` CLI instalado y autenticado con acceso a `trasplan2026`.
Si `gh` no está disponible, crear solo el archivo `.md` y mostrar el comando para crear el issue manualmente.

**Pasos:**
1. Buscar el número más alto en `documentacion/historias-usuario/**/*.md` con `grep -rh "^# HU-" ... | sort -t- -k2 -n | tail -1`
2. Asignar el siguiente número (`nnn`)
3. Generar el slug del título: minúsculas, espacios → guiones, máx 5 palabras
4. Crear el archivo `documentacion/historias-usuario/[actor]/HU-[nnn]-[slug].md` con el template poblado
5. Crear el issue en GitHub:
   ```bash
   ISSUE_URL=$(gh issue create \
     --repo trasplan2026/documentacion \
     --title "HU-[nnn] — [título]" \
     --body "$(cat documentacion/historias-usuario/[actor]/HU-[nnn]-[slug].md)" \
     --label "historia-usuario,[actor]")
   echo $ISSUE_URL
   ```
6. Agregar el issue al proyecto:
   ```bash
   gh project item-add 1 --owner trasplan2026 --url $ISSUE_URL
   ```
7. Reportar: ruta del archivo, URL del issue, URL del proyecto

**Si las labels no existen**, crearlas primero:
```bash
gh label create "historia-usuario" --repo trasplan2026/documentacion --color "0075ca"
gh label create "medico" --repo trasplan2026/documentacion --color "e4e669"
gh label create "coordinador" --repo trasplan2026/documentacion --color "d93f0b"
gh label create "procurador" --repo trasplan2026/documentacion --color "0e8a16"
gh label create "admin" --repo trasplan2026/documentacion --color "5319e7"
```

---

### `/doc nueva-feature [nombre]`
1. Preguntar: ¿backlog, en-desarrollo o activa?
2. Crear `documentacion/features/[estado]/[nombre].md` con el template de feature
3. Poblar campos inferibles del contexto
4. Reportar ruta del archivo creado

### `/doc nuevo-adr [título]`
1. Buscar el último `ADR-nnn` en `documentacion/decisiones/` para auto-incrementar
2. Crear `documentacion/decisiones/ADR-[nnn]-[slug].md` con el template de ADR
3. Reportar ruta del archivo creado

### `/doc listar`
Listar todos los `.md` en `documentacion/` organizados por carpeta, mostrando título y estado del encabezado.

### `/doc buscar [término]`
`grep -rn "[término]" documentacion/ --include="*.md"` y reportar matches con contexto.

### `/doc actualizar [ruta]`
Leer el archivo, preguntar qué sección actualizar, aplicar los cambios preservando el formato.

### `/doc status`
- Cuántos docs por carpeta
- HU por estado (propuesta/aceptada/en-desarrollo/implementada)
- Features sin documentar (comparando con `web/src/features/` y `web/src/pages/`)
- Docs en estado "borrador"

### `/doc push`
Commitear y pushear los cambios en `documentacion/` al repo `trasplan2026/documentacion`:
```bash
cd /home/fabian/src/codefuente/documentacion
git add .
git commit -m "docs: [descripción de los cambios]"
git push origin main
```
