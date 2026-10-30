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
- Treat `practice` as an ordered verification task: write concrete steps that
  produce evidence, not a list of resources to consume.
- Make every task self-contained: include the code, data, scenario, or links
  needed to start. Define unfamiliar terms before using them; replace phrases
  such as “try four invocation forms” or “check a similar example” with the
  exact variants and a concrete expected observation.
- Validate each task before rendering it: the fixture is specified, the action
  is unambiguous, the expected observation is stated, and the evidence needed
  to mark the step complete is observable.
- Prefer the four-part task shape: **Context → Action → Expected observation →
  Evidence**. A short task is acceptable only when all four parts are still
  unambiguous.
- If a diagnosed learning profile is available, shape the order and scaffolding
  of `practice` around it. For a conceptual profile, use problem -> system
  model -> prediction -> experiment -> implementation -> transfer. Do not
  encode a generic “learning style” label in the artifact.
- Treat `mastery` as observable completion criteria. Prefer statements such as
  "I can explain…", "I can predict…", "I can diagnose…", or "I can transfer…".
- Make each mastery claim testable in a named scenario: specify the input or
  changed requirement, the action the learner takes, and the evidence a reviewer
  should observe. Replace broad claims such as “explain state ownership” with a
  concrete diagram, code change, diagnosis, or transfer task.
- Keep the summary as the topic model: what the learner is trying to understand
  before they perform the verification task.
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
- a graph that fits the available viewport width by default, with zoom in,
  zoom out, and fit-to-viewport controls when labels need more space;
- blocked, ready, and completed states;
- completion checkboxes and aggregate progress;
- detail panels with practice and mastery evidence;
- filtering;
- local browser persistence scoped to the roadmap ID;
- reset of local progress;
- responsive light and dark themes;
- no CDN, analytics, network requests, or third-party JavaScript.

## Persistence

Browser behavior for `localStorage` on `file:` URLs is not consistent. For
reliable persistence, serve the output directory locally:

```bash
python3 -m http.server 8000 --directory /path/to/output
```

Then open `http://localhost:8000/roadmap.html`. Progress currently stays in the
browser profile; account-backed sync or a portable progress format is deferred
until there is a clear user workflow for it.

## Security boundary

The renderer makes no network requests and writes only the requested output
file. Generated pages use a restrictive Content Security Policy and render all
roadmap content as text.

Treat resource links as external navigation. Verify them during roadmap
research. Do not include credentials, internal URLs, confidential project
names, or proprietary descriptions in a roadmap intended for sharing.
