#!/usr/bin/python3
"""Module inherits_from"""


def inherits_from(obj, a_class):
    """
    Checks if object is an instance of a class
    inheriting from the specified class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
