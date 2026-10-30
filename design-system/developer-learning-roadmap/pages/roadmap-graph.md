# Roadmap graph page override

This is an interactive learning tool, not a marketing landing page. The chosen
composition is **editorial hero + workbench graph**: a calm typographic opening
followed by a practical workspace for repeated learning sessions.

## Locked decisions

- Use a calm editorial knowledge-atlas mood in the hero: light neutral canvas,
  near-black text, restrained borders, generous whitespace, and one muted pink
  accent.
- Make the graph area feel like a workbench: compact controls, visible filters,
  explicit statuses, a readable dependency canvas, and a persistent details
  panel.
- Use serif display hierarchy for the title and section headings; keep body
  copy in a readable system sans-serif so the standalone HTML has no font
  network dependency.
- Keep the graph as the primary visual object. Do not add marketing imagery,
  testimonials, decorative illustrations, or a CTA section.
- Use the pink accent for active/ready/focus states. Use green only for
  completed semantic feedback. Keep blocked states neutral.
- Keep the graph, list view, details panel, localStorage, reset, and
  keyboard-accessible controls. Visual changes must not alter their data
  contract.
- Motion stays subtle: short transitions for controls and cards, no parallax,
  no autoplay, and always respect `prefers-reduced-motion`.
- Preserve the existing CSP and no-network runtime boundary.

## Ownership boundaries

- `ui-ux-pro-max`: this visual direction and token choices.
- `better-layout`: graph/list/details grouping, responsive behavior, and
  translated-text resilience.
- `better-ui`: final surface, border, icon, and state polish only.
- `fluid-functionalism`: motion principles only; do not add a React registry to
  this dependency-free HTML artifact.
- `developer-learning-roadmap`: graph semantics and progress behavior.

## Stop conditions

Do not redesign the page again unless one of these changes:

1. a functional requirement changes;
2. a verified accessibility or responsive failure is found;
3. the user explicitly chooses a different visual direction.
