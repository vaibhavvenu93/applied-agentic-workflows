from pydantic import BaseModel, Field

from .company import CompanyProfile
from .person import PersonProfile
from .opportunity import OpportunityAnalysis
from .evidence import Fact, Inference


class ExecutiveBrief(BaseModel):
    """
    A concise summary for someone who needs to understand
    the account quickly before a conversation or decision.
    """

    account_summary: str

    why_this_account_matters: str | None = None

    key_signals: list[str] = Field(default_factory=list)

    key_risks: list[str] = Field(default_factory=list)

    conversation_angles: list[str] = Field(default_factory=list)

    discovery_questions: list[str] = Field(default_factory=list)


class AccountIntelligenceReport(BaseModel):
    """
    The final structured output produced by the
    Account Intelligence Agent.
    """

    company: CompanyProfile

    person: PersonProfile | None = None

    executive_brief: ExecutiveBrief

    opportunity_analysis: OpportunityAnalysis

    verified_facts: list[Fact] = Field(default_factory=list)

    hypotheses: list[Inference] = Field(default_factory=list)

    research_gaps: list[str] = Field(default_factory=list)

    confidence_score: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
    )
