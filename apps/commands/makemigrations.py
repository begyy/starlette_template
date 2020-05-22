from commands import base_command


@base_command.command()
def hello_world():
    print('hello')