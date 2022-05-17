#!/usr/bin/python3
"""Module Square"""


class Square:
    """class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """initilize method"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
        self.__position = position

    def area(self):
        """returns area of square"""
        return self.__size ** 2

    @property
    def size(self):
        """returns size"""
        return self.__size

    @size.setter
    def size(self, value):
        """changes size"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')

    def my_print(self):
        """prints square"""
        if self.__size == 0:
            print()
            return
        for k in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print('#', end='')
            print()

    @property
    def position(self):
        """returns position"""
        return self.__position

    @position.setter
    def position(self, value):
        """changes position"""
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
