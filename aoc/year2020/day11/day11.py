import sys

from aocd import data
from aoc.utils import character_lists
from copy import deepcopy


class Ferry:
    STEPS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    EMPTY_COUNT = 4
    MAX_DISTANCE = 1

    def get_status(self, lines, x, y):
        if 0 <= y < len(lines) and 0 <= x < len(lines[0]):
            return lines[y][x]
        return "X"

    def get_occupied_adjacent_count(self, lines, x, y):
        count = 0
        for step in self.STEPS:
            next_x, next_y = x, y
            for i in range(self.MAX_DISTANCE):
                next_x, next_y = step[0] + next_x, step[1] + next_y
                status = self.get_status(lines, next_x, next_y)
                if status == ".":
                    continue
                if status == "#":
                    count += 1
                    break
                if status == "L" or status == "X":
                    break
        return count

    def new_status(self, lines, x, y):
        count = self.get_occupied_adjacent_count(lines, x, y)
        status = self.get_status(lines, x, y)
        if status == "L" and count == 0:
            return "#"
        elif status == "#" and count >= self.EMPTY_COUNT:
            return "L"
        return status

    def run(self):
        new_lines = character_lists(data)
        lines = None
        while lines != new_lines:
            lines = deepcopy(new_lines)
            for y, line in enumerate(lines):
                for x, _ in enumerate(line):
                    new_lines[y][x] = self.new_status(lines, x, y)
        return ''.join(''.join(line) for line in lines).count("#")


class Ferry2(Ferry):
    EMPTY_COUNT = 5
    MAX_DISTANCE = sys.maxsize


print(Ferry().run())
print(Ferry2().run())
