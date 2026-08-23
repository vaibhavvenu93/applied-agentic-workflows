import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Application settings loaded from environment variables.
    """

    tavily_api_key: str | None = os.getenv("TAVILY_API_KEY")
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")


settings = Settings()
