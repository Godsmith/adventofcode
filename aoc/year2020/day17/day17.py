from aocd import data
from collections import defaultdict
from itertools import product, chain

from aoc.utils import rows


class Simulation:
    def __init__(self):
        self.cubes = defaultdict(lambda: ".")
        for y, row in enumerate(rows(data)):
            for x, value in enumerate(row):
                self.cubes[self._get_position(x, y)] = value

    def _get_position(self, x, y):
        return x, y, 0

    def _surrounding_positions(self, position):
        x, y, z = position
        return (p for p in product([x - 1, x, x + 1],
                                   [y - 1, y, y + 1],
                                   [z - 1, z, z + 1]) if p != position)

    def _get_active_neighbors(self, position):
        return sum(1 for neighbor in self._surrounding_positions(position)
                   if self.cubes[neighbor] == "#")

    def simulate(self):
        for _ in range(6):
            new_cubes = defaultdict(lambda: ".")
            positions_to_update = set(chain.from_iterable(
                self._surrounding_positions(position) for position in self.cubes if
                self.cubes[position] == "#"))
            for position in positions_to_update:
                active_neighbors = self._get_active_neighbors(position)
                if self.cubes[position] == "#" and active_neighbors not in (2, 3):
                    new_cubes[position] = "."
                elif self.cubes[position] == "." and active_neighbors == 3:
                    new_cubes[position] = "#"
                else:
                    new_cubes[position] = self.cubes[position]
            self.cubes = new_cubes
        return len([position for position in self.cubes if self.cubes[position] == "#"])


class Simulation2(Simulation):
    def _get_position(self, x, y):
        return x, y, 0, 0

    def _surrounding_positions(self, position):
        x, y, z, w = position
        return (p for p in product([x - 1, x, x + 1],
                                   [y - 1, y, y + 1],
                                   [z - 1, z, z + 1],
                                   [w - 1, w, w + 1]) if p != position)


print(Simulation().simulate())
print(Simulation2().simulate())
