from commands import base_command
from main import get_app
import uvicorn


@base_command.command()
def runserver():
    uvicorn.run(get_app())
