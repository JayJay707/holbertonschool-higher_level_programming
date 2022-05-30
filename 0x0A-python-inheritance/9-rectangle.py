#!/usr/bin/python3
"""Module rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry"""
    def __init__(self, width, height):
        """Initialization of a rectangle from BaseGeometry"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Defines the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Representation of the rectangle"""
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
