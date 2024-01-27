"""A decorator demo

Here we define a decorator that logs the start and/or end of a function
"""

from typing import Any
from demo_patrikspiess.log_helper import log


def log_me(func: Any) -> Any:
    """This is a simple logging decorator

    You can pass any function with any arguments and any return value. Then this decorator just
    logs start and end of the function and returns it's return value.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        log.info("This is before the function '%s'", func.__name__)
        return_value = func(*args, **kwargs)
        log.info("This is after the function '%s'", func.__name__)

        return return_value

    return wrapper


@log_me
def decorate(name: str = "Nobody") -> str:
    """Just a function to demonstrate a decorator"""
    log.info("This is within the function")

    return f"Hello {name}"
