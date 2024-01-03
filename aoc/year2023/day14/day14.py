from typing import Callable
from aocd import data
from aoc.utils import rows

rounded_rocks = set()
cubed_rocks = set()
for y, row in enumerate(rows(data)):
    for x, char in enumerate(row):
        if char == "#":
            cubed_rocks.add((x, y))
        elif char == "O":
            rounded_rocks.add((x, y))

max_y = len(rows(data)) - 1
max_x = len(rows(data)[0]) - 1


def get_moves(
    rounded_rocks: set[tuple[int, int]],
    cubed_rocks: set[tuple[int, int]],
    move: Callable[[int, int], tuple[int, int]],
    condition: Callable[[int, int], bool],
):
    return {
        (x, y): move(x, y)
        for x, y in rounded_rocks
        if move(x, y) not in rounded_rocks
        and move(x, y) not in cubed_rocks
        and condition(x, y)
    }


def move_up(
    rounded_rocks: set[tuple[int, int]], cubed_rocks: set[tuple[int, int]]
) -> dict[tuple[int, int], tuple[int, int]]:
    return get_moves(
        rounded_rocks, cubed_rocks, lambda x, y: (x, y - 1), lambda x, y: y > 0
    )


def move_left(
    rounded_rocks: set[tuple[int, int]], cubed_rocks: set[tuple[int, int]]
) -> dict[tuple[int, int], tuple[int, int]]:
    return get_moves(
        rounded_rocks, cubed_rocks, lambda x, y: (x - 1, y), lambda x, y: x > 0
    )


def move_down(
    rounded_rocks: set[tuple[int, int]], cubed_rocks: set[tuple[int, int]]
) -> dict[tuple[int, int], tuple[int, int]]:
    return get_moves(
        rounded_rocks, cubed_rocks, lambda x, y: (x, y + 1), lambda x, y: y < max_y
    )


def move_right(
    rounded_rocks: set[tuple[int, int]], cubed_rocks: set[tuple[int, int]]
) -> dict[tuple[int, int], tuple[int, int]]:
    return get_moves(
        rounded_rocks, cubed_rocks, lambda x, y: (x + 1, y), lambda x, y: x < max_x
    )


def tilt(rounded_rocks, cubed_rocks, move_function):
    while to_move := move_function(rounded_rocks, cubed_rocks):
        for from_, to_ in to_move.items():
            rounded_rocks.remove(from_)
            rounded_rocks.add(to_)


def total_load(rounded_rocks):
    return sum(max_y + 1 - y for _, y in rounded_rocks)


def part1():
    tilt(rounded_rocks, cubed_rocks, move_up)
    print(total_load(rounded_rocks))


for i in range(300):
    tilt(rounded_rocks, cubed_rocks, move_up)
    tilt(rounded_rocks, cubed_rocks, move_left)
    tilt(rounded_rocks, cubed_rocks, move_down)
    tilt(rounded_rocks, cubed_rocks, move_right)
    print(i, total_load(rounded_rocks))


# print(rounded_rocks)
# print(cubed_rocks)

# 241 98064
# 242 98062
# 243 98057
# 244 98038

# 260 98027

# 267 98064
# 268 98062
# 269 98057
# 270 98038

# 293 98064
# 294 98062
# 295 98057
# 296 98038

# cycle length = 26

# 1_000_000_000 % 26 == 12
# 260 + 12 = 272

# The right answer was 271, so evidently there was a +/- 1 error somewhere
