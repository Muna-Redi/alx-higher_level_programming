#!/usr/bin/python3

class LockedClass:
    """
        locked class that only allows the dynamic instatiation of
        the attribute first_name"""
    __slots__ = ['first_name']
