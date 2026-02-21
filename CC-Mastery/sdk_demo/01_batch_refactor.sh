#!/bin/bash
# =============================================================================
# Exercise 1: Batch Refactor with claude -p
# =============================================================================
# Module 10, CC-Mastery
#
# PURPOSE: Demonstrate massive parallel scripting pattern.
# Creates dummy Python files, then uses claude -p to add type hints to each.
#
# USAGE: Run from Git Bash or WSL on Windows
#   chmod +x 01_batch_refactor.sh
#   ./01_batch_refactor.sh
#
# PREREQUISITES: claude CLI installed and authenticated
# =============================================================================

set -euo pipefail

WORK_DIR="$(mktemp -d)"
RESULTS_DIR="$WORK_DIR/results"
mkdir -p "$RESULTS_DIR"

echo "=== Exercise 1: Batch Refactor ==="
echo "Work dir: $WORK_DIR"
echo ""

# --- Step 1: Create dummy files to refactor ---
cat > "$WORK_DIR/utils.py" << 'PYEOF'
def add(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}!"

def parse_csv(filepath):
    with open(filepath) as f:
        return [line.strip().split(",") for line in f]
PYEOF

cat > "$WORK_DIR/models.py" << 'PYEOF'
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def is_adult(self):
        return self.age >= 18

    def display(self):
        return f"{self.name} <{self.email}>"
PYEOF

cat > "$WORK_DIR/api.py" << 'PYEOF'
import json

def get_users(db):
    return db.query("SELECT * FROM users")

def create_user(db, data):
    name = data.get("name")
    email = data.get("email")
    age = data.get("age", 0)
    return db.insert("users", {"name": name, "email": email, "age": age})

def delete_user(db, user_id):
    return db.delete("users", user_id)
PYEOF

echo "Created 3 dummy files in $WORK_DIR"
echo ""

# --- Step 2: Sequential refactor (safe, easy to debug) ---
echo "=== Sequential Mode ==="
for file in "$WORK_DIR"/*.py; do
    filename=$(basename "$file")
    echo "Processing: $filename"

    claude -p "Add Python type hints to all functions in $file. \
Only modify type annotations, don't change logic. \
Return just 'DONE' when finished." \
        --allowedTools "Read" "Edit" \
        --permission-mode acceptEdits \
        --max-turns 3 \
        --no-session-persistence \
        --output-format json > "$RESULTS_DIR/$filename.json"

    echo "  -> Result saved to results/$filename.json"
done

echo ""
echo "=== Results ==="
for result in "$RESULTS_DIR"/*.json; do
    filename=$(basename "$result")
    cost=$(cat "$result" | python -c "import sys,json; print(json.load(sys.stdin).get('total_cost_usd','?'))")
    echo "  $filename: cost=\$$cost"
done

# --- Step 3: Show the refactored files ---
echo ""
echo "=== Refactored Files ==="
for file in "$WORK_DIR"/*.py; do
    echo "--- $(basename $file) ---"
    cat "$file"
    echo ""
done

echo ""
echo "=== Parallel Mode (uncomment to try) ==="
echo "# Requires: GNU parallel or background jobs"
echo "# find \$WORK_DIR -name '*.py' | parallel -j 3 \\"
echo "#   'claude -p \"Add type hints to {}\" --allowedTools Read Edit \\"
echo "#    --permission-mode acceptEdits --max-turns 3 --no-session-persistence'"

# Cleanup
echo ""
echo "Files in: $WORK_DIR (delete manually when done)"
