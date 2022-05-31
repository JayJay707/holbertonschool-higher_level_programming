#!/usr/bin/python3
"""Module to read a file"""


def read_file(filename=""):
    """Function that reads and prints a file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
