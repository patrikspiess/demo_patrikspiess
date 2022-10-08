"""Define demo exceptions"""


import sys


class DemoException(Exception):
    """Just a demo exception"""

    def __init__(self, message: str = None):
        """initialize the demo exception"""
        self.message = message if message else ""
        super().__init__(self.message)
        print(self.message)
        sys.exit(1)
