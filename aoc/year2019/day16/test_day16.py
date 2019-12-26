from itertools import islice
from aoc.year2019.day16.day16 import phase, iterator


def test_iterator():
    assert list(islice(iterator(1), 13)) == [0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1, 0, 0]


def test_phase():
    s = '12345678'
    assert phase(s) == "48226158"

