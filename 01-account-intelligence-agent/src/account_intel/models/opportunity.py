from typing import Literal

from pydantic import BaseModel, Field

from .evidence import Fact, Inference


class BusinessProblem(BaseModel):
    """
    A potential business or operational problem identified
    from company and market intelligence.
    """

    title: str
    description: str

    problem_type: Literal[
        "GROWTH",
        "SALES",
        "MARKETING",
        "OPERATIONS",
        "CUSTOMER_EXPERIENCE",
        "FINANCE",
        "COMPLIANCE",
        "DATA",
        "TECHNOLOGY",
        "PRODUCT",
        "PEOPLE",
        "OTHER",
    ] = "OTHER"

    severity: Literal[
        "LOW",
        "MEDIUM",
        "HIGH",
    ] = "MEDIUM"

    supporting_facts: list[Fact] = Field(default_factory=list)

    hypothesis: Inference | None = None


class AIOpportunity(BaseModel):
    """
    A possible AI, automation, analytics, or agentic opportunity.
    """

    title: str

    description: str

    opportunity_type: Literal[
        "AUTOMATION",
        "AI_AGENT",
        "COPILOT",
        "ANALYTICS",
        "COMPUTER_VISION",
        "DOCUMENT_AI",
        "VOICE_AI",
        "FORECASTING",
        "RAG",
        "WORKFLOW_REDESIGN",
        "OTHER",
    ] = "OTHER"

    business_problem: BusinessProblem

    expected_value: str | None = None

    implementation_complexity: Literal[
        "LOW",
        "MEDIUM",
        "HIGH",
    ] = "MEDIUM"

    confidence: float = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
    )

    why_now: str | None = None


class POCRecommendation(BaseModel):
    """
    A small proof of concept that could validate an opportunity
    before committing to a larger implementation.
    """

    name: str

    objective: str

    proposed_workflow: list[str] = Field(default_factory=list)

    required_inputs: list[str] = Field(default_factory=list)

    expected_outputs: list[str] = Field(default_factory=list)

    success_metrics: list[str] = Field(default_factory=list)

    estimated_build_complexity: Literal[
        "LOW",
        "MEDIUM",
        "HIGH",
    ] = "MEDIUM"


class OpportunityAnalysis(BaseModel):
    """
    The final opportunity layer for an account.
    """

    business_problems: list[BusinessProblem] = Field(
        default_factory=list
    )

    ai_opportunities: list[AIOpportunity] = Field(
        default_factory=list
    )

    recommended_pocs: list[POCRecommendation] = Field(
        default_factory=list
    )
