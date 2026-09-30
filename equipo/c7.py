"""Consulta Context7 (servidor MCP HTTP) desde la terminal.

Uso:
  python c7.py resolve "<librería>" "<qué necesitas>"
  python c7.py docs "</org/proyecto>" "<pregunta concreta>"
"""
import json
import sys
import urllib.request

URL = "https://mcp.context7.com/mcp"


def call(tool, args):
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                       "params": {"name": tool, "arguments": args}}).encode()
    req = urllib.request.Request(URL, data=body, headers={
        "Content-Type": "application/json", "Accept": "application/json, text/event-stream"})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read().decode("utf-8")
    data = next(line[6:] for line in raw.splitlines() if line.startswith("data: "))
    msg = json.loads(data)
    if "error" in msg:
        sys.exit(f"Error de Context7: {msg['error']}")
    return "\n".join(c.get("text", "") for c in msg["result"]["content"])


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] not in ("resolve", "docs"):
        sys.exit(__doc__)
    cmd, a, b = sys.argv[1:]
    sys.stdout.reconfigure(encoding="utf-8")
    if cmd == "resolve":
        print(call("resolve-library-id", {"libraryName": a, "query": b}))
    else:
        print(call("query-docs", {"libraryId": a, "query": b}))
