---
name: lead-enrichment
description: Gathers company background, business model, recent news, technologies, and hiring trends from domain websites and search results.
version: 1.0.0
---

# Lead Enrichment Skill

## Objective
Extract high-signal business intelligence from a target company URL and prospect profile without downloading excessive HTML bloat.

## Steps
1. **Domain Extraction**: Normalize the domain (strip `https://`, `www.`, path parameters).
2. **Landing Page Metadata Inspection**:
   - Extract page title, meta description, and primary value proposition from H1/H2 tags.
   - Identify core product/service offerings and target customer base (B2B vs B2C).
3. **Intent Signal Discovery**:
   - Search for recent press releases, funding rounds, or product launches in the last 6 months.
   - Inspect job postings for keywords indicating expansion or bottlenecks (e.g. hiring customer support reps, sales engineers, or revops).
4. **Output Synthesis**:
   - Return clean structured JSON conforming to the `research_dossier` schema in `AGENTS.md`.
