#!/usr/bin/python3
"""Module for MyInt class."""


class MyInt(int):
    def __equal__(self, x):
        """override and inverte equal."""
        return int(self) != int(x)

    def __notequal__(self, x):
        """override and inverte not equal."""
        return int(self) == int(x)
