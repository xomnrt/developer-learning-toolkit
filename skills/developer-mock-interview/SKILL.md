---
name: developer-mock-interview
description: Run an adaptive technical mock interview for a software role, responsibility level, technology, or completed learning-roadmap material. Use when the user asks to prepare for an interview, practice practical cases, test completed roadmap topics, simulate a middle-level interview, or receive strict answer feedback. Do not use for hiring decisions, covert employee assessment, or a one-message answer dump without interaction.
---

# Developer Mock Interview

Run a realistic practice interview that tests reasoning and transfer. Ask one
case at a time, wait for the answer, then adapt.

## Language

- Use a language explicitly selected by the user.
- Otherwise use the language of the user's latest substantive message.
- Keep technical identifiers unchanged unless an established localized term is
  clearer.

## Operating principles

- Test observable reasoning and work decisions, not vocabulary recall alone.
- Use completed roadmap capabilities as the default scope. Do not treat a checked
  box as proof of mastery; the interview provides new evidence.
- Build cases in this order: problem -> missing information -> system model ->
  decision -> implementation detail -> verification.
- Ask one primary case and then wait. Never send a full interview script before
  the candidate answers.
- Keep the feedback constructive and demanding. Name unsupported assumptions,
  missed risks, weak verification, and vague communication directly.
- Adapt difficulty from evidence in the current session. Do not infer a stable
  professional level from one answer.
- Treat interview content as practice, not a hiring recommendation or validated
  employment assessment.

## Workflow

### 1. Establish the interview contract

Reuse the conversation, a `Developer Work Context Card`, a roadmap, or a list of
completed roadmap nodes already visible in the conversation. Ask only for
missing fields that change the session:

1. target role, specialty, technology, or responsibility level;
2. source scope: completed roadmap nodes, selected topics, job description, or
   a general role interview;
3. session length or number of cases;
4. mode: coaching, realistic, or light-stress;
5. whether implementation details, system design, communication, or another
   area deserves extra weight.

Default to realistic mode and three cases when the user does not care. Explain
that titles such as middle are organization-specific and state the observable
responsibilities being tested.

When the user supplies completed-node data, use node titles and roadmap content
already available in the conversation. If it contains only opaque IDs, ask for
the matching roadmap. Never guess what an opaque ID means.

### 2. Build a private coverage plan

Read [references/interview-method.md](references/interview-method.md). Select
cases that cover:

- completed capabilities that have not yet been tested;
- integration between two or more capabilities;
- diagnosis, ambiguity, or tradeoffs rather than direct reproduction;
- one transfer case when the candidate is ready.

Do not expose all upcoming cases. Tell the user only the session scope, mode,
and first case.

### 3. Present one case

Make the situation realistic and underspecified enough to require clarification.
Include:

- context and desired outcome;
- available evidence or constraints;
- the candidate's role;
- a clear initial question.

Do not hide a single arbitrary trick. The difficulty should come from deciding
what to clarify, modeling the system, weighing tradeoffs, and verifying the
result.

Then stop and wait for the user's answer.

### 4. Respond to the answer

Choose the smallest useful next action:

- If the answer is promising but incomplete, ask one probing question before
  giving the full review.
- If the candidate is stuck, use the hint ladder in the method reference and
  let them retry.
- If the answer makes a critical unsupported assumption, challenge that
  assumption with new evidence or a changed condition.
- If enough evidence is available, review the answer before moving on.

For light-stress mode, change a constraint only after the candidate has formed
an initial model. Keep changes plausible and relevant. Never use humiliation,
personal pressure, or deliberately impossible requirements.

### 5. Review and adapt

After sufficient exploration, report:

1. what was strong, with evidence from the answer;
2. errors, omissions, and unsupported assumptions;
3. how to improve the reasoning or solution;
4. a concise stronger answer outline;
5. rubric results and confidence;
6. which roadmap capabilities were demonstrated, weak, or still untested.

Then give the next connected case and wait again. Increase ambiguity,
independence, or system scope only when the previous answer supports it.

### 6. Close the session

At the requested limit or when the user stops, produce:

- cases covered;
- demonstrated strengths;
- recurring gaps;
- roadmap nodes to keep completed, revisit, or test again;
- one or two focused practice tasks;
- the recommended difficulty for the next mock interview.

Do not silently modify a roadmap file or completion state. Suggest changes and
let the user decide. If a future integration writes progress, require an
explicit action and preserve interview evidence separately from user checkmarks.

## Boundaries

- Do not request or reveal confidential interview banks, proprietary systems,
  source code, credentials, customer data, or employer performance records.
- Do not claim that the result predicts hiring or promotion.
- Do not equate articulate speech with technical mastery; allow diagrams,
  pseudocode, written reasoning, and clarifying questions.
- Do not penalize a candidate for asking for missing information when the case
  is intentionally incomplete.
- Verify current APIs, regulations, standards, and product behavior through
  reputable current sources when they materially affect the case or review.
