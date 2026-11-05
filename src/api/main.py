"""
FastAPI Production Application for Lead Researcher Agent.
Serves the web dashboard, webhook ingestion endpoints, and orchestrator pipelines.
"""
import os
from typing import Optional, Dict, Any
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from src.models.schema import NormalizedLeadSignal, PlatformSource, SignalType, CompanyInfo, ContactInfo
from src.tools.connectors.web_scraper import WebDomainConnector
from src.agents.orchestrator import LeadOrchestratorAgent

app = FastAPI(
    title="ProspectPulse Lead Intelligence API",
    version="1.2.0",
    description="Autonomous multi-channel B2B lead intelligence and outbound synthesis engine."
)

frontend_dir = os.path.join(os.path.dirname(__file__), "..", "frontend")
scraper = WebDomainConnector()
orchestrator = LeadOrchestratorAgent()

class DomainResearchRequest(BaseModel):
    domain: str
    contact_name: str
    contact_title: str
    industry: Optional[str] = "Technology"

@app.get("/")
async def root():
    """Serves the interactive ProspectPulse dashboard."""
    index_file = os.path.join(frontend_dir, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"message": "ProspectPulse API is running. Dashboard file not found."}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "prospect-pulse-agent",
        "version": "1.2.0",
        "environment": os.getenv("ENVIRONMENT", "development")
    }

@app.post("/api/v1/research/domain")
async def research_domain(req: DomainResearchRequest):
    """
    Scrapes target domain, detects tech stack, extracts intent signals,
    and returns a verified research dossier and multi-channel outreach draft.
    """
    name_parts = req.contact_name.strip().split(" ", 1)
    first_name = name_parts[0]
    last_name = name_parts[1] if len(name_parts) > 1 else ""

    signal = await scraper.fetch_signal(
        domain_or_url=req.domain,
        contact_first_name=first_name,
        contact_last_name=last_name,
        contact_title=req.contact_title,
        industry=req.industry
    )

    if not signal:
        raise HTTPException(status_code=400, detail="Could not reach or parse target domain.")

    result = await orchestrator.execute_research(signal)
    return {
        "lead_signal": signal,
        "research_result": result
    }
