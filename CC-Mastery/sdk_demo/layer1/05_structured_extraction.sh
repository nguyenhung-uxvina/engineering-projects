#!/bin/bash
# =============================================================================
# Layer 1, Level 5: Structured Data Extraction
# =============================================================================
# --json-schema forces Claude to return VALIDATED JSON matching your schema.
# Combined with --output-format json, you get machine-readable results
# you can pipe into downstream tools.
#
# This is the CLI equivalent of Pydantic/Zod in the SDKs.
# =============================================================================

# --- 5A: Extract function signatures ---
cat sdk_demo/testbed/utils.py | claude -p \
  "Extract all function signatures from this Python code." \
  --output-format json \
  --json-schema '{
    "type": "object",
    "properties": {
      "functions": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {"type": "string"},
            "params": {"type": "array", "items": {"type": "string"}},
            "has_return_type": {"type": "boolean"}
          },
          "required": ["name", "params", "has_return_type"]
        }
      }
    },
    "required": ["functions"]
  }' \
  --tools "" | python -c "
import sys, json
data = json.load(sys.stdin)
for f in data.get('structured_output', {}).get('functions', []):
    hint = 'typed' if f['has_return_type'] else 'untyped'
    print(f\"  {f['name']}({', '.join(f['params'])}) [{hint}]\")
"

# --- 5B: Analyze git log into structured data ---
git log --oneline -10 2>/dev/null | claude -p \
  "Categorize these commits." \
  --output-format json \
  --json-schema '{
    "type": "object",
    "properties": {
      "commits": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "hash": {"type": "string"},
            "message": {"type": "string"},
            "category": {"type": "string", "enum": ["feature", "bugfix", "refactor", "docs", "chore", "test"]}
          },
          "required": ["hash", "message", "category"]
        }
      },
      "summary": {"type": "string"}
    },
    "required": ["commits", "summary"]
  }' \
  --tools ""

# --- 5C: Extract dependencies from a requirements file ---
echo "requests>=2.28.0
flask==3.0.0
pytest>=7.0
black
mypy>=1.0
sqlalchemy>=2.0,<3.0
redis[hiredis]" | claude -p \
  "Analyze these Python dependencies." \
  --output-format json \
  --json-schema '{
    "type": "object",
    "properties": {
      "packages": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {"type": "string"},
            "version_constraint": {"type": "string"},
            "category": {"type": "string", "enum": ["web", "database", "testing", "linting", "utility"]},
            "pinned": {"type": "boolean"}
          },
          "required": ["name", "version_constraint", "category", "pinned"]
        }
      },
      "risk_assessment": {"type": "string"}
    },
    "required": ["packages", "risk_assessment"]
  }' \
  --tools ""

# =============================================================================
# KEY RULES FOR --json-schema:
#
# 1. Schema must be a top-level OBJECT (not array, not string)
# 2. Use --output-format json (required with --json-schema)
# 3. Result is in .structured_output field of the JSON response
# 4. If Claude can't match the schema after retries:
#    result.subtype = "error_max_structured_output_retries"
# 5. --tools "" recommended for pure extraction (no tool call overhead)
# 6. Works with piped content — Claude sees stdin + schema constraint
# =============================================================================
