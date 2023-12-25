import itertools
from aoc.utils import rows
from aocd import data


def distance(galaxy1: tuple[int, int], galaxy2: tuple[int, int]):
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])


def expanded_galaxy(
    galaxy: tuple[int, int],
    columns_without_galaxies: list[int],
    rows_without_galaxies: list[int],
    expansion: int,
) -> tuple[int, int]:
    empty_columns_before = len(
        [x1 for x1 in columns_without_galaxies if x1 < galaxy[0]]
    )
    empty_rows_before = len([y1 for y1 in rows_without_galaxies if y1 < galaxy[1]])
    new_x = galaxy[0] + empty_columns_before * (expansion - 1)
    new_y = galaxy[1] + empty_rows_before * (expansion - 1)
    return (new_x, new_y)


def expanded_distance_sum(data: str, expansion: int):
    all_rows = rows(data)
    rows_without_galaxies = [
        y for y, row in enumerate(all_rows) if all(char == "." for char in row)
    ]
    columns_without_galaxies = [
        x for x, _ in enumerate(all_rows[0]) if all(row[x] == "." for row in all_rows)
    ]
    galaxies = {
        (x, y)
        for y, row in enumerate(all_rows)
        for x, char in enumerate(row)
        if char == "#"
    }

    expanded_galaxies = {
        expanded_galaxy(
            galaxy, columns_without_galaxies, rows_without_galaxies, expansion
        )
        for galaxy in galaxies
    }

    distances = [
        distance(galaxy1, galaxy2)
        for galaxy1, galaxy2 in itertools.combinations(expanded_galaxies, 2)
    ]

    return sum(distances)


print(expanded_distance_sum(data, 2))
print(expanded_distance_sum(data, 1000000))
