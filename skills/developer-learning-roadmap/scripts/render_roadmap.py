#!/usr/bin/env python3
"""Render a validated roadmap JSON file as a standalone interactive HTML page."""

from __future__ import annotations

import argparse
import json
import os
import re
import secrets
import sys
import tempfile
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import quote, urlparse


MAX_INPUT_BYTES = 2_000_000
MAX_NODES = 200
ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9._-]{0,79}$")
TEMPLATE_PATH = Path(__file__).resolve().parent.parent / "assets" / "roadmap-template.html"
FAVICON_PATH = Path(__file__).resolve().parent.parent / "assets" / "favicon.svg"


class ValidationError(ValueError):
    """Raised when the roadmap input does not satisfy the rendering contract."""


def require_text(value: object, field: str, maximum: int, *, optional: bool = False) -> str:
    if optional and value is None:
        return ""
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{field} must be a non-empty string")
    value = value.strip()
    if len(value) > maximum:
        raise ValidationError(f"{field} must be at most {maximum} characters")
    return value


def string_list(value: object, field: str, *, maximum_items: int = 20) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or len(value) > maximum_items:
        raise ValidationError(f"{field} must be a list with at most {maximum_items} items")
    return [require_text(item, f"{field}[{index}]", 300) for index, item in enumerate(value)]


def validate_resources(value: object, field: str) -> list[dict[str, str]]:
    if value is None:
        return []
    if not isinstance(value, list) or len(value) > 20:
        raise ValidationError(f"{field} must be a list with at most 20 items")

    resources: list[dict[str, str]] = []
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            raise ValidationError(f"{field}[{index}] must be an object")
        label = require_text(item.get("label"), f"{field}[{index}].label", 120)
        url = require_text(item.get("url"), f"{field}[{index}].url", 500)
        parsed = urlparse(url)
        if parsed.scheme not in {"https", "http"} or not parsed.netloc:
            raise ValidationError(f"{field}[{index}].url must be an absolute HTTP(S) URL")
        resources.append({"label": label, "url": url})
    return resources


def validate_acyclic(nodes: list[dict[str, object]]) -> None:
    incoming = {node["id"]: len(node["depends_on"]) for node in nodes}
    outgoing: dict[str, list[str]] = {node_id: [] for node_id in incoming}
    for node in nodes:
        for dependency in node["depends_on"]:
            outgoing[dependency].append(node["id"])

    queue = [node_id for node_id, count in incoming.items() if count == 0]
    visited = 0
    while queue:
        node_id = queue.pop()
        visited += 1
        for child in outgoing[node_id]:
            incoming[child] -= 1
            if incoming[child] == 0:
                queue.append(child)

    if visited != len(nodes):
        cyclic = sorted(node_id for node_id, count in incoming.items() if count > 0)
        raise ValidationError(f"dependency graph contains a cycle involving: {', '.join(cyclic)}")


def validate_roadmap(raw: object) -> dict[str, object]:
    if not isinstance(raw, dict):
        raise ValidationError("roadmap root must be an object")

    roadmap_id = require_text(raw.get("id"), "id", 80)
    if not ID_PATTERN.fullmatch(roadmap_id):
        raise ValidationError("id must use lowercase letters, digits, dots, underscores, or hyphens")

    raw_nodes = raw.get("nodes")
    if not isinstance(raw_nodes, list) or not raw_nodes or len(raw_nodes) > MAX_NODES:
        raise ValidationError(f"nodes must contain between 1 and {MAX_NODES} items")

    nodes: list[dict[str, object]] = []
    seen_ids: set[str] = set()
    for index, item in enumerate(raw_nodes):
        if not isinstance(item, dict):
            raise ValidationError(f"nodes[{index}] must be an object")
        node_id = require_text(item.get("id"), f"nodes[{index}].id", 80)
        if not ID_PATTERN.fullmatch(node_id):
            raise ValidationError(f"nodes[{index}].id has unsupported characters")
        if node_id in seen_ids:
            raise ValidationError(f"duplicate node id: {node_id}")
        seen_ids.add(node_id)

        depends_on = string_list(item.get("depends_on"), f"nodes[{index}].depends_on")
        if len(depends_on) != len(set(depends_on)):
            raise ValidationError(f"nodes[{index}].depends_on contains duplicates")
        if node_id in depends_on:
            raise ValidationError(f"node {node_id} cannot depend on itself")

        nodes.append(
            {
                "id": node_id,
                "title": require_text(item.get("title"), f"nodes[{index}].title", 120),
                "summary": require_text(
                    item.get("summary"), f"nodes[{index}].summary", 500, optional=True
                ),
                "phase": require_text(
                    item.get("phase"), f"nodes[{index}].phase", 80, optional=True
                ),
                "depends_on": depends_on,
                "practice": string_list(item.get("practice"), f"nodes[{index}].practice"),
                "mastery": string_list(item.get("mastery"), f"nodes[{index}].mastery"),
                "resources": validate_resources(item.get("resources"), f"nodes[{index}].resources"),
            }
        )

    for node in nodes:
        missing = sorted(set(node["depends_on"]) - seen_ids)
        if missing:
            raise ValidationError(f"node {node['id']} has unknown dependencies: {', '.join(missing)}")
    validate_acyclic(nodes)

    language = raw.get("language", "en")
    if language not in {"en", "ru"}:
        raise ValidationError("language must be 'en' or 'ru'")

    return {
        "schema_version": 1,
        "language": language,
        "id": roadmap_id,
        "title": require_text(raw.get("title"), "title", 160),
        "subtitle": require_text(raw.get("subtitle"), "subtitle", 300, optional=True),
        "description": require_text(raw.get("description"), "description", 1200, optional=True),
        "nodes": nodes,
        "storage_key": f"developer-learning-roadmap:v1:{roadmap_id}",
        "generated_at": datetime.now(UTC).isoformat(timespec="seconds"),
    }


def safe_json_for_html(data: object) -> str:
    serialized = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    return (
        serialized.replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


def render(input_path: Path, output_path: Path) -> None:
    if input_path.stat().st_size > MAX_INPUT_BYTES:
        raise ValidationError(f"input exceeds {MAX_INPUT_BYTES} bytes")
    try:
        raw = json.loads(input_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValidationError(f"invalid JSON: {error}") from error

    data = validate_roadmap(raw)
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    favicon_data = quote(FAVICON_PATH.read_text(encoding="utf-8"), safe="")
    nonce = secrets.token_urlsafe(18)
    if (
        template.count("__ROADMAP_DATA__") != 1
        or template.count("__CSP_NONCE__") != 5
        or template.count("__LANG__") != 1
        or template.count("__FAVICON_DATA__") != 1
    ):
        raise RuntimeError("roadmap template placeholders are missing or duplicated")

    html = template.replace("__ROADMAP_DATA__", safe_json_for_html(data))
    html = html.replace("__CSP_NONCE__", nonce)
    html = html.replace("__LANG__", data["language"])
    html = html.replace("__FAVICON_DATA__", favicon_data)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=output_path.parent, delete=False, suffix=".tmp"
    ) as handle:
        handle.write(html)
        temporary_path = Path(handle.name)
    os.replace(temporary_path, output_path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="roadmap JSON file")
    parser.add_argument("--output", "-o", required=True, type=Path, help="output HTML file")
    args = parser.parse_args()

    try:
        render(args.input.resolve(), args.output.resolve())
    except (OSError, ValidationError, RuntimeError) as error:
        print(f"render_roadmap: {error}", file=sys.stderr)
        return 2

    print(f"Rendered interactive roadmap: {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
