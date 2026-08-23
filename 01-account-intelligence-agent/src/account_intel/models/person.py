from pydantic import BaseModel, Field, HttpUrl

from .evidence import Fact, Inference


class PublicActivity(BaseModel):
    """
    A relevant piece of public activity from the target person.

    Examples:
    - interview
    - article
    - podcast
    - public post
    - conference appearance
    """

    activity_type: str
    title: str | None = None
    summary: str
    url: HttpUrl | None = None
    published_at: str | None = None


class PersonProfile(BaseModel):
    """
    Structured intelligence about the person or executive
    being researched.
    """

    name: str | None = None

    role: str | None = None

    company: str | None = None

    professional_summary: str | None = None

    previous_roles: list[str] = Field(default_factory=list)

    areas_of_responsibility: list[str] = Field(default_factory=list)

    public_activity: list[PublicActivity] = Field(default_factory=list)

    facts: list[Fact] = Field(default_factory=list)

    hypotheses: list[Inference] = Field(default_factory=list)
