"""This is the calc module

Here we define some examples classes and methods
"""

from typing import List
from rich import print  # pylint: disable=redefined-builtin
from rich.panel import Panel
from .exceptions import DemoException


class Demo:
    """A demo class"""

    def __init__(self, params: List[str]) -> None:
        """initialize the thing"""
        if len(params) > 1:
            if params[1] == "1":
                print("something")
            if params[1] == "2":
                raise DemoException("This is a demo exception (not really an error)")
        else:
            self.help()

    def add_one(self, number: int) -> int:
        """method to add one to a number"""
        return number + 1

    def subtract_one(self, number: int) -> int:
        """method to add one to a number"""
        return number + 1

    def help(self) -> None:
        """
        Define the help screen and print it with rich
        """
        help_text = (
            "This is the help screen for demo_patrikspiess\n"
            "You already found that you may start the tool with 'demops'. But to invoke some more "
            "fancy actions you may add a parameter. Here we show you what parameters are valid:"
            "\n\n"
            "1 : print something\n"
            "2 : Raise an exception"
        )
        print(Panel(help_text, border_style="blue", title="Help", title_align="right"))
