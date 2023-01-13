#!/usr/bin/python3
""" This module defines the read_file function"""

def read_file(filename="")
    """Reads a text file and print it to the stdout

    Args:
    filename(str): filename
    """
    with open(filename, encoding = 'utf-8') as file:
        for line in file:
            print(line, end="")

