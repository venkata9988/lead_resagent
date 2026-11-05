"""
Lead Signal Schemas (Pydantic models)
Platform-agnostic data models ensuring any data source can be normalized
for the core research and copywriting agents.
"""
from typing import List, Optional, Dict, Any
from enum import Enum
from pydantic import BaseModel, Field

class PlatformSource(str, Enum):
    LINKEDIN = "linkedin"
    CRUNCHBASE = "crunchbase"
    JOB_BOARD = "job_board"
    COMPANY_WEBSITE = "company_website"
    TWITTER_X = "twitter_x"
    MANUAL_ENTRY = "manual_entry"

class SignalType(str, Enum):
    JOB_CHANGE = "job_change"
    HIRING_SURGE = "hiring_surge"
    FUNDING_ROUND = "funding_round"
    POST_ENGAGEMENT = "post_engagement"
    PRODUCT_LAUNCH = "product_launch"
    GENERAL_PROSPECTING = "general_prospecting"

class CompanyInfo(BaseModel):
    name: str
    domain: Optional[str] = None
    industry: Optional[str] = None
    size_range: Optional[str] = None
    tech_stack: List[str] = Field(default_factory=list)

class ContactInfo(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    title: str
    profile_url: Optional[str] = None
    email: Optional[str] = None

class NormalizedLeadSignal(BaseModel):
    """Universal payload passed into the agentic reasoning pipeline."""
    source_platform: PlatformSource
    signal_type: SignalType
    company: CompanyInfo
    contact: ContactInfo
    raw_context: str
    source_url: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ResearchDossier(BaseModel):
    summary: str
    key_pain_points: List[str]
    growth_triggers: List[str]
    tech_stack: List[str]

class GeneratedOutreach(BaseModel):
    linkedin_connection_note: str
    cold_email_subject: str
    cold_email_body: str
    internal_sales_brief: str
    confidence_score: float
