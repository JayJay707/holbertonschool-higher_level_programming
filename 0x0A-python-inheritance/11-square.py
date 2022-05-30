#!/usr/bin/python3
"""Module square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""
    def __init__(self, size):
        """Initialization of the square"""
        self.__size = size
        self.integer_validator('size', self.__size)
        super().__init__(size, size)

    def area(self):
        """Defines area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Representation of the square"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
