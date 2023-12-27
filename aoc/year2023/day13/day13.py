import copy
from typing import Iterable, Sequence
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


def find_reflections(rows: Sequence[Sequence[str]]) -> list[int]:
    reflections = []
    for i, (row1, row2) in enumerate(more_itertools.pairwise(rows)):
        if row1 == row2:
            if check_reflection(rows, i):
                reflections.append(i)
    return reflections


def scores(pattern_string: str) -> list[int]:
    rows: list[str] = pattern_string.split("\n")
    scores_ = []
    if row_indices := find_reflections(rows):
        scores_.extend([100 * (row_index + 1) for row_index in row_indices])
    columns = to_columns(rows)
    if column_indices := find_reflections(columns):
        scores_.extend([column_index + 1 for column_index in column_indices])
    return scores_


def score(pattern_string: str) -> int:
    return scores(pattern_string)[0]


def to_columns(rows: Sequence[str]) -> list[list[str]]:
    return [[row[i] for row in rows] for i, _ in enumerate(rows[0])]


def variants(pattern_string: str) -> Iterable[str]:
    characters = list(pattern_string)
    for i, char in enumerate(characters):
        if char == "\n":
            continue
        new_characters = copy.deepcopy(characters)
        if char == ".":
            new_characters[i] = "#"
        elif char == "#":
            new_characters[i] = "."
        yield "".join(new_characters)


def variant_score(pattern_string: str):
    original_score = score(pattern_string)
    for variant in variants(pattern_string):
        for score_ in scores(variant):
            if score_ and score_ != original_score:
                return score_
    raise ValueError("no variant score found")


pattern_strings = data.split("\n\n")
print(sum(score(pattern_string) for pattern_string in pattern_strings))
print(sum(variant_score(pattern_string) for pattern_string in pattern_strings))
