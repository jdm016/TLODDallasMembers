"""Build the single-file Claude artifact version of the portal.

Usage: python3 tools/build_artifact.py > build/portal-artifact.html

The Netlify site loads site/data/portal.json at runtime. The Claude artifact
version has no data file, so this script embeds the JSON into the page and
drops the document wrapper (the artifact host adds its own).
"""
import json
import pathlib
import re

root = pathlib.Path(__file__).resolve().parent.parent
page = (root / "site" / "index.html").read_text()
data = json.loads((root / "site" / "data" / "portal.json").read_text())

head = re.search(r"<title>.*?</style>\n", page, re.S).group(0)
body = re.search(r"<body>\n(.*)</body>", page, re.S).group(1)
state = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
embed = '<script type="application/json" id="portal-state">' + state + "</script>\n\n"
body = body.replace('<script id="portal-app">', embed + '<script id="portal-app">', 1)
print(head + "\n" + body, end="")
