import re
import typing

def lmap(func, *iterables):
    return list(map(func, *iterables))

def ints(s: str) -> typing.List[int]:
    """Finds all ints in a string"""
    return lmap(int, re.findall(r"-?\d+", s))