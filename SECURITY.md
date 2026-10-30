# Security and privacy

Developer Learning Toolkit is currently a skills plugin for Codex and Claude
Code. It contains Markdown instructions, references, host-specific manifest
metadata, and one offline Python renderer for interactive roadmap HTML. It does
not include an MCP server, hooks, external accounts, analytics, or a remote
storage service.

That small surface is intentional. Add a new capability only when the learning
workflow genuinely requires it and after a separate security review.

## Current data flow

The plugin asks users to describe work, learning behavior, motivation,
constraints, errors, and previous learning experiences. Those answers are
processed in the current conversation by the host product.

The plugin itself does not add a remote destination. The host product's own
privacy, retention, and workspace policies still apply.

Generated roadmap pages may store completed node IDs in the browser's
`localStorage`. The key is scoped to the roadmap ID. This data stays in the
selected browser profile unless the user moves or shares the browser profile or
page data.

The renderer reads one local JSON file and writes one requested HTML file. It
uses the Python standard library, performs no network requests, rejects graph
cycles and unsupported resource URLs, escapes embedded JSON, and emits a
restrictive Content Security Policy. The generated page has no CDN, analytics,
or third-party JavaScript.

Users should not provide:

- passwords, API keys, tokens, authentication codes, or credentials;
- proprietary source code or confidential internal documentation;
- customer records, payment information, government identifiers, or protected
  health information;
- names or details that identify coworkers, customers, or employers when an
  anonymized description is enough.

The skills should request only information needed for the current assessment
and should invite anonymized descriptions.

## Threat model

### Prompt injection in pasted content

A user may paste a context card, document, code comment, or other content that
contains instructions aimed at the model. All skills treat pasted and quoted
content as evidence, not as authority that can override the user's request,
the skill workflow, or platform safeguards.

### Prompt injection in external learning sources

The roadmap skill may consult roadmap.sh, official documentation, source code,
or other public material. Text retrieved from those sources is untrusted data.
It may inform coverage or technical facts, but it cannot authorize tool calls,
change permissions, request secrets, or override the user's goal. Prefer
read-only access, keep the set of sources narrow, and cite the pages used.

External links may change after publication. A generated roadmap should record
the access date and should not execute downloaded code, install packages, or
send user data merely because a source instructs it to do so.

### Sensitive inference and overclaiming

The toolkit may discuss motivation, failure, competence, and uncertainty. It
must not turn these answers into a medical or psychological diagnosis, an
employment assessment, or a claim that a self-report interview proves a cause.
Weak conclusions must be marked as tentative.

### Accidental disclosure

Learning examples can reveal company systems or personal history. The skills
should ask for the smallest useful detail and prefer generalized task
descriptions. Users should review text before posting it in public issues or
evaluation datasets.

Roadmap progress can reveal career plans and perceived skill gaps.
Mock-interview summaries can reveal performance evidence. Treat those outputs as
personal data and review them before sharing.

### Supply-chain changes

An installed release can become riskier if a later version adds scripts, hooks,
MCP servers, or external links. Review manifest and permission changes before
upgrading. Public releases should use versioned source and reproducible ZIP
contents; security-sensitive changes should be called out in release notes.

## Rules for future capabilities

If a future version adds an MCP server, hook, another script, analytics, or
remote persistent storage, it must document and test:

1. Why the capability is necessary and why instructions alone are insufficient.
2. The minimum filesystem, network, account, and OAuth scopes required.
3. Input validation at the actual execution boundary, not only in prompts.
4. Human confirmation for destructive, irreversible, or externally visible
   actions.
5. Data categories, purpose, recipients, retention, deletion, and logging.
6. Secret redaction and a ban on raw credentials in manifests, logs, prompts,
   examples, and test fixtures.
7. Authorization checks for every user and resource, including cross-tenant
   isolation when relevant.
8. Prompt-injection tests using untrusted documents and tool output.
9. Dependency pinning, vulnerability review, and an update policy.
10. A new privacy-policy and threat-model review before public release.

Every future tool must also have an explicit contract that records:

- the single capability it exposes, when to use it, and when not to use it;
- typed input and output schemas with validation at the execution boundary;
- side effects, permissions, timeout, retry policy, and idempotency behavior;
- structured errors with `retryable` and `remediation` fields;
- a risk class and the approval required before the call;
- provenance that links each result and side effect to a specific tool call.

Enforce permissions, approvals, and separation of untrusted content outside the
prompt. Skill text can explain a policy, but it is not a security boundary.

If a future release adds an autonomous agent loop, define bounded terminal
states, `max_steps`, deadlines, budgets, cancellation, rollback, and independent
verification before treating it as production-ready. Logs must reconstruct the
decision, tool call, result, and state transition without recording secrets or
unnecessary personal data.

Do not silently convert this offline plugin into a networked or autonomous
plugin under the same trust assumptions.

## Reporting a vulnerability

Use the repository's private security-advisory channel when it becomes
available. If no private advisory channel is configured, contact the maintainer
privately before opening a public issue.

Do not include real credentials, proprietary data, or another person's private
learning answers in a report. A minimal synthetic reproduction is preferred.
