# Claude Code Skills

Shared skills for the Todo List Application team in Claude Code.

## Available Skills

### git-commit-helper
Generate formatted commit messages from staged changes automatically.

- **Invocation:** `/git-commit-helper`
- **Purpose:** Analyze `git diff --cached` and output TYPE, TITLE, and BODY
- **Documentation:** [git-commit-helper/SKILL.md](git-commit-helper/SKILL.md)
- **Use case:** After staging changes with `git add`, generates a well-formatted commit message following conventional commit standards

### pr-review-assistant
Comprehensive code review that catches bugs, quality issues, and improvements before pushing.

- **Invocation:** `/pr-review-assistant`
- **Purpose:** Analyze pending changes for correctness, quality, security, and testing
- **Documentation:** [pr-review-assistant/SKILL.md](pr-review-assistant/SKILL.md)
- **Use case:** Before opening a PR, identify issues and get actionable feedback

## How to use skills

1. Open this project in Claude Code (VS Code, terminal, web app, or IDE extension)
2. Run any skill by typing `/` followed by the skill name in a chat
3. Review the output and apply suggestions as needed

Example:
```bash
git add src/MyComponent.tsx
/git-commit-helper
```

## Recommended workflow

1. **Make changes** — Edit your code
2. **Stage changes** — `git add [files]`
3. **Generate commit** — `/git-commit-helper`
4. **Review changes** — `/pr-review-assistant` before creating PR
5. **Commit and push** — `git commit -m "[message]" && git push`

## Adding new skills

To add a new custom skill to this project:

1. Create a new directory under `.claude/skills/`: `mkdir .claude/skills/my-skill`
2. Add a `SKILL.md` file with:
   - YAML frontmatter (`name`, `description`, `when_to_use`, `allowed-tools`)
   - Clear markdown documentation
3. Update this `README.md` with the new skill entry
4. Commit and push: `git add .claude/skills/ && git commit -m "feat: add my-skill"`

### Skill template

```markdown
---
name: my-skill
description: One-line purpose for this skill
when_to_use: When should someone use this?
allowed-tools: Bash(git *) Read
---

# my-skill

**Purpose:** ...

**Usage:** `/my-skill`

## What it does

...

## When to use

...
```

## Team guidelines

- Keep skill documentation clear and concise
- Include practical examples in skill documentation
- Mention the recommended workflow in `when_to_use`
- Test skills locally before pushing
- Update this README when adding/removing skills
