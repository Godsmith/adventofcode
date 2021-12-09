import math
from aocd import get_data

from aoc.utils import rows


def risk_sum(lines):
    risk = 0
    for y, line in enumerate(lines):
        for x, height in enumerate(line):
            for x2, y2 in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                try:
                    if lines[y2][x2] <= height:
                        break
                except IndexError:
                    pass
            else:
                risk += lines[y][x] + 1
    return risk


def add_to_basin(x, y, basin, lines):
    basin.add((x, y))
    neighbors = [(x2, y2) for x2, y2 in
                 ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)) if
                 -1 < x2 < len(lines[0]) and
                 -1 < y2 < len(lines) and
                 lines[y2][x2] < 9]
    for x2, y2 in neighbors:
        if (x2, y2) not in basin:
            add_to_basin(x2, y2, basin, lines)


def create_basin(x, y, basins, lines):
    basin = set()
    add_to_basin(x, y, basin, lines)
    basins.append(basin)


def is_in_basin(x, y, basins):
    for basin in basins:
        if (x, y) in basin:
            return True
    return False


def basin_sizes(lines):
    basins = []
    for y, line in enumerate(lines):
        for x, height in enumerate(line):
            if height < 9 and not is_in_basin(x, y, basins):
                create_basin(x, y, basins, lines)
    return (len(basin) for basin in basins)


input_lines = [[int(c) for c in line] for line in rows(get_data())]

print(risk_sum(input_lines))
print(math.prod(sorted(basin_sizes(input_lines))[-3:]))
