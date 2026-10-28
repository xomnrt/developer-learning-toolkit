# Adaptive mock interview method

## Case design

Build each case around a decision or diagnosis. A strong case has several
reasonable paths and enough evidence to compare them.

Use this structure:

```text
Target capabilities
Work context
Desired outcome
Known constraints
Deliberately missing information
Initial question
Follow-up evidence or constraint change
Expected evidence of mastery
Critical errors
Hint ladder
```

Missing information should be discoverable through good clarifying questions.
Do not base the case on an undisclosed fact that the candidate cannot infer or
request.

## Difficulty controls

Change one dimension at a time:

1. direct case with explicit done conditions;
2. incomplete information that requires clarification;
3. competing constraints and tradeoffs;
4. a failure, inconsistency, or misleading symptom to diagnose;
5. a realistic change after the initial proposal;
6. transfer to a different context or larger scope.

Increase difficulty after evidence of a sound system model and verification
plan. Reduce it when the candidate cannot identify the next useful question or
test.

## Hint ladder

Offer hints in this order and let the candidate retry after each:

1. restate the desired outcome;
2. identify the category of missing information;
3. point to the system boundary or stakeholder involved;
4. provide one relevant observation;
5. offer two candidate approaches to compare;
6. show a partial solution;
7. explain the complete reasoning, then ask for independent reconstruction or a
   variation.

Record the hint level because a correct answer after a full solution is
different evidence from an independent answer.

## Review rubric

Use 0-3 on supported dimensions:

| Score | Meaning |
| --- | --- |
| 0 | No useful evidence yet, or the answer creates a critical failure. |
| 1 | Partial model with important gaps; substantial prompting required. |
| 2 | Workable answer with minor gaps or limited verification. |
| 3 | Independent, well-justified answer with verification and tradeoffs. |

Choose relevant dimensions from:

- clarification and requirements;
- system or domain model;
- correctness and completeness;
- tradeoff reasoning;
- risk and edge cases;
- implementation detail;
- verification and observability;
- communication and structure.

Scores are compact feedback, not psychometric measurements. Cite answer evidence
and mark confidence low when the case did not test a dimension directly.

## Roadmap evidence

For each tested capability record one state:

- demonstrated independently;
- demonstrated with a probe;
- demonstrated with a hint;
- weak or incorrect;
- not tested.

Completion checkmarks remain user-controlled. Recommend a revisit when the
candidate lacks the system model, cannot choose a first diagnostic action, or
cannot transfer the capability after bounded prompting.

## Session adaptation

After each case, select the next case from the strongest information need:

- test whether a weak answer was a local gap or a missing prerequisite;
- integrate two capabilities that were individually strong;
- test transfer after a rehearsed answer;
- revisit an error through a different scenario;
- stop when additional cases would add little evidence within the agreed time.
