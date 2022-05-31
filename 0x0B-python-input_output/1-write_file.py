#!/usr/bin/python3
"""Module that writes to a text file and returns length"""


def write_file(filename="", text=""):
    """Function that writes to a text file and returns length"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
