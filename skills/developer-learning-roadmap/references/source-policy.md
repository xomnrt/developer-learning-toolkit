# Source policy

Use sources to establish coverage, dependencies, current technical facts, and
target-work expectations. Keep source authority proportional to the claim.

## Preferred sources

1. Official specifications, standards, and vendor documentation for current
   behavior, APIs, compatibility, and supported practices.
2. Maintained open-source source code, tests, release notes, and design records
   for implementation behavior.
3. Primary research, systematic reviews, and university course materials for
   learning or computer-science claims.
4. Published engineering material from established teams or recognized experts
   for practice patterns and tradeoffs. Present these as informed practice, not
   universal law.
5. Community roadmaps, including roadmap.sh, for discovery and coverage checks.

For programming languages and technologies, prefer the official language
reference, framework documentation, specification, release notes, and maintained
source repository. Use tutorial sites to improve explanation and practice, not
to override a current primary source.

## roadmap.sh use

roadmap.sh contains community-created role-based and skill-based roadmaps. Use a
relevant roadmap to discover candidate topics and dependency relationships.

Do not:

- claim that its full graph defines a job level;
- copy a roadmap or its explanations into the output;
- assume every node is required for this learner;
- use it as the only source for an API or current platform fact.

Record the exact roadmap URL and access date. Then verify selected technical
topics through their primary sources.

## Evidence notes

For each major source-dependent decision record:

```text
Claim or planning decision | source | checked date | confidence | caveat
```

Use short inline links in the user-facing roadmap and a compact source appendix.
Distinguish a sourced fact from a practical planning judgment.

For user-supplied GitHub curricula, interview banks, project collections, and
handbooks, consult
[community-source-catalog.md](community-source-catalog.md). Select only sources
relevant to the current target and recheck availability, recency, and license
before substantial reuse.
