import re
from typing import List


def lmap(func, *iterables):
    return list(map(func, *iterables))


def ints(s: str) -> List[int]:
    """Finds all ints in a string"""
    return lmap(int, re.findall(r"-?\d+", s))


def csv_rows(s: str) -> List[List[str]]:
    """Returns a list of list of strings from comma-separated rows"""
    return [row.split(',') for row in s.split('\n')]
