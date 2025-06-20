from typing import Annotated

import black
import requests
import typer


app = typer.Typer()
url = "https://six-sigma.containerapps.ru/data"


@app.command()
def main(
    tests: Annotated[
        int,
        typer.Option(
            "--tests", "-t",
            help="Total number of tests",
            min=1,
            show_default=False,
            rich_help_panel="Process parameters"
        )
    ],
    fails: Annotated[
        int,
        typer.Option(
            "--fails", "-f",
            help="Number of tests qualified as failed",
            min=1,
            show_default=False,
            rich_help_panel="Process parameters"
        )
    ],
    name: Annotated[
        str | None,
        typer.Option(
            "--name", "-n",
            help="Name of the process",
            rich_help_panel="Process parameters"
        )
    ] = None
) -> None:
    """Evaluate a single process with the \"6 Sigma\" approach. """
    params = {"tests": tests, "fails": fails, "name": name}
    process = requests.get(url, params=params).json()[0]
    print(black.format_str(repr(process), mode=black.Mode()))
