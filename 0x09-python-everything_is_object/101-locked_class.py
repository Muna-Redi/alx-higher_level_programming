#!/usr/bin/python3

class LockedClass:
    """locked class that only allows the dynamic instatiation of
        the attribute first_name

    Attributes:
        first_name: only permited dynamically created attribute
    """
    __slots__ = ['first_name']
    """ the permits only the creation of new instances
        with attribute first name

    Attributes:
        first_name: permited dynamically created attribute
    """
