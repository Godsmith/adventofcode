from aocd import data
from aoc.utils import rows

DIRECTIONS = {'E': (1, 0), "S": (0, 1), "W": (-1, 0), "N": (0, -1)}


class Ship:
    def __init__(self):
        self.x, self.y = (0, 0)
        self.direction = 'E'

    def run(self):
        for row in rows(data):
            instruction = row[0]
            value = int(row[1:])
            self._run_instruction(instruction, value)
        return abs(self.x) + abs(self.y)

    def _move(self, direction, value):
        if direction == "N":
            self.y -= value
        elif direction == "S":
            self.y += value
        elif direction == "E":
            self.x += value
        elif direction == "W":
            self.x -= value

    def _run_instruction(self, instruction, value):
        direction_index = list(DIRECTIONS.keys()).index(self.direction)
        if instruction in ('NSEW'):
            self._move(instruction, value)
        elif instruction == "L":
            direction_index = int(direction_index - value / 90) % 4
        elif instruction == "R":
            direction_index = int(direction_index + value / 90) % 4
        elif instruction == "F":
            self._move(self.direction, value)
        self.direction = list(DIRECTIONS.keys())[direction_index]


class Ship2(Ship):
    def __init__(self):
        super().__init__()
        self.waypoint_x, self.waypoint_y = (10, -1)

    def _run_instruction(self, instruction, value):
        if instruction == "N":
            self.waypoint_y -= value
        elif instruction == "S":
            self.waypoint_y += value
        elif instruction == "E":
            self.waypoint_x += value
        elif instruction == "W":
            self.waypoint_x -= value
        elif instruction in "LR":
            for _ in range(int(value / 90)):
                multiplier = 1 if instruction == "L" else -1
                self.waypoint_x, self.waypoint_y = (multiplier * self.waypoint_y,
                                                    -multiplier * self.waypoint_x)
        elif instruction == "F":
            self.x += self.waypoint_x * value
            self.y += self.waypoint_y * value


print(Ship().run())
print(Ship2().run())
