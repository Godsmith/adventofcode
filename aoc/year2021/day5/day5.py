from collections import Counter

from aocd import data
from aoc.utils import rows
from more_itertools import flatten


def to_coordinates(line, diagonals: bool):
    x1, y1, x2, y2 = [int(number) for point in line.split(" -> ") for number in point.split(",")]
    if x1 != x2 and y1 != y2 and not diagonals:
        return []
    dx = 0 if x1 == x2 else (1 if x2 > x1 else -1)
    dy = 0 if y1 == y2 else (1 if y2 > y1 else -1)
    xs = range(x1, x2 + dx, dx) if x1 != x2 else [x1] * (abs(y2 - y1) + 1)
    ys = range(y1, y2 + dy, dy) if y1 != y2 else [y1] * (abs(x2 - x1) + 1)
    return zip(xs, ys)


def overlaps(data, diagonals):
    coordinates = flatten(to_coordinates(line, diagonals) for line in rows(data))
    return sum(1 for _, count in Counter(coordinates).most_common() if count > 1)


if __name__ == '__main__':
    print(overlaps(data, diagonals=False))
    print(overlaps(data, diagonals=True))
