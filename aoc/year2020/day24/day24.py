from collections import defaultdict

from aocd import data
from aoc.utils import rows
from copy import deepcopy

d = defaultdict(lambda: False)

for row in rows(data):
    row = row.replace("nw", "new").replace("se", "swe"). \
        replace("ne", "n").replace("sw", "s")
    x, y = 0, 0
    for s in row:
        if s == "n":
            y -= 1
        elif s == "e":
            x += 1
        elif s == "w":
            x -= 1
        elif s == "s":
            y += 1
    d[(x, y)] = not d[(x, y)]


def surrounding_tiles(x, y):
    return {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),
            (x - 1, y - 1), (x + 1, y + 1)}


def tiles_to_consider(d):
    for coordinate in d:
        yield from surrounding_tiles(*coordinate)


print(sum(d.values()))

for _ in range(100):
    new_d = deepcopy(d)
    for x, y in set(tiles_to_consider(d)):
        count = sum(d[(x, y)] for x, y in surrounding_tiles(x, y))
        if ((d[(x, y)] and (count == 0 or count > 2)) or (
                not d[(x, y)] and count == 2)):
            new_d[(x, y)] = not d[(x, y)]
    d = new_d

print(sum(d.values()))
