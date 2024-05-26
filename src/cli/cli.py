import typer
from rich import print

from cli.config import settings

app = typer.Typer(
    name="cli", help="Description"
)


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


@app.command()
def version():
    print(f"Cli [green]v{settings.VERSION}[/green]")
