from dataclasses import dataclass

import httpx


@dataclass
class SearchResult:
    title: str
    url: str
    content: str | None = None
    score: float | None = None


class TavilySearchClient:
    """
    Minimal Tavily search wrapper.

    Tavily is used only as a research source.
    Later stages are responsible for extracting facts,
    validating evidence, and producing inferences.
    """

    BASE_URL = "https://api.tavily.com/search"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def search(
        self,
        query: str,
        max_results: int = 5,
    ) -> list[SearchResult]:
        payload = {
            "api_key": self.api_key,
            "query": query,
            "search_depth": "advanced",
            "max_results": max_results,
            "include_answer": False,
            "include_raw_content": False,
        }

        response = httpx.post(
            self.BASE_URL,
            json=payload,
            timeout=30.0,
        )

        response.raise_for_status()

        data = response.json()

        results: list[SearchResult] = []

        for item in data.get("results", []):
            results.append(
                SearchResult(
                    title=item.get("title", ""),
                    url=item.get("url", ""),
                    content=item.get("content"),
                    score=item.get("score"),
                )
            )

        return results
