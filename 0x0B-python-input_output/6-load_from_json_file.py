#!/usr/bin/python3
"""Module that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Function that creates an object from a JSON file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
