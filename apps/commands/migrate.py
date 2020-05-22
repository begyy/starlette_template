from commands import base_command


@base_command.command()
def hello():
    print('hello')