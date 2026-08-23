import typer
from rich.console import Console
from rich.panel import Panel

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
            f"Status: CLI is working. Research pipeline coming next.",
            title="Build #01",
        )
    )


if __name__ == "__main__":
    app()
