#!/usr/bin/python3
"""Module BaseGeometry"""


class BaseGeometry():
    """Empty class"""
    def area(self):
        """Raise exception "area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
