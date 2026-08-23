from typing import Literal

from pydantic import BaseModel, Field, HttpUrl

from .evidence import Fact, Inference


class Product(BaseModel):
    """
    A product or service offered by the company.
    """

    name: str
    description: str | None = None
    url: HttpUrl | None = None


class StrategicSignal(BaseModel):
    """
    A recent development that may indicate a change in
    company strategy, priorities, investment, or operations.
    """

    signal_type: Literal[
        "HIRING",
        "FUNDING",
        "PRODUCT_LAUNCH",
        "PARTNERSHIP",
        "EXPANSION",
        "LEADERSHIP_CHANGE",
        "ACQUISITION",
        "TECHNOLOGY",
        "REGULATORY",
        "OTHER",
    ]

    description: str

    importance: Literal[
        "LOW",
        "MEDIUM",
        "HIGH",
    ] = "MEDIUM"

    supporting_facts: list[Fact] = Field(default_factory=list)


class CompanyProfile(BaseModel):
    """
    Structured intelligence about a researched company.

    This model represents what the system currently knows
    about an account.
    """

    company_name: str

    website: HttpUrl | None = None

    description: str | None = None

    industry: str | None = None

    headquarters: str | None = None

    business_model: str | None = None

    customer_segments: list[str] = Field(default_factory=list)

    products: list[Product] = Field(default_factory=list)

    technologies: list[str] = Field(default_factory=list)

    strategic_signals: list[StrategicSignal] = Field(
        default_factory=list
    )

    facts: list[Fact] = Field(default_factory=list)

    hypotheses: list[Inference] = Field(default_factory=list)
