# Production Architecture & Data Flow

## 1. Pipeline Lifecycle

```
[Inbound Request] 
       │
       ▼
[FastAPI Route: /api/v1/research]
       │
       ▼
[Supervisor Agent] ──▶ Coordinates steps & validates intermediate state
       │
       ├──▶ 1. [Company Recon Tool] ──▶ Scrapes domain & news signals
       ├──▶ 2. [People Analyst]     ──▶ Evaluates prospect role & pain points
       ├──▶ 3. [Copywriter Agent]   ──▶ Generates short, humanized pitch
       └──▶ 4. [Quality Gate]       ──▶ Verifies facts against source material
       │
       ▼
[Structured Response (JSON)] ──▶ Saved to Supabase DB & returned to client
```

## 2. Cost Control & Token Optimization
* **Scraper Sanitization**: Strip CSS, SVGs, and inline JavaScript before feeding text into the model to avoid wasting context tokens.
* **Tiered Model Routing**:
  * Fast extraction & parsing: `gemini-2.5-flash` or `gemini-3.8-flash`.
  * Deep pitch synthesis: `gemini-3.8-flash` with thinking budget or `gemini-pro`.
* **Zero-Cost Free Tier Strategy**:
  * Keep request payload under 8k tokens per lead.
  * Cache recurring company lookups in Redis/memory to prevent redundant scraping.
