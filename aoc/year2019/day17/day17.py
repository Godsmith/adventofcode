from aocd import data

from aoc.utils import ints
from aoc.year2019.intcode import Intcode


def main():
    intcode = Intcode(ints(data))
    outputs = intcode.run_to_next_input(None)
    s = ''.join(map(chr, outputs))
    print(alignment_parameter_sum(s))


def alignment_parameter_sum(s):
    matrix = s.split('\n')
    sum_ = 0
    for y, _ in enumerate(matrix):
        for x, _ in enumerate(matrix[0]):
            if is_intersection(s, x, y):
                sum_ += x * y
    return sum_


def character_at(s, x, y):
    matrix = s.split('\n')
    try:
        return matrix[y][x]
    except IndexError:
        return None


def is_intersection(s, x, y):
    return all(character_at(s, x2, y2) == '#' for x2, y2 in neighbors_and_itself(x, y))


def neighbors_and_itself(x, y):
    return [(x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


if __name__ == '__main__':
    main()
