#!/usr/bin/python3
"""This module defines the function inherit_from
"""

def inherit_from(obj, a_class):
    """Returns True if obj is instance of class based on inheritance
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class type must be type")
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
