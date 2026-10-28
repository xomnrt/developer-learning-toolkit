# Frontend learning add-on draft

Status: source material for a future companion skill or plugin add-on. This
file is deliberately outside `developer-learning-coach`, so the core skill
stays independent of a particular stack.

## Purpose

Adapt a general developer-learning assessment to the learner's real frontend
work without changing the evidence rules, diagnostic sequence, or final
learning-model format of the core skill.

The add-on should provide two optional inputs:

1. A work-context inventory covering technologies already used, technologies
   expected at work, prior depth of experience, recurring tasks, and near-term
   goals.
2. Frontend-specific situational scenarios that reveal initiation difficulty,
   ambiguity tolerance, response to errors, need for scaffolding, and transfer
   of knowledge.

It should output a compact context card that can be passed to the core
`developer-learning-coach` skill. It must not produce a learning profile or
recommendations before the core diagnostic interview is complete.

## Work-context inventory to preserve

Ask about concrete behavior and experience rather than confidence alone.

- Current role, product area, team context, and typical responsibility level.
- Technologies used regularly at work.
- Technologies used occasionally or only read in the codebase.
- Technologies used previously but not recently.
- Technologies the learner expects or wants to use in the next 3–12 months.
- For each relevant technology: time used, recency, frequency, task types,
  degree of independence, debugging experience, and ability to explain the
  underlying model.
- Which technologies are required by work, chosen from curiosity, or pursued
  for career growth.
- Which skills have immediate feedback at work and which have delayed or
  ambiguous feedback.
- Recurring tasks that feel routine, challenging-but-manageable, or currently
  out of reach.
- Constraints imposed by the real codebase: size, legacy code, tests,
  documentation, ownership, deadlines, and access to reviewers or mentors.

Avoid turning years of experience into a mastery score. Prefer observable
evidence such as "implemented independently", "debugged in production",
"can modify with an example", or "recognize but cannot yet use".

## Frontend scenarios from the original prompt

Use several of these, selected to match the learner's actual context:

- Learn the JavaScript Event Loop.
- Explain why a React component rerenders.
- Read and understand an unfamiliar selector.
- Understand middleware in an existing application.
- Navigate a large production component.
- Solve an algorithmic problem.
- Learn a new library.
- Debug a race condition.
- Implement a small feature in an unfamiliar part of a project.

For each selected scenario, compare:

- willingness to start;
- expected interest;
- perceived competence;
- uncertainty about where to search and when the task is done;
- preferred first action;
- time tolerated without progress;
- likelihood of seeking an example, hint, documentation, colleague, or AI;
- what outcome would count as mastery rather than mere completion.

## Possible future packaging

Preferred shape if this becomes public:

```text
developer-learning-coach          # stack-independent core skill
developer-work-context            # generic technology/context inventory
developer-learning-roadmap        # generic technology, level, and transition plan
developer-learning-frontend       # frontend scenario adapter
```

A Codex plugin may bundle these skills for distribution, but the plugin should
not be required to use the core skill. The generic work-context inventory is
separate from the frontend adapter because backend, data, mobile, DevOps, and
other adapters can reuse it.

Detailed frontend curriculum coverage, project examples, and the requested
roadmap granularity are backed up separately in
[`frontend-roadmap-addon.md`](frontend-roadmap-addon.md).
