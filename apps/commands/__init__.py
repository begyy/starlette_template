import typer

base_command = typer.Typer()
from commands import runserver
from commands import makemigrations
from commands import migrate
