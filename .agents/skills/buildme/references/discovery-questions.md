# Full-build Grill Me question bank

Ask 3–6 related questions per round. Reuse supplied answers and repository facts;
do not ask all 41 questions at once. Cover all 12 groups with an answer, agreed
default, explicit not-applicable reason or unresolved decision. Ask conditional
follow-ups only when relevant. Silence is not confirmation.

## 1. Product and platform (seed answers before research)

1. What are we building, for whom, and what problem does it solve?
2. Website, web app, PWA, native iOS/Android, desktop or cross-platform? Which ships first?
3. What are the top three user jobs, required screens and success measures?
4. New or existing build? Which repo, stack, deadline, constraints and exclusions apply?

Routes: Agent 0 scopes work; Agents 1–5 assess UI/platform needs. Native builds need
an explicit implementation owner, toolchain and native validation, beyond web checks.

## 2. Market and references

5. Who are the known competitors, alternatives and aspirational references?
6. What category, region, language and customer segment should research target?
7. Which sites/repos do you admire or dislike? May we discover alternatives, and what must differ?
8. What research budget applies? Which Agent-Reach, OpenComputer or BrowserAct tools
   are available? Keep public/keyless mode, or explicitly authorize a named provider
   exception to the no-key/no-account/no-credit policy? Never request secrets in chat.

Routes: Agent 15 discovers sources; Agent 11 deep-analyzes the shortlist.

## 3. Roles and journeys

9. What user roles exist, and what may each role access or change?
10. What is the main journey from first visit through completion and return?
11. Which onboarding, search, filters, detail, edit and account flows are required?
    What loading, empty, error, success and recovery states must exist?
12. Are approval, collaboration, invitations, notifications or real-time updates needed?

Routes: Agents 0, 1, 4, 8 and 9; specify flow and permission acceptance criteria.

## 4. Visual identity and content

13. What visual direction, colours, typography and layout fit the brand?
14. Which logos, copy, icons, images and proof points are supplied, licensed or missing?
15. Which languages, tone, localization, RTL, themes and CMS needs apply?
16. Is direction settled, or should Design Arena compare alternatives?

Routes: Agents 1, 2, 3, 9, 11 and 12; Design Arena when selected.

## 5. Backend, data and integrations

17. What entities, fields, relationships and validation rules are required?
18. Where does data live? Existing APIs/database, persistence, migration, backups,
    import/export and retention requirements?
19. Which authentication, recovery, permissions and admin tools are needed?
    What personal or sensitive data must be protected?
20. Which payments, subscriptions, maps, email, uploads, analytics or external
    integrations are required? What free/local substitute is acceptable if needed?

Routes: Agent 0 names API/data/auth implementation owners and interface contracts.
Agents 4 and 8 test flows/permissions; Agent 10 audits applicable quality constraints.
Frontend specialty roles do not imply a backend exists. Record capability gaps.

## 6. AI and automation

21. Does the product need an assistant, chatbot, tool-using agent or AI workflow?
22. What knowledge and tools may it use, and which actions require confirmation?
23. What quality, privacy, refusal, latency and local-model hardware requirements
    apply? Which acceptance prompts demonstrate success?

Routes: Agent 14 only for in-product AI. Agent 0 names the frontend integration
owner and freezes the UI/API contract; disclose local-model limitations.

## 7. Mobile, native and offline

24. Which phones, tablets, orientations, browsers and OS versions must work?
    Should primary tasks work one-handed and with the software keyboard open?
25. How should menus, tables, forms, dialogs and primary actions adapt on mobile?
26. Are installation, offline reads/writes, sync conflicts, push, camera, location,
    files, deep links or platform permissions required?
27. What signing, simulator/device, store-review and distribution constraints apply
    for native? What PWA/browser fallback behavior applies for web?

Routes: Agents 2, 4, 5, 8, 10 and 12. Name separate native/offline implementation
owners where needed; do not promise unavailable hardware or store checks.

## 8. Motion and interaction

28. Which transitions, gestures, scroll effects, 3D and motion intensity are useful?
29. What reduced-motion, low-power, slow-network and rendering fallbacks apply?
    What immediate feedback should each action provide?

Routes: Agent 5 owns motion; Agents 2, 4, 8 and 10 verify integration/fallbacks.

## 9. Accessibility, usability and performance

30. What accessibility standard, assistive technologies and target users apply?
31. Which devices/networks and load, interaction and asset budgets matter?
32. What are the biggest usability risks? How will core journeys satisfy all 14
    UX laws, including recovery and completion?

Routes: Agents 4, 7, 8 and 10; Agent 12 captures matched mobile/desktop evidence.

## 10. Discoverability and measurement

33. Is the product publicly indexable? Which metadata, structured data, sitemap,
    robots rules and llms.txt are appropriate, and what must remain private?
34. What conversion events matter and what privacy/consent constraints apply?
    Can they be checked with free/local tools?

Routes: Agents 6 and 9 for public content; Agents 0 and 8 prevent private-data
disclosure. Record why SEO/llms.txt is inapplicable for private/native-only products.

## 11. Testing, delivery and operations

35. Which critical journeys, permissions, integrations and edge cases must pass?
36. What automated tests, browser/device evidence and user acceptance are required?
37. What environments, preview hosting, deployment, rollback, logs and monitoring
    exist? Who can authorize publication and what delivery format is expected?
38. Who maintains the product, and what setup/runbook/handoff is needed?

Routes: Agents 0, 8 and 10; Agent 13 only after an authorized live URL exists.

## 12. Priorities and confirmation

39. What must ship now, what can wait and which tradeoffs should we make first?
40. Which decisions or capabilities remain unresolved under available tools/budget?
41. Does the proposed scope, journeys, stack, research, activation matrix and
    acceptance plan match what you want built?

Write BUILD_BRIEF.md using the bundled template and confirm it before implementation.
Assess every Agent 0–15; activate applicable responsibilities, not unnecessary work.
Mandatory quality gates remain required; deferred or blocked work is never passed.
