# Interactive roadmap artifact

Generate the visual artifact when the user asks for HTML, a dependency graph,
progress tracking, or an interactive roadmap. It is also useful for a roadmap
with at least four dependent capabilities when the user wants a reusable file.

## Input contract

Create a UTF-8 JSON file with this shape:

```json
{
  "id": "frontend-middle-2026",
  "language": "ru",
  "title": "Frontend responsibility roadmap",
  "subtitle": "Current state to target evidence",
  "description": "Optional longer description",
  "nodes": [
    {
      "id": "react-rendering-model",
      "title": "React rendering model",
      "summary": "Predict, measure, and explain component rerenders.",
      "phase": "Rendering and state",
      "depends_on": ["javascript-execution-model"],
      "practice": [
        "Predict rerenders in a small component tree",
        "Verify the prediction with React DevTools Profiler"
      ],
      "mastery": [
        "Diagnose an unnecessary rerender without a supplied fix",
        "Explain why the chosen change is safe"
      ],
      "resources": [
        {
          "label": "React documentation",
          "url": "https://react.dev/learn/render-and-commit"
        }
      ]
    }
  ]
}
```

Rules:

- `language` is `ru` or `en` and controls the interface language. It defaults to
  `en` when omitted.
- `id` and node IDs use lowercase letters, numbers, dots, underscores, and
  hyphens. Keep them stable across regenerated versions so progress remains
  attached to the same capability.
- `depends_on` contains node IDs and must form an acyclic graph.
- Write plain text in content fields. The renderer inserts it through safe DOM
  APIs and does not interpret HTML.
- Use only absolute HTTP(S) resource links.
- Keep one node per observable capability. A node should fit one mastery check,
  not a whole career phase.
- When a capability changes meaning substantially, give it a new ID instead of
  reusing stored completion state.

## Render command

Run the bundled renderer from the skill directory:

```bash
python3 scripts/render_roadmap.py roadmap.json --output roadmap.html
```

The renderer uses only the Python standard library. It validates IDs, links,
dependencies, input size, and graph cycles before writing the file atomically.

## Artifact behavior

The generated page provides:

- a dependency graph and accessible list view;
- blocked, ready, and completed states;
- completion checkboxes and aggregate progress;
- detail panels with practice and mastery evidence;
- filtering;
- local browser persistence scoped to the roadmap ID;
- progress export, import, and reset;
- responsive light and dark themes;
- no CDN, analytics, network requests, or third-party JavaScript.

## Persistence

Browser behavior for `localStorage` on `file:` URLs is not consistent. For
reliable persistence, serve the output directory locally:

```bash
python3 -m http.server 8000 --directory /path/to/output
```

Then open `http://localhost:8000/roadmap.html`. Keep an exported progress JSON
as a backup. The export includes completed node IDs and titles, so it can also
scope a `developer-mock-interview` session.

## Security boundary

The renderer makes no network requests and writes only the requested output
file. Generated pages use a restrictive Content Security Policy and render all
roadmap content as text.

Treat resource links as external navigation. Verify them during roadmap
research. Do not include credentials, internal URLs, confidential project
names, or proprietary descriptions in a roadmap intended for sharing.
