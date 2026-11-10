#!/usr/bin/env python3
"""Builds the page from build/src.html.

  index.html       the page body only (this is what the Claude artifact preview publishes)
  dist/index.html  a complete standalone HTML document, ready to host or open in a browser

usage: python3 build/build.py
"""
import json, pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "build" / "src.html").read_text(encoding="utf8")
thumbs = json.loads((root / "build" / "thumbs.json").read_text(encoding="utf8"))
assert "/*THUMBS*/{}" in src
page = src.replace("/*THUMBS*/{}", json.dumps(thumbs))
(root / "index.html").write_text(page, encoding="utf8")

head_end = page.index("<header")           # everything before the header is title, meta, fonts and styles
head = re.sub(r'<meta name="claude:[^>]*>\n?', "", page[:head_end])
doc = ('<!doctype html>\n<html lang="en-AU">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       "<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"
       + head + "</head>\n<body>\n" + page[head_end:] + "</body>\n</html>\n")
(root / "dist").mkdir(exist_ok=True)
(root / "dist" / "index.html").write_text(doc, encoding="utf8")
print("built index.html and dist/index.html")
