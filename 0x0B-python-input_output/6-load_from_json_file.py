#!/usr/bin/python3
"""Defines Json file reading function"""
import json
def load_from_json_file(filename):
    """Return Python object of JSON Representation"""
    with open(filename) as file:
        return json.load(file)
