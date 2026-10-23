# UX Laws Reference for Web & App Development

**Purpose**: Use this as a mandatory reference when planning, designing, building, or auditing websites and applications. Apply during planning. After every build, run a compliance audit against these laws and fix violations before considering the work complete.

---

## How Agents Must Use This

### Planning Phase
1. Read all laws below.
2. Map each law to the proposed features, layouts, flows, and components.
3. Explicitly note in the plan how each relevant law is satisfied.
4. Prefer designs that satisfy multiple laws at once.

### Build Phase
- Implement with the laws as constraints.
- Prefer progressive disclosure, clear hierarchy, and low cognitive load.

### Post-Build Audit Phase (Mandatory Loop)
After every build or significant change:

1. Review the live interface or code against **every** law below.
2. For each law, answer: Compliant / Partial / Violated + evidence.
3. List specific fixes for every Partial or Violated item.
4. Implement the fixes.
5. Re-audit until all laws are Compliant or justifiably Partial (with documented reason).
6. Only then mark the build complete.

---

## Core UX Laws

### 1. Fitts’s Law
**Statement**: The time required to move to a target is a function of the distance to the target and the size of the target. Larger and closer targets are faster and easier to hit.

**Implications**:
- Primary actions must be large and easy to reach.
- Important buttons should not be tiny or placed at the edges of reachability.
- On mobile, place primary CTAs in the thumb zone.
- Increase hit areas beyond visual size (padding).

**Examples**:
- Good: Large “Add to Cart” button, sticky bottom CTA on mobile, generous padding around icon buttons.
- Bad: Tiny 12px close icon in the corner, primary button only in the footer of a long page, small text links for critical actions.

**Checklist**:
- [ ] Primary actions are large enough (≥44×44px touch target).
- [ ] Critical buttons are positioned for easy reach (thumb zone on mobile, near cursor path on desktop).
- [ ] Interactive elements have adequate spacing to avoid mis-taps.

---

### 2. Hick’s Law
**Statement**: The time it takes to make a decision increases with the number and complexity of choices.

**Implications**:
- Reduce options at each decision point.
- Use progressive disclosure.
- Group related options.
- Default to the most common path.

**Examples**:
- Good: Checkout with 1–3 clear steps, limited navigation items, filtered search results, smart defaults.
- Bad: Homepage with 20+ equally weighted CTAs, mega menu with 50 links, form with 15 required fields at once.

**Checklist**:
- [ ] Decision points present ≤5–7 clear options.
- [ ] Complex choices are broken into steps or filtered.
- [ ] Primary path is visually and functionally obvious.

---

### 3. Jakob’s Law
**Statement**: Users spend most of their time on other sites. They prefer your site to work the same way as all the other sites they already know.

**Implications**:
- Follow established conventions for navigation, forms, icons, and patterns.
- Do not invent new interaction models without strong justification.
- Place logo top-left, search in header, cart top-right, etc.

**Examples**:
- Good: Standard hamburger menu on mobile, familiar form field styles, breadcrumb navigation, standard button shapes.
- Bad: Custom navigation that requires learning, non-standard form controls, unique gesture language without onboarding.

**Checklist**:
- [ ] Navigation, forms, buttons, and icons follow platform and web conventions.
- [ ] Users can complete core tasks without learning a new interface language.
- [ ] Any novel pattern has clear onboarding or is secondary.

---

### 4. Miller’s Law
**Statement**: The average person can only keep 7 (±2) items in their working memory.

**Implications**:
- Chunk information.
- Limit navigation items.
- Break long forms and content into groups.
- Use progressive disclosure and summarization.

**Examples**:
- Good: Phone number formatted as (123) 456-7890, navigation with 5–7 items, form sections, product features in groups of 3–5.
- Bad: Unformatted 10-digit number, 15 top-level nav items, single long form with 20 fields, dense unchunked text.

**Checklist**:
- [ ] Information is chunked into groups of 3–7.
- [ ] Navigation and menus stay within working memory limits.
- [ ] Long processes are broken into steps with clear progress.

---

### 5. Tesler’s Law (Law of Conservation of Complexity)
**Statement**: Every application has an inherent amount of complexity that cannot be removed. It can only be moved between the system and the user.

**Implications**:
- Shift complexity to the system (smart defaults, automation, good information architecture).
- Never force users to handle complexity that the product can absorb.
- Balance power-user features with simplicity for the majority.

**Examples**:
- Good: Auto-formatting phone numbers, smart address autocomplete, calculated shipping, “Recommended” defaults.
- Bad: Forcing users to calculate tax, manually format data, or understand internal system constraints.

**Checklist**:
- [ ] The system handles as much complexity as possible.
- [ ] Users are not asked to perform calculations or remember system rules.
- [ ] Advanced options are available but not required for the main path.

---

### 6. Aesthetic-Usability Effect
**Statement**: Users often perceive aesthetically pleasing designs as more usable.

**Implications**:
- Visual polish increases perceived quality and trust.
- Poor aesthetics can make a functionally correct interface feel broken.
- Consistency in spacing, type, color, and alignment matters.

**Examples**:
- Good: Clean typography, consistent spacing system, balanced whitespace, coherent color palette.
- Bad: Inconsistent fonts, cramped layouts, clashing colors, misaligned elements — even if functional.

**Checklist**:
- [ ] Visual hierarchy is clear.
- [ ] Spacing, alignment, and typography are consistent.
- [ ] The interface looks intentional and polished.

---

### 7. Doherty Threshold
**Statement**: Productivity soars when a computer and its users interact at a pace (<400 ms) that ensures neither has to wait on the other.

**Implications**:
- Interactions must feel instant.
- Provide immediate feedback for every action.
- Optimize loading, use optimistic UI, and show progress for longer operations.

**Examples**:
- Good: Instant button state change, skeleton loaders, optimistic updates, <400 ms responses for common actions.
- Bad: Full page reload on filter, no feedback on button click, long uncommunicated waits.

**Checklist**:
- [ ] Common interactions respond in <400 ms or show immediate feedback.
- [ ] Loading states and progress indicators are present for slower operations.
- [ ] No silent waits.

---

### 8. Peak-End Rule
**Statement**: People judge an experience largely based on how they felt at its peak (most intense point) and at its end, rather than the total sum or average.

**Implications**:
- Make the most important moments and the ending excellent.
- A smooth ending can salvage a mixed experience.
- Avoid negative peaks and abrupt or confusing endings.

**Examples**:
- Good: Delightful confirmation screen, clear success state, helpful empty states, graceful error recovery.
- Bad: Abrupt “Done” with no confirmation, frustrating error at the final step, cold or missing end state.

**Checklist**:
- [ ] Key moments (especially success and error) are well designed.
- [ ] Task endings are clear, positive, and informative.
- [ ] Negative peaks are minimized or recovered from gracefully.

---

### 9. Serial Position Effect
**Statement**: Users tend to remember the first and last items in a series best (primacy and recency effects).

**Implications**:
- Place the most important information or actions at the beginning and end of lists, menus, and pages.
- Avoid burying critical items in the middle.

**Examples**:
- Good: Primary CTA at top and sticky at bottom, most important nav items first and last, key product benefits first and last in a list.
- Bad: Critical action buried in the middle of a long menu or form.

**Checklist**:
- [ ] Most important items appear at the start and end of sequences.
- [ ] Middle positions are used for secondary content.

---

### 10. Von Restorff Effect (Isolation Effect)
**Statement**: When multiple similar objects are present, the one that differs from the rest is most likely to be remembered.

**Implications**:
- Make the primary action or key information visually distinct.
- Use contrast sparingly and intentionally.

**Examples**:
- Good: Primary button in brand color while secondary buttons are outlined, highlighted “Recommended” plan, one distinct callout.
- Bad: All buttons the same style, no visual hierarchy, everything equally emphasized.

**Checklist**:
- [ ] Primary action or key message is visually distinct.
- [ ] Contrast is used deliberately, not randomly.

---

### 11. Pareto Principle (80/20 Rule)
**Statement**: Roughly 80% of effects come from 20% of causes.

**Implications**:
- Focus design and engineering effort on the features and flows that deliver most of the value.
- Identify and perfect the core 20%.
- Deprioritize or hide the long tail until needed.

**Examples**:
- Good: Optimizing the main user journey and top 3 features first, progressive disclosure of advanced settings.
- Bad: Equal effort on every feature, bloated interface with rarely used options always visible.

**Checklist**:
- [ ] Core user paths are prioritized and polished.
- [ ] Secondary features are de-emphasized or hidden until needed.

---

### 12. Occam’s Razor
**Statement**: Among competing hypotheses (or designs), the one with the fewest assumptions should be selected. Prefer the simplest solution that works.

**Implications**:
- Remove unnecessary elements, steps, and features.
- If two designs solve the problem, choose the simpler one.
- Avoid cleverness that adds complexity.

**Examples**:
- Good: Single clear CTA, minimal form fields, straightforward navigation.
- Bad: Multiple ways to do the same thing without reason, decorative complexity, over-engineered interactions.

**Checklist**:
- [ ] Every element has a clear purpose.
- [ ] Unnecessary steps, fields, or options have been removed.
- [ ] The simplest viable solution was chosen.

---

### 13. Postel’s Law (Robustness Principle)
**Statement**: Be liberal in what you accept from others, and conservative in what you send.

**Implications**:
- Accept varied user input gracefully (flexible formats, forgiving validation).
- Output clear, consistent, predictable results.
- Handle edge cases without punishing the user.

**Examples**:
- Good: Accept phone numbers with or without dashes/spaces, flexible date formats, helpful error messages that guide correction.
- Bad: Rigid exact-format validation with no guidance, cryptic errors, system that breaks on slightly non-standard input.

**Checklist**:
- [ ] Input is accepted flexibly and validated helpfully.
- [ ] Error messages are clear and actionable.
- [ ] Output is consistent and predictable.

---

### 14. Zeigarnik Effect
**Statement**: People remember uncompleted or interrupted tasks better than completed ones.

**Implications**:
- Use progress indicators and incomplete states to encourage completion.
- Show what’s left to do.
- Avoid leaving users in ambiguous unfinished states without guidance.

**Examples**:
- Good: Progress bars, “3 steps left”, incomplete profile indicators, clear next-step prompts.
- Bad: No indication of progress, abandoned flows with no recovery path.

**Checklist**:
- [ ] Multi-step processes show clear progress and remaining work.
- [ ] Incomplete states are visible and actionable.
- [ ] Users know how to finish what they started.

---

## Audit Template (Copy for every review)

```
## UX Laws Audit — [Feature / Page / Build]

| Law                    | Status          | Evidence / Notes                          | Required Fix |
|------------------------|-----------------|-------------------------------------------|--------------|
| Fitts’s Law            | Compliant/Partial/Violated |                                           |              |
| Hick’s Law             |                 |                                           |              |
| Jakob’s Law            |                 |                                           |              |
| Miller’s Law           |                 |                                           |              |
| Tesler’s Law           |                 |                                           |              |
| Aesthetic-Usability    |                 |                                           |              |
| Doherty Threshold      |                 |                                           |              |
| Peak-End Rule          |                 |                                           |              |
| Serial Position Effect |                 |                                           |              |
| Von Restorff Effect    |                 |                                           |              |
| Pareto Principle       |                 |                                           |              |
| Occam’s Razor          |                 |                                           |              |
| Postel’s Law           |                 |                                           |              |
| Zeigarnik Effect       |                 |                                           |              |

### Summary
- Violations found: X
- Fixes applied: Y
- Re-audit required: Yes/No
```

---

## Agent Workflow Summary

1. **Plan** — Explicitly address relevant laws in the design plan.
2. **Build** — Implement while respecting the laws.
3. **Audit** — Fill the audit template against the actual interface.
4. **Fix** — Resolve every violation or partial.
5. **Re-audit** — Confirm compliance.
6. **Ship** — Only after the loop closes.

This document is the single source of truth for UX law compliance. Update it only when new validated laws or stronger patterns emerge.
