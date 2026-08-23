from typing import Literal

from pydantic import BaseModel, Field, HttpUrl


class SourceEvidence(BaseModel):
    """
    A source supporting a factual claim.

    Account Intelligence Agent should preserve the source of every
    meaningful factual statement wherever possible.
    """

    url: HttpUrl

    title: str | None = None

    source_type: Literal[
        "COMPANY_WEBSITE",
        "NEWS",
        "JOB_POSTING",
        "EXECUTIVE_PROFILE",
        "INTERVIEW",
        "REGULATORY",
        "OTHER",
    ] = "OTHER"

    published_at: str | None = None

    raw_text: str | None = None

    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
    )


class Fact(BaseModel):
    """
    A factual statement discovered during research.

    Facts must be supported by evidence.
    """

    statement: str

    category: Literal[
        "COMPANY",
        "PRODUCT",
        "CUSTOMER",
        "MARKET",
        "HIRING",
        "LEADERSHIP",
        "STRATEGY",
        "FINANCIAL",
        "TECHNOLOGY",
        "OTHER",
    ] = "OTHER"

    evidence: list[SourceEvidence] = Field(default_factory=list)

    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
    )


class Inference(BaseModel):
    """
    A reasoned hypothesis derived from one or more facts.

    An inference is explicitly NOT a verified fact.
    """

    statement: str

    supporting_facts: list[Fact] = Field(default_factory=list)

    confidence: float = Field(
        ge=0.0,
        le=1.0,
    )

    reasoning_summary: str | None = None
