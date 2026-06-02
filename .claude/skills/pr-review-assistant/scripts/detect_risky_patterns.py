#!/usr/bin/env python3
"""
Detect Risky Patterns in Code Changes

This script scans code diffs for common security and quality issues including:
- eval() and exec() calls
- Hardcoded passwords and API keys
- Raw SQL queries (string concatenation)
- Blocking sleep calls
- TODO/FIXME comments
- Hardcoded credentials patterns

Outputs a quality score report with category breakdown and severity metrics.

Usage:
    python3 detect_risky_patterns.py <diff_file_or_stdin>

    Or pipe a git diff:
    git diff HEAD~1 | python3 detect_risky_patterns.py
"""

import re
import sys
from typing import List, Dict

# Pattern definitions for risky code patterns
RISKY_PATTERNS = {
    'eval_exec': {
        'patterns': [
            r'\b(eval|exec)\s*\(',
        ],
        'severity': 'CRITICAL',
        'description': 'Use of eval() or exec() allows arbitrary code execution',
        'recommendation': 'Replace with safer alternatives: json.loads() for JSON, ast.literal_eval() for literals, or safe templating libraries'
    },
    'hardcoded_password': {
        'patterns': [
            r'(password|passwd|pwd)\s*=\s*["\']([^"\']*)["\']',
            r'(api_key|apikey|api[-_]?secret|secret)\s*=\s*["\']([^"\']*)["\']',
            r'(token|auth_token)\s*=\s*["\']([^"\']*)["\']',
        ],
        'severity': 'CRITICAL',
        'description': 'Hardcoded credentials found in code',
        'recommendation': 'Use environment variables, secrets management systems, or credential providers'
    },
    'raw_sql': {
        'patterns': [
            r'(?:query|execute|sql)\s*\(\s*["\'].*\+.*["\']',
            r'(?:SELECT|INSERT|UPDATE|DELETE).*["\'].*\+',
            r'(?:SELECT|INSERT|UPDATE|DELETE).*%\s*\(',
        ],
        'severity': 'CRITICAL',
        'description': 'SQL query built with string concatenation (SQL injection risk)',
        'recommendation': 'Use parameterized queries or prepared statements (?, ?, :param, etc.)'
    },
    'blocking_sleep': {
        'patterns': [
            r'\b(time\.sleep|sleep)\s*\(',
            r'\basyncio\.sleep\s*\(.*\)\s*(?!await)',
        ],
        'severity': 'HIGH',
        'description': 'Blocking sleep call found, may freeze event loop or thread',
        'recommendation': 'Use async sleep (await asyncio.sleep) in async code or move to background task'
    },
    'todo_fixme': {
        'patterns': [
            r'#\s*(TODO|FIXME|XXX|HACK|BUG)\b',
            r'//\s*(TODO|FIXME|XXX|HACK|BUG)\b',
        ],
        'severity': 'MEDIUM',
        'description': 'TODO/FIXME comment indicates unfinished work',
        'recommendation': 'Resolve the TODO or create a tracked issue if intentionally deferred'
    },
    'console_logs': {
        'patterns': [
            r'\bconsole\.(log|debug|info|warn|error)\s*\(',
            r'\bprint\s*\(',
        ],
        'severity': 'LOW',
        'description': 'Debug logging found in production code',
        'recommendation': 'Remove debug logs or use a proper logging framework with log levels'
    },
}

class PatternDetector:
    def __init__(self):
        self.findings: List[Dict] = []

    def detect_component(self, filename: str) -> str:
        """Determine component category based on file path."""
        filename_lower = filename.lower()

        # Backend indicators
        if any(x in filename_lower for x in ['backend', 'api', 'server', '.py', '.go', '.java', '.rs', 'services', 'models', 'routes']):
            return 'Backend'

        # Frontend indicators
        if any(x in filename_lower for x in ['frontend', 'ui', 'component', '.tsx', '.jsx', '.vue', 'pages', 'client', 'web']):
            return 'Frontend'

        # DevOps indicators
        if any(x in filename_lower for x in ['docker', 'kubernetes', 'helm', 'terraform', '.yaml', '.yml', 'infra', 'deploy']):
            return 'DevOps'

        # Database indicators
        if any(x in filename_lower for x in ['migration', 'schema', '.sql', 'database', 'postgres', 'mysql']):
            return 'Database'

        # Config/Misc
        return 'Config/Other'

    def detect_patterns(self, content: str, filename: str = "unknown") -> None:
        """Scan content for risky patterns."""
        lines = content.split('\n')
        current_file = filename

        for line_num, line in enumerate(lines, 1):
            # Update current file from diff headers (--- a/path or +++ b/path)
            if line.startswith('--- a/') or line.startswith('+++ b/'):
                current_file = line.split('/')[-1] if '/' in line else line
                current_file = current_file.replace('b/', '').replace('a/', '').strip()
                continue

            # Skip removed lines in diffs (those starting with -)
            if line.startswith('-'):
                continue

            # Skip diff metadata
            if line.startswith('@@') or line.startswith('diff ') or line.startswith('index '):
                continue

            for pattern_key, pattern_info in RISKY_PATTERNS.items():
                for pattern in pattern_info['patterns']:
                    if re.search(pattern, line, re.IGNORECASE):
                        self.findings.append({
                            'pattern': pattern_key,
                            'severity': pattern_info['severity'],
                            'description': pattern_info['description'],
                            'recommendation': pattern_info['recommendation'],
                            'file': current_file,
                            'line': line_num,
                            'code': line.strip(),
                            'component': self.detect_component(current_file),
                        })

    def generate_quality_score_report(self) -> str:
        """Generate quality score report with category breakdown."""
        if not self.findings:
            return "✓ No issues detected - Code quality looks good!"

        # Group by component
        components = {}

        for finding in self.findings:
            comp = finding['component']
            if comp not in components:
                components[comp] = {
                    'CRITICAL': 0,
                    'HIGH': 0,
                    'MEDIUM': 0,
                    'LOW': 0,
                    'findings': []
                }
            components[comp][finding['severity']] += 1
            components[comp]['findings'].append(finding)

        # Calculate totals
        total_findings = len(self.findings)
        total_critical = sum(c['CRITICAL'] for c in components.values())
        total_high = sum(c['HIGH'] for c in components.values())
        total_medium = sum(c['MEDIUM'] for c in components.values())
        total_low = sum(c['LOW'] for c in components.values())

        # Build report - START WITH THE TABLE
        report = []
        report.append("Code Review Quality Score:")
        report.append("")

        # Build table with proper column widths for readability
        report.append("| Category | Findings | Severity Breakdown |")
        report.append("|----------|----------|-------------------|")

        # Sort components by number of findings (descending)
        for comp in sorted(components.keys(), key=lambda x: components[x]['CRITICAL'] + components[x]['HIGH'], reverse=True):
            counts = components[comp]
            total = sum(counts[s] for s in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW'])

            severity_parts = []
            if counts['CRITICAL'] > 0:
                severity_parts.append(f"{counts['CRITICAL']} CRITICAL")
            if counts['HIGH'] > 0:
                severity_parts.append(f"{counts['HIGH']} HIGH")
            if counts['MEDIUM'] > 0:
                severity_parts.append(f"{counts['MEDIUM']} MEDIUM")
            if counts['LOW'] > 0:
                severity_parts.append(f"{counts['LOW']} LOW")

            severity_str = ", ".join(severity_parts) if severity_parts else "None"
            findings_label = f"{total} findings" if total != 1 else "1 finding"
            report.append(f"| {comp} | {findings_label} | {severity_str} |")

        # Add total row
        total_severity_parts = []
        if total_critical > 0:
            total_severity_parts.append(f"{total_critical} CRITICAL")
        if total_high > 0:
            total_severity_parts.append(f"{total_high} HIGH")
        if total_medium > 0:
            total_severity_parts.append(f"{total_medium} MEDIUM")
        if total_low > 0:
            total_severity_parts.append(f"{total_low} LOW")

        total_severity_str = ", ".join(total_severity_parts)
        total_findings_label = f"{total_findings} findings" if total_findings != 1 else "1 finding"
        report.append(f"| Total | {total_findings_label} | {total_severity_str} |")

        report.append("")
        report.append("## Detailed Findings")
        report.append("")

        # Group by component and severity
        for comp in sorted(components.keys()):
            comp_findings = components[comp]['findings']
            if not comp_findings:
                continue

            for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
                severity_findings = [f for f in comp_findings if f['severity'] == severity]
                if not severity_findings:
                    continue

                report.append(f"### {comp} - {severity} ({len(severity_findings)})")
                report.append("")
                for finding in severity_findings:
                    report.append(f"- **{finding['pattern'].upper()}**: {finding['description']}")
                    report.append(f"  - File: `{finding['file']}:{finding['line']}`")
                    report.append(f"  - Code: `{finding['code']}`")
                    report.append(f"  - Fix: {finding['recommendation']}")
                    report.append("")

        return '\n'.join(report)


def read_input() -> str:
    """Read input from stdin or file argument."""
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            return f.read()
    else:
        return sys.stdin.read()


def main():
    content = read_input()
    detector = PatternDetector()

    # Process the content (could be a diff or code)
    detector.detect_patterns(content, "diff")

    print(detector.generate_quality_score_report())

    # Exit with code 0 if no critical issues, 1 if critical issues found
    critical_count = len([f for f in detector.findings if f['severity'] == 'CRITICAL'])
    sys.exit(1 if critical_count > 0 else 0)


if __name__ == '__main__':
    main()
