#!/usr/bin/bash
"""Creates an object from a JSON file"""
def load_from_json_file(filename):
    """Return Python object of JSON Representation"""
    return json.loads(filename)
