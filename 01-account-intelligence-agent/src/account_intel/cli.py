import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from .config import settings
from .research.search import TavilySearchClient

app = typer.Typer(
    help="Evidence-backed account intelligence from public company research."
)

console = Console()


@app.command()
def analyze(
    company: str = typer.Option(
        ...,
        "--company",
        "-c",
        help="Company name to research.",
    ),
    person: str | None = typer.Option(
        None,
        "--person",
        "-p",
        help="Optional person or role to research.",
    ),
):
    """
    Analyze a company and generate an account intelligence brief.
    """

    target = company

    if person:
        target = f"{company} — {person}"

    console.print(
        Panel.fit(
            f"[bold]Account Intelligence Agent[/bold]\n\n"
            f"Target: {target}\n\n"
            f"Status: Full intelligence pipeline coming next.",
            title="Build #01",
        )
    )


@app.command()
def search(
    company: str = typer.Option(
        ...,
        "--company",
        "-c",
        help="Company name to research.",
    ),
    max_results: int = typer.Option(
        5,
        "--max-results",
        "-n",
        help="Maximum number of search results.",
    ),
):
    """
    Search the web for public company intelligence.
    """

    if not settings.tavily_api_key:
        console.print(
            "[red]Missing TAVILY_API_KEY.[/red]\n"
            "Add it to your local .env file."
        )
        raise typer.Exit(code=1)

    client = TavilySearchClient(
        api_key=settings.tavily_api_key
    )

    query = (
        f"{company} company products customers strategy "
        f"recent news hiring expansion"
    )

    console.print(
        f"\n[bold]Researching:[/bold] {company}\n"
    )

    results = client.search(
        query=query,
        max_results=max_results,
    )

    table = Table(
        title=f"Research Results — {company}"
    )

    table.add_column("#", style="dim")
    table.add_column("Title")
    table.add_column("Source")
    table.add_column("Score")

    for index, result in enumerate(results, start=1):
        score = (
            f"{result.score:.2f}"
            if result.score is not None
            else "-"
        )

        table.add_row(
            str(index),
            result.title,
            result.url,
            score,
        )

    console.print(table)


if __name__ == "__main__":
    app()
