"""Frontmatter parsing and serialization."""

from __future__ import annotations

import re
from typing import Any


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    block = text[3:end]
    body = text[end + 4 :].lstrip("\n")
    data: dict[str, Any] = {}
    current_key = None
    current_dict: dict | None = None
    list_key = None
    list_items: list = []

    for line in block.splitlines():
        if not line.strip():
            continue
        if line.startswith("  ") and current_dict is not None and ":" in line:
            k, v = line.strip().split(":", 1)
            v = v.strip().strip('"')
            if v == "true":
                current_dict[k] = True
            elif v == "false":
                current_dict[k] = False
            elif v.isdigit():
                current_dict[k] = int(v)
            else:
                current_dict[k] = v
            continue
        if line.startswith("  - ") and list_key:
            list_items.append(line[4:].strip().strip('"'))
            continue
        if list_key and not line.startswith("  "):
            data[list_key] = list_items
            list_key = None
            list_items = []
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        k = k.strip()
        v = v.strip()
        if v == "" or v == "|":
            if k == "related":
                data[k] = {}
                current_dict = data[k]
            else:
                list_key = k
                list_items = []
            current_key = k
            continue
        current_dict = None
        list_key = None
        if v.startswith("[") and v.endswith("]"):
            inner = v[1:-1].strip()
            data[k] = [] if not inner else [i.strip().strip('"') for i in inner.split(",")]
        elif v in ("true", "false"):
            data[k] = v == "true"
        elif v.replace(".", "", 1).isdigit():
            data[k] = float(v) if "." in v else int(v)
        else:
            data[k] = v.strip('"')
    if list_key:
        data[list_key] = list_items
    return data, body


def yaml_block(d: dict, indent: int = 0) -> list[str]:
    lines = []
    sp = "  " * indent
    for k, v in d.items():
        if isinstance(v, dict):
            lines.append(f"{sp}{k}:")
            for sk, sv in v.items():
                if isinstance(sv, dict):
                    lines.append(f"{sp}  {sk}:")
                    lines.extend(yaml_block(sv, indent + 2))
                elif isinstance(sv, bool):
                    lines.append(f"{sp}  {sk}: {'true' if sv else 'false'}")
                elif isinstance(sv, list):
                    if not sv:
                        lines.append(f"{sp}  {sk}: []")
                    else:
                        lines.append(f"{sp}  {sk}: [{', '.join(str(i) for i in sv)}]")
                elif isinstance(sv, (int, float)):
                    lines.append(f"{sp}  {sk}: {sv}")
                else:
                    s = str(sv).replace('"', '\\"')
                    lines.append(f'{sp}  {sk}: "{s}"')
        elif isinstance(v, list):
            if not v:
                lines.append(f"{sp}{k}: []")
            elif all(isinstance(i, str) for i in v):
                lines.append(f"{sp}{k}: [{', '.join(i for i in v)}]")
            else:
                lines.append(f"{sp}{k}:")
                for i in v:
                    lines.append(f"{sp}  - {i}")
        elif isinstance(v, bool):
            lines.append(f"{sp}{k}: {'true' if v else 'false'}")
        elif isinstance(v, (int, float)):
            lines.append(f"{sp}{k}: {v}")
        else:
            s = str(v).replace('"', '\\"')
            lines.append(f'{sp}{k}: "{s}"')
    return lines


def serialize_page(fm: dict, body_lines: list[str]) -> str:
    body = "\n".join(body_lines).rstrip() + "\n"
    return "---\n" + "\n".join(yaml_block(fm)) + "\n---\n\n" + body
