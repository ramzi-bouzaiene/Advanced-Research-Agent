from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class CompanyAnalysis(BaseModel):
    pricing_model: str
    is_open_source: Optional[bool] = None
    tech_stack: List[str] = []
    description: str =""
    api_available: Optional[bool] = None
    language_support: List[str] = []
    integration_capabilities: List[str] = []

class CompanyInfo(BaseModel):
    name: str
    description: str
    website: str
    pricing_model: Optional[bool] = None
    is_open_source: Optional[bool] = None
    tech_stack: List[str] = []
    competitors: List[str] = []
    # Developer-specific fields
    api_available: Optional[bool] = None
    language_support: List[str] = []
    integration_capabilities: List[str] = []
    developer_experience_rating: Optional[str] = None

class ResearchState(BaseModel):
    query: str
    extracted_tools: List[str] = []
    companies : List[CompanyInfo]
    search_results: List[Dict[str, Any]] = []
    analysis: Optional[str] = None