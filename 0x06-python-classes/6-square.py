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
            return()
        for k in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()

    @property
    def position(self):
        """returns position"""
        return(self.__position)

    @position.setter
    def position(self, value):
        """changes position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
