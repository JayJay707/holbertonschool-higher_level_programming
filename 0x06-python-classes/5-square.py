#!/usr/bin/python3
"""Module Square"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """initialize method"""
        self.__size = size

    def area(self):
        "returns area of square"""
        return(self.__size ** 2)

    @property
    def size(self):
        """returns size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """changes size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must not be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints square"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                print("#" * self.__size)
