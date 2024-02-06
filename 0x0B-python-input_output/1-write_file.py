#!/usr/bin/python3
"""Writes a string to a text file"""
def write_file(filename="", text=""):
    """Write to UTF-8.
    Args:
    filename (str): The name of the file to write.
    Returns:
    The number of characters in it
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
