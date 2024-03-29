#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 31/october/23
@author: Amos Hiamatsu
"""


class LockedClass:
    """A locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']
