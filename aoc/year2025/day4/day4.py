import itertools
from aocd import data


# data = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@."""


def main():
    count = 0
    rows = list(map(lambda row: list(row), data.splitlines()))
    while True:
        to_remove = []
        for y, x in itertools.product(range(len(rows[0])), range(len(rows))):
            if rows[y][x] == "@" and is_removable(x, y, rows):
                to_remove.append((x, y))
        count += len(to_remove)
        for x, y in to_remove:
            rows[y][x] = "."
        if not to_remove:
            break

    print(count)


def is_removable(x, y, rows):
    neighbor_count = 0
    for new_x, new_y in itertools.product(range(x - 1, x + 2), range(y - 1, y + 2)):
        if x == new_x and y == new_y:
            continue
        if 0 <= new_x < len(rows[0]) and 0 <= new_y < len(rows):
            if rows[new_y][new_x] == "@":
                neighbor_count += 1
    return neighbor_count < 4


if __name__ == "__main__":
    main()
