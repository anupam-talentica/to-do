# Claude Code Skills

This project includes custom Claude Code skills to streamline development workflows.

## Available Skills

### 1. git-commit-helper
Generate formatted commit messages automatically from your staged changes.

**Quick start:**
```bash
git add [files]
/git-commit-helper
```

Outputs a commit message with TYPE, TITLE, and BODY following conventional commit standards.

**Learn more:** [.claude/skills/git-commit-helper.md](.claude/skills/git-commit-helper.md)

---

### 2. pr-review-assistant
Comprehensive code review that catches bugs, quality issues, and improvements before you push.

**Quick start:**
```bash
/pr-review-assistant
```

Reviews your changes for:
- ✓ Correctness bugs
- ✓ Code quality and style
- ✓ Simplification opportunities
- ✓ Performance issues
- ✓ Security vulnerabilities
- ✓ Test coverage

**Learn more:** [.claude/skills/pr-review-assistant.md](.claude/skills/pr-review-assistant.md)

---

## How to Use Skills in Claude Code

1. **Open this project in Claude Code** (via VS Code, terminal, or web app)
2. **Run any skill** by typing `/` followed by the skill name
3. **Review findings** and adjust code as needed

## Adding More Skills

To add custom skills to this project:
1. Create a `.md` file in `.claude/skills/`
2. Document the skill's purpose, usage, and examples
3. Add an entry to this `SKILLS.md`

## Need Help?

- Type `/help` in Claude Code for general help
- Check individual skill docs for detailed usage
- See [README.md](README.md) for project setup and features
