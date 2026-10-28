# Frontend roadmap add-on draft

Status: preserved source material for a future frontend adapter. This file is
outside the generic skills and is not loaded unless the adapter is being built.

## Purpose

Provide frontend-specific capability maps, scenarios, and project ideas to
`developer-learning-roadmap` without turning the core toolkit into a frontend
curriculum.

The source material came from user-supplied examples. It records the requested
level of detail and candidate coverage. It is not a validated or current
curriculum. Before publication, check every technical topic against current
official documentation and compare the coverage with the current frontend,
JavaScript, TypeScript, and React roadmaps on roadmap.sh.

## Coverage map to preserve

### Web platform foundations

- Internet and client-server model: TCP/IP at an overview level, HTTP/HTTPS,
  DNS, hosting, domains, TLS, CORS, REST, WebSocket.
- HTTP requests: methods, status classes, Fetch, Axios when justified, error,
  loading, and empty states.
- Browser loading and rendering: resource loading, DOM, CSSOM, critical
  rendering path, JavaScript execution, reflow, repaint, and basic performance.
- Browser storage and APIs: cookies, localStorage, sessionStorage, IndexedDB,
  caching, service workers, and PWA concepts.
- DevTools: Elements, Network, Console, Performance, Lighthouse, Application,
  breakpoints, profiling, and evidence-driven debugging.
- Media formats and resource optimization: WebP, WebM, JPEG, PNG, and MP4.

### Interface foundations

- Semantic HTML, forms, labels, metadata, keyboard navigation, focus, roles,
  ARIA, and accessibility checks.
- CSS box model, display, positioning, Flexbox, Grid, responsive layout,
  mobile-first design, media queries, cascade, specificity, selectors, custom
  properties, SCSS, browser support, transitions, transforms, and keyframes.

### JavaScript and TypeScript

- Types, coercion, nullish values, functions, scope, hoisting, closures, `this`,
  immutability, arrays, objects, destructuring, spread/rest, iteration methods,
  recursion, modules, and DOM events.
- Event loop, promises, async/await, async error handling, request control, and
  race-condition debugging.
- TypeScript types and interfaces, function typing, unions, intersections,
  generics, mapped and utility types, discriminated unions, `any`, `unknown`,
  `never`, `readonly`, optional values, API boundaries, and common anti-patterns.

### React and application architecture

- Component model, JSX, props, state, events, conditional rendering, lifecycle,
  and causal understanding of rendering.
- Hooks, effects and cleanup, stale closures, refs, reducers, context, custom
  hooks, and local/global state choices.
- React Router, SPA/SSR/SSG, hydration, Next.js foundations, state managers,
  lazy loading, code splitting, memoization, Suspense, profiling, and list
  virtualization.
- Separation of UI, business logic, and API access; feature-oriented structure;
  ownership boundaries; decomposition; naming; and maintainable folder layout.

### Delivery and team practice

- Git fundamentals and collaboration: branches, commits, pull requests, review,
  diff, blame, merge, rebase, cherry-pick, conflict resolution, and recovery.
- Package managers, package metadata, Vite, Webpack when relevant, ESLint,
  Prettier, Stylelint, UI libraries, and basic CI/CD.
- Unit, component, hook, snapshot when justified, and end-to-end testing with
  current tools such as Vitest or Jest, Testing Library, Playwright, or Cypress.
- Responsible AI-assisted development with independent verification.

## Desired roadmap detail

Each period should contain:

| Field | Requirement |
| --- | --- |
| Outcome | Observable frontend work, not a list of material to watch |
| System model | Why the browser, language, framework, or tool behaves this way |
| Topics | Only concepts exercised during the period |
| Practice | Small tasks, debugging, and a transfer case |
| Artifact | A project increment, test suite, profiler trace, review, or explanation |
| Mastery | Evidence required before progression |

The user's sample six-month Junior to Middle progression used these candidate
phase themes:

1. deeper JavaScript and TypeScript plus React rendering foundations;
2. rerenders, local state, effects, and component practice;
3. global state, asynchronous flows, normalization, and optimistic updates;
4. project architecture, decomposition, delivery, and review;
5. performance measurement and optimization;
6. testing, technical communication, review, and consolidation.

The sample projects included a typed API SDK, a small component collection,
an asynchronous CRUD application, a dashboard, a large virtualized table, and
test/review work over earlier projects. Treat these as candidates. Select or
replace them according to the learner's current evidence and target work.

## Three-month example constraints to preserve

The user also supplied a detailed 12-week curriculum example with approximately
12-15 hours per week. Its useful design characteristics were:

- weekly system themes rather than isolated daily topics;
- direct DevTools practice alongside browser and network concepts;
- a small artifact every week and larger artifacts at phase boundaries;
- repeated retrieval after one day, one week, and one month;
- progression from web foundations through JavaScript and TypeScript into React,
  ecosystem, architecture, Git, infrastructure, and testing.

Do not preserve the exact timing automatically. A learner with existing
frontend experience should start from a baseline gap assessment. A new learner
may need a narrower target or a longer horizon. Algorithm exercises should be
included only when they serve the target work or interview requirements.

## Candidate scenario bank

- Predict and verify a React rerender.
- Trace a URL request through DNS, TLS, HTTP, browser parsing, and rendering.
- Diagnose a request with incorrect CORS behavior.
- Read an unfamiliar selector or middleware chain.
- Navigate and decompose a large production component.
- Find a stale closure, race condition, or missing effect cleanup.
- Profile an unnecessary render or a large list.
- Add an accessible modal with keyboard and focus behavior.
- Type an API boundary and handle loading, empty, error, cancellation, and retry.
- Review a change for architecture, tests, accessibility, and performance.

## Publication boundary

Before this becomes an installable adapter:

1. verify sources and current APIs;
2. add baseline tasks for beginner, current frontend developer, and level-growth
   cases;
3. define target-work evidence without claiming a universal junior or middle
   standard;
4. test whether the adapter improves roadmap relevance over the generic skill;
5. keep optional frameworks and tools out of the required core.
