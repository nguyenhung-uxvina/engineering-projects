---
name: web-search
description: Web search using Brave Search API via CLI script. This skill should be used when performing web searches for research, competitive analysis, or technical documentation lookup. Replaces the Brave Search MCP server with a stateless CLI call.
---

# Web Search

Perform web searches via `scripts/brave_search.py` — a direct Brave Search API wrapper.
No MCP server needed. Each search is a single stateless HTTP call.

## Prerequisites

Set the `BRAVE_API_KEY` environment variable before use.

## Usage

To search the web, run the script directly:

```bash
python scripts/brave_search.py "search query"
python scripts/brave_search.py "MIL-STD-810H temperature testing" --count 5
python scripts/brave_search.py "Vietnamese defense industry 2025" --count 10 --offset 10
```

Output is JSON: array of `{title, url, description}` objects.

## When to Use

- Technical documentation lookup
- Defense industry research and competitive analysis
- Standards and regulation search
- Supplier and vendor discovery

## Why This Is a Skill, Not an MCP

Brave Search is stateless — each query is an independent HTTP request with no session, no cookies,
no persistent connection. Running an MCP server (Node.js process via npx) for this adds:

- Process overhead (Node.js runtime)
- Startup latency (npx download on first run)
- A failure mode (server crashes, stdio pipe breaks)
- Complexity (MCP protocol framing for a single GET request)

The script does the same thing in 70 lines of Python with zero dependencies.
