#!/usr/bin/python3
"""Defines: class MyList"""


class MyList(list):
    """
    Represents MyList class

    Attributes:
        None
    """

    def __init__(self):
        """
        initializes list

        Arguments: None
        Returns: None
        """
        super().__init__

    def print_sorted(self):
        """
        prints a sorted list

        Arguments:
            None

        Returns:
            None
        """

        print(sorted(self))
