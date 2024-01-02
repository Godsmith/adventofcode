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

while True:
    to_move = {}
    for x, y in rounded_rocks:
        if (x, y - 1) not in rounded_rocks and (x, y - 1) not in cubed_rocks and y > 0:
            to_move[(x, y)] = (x, y - 1)
    if to_move:
        for from_, to_ in to_move.items():
            rounded_rocks.remove(from_)
            rounded_rocks.add(to_)
    else:
        break

total_load = sum(len(rows(data)) - y for _, y in rounded_rocks)
print(total_load)


# print(rounded_rocks)
# print(cubed_rocks)
