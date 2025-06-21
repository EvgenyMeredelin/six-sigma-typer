from typing import Annotated

import requests
import rich
import typer


app = typer.Typer()
url = "https://six-sigma.containerapps.ru/data"


def prevent_fails_greater_than_tests(
    fails: int, context: typer.Context
) -> int:
    if fails > context.params["tests"]:
        raise typer.BadParameter(
            "Number of fails can't be greater than "
            "the total number of tests"
        )
    return fails


@app.command()
def main(
    tests: Annotated[
        int,
        typer.Option(
            "--tests", "-t",
            help="Total number of tests",
            min=1,
            show_default=False,
            show_envvar=False,
            rich_help_panel="Process parameters"
        )
    ],
    fails: Annotated[
        int,
        typer.Option(
            "--fails", "-f",
            help="Number of tests qualified as failed",
            min=0,
            callback=prevent_fails_greater_than_tests,
            show_default=False,
            show_envvar=False,
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
    """
    Evaluate a single process with the \"6 Sigma\" approach.
    Calls https://six-sigma.containerapps.ru/ under the hood.
    """
    params = {"tests": tests, "fails": fails, "name": name}
    rich.print(requests.get(url, params=params).json()[0])
