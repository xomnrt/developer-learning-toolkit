# Roadmap design method

## Capability unit

Represent each capability as a small contract:

```text
Capability
Why it matters for the target work
Prerequisites
System model to explain
Representative task
Evidence of independent use
Transfer or debugging check
Likely failure modes
Feedback source
```

A topic name alone is not a capability. "React rendering" becomes useful when
the learner can predict why a component rerenders, verify the prediction with
tools, correct an unnecessary rerender, and explain the tradeoff of the fix.

## Priority model

Classify capabilities as:

- foundation: blocks several later capabilities;
- target-critical: directly required by the target work;
- multiplier: improves debugging, feedback, automation, or transfer;
- supporting: useful after the core path works;
- later: outside the current capacity or target.

Prioritize by dependency and target relevance. Use feedback speed as a
tie-breaker so the learner can test understanding early.

## Progression

Use a confidence-first ladder when there is no stronger learner-specific model:

1. retrieve prerequisite concepts;
2. trace and explain a worked system example;
3. complete a close task with scaffolding;
4. solve a standard task independently;
5. debug a broken or ambiguous case;
6. transfer the principle to a new context;
7. justify tradeoffs or review another solution.

Advance on performance evidence. Step down when the learner cannot explain the
model, choose a first diagnostic action, or make progress after bounded hints.

## Role and specialty transitions

For a transition, divide the map into four tracks:

1. transferable strengths from the current role;
2. target-domain foundations;
3. target work and tools;
4. evidence visible to a reviewer, mentor, interviewer, or team.

Prefer bridge projects that join existing strengths with one new layer. A
frontend developer moving toward data engineering might first build and observe
a small ingestion pipeline for product events instead of starting with an
unrelated large platform.

## Detail without overload

Each week should contain a coherent outcome rather than a bag of topics. Limit
new concepts to what the practice task can exercise. Move optional breadth into
a backlog.

The detailed plan should answer:

- what problem the learner is solving;
- what model explains the system;
- what implementation or API they will use;
- what they will build, debug, or explain;
- how another person or test can verify the result;
- what evidence permits progression.
