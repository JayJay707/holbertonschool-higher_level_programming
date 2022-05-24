#!/usr/bin/python3
"""Module that prints a name"""

def say_my_name(first_name, last_name=""):
    """Function that prints "My name is" + name"""

    if type(first_name) is not str:
        raise TypeError("first name must be a string")
    if type(last_name) is not str:
        raise TypeError("last name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
