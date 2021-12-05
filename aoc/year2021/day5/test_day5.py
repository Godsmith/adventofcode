from aoc.year2021.day5.day5 import overlaps

data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def test_overlaps_no_diagonals():
    assert overlaps(data, diagonals=False) == 5


def test_overlaps_diagonals():
    assert overlaps(data, diagonals=True) == 12
