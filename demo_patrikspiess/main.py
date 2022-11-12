"""This is the main module

It just starts the demo
"""

import sys
from . import Demo


def main() -> None:
    """The main script"""
    Demo(sys.argv)


if __name__ == "__main__":
    main()
