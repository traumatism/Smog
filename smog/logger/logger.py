""" Logger module for Smog. """
from rich.console import Console

console = Console()


class Logger:
    """ Logger class for Smog """

    @classmethod
    def __log(cls, message: str, prefix: str):
        """ Log a message to the console """
        console.print(f"[bold white][{prefix}][/bold white] {message}")

    @classmethod
    def info(cls, message: str):
        """ Log an info message """
        cls.__log(message, "[bold cyan]*[/bold cyan]")

    @classmethod
    def warn(cls, message: str):
        """ Log a warning message """
        cls.__log(message, "[bold yellow]^[/bold yellow]")

    @classmethod
    def error(cls, message: str):
        """ Log an error message """
        cls.__log(message, "[bold red]-[/bold red]")

    @classmethod
    def success(cls, message: str):
        """ Log a success message """
        cls.__log(message, "[bold green]+[/bold green]")
