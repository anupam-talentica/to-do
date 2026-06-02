# Claude Code Skills

Custom skills for the Todo List Application team in Claude Code.

## Installation & Setup

### Global Installation

To make these skills available globally across all Claude Code projects:

1. **Copy skills to global directory:**
   ```bash
   # On macOS
   cp -r .claude/skills/* ~/.claude/skills/
   
   # On Linux
   cp -r .claude/skills/* ~/.claude/skills/
   
   # On Windows (PowerShell)
   Copy-Item -Path ".claude\skills\*" -Destination "$env:USERPROFILE\.claude\skills\" -Recurse
   ```

2. **Verify installation:**
   ```bash
   ls ~/.claude/skills/
   # Should show: git-commit-helper/, pr-review-assistant/
   ```

3. **Verify in Claude Code:**
   - Open any Claude Code session
   - Type `/` to see available skills
   - Both skills should appear in the list

### Project-Local Installation

Skills are already available in this project at `.claude/skills/` and can be used immediately with:
```bash
/git-commit-helper
/pr-review-assistant <identifier>
```

### Updating Global Skills

When skills are updated in the project:
```bash
# Copy updated skills to global location
cp -r .claude/skills/* ~/.claude/skills/
```

Claude Code will automatically load the latest version on next invocation.

---

## Available Skills

### 1. git-commit-helper
**Auto-generate formatted commit messages from staged changes.**

- **Usage:** `/git-commit-helper`
- **Invocation:** After staging changes with `git add`
- **Output:** Formatted commit with TYPE, TITLE, and BODY
- **Types:** feat, fix, docs, test, refactor, perf, chore, ci

**Example:**
```bash
git add src/TodoItem.tsx
/git-commit-helper
```

Output:
```
TYPE: feat
TITLE: add priority levels to todo items
BODY: Implement priority management:
- Add Priority enum (HIGH, MEDIUM, LOW) to Todo entity
- Add priority field with MEDIUM default
- Update TodoForm and TodoItem components with priority UI
```

---

### 2. pr-review-assistant
**Comprehensive code review with quality metrics and detailed findings.**

- **Usage:** `/pr-review-assistant <identifier>`
- **Supports:** PR numbers, GitHub URLs, branch ranges, HEAD
- **Output:** Quality score table + detailed findings organized by component and severity

**Review Dimensions:**
- Security (hardcoded credentials, SQL injection, XSS, etc.)
- Performance (N+1 queries, blocking operations, etc.)
- Maintainability (complexity, error handling, test coverage, etc.)

**Severity Levels:**
- **CRITICAL** — Production risks, security vulnerabilities
- **HIGH** — Performance issues, significant quality problems
- **MEDIUM** — Maintainability concerns, code quality issues
- **LOW** — Minor improvements, suggestions

**Examples:**
```bash
# Review by PR number
/pr-review-assistant 123

# Review by GitHub URL
/pr-review-assistant https://github.com/org/repo/pull/123

# Review a branch
/pr-review-assistant main..feature-auth

# Review uncommitted changes
/pr-review-assistant HEAD
```

**Pattern Detection (Automated):**

The skill scans for risky patterns and auto-categorizes by component:
- **eval() / exec()** → CRITICAL: Arbitrary code execution
- **Hardcoded credentials** → CRITICAL: API keys, passwords in code
- **SQL injection** → CRITICAL: String concatenation in queries  
- **Blocking sleep** → HIGH: Freezes event loops
- **Missing error handling** → HIGH: Async without try-catch
- **TODO/FIXME** → MEDIUM: Unfinished work
- **Debug logging** → LOW: console.log, print statements

---

## Workflow

### Using git-commit-helper

1. Make changes to files
2. Stage your changes: `git add [files]`
3. Run: `/git-commit-helper`
4. Review and copy the output
5. Commit: `git commit -m "[pasted message]"`

### Using pr-review-assistant

1. Create a feature branch and push changes
2. Before opening PR, run: `/pr-review-assistant main..feature-branch`
3. Review findings and severity breakdown
4. Fix CRITICAL and HIGH issues before creating PR
5. Document or link MEDIUM/LOW issues in PR description if intentional

---

## How Skills Are Implemented

### git-commit-helper

**File:** `git-commit-helper/SKILL.md`

Analyzes `git diff --cached` and outputs a formatted commit message following conventional commit standards. No additional scripts needed.

### pr-review-assistant

**Files:**
- `pr-review-assistant/SKILL.md` — Skill definition and usage
- `pr-review-assistant/scripts/detect_risky_patterns.py` — Pattern detection engine
- `pr-review-assistant/references/review-checklist.md` — Security, performance, and quality checklist

**Workflow:**
1. Skill fetches git diff using `gh pr diff`, `git diff`, or HEAD
2. Passes diff to Python pattern detector
3. Python script scans for risky patterns, categorizes by component, assigns severity
4. Outputs quality score table + detailed findings with file:line references

---

## Adding New Skills

To create a new skill for the team:

1. Create a directory: `mkdir .claude/skills/my-skill`
2. Add `SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: my-skill
   description: One-line purpose
   type: agent
   ---
   
   Your skill instructions here...
   ```
3. Add supporting files (scripts, references, examples) in subdirectories
4. Update this README with the new skill
5. Commit: `git add .claude/skills/ && git commit -m "feat: add my-skill"`

---

## Team Guidelines

- **Test locally** before pushing skills
- **Document clearly** with examples in SKILL.md
- **Keep skills focused** — one concern per skill
- **Use subdirectories** for supporting files (scripts/, references/, examples/)
- **Update README** when adding/removing/modifying skills
- **Version incrementally** — keep breaking changes rare

---

## Support

For issues or improvements:
- Check skill documentation: [individual SKILL.md files](.)
- Review checklist: [pr-review-assistant/references/review-checklist.md](pr-review-assistant/references/review-checklist.md)
- Detect patterns: [pr-review-assistant/scripts/detect_risky_patterns.py](pr-review-assistant/scripts/detect_risky_patterns.py)
