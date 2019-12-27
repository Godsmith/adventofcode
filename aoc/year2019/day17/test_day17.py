from aoc.year2019.day17.day17 import alignment_parameter_sum, character_at, \
    is_intersection

S = """"..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^.."""


def test_alignment_parameter_sum():
    assert alignment_parameter_sum(S) == 76


def test_character_at():
    assert character_at(S, 0, 3) == "#"


def test_is_intersection():
    assert not is_intersection(S, 0, 0)
    assert is_intersection(S, 2, 4)
