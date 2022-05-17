#!/usr/bin/python3
"""Module Square"""


class Square:
    """class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize method"""
        self.__size = size
        self.__position = position

    def area(self):
        """returns area of square"""
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
            print("\n" * self.__position[1], end="")
            for x in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def position(self):
        """returns position"""
        return(self.__position)

    @position.setter
    def position(self, value):
        """changes position"""
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
