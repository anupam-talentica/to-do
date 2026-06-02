---
name: git-commit-helper
description: Generate formatted commit messages from staged changes using git diff --cached
when_to_use: After staging files with `git add`, run this to auto-generate a commit message
allowed-tools: Bash(git diff, git status) Read
---

# git-commit-helper

**Purpose:** Generate a formatted commit message for staged changes using `git diff --cached`.

**Usage:** `/git-commit-helper`

## What it does

Analyzes your staged changes and automatically generates a commit message with:
- **TYPE:** The change type (feat, fix, docs, refactor, test, chore, etc.)
- **TITLE:** A concise one-line summary
- **BODY:** Detailed description of what changed and why

## When to use

Run this after staging your changes:

```bash
git add [files]
/git-commit-helper
```

The skill will output a formatted commit message that you can review, adjust, and use with `git commit -m`.

## Example output

```
TYPE: feat
TITLE: Add priority levels to todo items
BODY: Implement priority management across the application:
- Add Priority enum (HIGH, MEDIUM, LOW) to Todo entity
- Add priority field with MEDIUM as default in database
- Update TodoForm and TodoItem components with priority UI
```

## Best practices

1. Stage your changes first: `git add [files]`
2. Review the generated message before committing
3. Edit the output if needed for clarity or accuracy
4. Follow conventional commit standards for consistency
