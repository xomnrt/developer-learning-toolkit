# Roadmap output contract

## 1. Target and constraints

State the target in observable terms. If the user supplied a title such as
"middle", explain how the roadmap interprets it and which expectations remain
organization-specific.

Include:

- current evidence;
- target responsibilities and representative tasks;
- horizon and weekly capacity;
- sources of feedback;
- assumptions and unknowns.

## 2. Gap map

Use a compact table:

| Capability area | Current evidence | Target evidence | Priority | How to verify |
| --- | --- | --- | --- | --- |

Separate foundations, target-critical capabilities, multipliers, supporting
topics, and later backlog.

## 3. Summary roadmap

Use a table at the time scale that fits the horizon:

| Period | Outcome | Capabilities | Practice or artifact | Exit evidence |
| --- | --- | --- | --- | --- |

The outcome must describe performance. Topic exposure belongs in the
capabilities column, not the outcome column.

## 4. Detailed phases

For every phase include:

```text
Outcome
Problem and system model
Concepts and concrete APIs
Worked or guided practice
Independent and transfer task
Artifact
Feedback and review
Mastery check
Exit criteria
Sources
```

Show the first 1-2 weeks at session-level detail. Later phases may remain less
granular because checkpoint evidence can change them.

## 5. Practice system

Define:

- session loop and minimum viable session;
- supported-to-independent progression;
- stuck and hint policy;
- retrieval and spaced review;
- project or workplace practice sequence;
- how missed sessions are handled without backlog.

If a learning profile exists, use it. Otherwise label settings as initial
experiments and provide adjustment rules.

## 6. Mastery and review

Use an observable scale suited to the target. A default is:

0. unfamiliar;
1. recognize and trace with materials;
2. explain and complete with a worked example;
3. perform a standard task with hints;
4. perform and debug independently;
5. transfer, compare alternatives, and explain to another developer.

State the checkpoint cadence and the evidence needed to continue, repeat, step
down, or revise the roadmap.

## 7. Sources, exclusions, and risks

List current source links and access dates. Explain which decisions are sourced
facts and which are planning judgments. End with:

- explicit exclusions from the current horizon;
- later backlog;
- largest risks to completion or transfer;
- the first concrete action.

## 8. Optional interactive artifact

When requested, provide the roadmap JSON and rendered standalone HTML described
in `visual-roadmap.md`. Keep node IDs stable between revisions. The visual state
tracks user checkmarks, while mastery claims remain grounded in the roadmap's
exit criteria and later practice evidence.
