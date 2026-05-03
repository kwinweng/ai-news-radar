# Team AI Growth Radar Design

## Goal

Build a team-facing daily AI news board for Alibaba product operations and growth operations teams. The first version should remain a fast daily information board, while adding business-oriented categories that help the team scan model releases, product trends, growth opportunities, tools, industry analysis, and reusable AI cases.

## Audience

The primary users are product operations and growth operations teammates. They need a shared daily page that answers what changed in AI, what products and tools are emerging, and which signals may matter for user growth, commercialization, and operational efficiency.

## Recommended Approach

Use the existing static site, JSON data pipeline, GitHub Actions update workflow, and GitHub Pages deployment model. Add a lightweight category classifier in the data pipeline and update the UI copy and filters around the team use case. Avoid adding model-generated summaries in the first version, because that would add API keys, cost, quality review, and compliance questions before the team has validated the daily board habit.

## Information Categories

- `models_platforms`: 模型与平台. Model releases, APIs, agent platforms, capability updates, infrastructure changes.
- `product_trends`: 产品趋势. AI product patterns, feature launches, pricing, interaction models, market positioning.
- `growth_commercial`: 增长与商业化. Acquisition, retention, conversion, PLG, community growth, content growth, monetization.
- `industry_insight`: 行业洞察. Funding, market structure, competitive dynamics, enterprise adoption, opportunity analysis.
- `tooling_ops`: 工具生态. AI tools useful for product, operations, growth, marketing, analytics, support, and automation.
- `case_playbooks`: 案例玩法. AI cases, campaigns, business applications, and reusable operating patterns worth reviewing.
- `other`: 其他信号. Relevant AI items that do not confidently match the business categories.

## UX

The page should be branded as a team AI growth radar rather than a generic AI signal board. The first viewport should keep update time, source health, and volume stats. The main controls should add a category filter next to search, and the list title should reflect the selected category. Source health remains under the advanced panel for maintainers.

The existing AI/full-mode switch should remain available so the team can switch between AI-filtered items and the broader update pool. Category filtering should work in both modes after all-mode data is loaded.

## Data Flow

`scripts/update_news.py` continues to collect and deduplicate items. Before writing `latest-24h.json` and `latest-24h-all.json`, it should enrich every item with:

- `business_category`: stable category id.
- `business_category_label`: Chinese display label.
- `business_category_reason`: short reason string useful for debugging.

The first version uses deterministic keyword rules over title, translated title, source, site name, and URL. This keeps the workflow free of API keys and makes GitHub Actions reliable.

## RSS

RSS remains supported through the existing OPML path. Local users can pass `--rss-opml feeds/follow.opml`. GitHub Actions can read `FOLLOW_OPML_B64`, decode it into `feeds/follow.opml`, and include those feeds in the update job. OPML-derived items should receive the same business categories as built-in sources.

## Testing

Add focused tests for the business classifier. Verify representative records for all six categories and one fallback record. Run the existing unit test suite after implementation. For the frontend, serve the static site locally and verify that category filtering works with the checked-in data files.
