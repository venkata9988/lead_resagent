# 01 Lead Researcher & Outbound Intelligence Agent

A production-ready autonomous multi-agent pipeline that takes raw target leads, performs deep automated research, and generates personalized, non-generic sales pitches.

## Directory Structure

```
01_lead_researcher_agent/
├── AGENTS.md                  # Multi-agent roles, schemas, contracts & state flow
├── README.md                  # Setup, run guide & zero-cost deployment instructions
├── config/                    # Configuration, prompt templates, and API keys
│   └── settings.example.json
├── docs/                      # Architectural specs & hosting guide
│   └── ARCHITECTURE.md
├── skills/                    # Modular skills library
│   ├── lead-enrichment/       # Web scraping & intent extraction rules
│   │   └── SKILL.md
│   └── pitch-crafting/        # Humanized outreach generation rules
│       └── SKILL.md
└── src/                       # Core application source
    ├── agents/                # Agent definitions (Supervisor, Scout, Copywriter)
    ├── api/                   # FastAPI REST endpoints
    └── tools/                 # Scraper, search & verification tools
```

## Zero-Cost Stack Compatibility
* **Frontend**: Next.js deployed on Vercel (\$0/mo).
* **Backend**: FastAPI / Python deployed on Render or Fly.io free tier (\$0/mo).
* **Database & Auth**: Supabase PostgreSQL free tier (\$0/mo).
* **LLM**: Gemini Flash (Free tier / pay-as-you-go).
