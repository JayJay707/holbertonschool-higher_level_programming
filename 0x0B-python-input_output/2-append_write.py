#!/usr/bin/python3
"""Module that appends text to a file and returns length"""


def append_write(filename="", text=""):
    """Function that appends text to a file and returns length"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
