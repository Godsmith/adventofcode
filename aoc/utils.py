import re
from typing import List
from itertools import zip_longest


def lmap(func, *iterables):
    return list(map(func, *iterables))

# STRINGS

def ints(s: str) -> List[int]:
    """Finds all ints in a string"""
    return lmap(int, re.findall(r"-?\d+", s))


def csv_rows(s: str) -> List[List[str]]:
    """Returns a list of list of strings from comma-separated rows"""
    return [row.split(',') for row in s.split('\n')]


def rows(s: str) -> List[str]:
    return s.split('\n')


def sign_of_difference(a, b):
    """
    >>> sign_of_difference(10, 5)
    1
    >>> sign_of_difference(5, 10)
    -1
    >>> sign_of_difference(5, 5)
    0
    """
    if a == b:
        return 0
    else:
        return int((a - b) / abs(a - b))

# ITERTOOLS

def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks
    >>> list(grouper('ABCDEFG', 3, 'x'))
    [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'x', 'x')]"""
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)

