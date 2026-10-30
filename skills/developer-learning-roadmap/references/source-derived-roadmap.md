# Source-derived roadmap

Use this mode when the learner names a book, course, documentation set, syllabus,
repository, or other bounded source and asks to turn it into a roadmap.

## Source contract

Collect the strongest available source material in this order:

1. user-provided table of contents, syllabus, or chapter list;
2. official publisher, author, course, or documentation page;
3. a maintained repository that contains the source outline;
4. secondary summaries only to fill a clearly marked gap.

Record the source title, edition or version, URL, and access date. If only a
title is provided, ask for the edition or a table of contents when different
editions could change the plan. Do not invent chapter names from memory.

## Transform the outline into capabilities

Use the source hierarchy as a traceability scaffold:

| Source item | Roadmap representation |
| --- | --- |
| Part, section, or module | phase or `phase` label |
| Chapter or coherent lesson | one or more capability candidates |
| Subheading | concept, prerequisite, or practice ingredient |
| Exercise or example | guided task or worked example |
| Review question | retrieval or mastery check |

For each candidate, write a compact capability contract:

- **Topic**: what system or idea the learner is trying to understand;
- **Why it matters**: the problem this knowledge helps solve;
- **Prerequisites**: dependencies supported by the source or by a clear causal
  relationship;
- **Practice**: ordered actions that produce evidence;
- **Mastery**: observable claims such as “I can explain…”, “I can predict…”,
  “I can diagnose…”, or “I can transfer…”;
- **Source trace**: chapter, section, page, or URL.

Keep one node small enough for one meaningful mastery check. Split a chapter
when it contains independent skills. Keep it as one node when splitting would
create trivia-level checkboxes with no separate evidence.

## Preserve the source without becoming a checklist

Build two layers:

1. **Source coverage**: what the book or course claims to cover;
2. **Learning evidence**: what the learner can do after studying it.

The roadmap may reorder chapters when prerequisites or practice feedback justify
it. Show the original chapter or module in the phase and source trace so the
learner can navigate back to the material. Mark additions as “roadmap addition”
when they are not present in the source.

Do not claim that finishing the source proves professional mastery. A completed
chapter is activity evidence; mastery requires retrieval, implementation,
debugging, explanation, or transfer.

## Custom requests and examples

For “I want to learn *You Don’t Know JS Yet*”, ask which edition or provide the
user's table of contents. Then:

1. map parts and books to phases;
2. turn a chapter such as scope, closures, or async into capability nodes;
3. connect prerequisites such as execution model before advanced async patterns;
4. add a small code-reading, prediction, or implementation task per node;
5. add transfer checks that use a new example rather than repeating the text;
6. keep browser APIs, testing, or project work as explicit additions when the
   learner's goal requires them but the book does not cover them.

The same procedure applies to “turn this course syllabus into a 10-week plan”,
“make a graph from this documentation sidebar”, and “use this interview book as
the backbone of my preparation”.

## Quality check

Before producing the roadmap, verify:

- every node has a source trace or is explicitly marked as an addition;
- dependencies are justified and acyclic;
- practice produces evidence rather than only more reading;
- mastery checks can be observed by the learner or reviewer;
- skipped or deferred source items remain visible in a backlog;
- the plan fits the learner's time budget.
