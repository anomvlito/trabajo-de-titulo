---
name: skill-creator
description: Automates the creation and formatting of new agent skills. Use when user asks to "crear una skill", "create a skill", "generate new skill", or "crear nueva skill".
---

# Skill Creator & Standardizer

This skill automates the creation of new Claude/Codex Agent Skills in this repository, enforcing the standardized `SKILL.md` format, Level 1 YAML frontmatter trigger phrases, and Obsidian-style interlinking.

---

## 1. Directory Structure

Every skill created must live in `.claude/skills/[skill-name]/` and contain at least:
- `SKILL.md` (metadata frontmatter and instructions)

Optional folders:
- `references/` (documentation loaded on demand - Level 3)
- `scripts/` (executable helper tools)

---

## 2. Standardized SKILL.md Template

When creating a new skill, generate the file with the following exact structure:

```markdown
---
name: [lowercase-kebab-case-name]
description: [What the skill does in 1 sentence]. Use when user asks to "[trigger 1]", "[trigger 2]", or "[trigger 3]".
---

# [Human Readable Title]

## Overview
[Concise description of the goal]

## Execution Steps
1. **[Step 1 Title]**: [Brief description of actions]
2. **[Step 2 Title]**: [Brief description of actions]

## Constraints
- [Constraint 1]
- [Constraint 2]

## References & Interconnections
- [[math-solver-style]](../math-solver-style/SKILL.md) (e.g., if it solves mathematical exercises)
- [[exercise-solver]](../exercise-solver/SKILL.md) (e.g., if it is an orchestrator or solver)
```

---

## 3. Interconnection Protocol (Obsidian-Style)

- New skills must be linked to pre-existing relative skills inside the workspace using Obsidian-style links: `[[target-skill]](../target-skill/SKILL.md)`.
- If the new skill is mathematical, it **must** link to:
  - [[math-solver-style]](../math-solver-style/SKILL.md)
  - [[exercise-solver]](../exercise-solver/SKILL.md)
- Register the new skill in the global index:
  - [[SKILLS.md]](../SKILLS.md)

---

## 4. Execution Workflow for the Agent

1. **Ask for Details**: Prompt the user for the name and high-level description of the new skill.
2. **Determine Triggers**: Generate at least 4 trigger phrases (both Spanish and English if applicable).
3. **Write File**: Create `.claude/skills/[name]/SKILL.md`.
4. **Register**: Append the new skill to the global list in `.claude/skills/SKILLS.md`.
