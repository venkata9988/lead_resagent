# Master Product & Architecture Blueprint: Lead Researcher Agent

**Authoritative Reference Document** for the Lead Intelligence & B2B Outbound Agent platform.

---

## 1. Executive Summary & Value Proposition
* **What it is**: An autonomous multi-platform B2B lead intelligence agent that detects buying triggers (job changes, hiring sprees, funding rounds) and writes hyper-personalized, non-AI-sounding outreach across LinkedIn, cold email, and CRM.
* **Target Buyer**: B2B sales teams, niche digital agencies, IT consultancies, and solopreneurs who need high-converting pipeline generation.
* **Pricing Model**:
  * Starter: $49/mo (up to 300 enriched leads).
  * Growth: $149/mo (up to 1,500 leads + multi-channel sequences).
  * Agency: $499/mo (white-labeled multi-client dashboard).

---

## 2. Infrastructure & Zero-Dollar Hosting Roadmap

| Layer | $0 Free Launch Tier | Production Cloud Scaling ($1,000+/mo revenue) |
| :--- | :--- | :--- |
| **Frontend** | Vercel / Cloudflare Pages | CloudFront + S3 |
| **Backend** | Render / Fly.io Free Containers | AWS App Runner / ECS Fargate |
| **Database & Auth** | Supabase (Free PostgreSQL + Auth for 50k users) | AWS RDS PostgreSQL (db.t4g.micro) |
| **Task Queue** | Upstash Redis (10,000 requests/day free) | AWS SQS / ElastiCache Redis |
| **LLM Inference** | Gemini Flash API (Free Tier & pay-as-you-go) | Vertex AI / Gemini 3.8 Flash |

---

## 3. Defense-in-Depth Security & Storage Architecture
1. **DDoS Protection**: Cloudflare WAF handles IP rate-limiting and bot traffic.
2. **Prompt Injection Sanitization**: Strips scripts, style tags, and wraps all scraped context inside strict XML delimiters (`<untrusted_lead_context>`).
3. **Multi-Tenant Isolation**: PostgreSQL Row Level Security (RLS) cryptographically prevents cross-tenant data leakage.
4. **Anti-Storage Bloat**: "Extract and Discard" pattern—extracts 4 KB JSON signals from 2 MB web pages and purges raw HTML immediately; 7-day S3 auto-expiration for temporary files.

---

## 4. Multi-Domain Adaptation (Healthcare, Retail, Banking, Middleware)
* The agent automatically detects the company's industry sector and injects domain-specific playbooks:
  * **Healthcare**: Patient intake hold times, HIPAA, front-desk staffing burnout.
  * **Retail / E-commerce**: Cart abandonment, SKU catalog expansion, 3PL fulfillment.
  * **Banking / FinTech**: KYC/AML friction, compliance audit trails, false-positive alerts.
  * **Middleware & IT**: Kafka/MQ consumer lag, microservice decoupling, legacy migration latency.

---

## 5. Pre-Flight Quality & Anti-Hallucination Testing
* Automated regression test suite runs on every build (`tests/test_validation.py`):
  * **LinkedIn character limit**: Strictly $\le$ 250 characters.
  * **Email length**: Strictly $\le$ 85 words.
  * **Grounding Gate**: All company stats and funding amounts must verifiably exist in the raw scrape.
  * **Startup Hook**: `scripts/start.ps1` and `scripts/start.sh` enforce zero-defect startup.
