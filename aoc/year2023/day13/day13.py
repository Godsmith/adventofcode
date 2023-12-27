from typing import Sequence
from aocd import data
import more_itertools


def check_reflection(rows: Sequence[Sequence[str]], index: int) -> bool:
    i = index
    j = index + 1
    while i >= 0 and j < len(rows):
        if rows[i] != rows[j]:
            return False
        i -= 1
        j += 1
    return True


def find_reflection(rows: Sequence[Sequence[str]]) -> int:
    for i, (row1, row2) in enumerate(more_itertools.pairwise(rows)):
        if row1 == row2:
            if check_reflection(rows, i):
                return i
    return -1


def score(pattern_string: str) -> int:
    rows: list[str] = pattern_string.split("\n")
    if (row_index := find_reflection(rows)) != -1:
        return 100 * (row_index + 1)
    columns = to_columns(rows)
    column_index = find_reflection(columns)
    return column_index + 1


def to_columns(rows: Sequence[str]) -> list[list[str]]:
    return [[row[i] for row in rows] for i, _ in enumerate(rows[0])]


pattern_strings = data.split("\n\n")
print(sum(score(pattern_string) for pattern_string in pattern_strings))

# test_pattern = """#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#."""

# test_pattern_2 = """#...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#"""

# print(score(test_pattern))
# print(score(test_pattern_2))
