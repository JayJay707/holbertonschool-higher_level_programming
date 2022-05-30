#!/usr/bin/python3
"""List inheritance module"""


class MyList(list):
    """Class list"""
    def print_sorted(self):
        """Prints a sorted List"""
        print(sorted(self))
