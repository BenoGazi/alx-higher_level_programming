#!/usr/bin/python3
"""Appends a string at the end of a text"""
def append_write(filename="", text=""):
    """Appends a string to the file.
    Args:
    filename (str): The filename
    text (str): The string to append to the file
    Returns:
    The number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
