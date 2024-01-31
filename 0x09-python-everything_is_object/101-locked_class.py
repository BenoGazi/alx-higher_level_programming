#!/usr/bin/python3
"""Defines a locked Class"""
class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes
    except if the new instance is called first name
    """
    __slots__ = ["first_name"]
