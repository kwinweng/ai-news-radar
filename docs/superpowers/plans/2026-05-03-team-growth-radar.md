# Team AI Growth Radar Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add product-operations and growth-operations category filtering to the AI news board.

**Architecture:** Keep the current static-site architecture. Enrich news records in `scripts/update_news.py` with deterministic business category fields, then render category filters in `index.html` and `assets/app.js`. Style the controls in `assets/styles.css` and document RSS/team setup in `README.md`.

**Tech Stack:** Python 3.11 data pipeline, vanilla HTML/CSS/JavaScript, GitHub Actions, GitHub Pages.

---

### Task 1: Business Category Classifier

**Files:**
- Modify: `scripts/update_news.py`
- Test: `tests/test_business_categories.py`

- [ ] Add category constants and keyword rules near the existing topic filter constants.
- [ ] Implement `classify_business_category(record)` returning `business_category`, `business_category_label`, and `business_category_reason`.
- [ ] Apply the classifier to AI and all-mode items before deduplication payloads are written.
- [ ] Add tests for models/platforms, product trends, growth/commercial, industry insight, tooling/ops, case playbooks, and fallback.
- [ ] Run `python3 -m pytest tests/test_business_categories.py -v`.

### Task 2: Category UI

**Files:**
- Modify: `index.html`
- Modify: `assets/app.js`
- Modify: `assets/styles.css`

- [ ] Add a category select and quick category pills to the primary controls.
- [ ] Track `categoryFilter` in UI state.
- [ ] Include category fields in search haystack and filtering logic.
- [ ] Render the category label on each news card.
- [ ] Update page title, hero copy, stat labels, and list title for the team radar positioning.
- [ ] Verify category filtering works in AI mode and all mode.

### Task 3: Documentation

**Files:**
- Modify: `README.md`

- [ ] Update the project title and intro for the Alibaba product/growth operations team use case.
- [ ] Document the six categories.
- [ ] Keep the existing OPML/RSS instructions and make clear that `FOLLOW_OPML_B64` remains the recommended team RSS path.

### Task 4: Verification

**Files:**
- No direct edits.

- [ ] Run `python3 -m pytest -q`.
- [ ] Run `python3 -m http.server 8080` and open the page locally.
- [ ] Check that the hero, category controls, item cards, WaytoAGI section, and advanced source status do not overlap on desktop and mobile widths.
- [ ] Run `git diff --check`.
