---
name: pr-review-assistant
description: Comprehensive code review analyzing changes for correctness, quality, and best practices
when_to_use: Before opening a pull request, run this to catch issues early
allowed-tools: Bash(git diff, git log) Read WebSearch
---

# pr-review-assistant

**Purpose:** Comprehensive PR review assistant that analyzes code changes for correctness, style, and best practices.

**Usage:** `/pr-review-assistant`

## What it does

Performs a detailed review of pending changes on the current branch by checking for:
- **Correctness bugs** — Logic errors, edge cases, null/undefined handling
- **Code quality** — Style consistency, naming, complexity
- **Simplification opportunities** — Reusable patterns, DRY violations
- **Performance** — Inefficient operations, unnecessary renders (React)
- **Security** — Input validation, injection vulnerabilities, credential exposure
- **Testing** — Test coverage, mocked dependencies that should be real

## When to use

Run before creating a pull request to catch issues early:

```bash
git checkout feature/my-feature
/pr-review-assistant
```

## What to do with findings

The skill returns a list of findings with:
1. **File and line location** — Exactly where to look
2. **Issue description** — What the problem is
3. **Suggested fix** — How to resolve it

Review each finding and decide whether to:
- ✅ Apply the suggested fix
- 📝 Adjust it based on context
- ⊘ Dismiss it if it doesn't apply to your use case

## Tips

- Run this on your feature branch before opening a PR
- Use the findings to improve code quality proactively
- Revisit after significant changes to catch new issues
- Share interesting findings with your team for knowledge sharing

## Integration with PR workflow

1. Make changes on your feature branch
2. Commit and push to origin
3. Run `/pr-review-assistant` before opening the PR
4. Address findings or add context in PR description
5. Open PR with higher confidence in code quality
