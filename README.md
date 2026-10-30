# Developer Learning Toolkit

[English](README.md) | [Русский](README.ru.md)

Learning often breaks somewhere between motivation, uncertainty, task
difficulty, practice, and feedback. A generic study plan cannot tell you where.

Developer Learning Toolkit maps your work and career goals, examines how your
learning system behaves, and builds a detailed path toward a technology, role,
or responsibility target.

It is designed for software developers in any domain or stack.

## What is included

| Skill | Purpose |
| --- | --- |
| [`developer-work-context`](skills/developer-work-context/) | Maps the technologies you use now, have used before, and expect to use next. Produces a reusable work-context card. |
| [`developer-learning-coach`](skills/developer-learning-coach/) | Diagnoses how your current learning system behaves and creates a personalized practice, review, planning, and difficulty-management system. |
| [`developer-learning-roadmap`](skills/developer-learning-roadmap/) | Builds a source-backed roadmap for a technology, responsibility level, or transition into another technical specialty. |
| [`developer-mock-interview`](skills/developer-mock-interview/) | Runs one adaptive technical case at a time and tests capabilities completed in the roadmap. |

The skills work independently, but they are most useful together.

## How the full flow works

```text
Work, technology, and career-direction inventory
        ↓
Developer Work Context Card
        ├── Learning diagnostic interview
        │        ↓
        │   Learning model, session loop, difficulty ladder,
        │   stuck protocol, and mastery metrics
        │
        └── Current-to-target gap map
                 ↓
            Detailed technology, level, or career-transition roadmap
                 ↓
            Rolling 1–2 week cycles with mastery checkpoints
                 ↓
            Interactive dependency graph and local progress
                 ↓
            Adaptive mock interviews on completed capabilities
```

The toolkit does not produce a profile before collecting your answers. The
first interview ends with questions and waits for you to respond.

## Install the toolkit

The repository is packaged as a plugin for Codex and Claude Code.
Both hosts use the same `skills/` directories. The plugin has no MCP server,
hooks, external accounts, analytics, or third-party runtime dependencies. Its
offline HTML renderer uses the Python standard library.

### Quick start

If this is your first time using the toolkit:

1. Install the plugin for Codex or Claude Code using one of the methods below.
2. Start a new conversation.
3. Paste this request:

   ```text
   Use developer-learning-toolkit. Help me build a TypeScript learning roadmap.
   Ask about my goal, current experience, and available time first. Respond in
   English and give concrete tasks with observable checks.
   ```

To request the visual artifact as well:

```text
Generate the roadmap JSON and an interactive HTML dependency graph with browser
progress storage.
```

The conversation and the HTML graph serve different purposes: the conversation
builds and explains the plan, while the graph shows dependencies, opens tasks,
and lets you mark topics as completed.

### Codex

After the public listing is available, open `/plugins`, search for
`Developer Learning Toolkit`, and select **Install**. Start a new conversation
after the first installation.

Until then, install the standalone skills for your user:

```bash
mkdir -p ~/.codex/skills
cp -R skills/developer-work-context skills/developer-learning-coach \
  skills/developer-learning-roadmap skills/developer-mock-interview \
  ~/.codex/skills/
```

For one repository, copy them into that repository's `.codex/skills` directory:

```bash
mkdir -p /path/to/project/.codex/skills
cp -R skills/developer-work-context skills/developer-learning-coach \
  skills/developer-learning-roadmap skills/developer-mock-interview \
  /path/to/project/.codex/skills/
```

See the [official OpenAI skills documentation](https://developers.openai.com/plugins/concepts/skills)
for discovery and activation details.

### Claude Code from the marketplace

On Claude Code 2.1.275 or later, install directly from the hosted GitHub
repository:

```text
/plugin install developer-learning-toolkit --marketplace xomnrt/developer-learning-toolkit
```

The equivalent shell commands register the marketplace first and then install
the plugin:

```bash
claude plugin marketplace add xomnrt/developer-learning-toolkit
claude plugin install \
  developer-learning-toolkit@developer-learning-toolkit-marketplace
```

The repository already contains `.claude-plugin/marketplace.json`, so no
separate marketplace repository is required.

### Claude Code from a local checkout

Validate the checkout and load it for one session:

```bash
claude plugin validate .
claude --plugin-dir .
```

To load it automatically in future local sessions, clone the repository into
Claude Code's personal skills directory:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/xomnrt/developer-learning-toolkit.git \
  ~/.claude/skills/developer-learning-toolkit
```

Claude Code treats a directory under `~/.claude/skills/` that contains
`.claude-plugin/plugin.json` as a personal plugin. See Anthropic's official
[plugin documentation](https://code.claude.com/docs/en/plugins/overview) and
[skills documentation](https://code.claude.com/docs/en/skills).

### Invocation names

| Host | Work context | Learning diagnostic | Detailed roadmap | Mock interview |
| --- | --- | --- | --- | --- |
| Codex | `$developer-work-context` | `$developer-learning-coach` | `$developer-learning-roadmap` | `$developer-mock-interview` |
| Claude Code plugin | `/developer-learning-toolkit:developer-work-context` | `/developer-learning-toolkit:developer-learning-coach` | `/developer-learning-toolkit:developer-learning-roadmap` | `/developer-learning-toolkit:developer-mock-interview` |

Natural-language activation also works when the request matches a skill's
description.

The commands above use macOS/Linux paths. On another operating system, use the
equivalent user and project directories.

If a skill does not activate automatically, invoke it explicitly using the name
from the table above. After installing a plugin, starting a new conversation
usually makes discovery predictable.

## Recommended usage

The examples below use Codex invocation names. In Claude Code, substitute the
names from the table above.

### Step 1: map your work context

Start with:

```text
Use $developer-work-context to map the technologies I use at work,
my previous experience, and the technologies I expect to learn next.
```

The skill will ask about:

- your role and recurring work;
- technologies used regularly, occasionally, or in the past;
- technologies planned for the next 3–12 months;
- tasks you can perform independently;
- tasks that still require examples or help;
- feedback, support, deadlines, and time constraints;
- current-role goals, technology goals, and possible career transitions;
- one observable outcome for the next short cycle, while other goals remain in
  the context card.

It will turn your answers into a `Developer Work Context Card`. The card records
facts and goals without assigning you a seniority label or a learning type.

### Step 2: run the learning diagnostic

In the same conversation, continue with:

```text
Use $developer-learning-coach with the context card we just created.
I want to understand why my learning stalls and build a system I can sustain.
```

The coach will first ask approximately 15–20 questions. They combine concrete
scenarios, rankings, scales, choices, and short descriptions of past learning
episodes.

Answer by number. Short answers are fine unless the question asks for a real
example.

After the first round, the coach may ask 3–7 focused follow-up questions when
an important contradiction or gap remains. It should not extend the interview
only for the sake of collecting more data.

### Step 3: receive the learning system

Once enough evidence is available, the coach builds:

- a causal model from motivation to continued learning;
- an approximate profile across practical learning dimensions;
- a repeatable structure for one study session;
- a 5–8 level difficulty ladder;
- a protocol for getting unstuck without immediately opening the solution;
- a 4–8 week plan that does not create debt after missed days;
- activity and mastery metrics;
- rules for choosing materials and appropriately difficult tasks;
- a representative week based on your actual development work.

Recommendations should be connected to your answers. Uncertain conclusions
should be marked as tentative rather than presented as facts.

### Step 4: build a detailed roadmap

Roadmaps can start from four kinds of input:

| Mode | Use it when | Map backbone |
| --- | --- | --- |
| Goal-driven | You need a role transition or a work outcome | Target responsibilities and a gap map |
| Technology-driven | You want to learn a language, framework, or tool | Concept dependencies and practice tasks |
| Source-driven | You have a book, course, documentation set, or syllabus | The source outline with chapter traceability |
| Hybrid | You need to connect a source to real work | The source plus work-context requirements |

For source-driven roadmaps you can provide a book title and edition, an official
table-of-contents URL, a course syllabus, a documentation sidebar, or your own
topic outline. When the source is incomplete, the skill marks the gap instead of
inventing chapters. Nodes added for practice or work requirements remain distinct
from nodes derived from the source.

Use the context card and, when available, the diagnosed learning system:

```text
Use $developer-learning-roadmap. I want to move from frontend development into
data engineering over the next six months. Build a current-to-target gap map,
use roadmap.sh for coverage discovery, verify technical details in primary
sources, and give me detailed phases, projects, mastery checks, and the first
two weeks at session level.
```

The roadmap skill can also plan one technology or growth toward a responsibility
level:

```text
Use $developer-learning-roadmap to plan my growth toward middle-level frontend
responsibilities. Translate the title into observable work and independence.
I have 8 hours per week for 16 weeks.
```

It may use a relevant [roadmap.sh](https://roadmap.sh/) roadmap as a coverage and
dependency map. It selects only topics that serve the target work, checks
current technical facts against primary sources, and keeps excluded topics in a
later backlog. A role title is never treated as a universal standard across
companies.

The roadmap can also be source-driven: use a book, course syllabus, or
documentation outline as the backbone:

```text
Use $developer-learning-roadmap. I want to study You Don't Know JS Yet.
Use the table of contents for my edition as the source outline, turn chapters
into small capabilities with dependencies, practice tasks, and observable
mastery checks. Mark which nodes come from the book and which are additions for
real frontend work. Produce the roadmap JSON and interactive HTML graph.
```

If editions differ, provide the table of contents or the exact edition URL. The
outline is a coverage map, not a checkbox list: chapters are split into
observable skills, dependencies are checked, and reading is supplemented with
practice, debugging, and transfer tasks.

Each node can include the topic and problem it solves, prerequisites and the
original chapter or section, an ordered verification task, observable “I can…”
mastery criteria, primary source links, and the next available step in the graph.

The diagnostic is optional for roadmap creation. Use it when motivation,
starting, task difficulty, or review habits are likely to affect execution.

If you have completed the diagnostic, pass its profile with the roadmap request:

```text
Use my profile: conceptual, example-first, guided with gradually fading
scaffolding. For every node, start with the problem and causal model, then give
a prediction, a small experiment, an implementation task, and a transfer task.
```

The profile changes the explanation order and hint level; it is not a personality
type or a sensory learning-style label.

### Step 5: generate the interactive roadmap

Ask the roadmap skill for an HTML artifact:

```text
Use $developer-learning-roadmap to generate the roadmap JSON and an interactive
HTML dependency graph. I want to mark capabilities as completed and keep progress
in local browser storage.
```

The standalone page includes graph and list views, blocked/ready/completed
states, progress filters, details for practice and mastery, and local reset.
Progress is stored in the browser and scoped to the roadmap ID. The page has no
CDN, analytics, or network requests. The graph fits the available workspace
width by default without horizontal scrolling; zoom controls let you enlarge it
or return to the fitted scale.

For reliable browser persistence, serve the output directory locally:

```bash
python3 -m http.server 8000 --directory /path/to/output
```

Then open `http://localhost:8000/roadmap.html`. Opening the file directly also
works, but browser behavior for `localStorage` on `file:` URLs varies.

### Troubleshooting

- **Not sure where to start** — use `developer-work-context`, then
  `developer-learning-coach`, then `developer-learning-roadmap`.
- **The plan is too generic** — provide concrete code, a project, a book or
  table of contents, a deadline, and available hours per week.
- **The graph does not open** — verify the JSON path and run the renderer from
  `skills/developer-learning-roadmap/scripts`.
- **Progress is not saved** — serve the HTML with `python3 -m http.server`
  instead of opening a `file:` URL directly.
- **Need another language** — state it explicitly, for example “Respond in
  Russian” or “Conduct the roadmap in English”.

### Step 6: practice completed material in a mock interview

Use the current roadmap and the completed nodes visible in the current session:

```text
Use $developer-mock-interview with the completed nodes from my current roadmap. Run a realistic
mock interview for a middle system analyst. Ask one practical case at a time,
wait for my answer, give strict constructive feedback, and gradually increase
the ambiguity.
```

The interview skill does not equate a checkmark with mastery. It tests completed
capabilities through clarification, system modeling, diagnosis, tradeoffs, and
verification. At the end it identifies demonstrated capabilities and roadmap
nodes worth revisiting.

## Faster ways to use it

### Skip the work-context inventory

If the coach already has enough information about your role and target topic:

```text
Use $developer-learning-coach to diagnose how I learn database internals.
I am a backend developer, and my goal is to debug query-performance problems
independently. Start with the interview and do not give advice yet.
```

### Bring an existing context description

```text
Use $developer-learning-coach with the context below.

[Paste your role, technologies, constraints, and target capability here.]
```

### Continue after a break

```text
Continue the $developer-learning-coach assessment from my previous answers.
First summarize what is known and ask only the unresolved questions.
```

### Inspect your learning system without rebuilding it

```text
Use $developer-learning-coach to review this learning plan against my existing
profile. Identify which assumptions still fit and which need to be tested again.
```

### Plan a transition into another specialty

```text
Use $developer-work-context to record my current experience and possible move
from mobile development into backend engineering. Then use
$developer-learning-roadmap to compare transferable skills, missing foundations,
bridge projects, and a realistic six-month sequence.
```

## What this toolkit does not do

It does not:

- classify you as a visual, auditory, or kinesthetic learner;
- diagnose ADHD, anxiety, depression, or another medical condition;
- infer mastery from years of experience or hours studied;
- treat course completion as proof of learning;
- promise that one interview reveals the true cause of every difficulty;
- replace professional medical or psychological assessment.

The result is a working model based mainly on self-report. Its recommendations
should be tested against your behavior and updated when the evidence changes.

## Privacy

You do not need to share source code, credentials, customer information, company
names, or confidential architecture.

Describe work in anonymized terms, for example:

```text
I maintain a large event-driven service with slow integration tests.
```

instead of pasting proprietary code or internal documentation.

## Evidence and design principles

The coach distinguishes:

- what you directly reported;
- what it infers from your answers;
- what is supported by broader learning research;
- what remains an experiment to validate in your situation.

Its evidence boundaries and starting sources are documented in
[`evidence-base.md`](skills/developer-learning-coach/references/evidence-base.md).
The toolkit intentionally avoids unsupported learning-style labels and does not
assume that findings from controlled education research transfer unchanged to
professional software development.

## Language and domain

The skill instructions are written in English for portability. The skills
should conduct the interview and produce the final result in the language used
by the user.

You can select a language explicitly:

```text
Use $developer-learning-coach. Conduct the interview in English.
```

```text
Используй $developer-learning-coach. Проводи опрос и анализ на русском языке.
```

If no language is specified, the skills use the language of the user's latest
substantive message. They ask only when the intended language is ambiguous.

The core is stack-independent. Domain-specific scenarios should be generated
from the user's real work rather than from a fixed frontend, backend, data, or
infrastructure curriculum.

The original frontend scenarios and curriculum examples are preserved as draft
adapter material in [`drafts/`](drafts/). They are not loaded into the generic
skills and do not constrain roadmaps for other specialties.

## Current status

This is an early plugin release. The four skills remain independently
usable and do not require external services.

Feedback is most useful when it includes:

- the prompt you used;
- which skill activated;
- where the interview felt unclear or repetitive;
- whether the final recommendations were traceable to your answers;
- what changed after testing the system for one or two weeks.

## License

Licensed under the [MIT License](LICENSE).

## Security

Read [SECURITY.md](SECURITY.md) for the current threat model, privacy guidance,
and the security requirements for any future MCP server, hook, script, or data
storage feature.
