"""This is the write module

It just write text to the console
"""

import sys
from . import Demo


def main() -> None:
    """The main script"""
    Demo(sys.argv)


if __name__ == "__main__":
    main()
