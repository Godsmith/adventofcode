import itertools
from aoc.utils import character_lists, rows
from aocd import data


def expand(data: str):
    row_length = len(rows(data)[0])

    empty_row = "." * row_length
    data = data.replace(empty_row, empty_row + "\n" + empty_row)

    all_rows = rows(data)

    x_with_galaxy = set()

    for row in all_rows:
        for x, char in enumerate(row):
            if char == "#":
                x_with_galaxy.add(x)

    new_rows = []
    for row in all_rows:
        new_row = []
        for x, char in enumerate(row):
            if not x in x_with_galaxy:
                char = ".."
            new_row.append(char)
        new_rows.append("".join(new_row))

    return "\n".join(new_rows)


new_data = expand(data)

all_rows = rows(new_data)

galaxies = set()
for x, row in enumerate(all_rows):
    for y, char in enumerate(row):
        if char == "#":
            galaxies.add((x, y))


def distance(galaxy1: tuple[int, int], galaxy2: tuple[int, int]):
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


distances = [
    distance(galaxy1, galaxy2)
    for galaxy1, galaxy2 in itertools.combinations(galaxies, 2)
]

print(sum(distances))
