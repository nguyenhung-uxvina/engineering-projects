#!/usr/bin/env python3
"""
Brave Search CLI — replaces @modelcontextprotocol/server-brave-search MCP.

Usage:
    python brave_search.py "search query" [--count N] [--offset N]

Environment:
    BRAVE_API_KEY — required, Brave Search API key

Output:
    JSON array of results with title, url, description.
"""

import argparse
import gzip
import json
import os
import sys
import urllib.request
import urllib.parse
import urllib.error


API_URL = "https://api.search.brave.com/res/v1/web/search"


def search(query, count=10, offset=0):
    """Call Brave Search API and return results."""
    api_key = os.environ.get("BRAVE_API_KEY")
    if not api_key:
        print("Error: BRAVE_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    params = urllib.parse.urlencode({
        "q": query,
        "count": min(count, 20),
        "offset": offset,
    })

    url = f"{API_URL}?{params}"
    req = urllib.request.Request(url, headers={
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": api_key,
    })

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read()
            if resp.headers.get("Content-Encoding") == "gzip":
                raw = gzip.decompress(raw)
            data = json.loads(raw.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}", file=sys.stderr)
        sys.exit(1)

    results = []
    for item in data.get("web", {}).get("results", []):
        results.append({
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "description": item.get("description", ""),
        })

    return results


def main():
    parser = argparse.ArgumentParser(description="Brave Search CLI")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--count", type=int, default=10, help="Number of results (max 20)")
    parser.add_argument("--offset", type=int, default=0, help="Result offset for pagination")
    args = parser.parse_args()

    results = search(args.query, args.count, args.offset)
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
