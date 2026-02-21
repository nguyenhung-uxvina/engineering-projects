#!/bin/bash
# =============================================================================
# Layer 1, Level 6: Real CI/CD Patterns
# =============================================================================
# These are production-ready patterns you'd put in:
#   - GitHub Actions workflows
#   - Pre-commit hooks
#   - Makefile targets
#   - Shell aliases
# =============================================================================

# ╔═══════════════════════════════════════════════════════════╗
# ║ PATTERN A: Smart Commit Messages                         ║
# ╚═══════════════════════════════════════════════════════════╝
# Generate commit message from staged diff

smart_commit() {
    local diff=$(git diff --cached)
    if [ -z "$diff" ]; then
        echo "Nothing staged. Stage files first: git add ..."
        return 1
    fi

    # Claude reads the diff, generates a message
    local msg=$(echo "$diff" | claude -p \
        "Write a concise git commit message for this diff. \
         Format: <type>: <description> (max 72 chars). \
         Types: feat, fix, refactor, docs, test, chore. \
         Only output the message, nothing else." \
        --tools "" \
        --model sonnet \
        --output-format text)

    echo "Proposed commit message:"
    echo "  $msg"
    echo ""
    read -p "Use this message? (y/n/e=edit) " choice
    case $choice in
        y) git commit -m "$msg" ;;
        e) git commit -e -m "$msg" ;;  # Open editor with suggestion
        *) echo "Aborted." ;;
    esac
}

# Usage: stage files, then run:
#   smart_commit


# ╔═══════════════════════════════════════════════════════════╗
# ║ PATTERN B: PR Review Bot                                  ║
# ╚═══════════════════════════════════════════════════════════╝
# Review a PR diff and post comments

review_pr() {
    local pr_number=${1:?"Usage: review_pr <PR_NUMBER>"}

    echo "Reviewing PR #$pr_number..."

    # Get the diff
    local diff=$(gh pr diff "$pr_number")

    # Review with Claude (read-only, no tools)
    local review=$(echo "$diff" | claude -p \
        "Review this pull request diff. Check for:
         1. Bugs or logic errors
         2. Security vulnerabilities
         3. Performance issues
         4. Missing error handling
         5. Style inconsistencies

         Format your review as:
         ## Summary
         <1-2 sentences>

         ## Issues Found
         - **[severity]** file:line — description

         ## Suggestions
         - <improvement ideas>

         Be specific. Reference exact lines." \
        --tools "" \
        --model sonnet \
        --output-format text)

    echo "$review"
    echo ""
    read -p "Post this review as a PR comment? (y/n) " choice
    if [ "$choice" = "y" ]; then
        echo "$review" | gh pr comment "$pr_number" --body-file -
        echo "Review posted!"
    fi
}

# Usage: review_pr 42


# ╔═══════════════════════════════════════════════════════════╗
# ║ PATTERN C: Changelog Generator                            ║
# ╚═══════════════════════════════════════════════════════════╝
# Generate a changelog from commits between two tags/refs

generate_changelog() {
    local from=${1:-"HEAD~10"}
    local to=${2:-"HEAD"}

    echo "Generating changelog: $from..$to"

    git log "$from".."$to" --pretty=format:"%h %s" | claude -p \
        "Generate a user-friendly changelog from these git commits. \
         Group by category (Features, Bug Fixes, Improvements, etc.). \
         Use markdown format. Don't include commit hashes — \
         users don't care about them. Focus on what changed and why it matters." \
        --tools "" \
        --model sonnet \
        --output-format text
}

# Usage: generate_changelog v1.0 v1.1


# ╔═══════════════════════════════════════════════════════════╗
# ║ PATTERN D: Explain Codebase to New Developer              ║
# ╚═══════════════════════════════════════════════════════════╝
# Generate an onboarding doc for a directory

explain_codebase() {
    local dir=${1:-.}

    claude -p "Explore the codebase in $dir. Read the key files. \
        Generate a developer onboarding guide that covers: \
        1. Project purpose (1 sentence) \
        2. Directory structure (tree with descriptions) \
        3. Key files and what they do \
        4. How to run/test the project \
        5. Architecture decisions worth knowing \
        Keep it under 200 lines." \
        --tools "Read,Glob,Grep" \
        --max-turns 15 \
        --max-budget-usd 0.25 \
        --model sonnet \
        --output-format text
}

# Usage: explain_codebase ./sdk_demo


# ╔═══════════════════════════════════════════════════════════╗
# ║ PATTERN E: Security Audit (Read-Only)                     ║
# ╚═══════════════════════════════════════════════════════════╝

security_audit() {
    local dir=${1:-.}

    claude -p "Perform a security audit on the code in $dir. \
        Check for: \
        1. Hardcoded secrets (API keys, passwords, tokens) \
        2. SQL injection vulnerabilities \
        3. Command injection risks \
        4. Unsafe deserialization \
        5. Missing input validation \
        6. Insecure file operations \
        Report each finding with file path, line number, severity, and fix." \
        --tools "Read,Glob,Grep" \
        --max-turns 20 \
        --model sonnet \
        --output-format json \
        --json-schema '{
          "type": "object",
          "properties": {
            "findings": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "file": {"type": "string"},
                  "line": {"type": "integer"},
                  "severity": {"type": "string", "enum": ["critical", "high", "medium", "low"]},
                  "category": {"type": "string"},
                  "description": {"type": "string"},
                  "fix": {"type": "string"}
                },
                "required": ["file", "severity", "category", "description"]
              }
            },
            "overall_risk": {"type": "string", "enum": ["critical", "high", "medium", "low"]},
            "summary": {"type": "string"}
          },
          "required": ["findings", "overall_risk", "summary"]
        }'
}

# Usage: security_audit ./src


# ╔═══════════════════════════════════════════════════════════╗
# ║ PATTERN F: Batch File Processing (Parallel)               ║
# ╚═══════════════════════════════════════════════════════════╝

batch_add_docstrings() {
    local dir=${1:-.}
    local max_parallel=${2:-3}

    echo "Adding docstrings to Python files in $dir (${max_parallel} parallel)..."

    find "$dir" -name "*.py" -not -path "*/__pycache__/*" | \
      xargs -P "$max_parallel" -I {} bash -c '
        echo "Processing: {}"
        claude -p "Read {} and add Google-style docstrings to any function or class that lacks one. Do not change logic." \
          --allowedTools "Read" "Edit" \
          --permission-mode acceptEdits \
          --max-turns 4 \
          --no-session-persistence \
          --model sonnet \
          --output-format json | python -c "
import sys, json
d = json.load(sys.stdin)
print(f\"  {}: {d.get(chr(39)subtype chr(39), chr(39)?chr(39))} cost=\\${d.get(chr(39)total_cost_usd chr(39), 0):.4f}\")" 2>/dev/null
      '

    echo "Done!"
}

# Usage: batch_add_docstrings ./sdk_demo/testbed 2


# =============================================================================
# QUICK REFERENCE: Which pattern for which CI/CD stage?
# =============================================================================
#
# | CI Stage         | Pattern | Tools         | Mode            |
# |------------------|---------|---------------|-----------------|
# | Pre-commit       | A       | (none)        | text output     |
# | PR review        | B       | (none)        | text output     |
# | Release notes    | C       | (none)        | text output     |
# | Security gate    | E       | Read,Glob,Grep| json+schema     |
# | Auto-fix         | F       | Read,Edit     | acceptEdits     |
# | Onboarding docs  | D       | Read,Glob,Grep| text output     |
# =============================================================================
