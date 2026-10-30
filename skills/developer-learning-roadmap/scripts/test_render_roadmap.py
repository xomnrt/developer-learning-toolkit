#!/usr/bin/env python3

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("render_roadmap.py")


class RenderRoadmapTest(unittest.TestCase):
    def run_renderer(self, payload: dict) -> tuple[subprocess.CompletedProcess[str], str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "roadmap.json"
            output = root / "roadmap.html"
            source.write_text(json.dumps(payload), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(source), "--output", str(output)],
                capture_output=True,
                text=True,
                check=False,
            )
            html = output.read_text(encoding="utf-8") if output.exists() else ""
            return result, html

    def test_renders_safe_standalone_html(self) -> None:
        result, html = self.run_renderer(
            {
                "id": "frontend-middle-demo",
                "title": "Frontend </script> roadmap",
                "subtitle": "A dependency map",
                "nodes": [
                    {
                        "id": "javascript-model",
                        "title": "JavaScript execution model",
                        "summary": "Explain scope and async execution.",
                        "depends_on": [],
                        "practice": ["Trace an event loop example"],
                        "mastery": ["Predict callback ordering"],
                    },
                    {
                        "id": "react-rendering",
                        "title": "React rendering",
                        "depends_on": ["javascript-model"],
                    },
                ],
            }
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Content-Security-Policy", html)
        self.assertIn("data:image/svg+xml,", html)
        self.assertIn("developer-learning-roadmap:v1:frontend-middle-demo", html)
        self.assertNotIn("Frontend </script>", html)
        self.assertIn("Frontend \\u003c/script\\u003e roadmap", html)

    def test_rejects_dependency_cycles(self) -> None:
        result, html = self.run_renderer(
            {
                "id": "cycle-demo",
                "title": "Cycle",
                "nodes": [
                    {"id": "a", "title": "A", "depends_on": ["b"]},
                    {"id": "b", "title": "B", "depends_on": ["a"]},
                ],
            }
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("contains a cycle", result.stderr)
        self.assertEqual(html, "")


if __name__ == "__main__":
    unittest.main()
