from collections import namedtuple
from dataclasses import dataclass
import dataclasses
from aoc.utils import rows


data = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

grid = rows(data)
max_x = len(grid[0]) - 1
max_y = len(grid) - 1


@dataclass
class Beam:
    x: int
    y: int
    dx: int
    dy: int

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def is_inside(self):
        return (0 <= self.x <= max_x) and (0 <= self.y <= max_y)

    def __str__(self):
        if self.dx > 0:
            return ">"
        elif self.dx < 0:
            return "<"
        elif self.dy > 0:
            return "v"
        else:
            return "^"


beams = [Beam(0, 0, 1, 0)]


def is_inside(position: tuple[int, int]):
    return (0 <= position[0] <= max_x) and (0 <= position[1] <= max_y)


def print_beams(beams):
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            for beam in beams:
                if beam.x == x and beam.y == y:
                    print(str(beam), end="")
                    break
            else:
                print(char, end="")
        print()


energized = set()
existing_beams = set()
while beams:
    new_beams = []
    energized.update((beam.x, beam.y) for beam in beams)
    for beam in beams:
        value = grid[beam.y][beam.x]
        if value == "/":
            beam.dx, beam.dy = beam.dy, beam.dx
            beam.dx *= -1
            beam.dy *= -1
        elif value == "\\":
            beam.dx, beam.dy = beam.dy, beam.dx
        elif value == "-":
            if beam.dy:
                beam.dy = 0
                beam.dx = -1
                new_beam = dataclasses.replace(beam, dx=1)
                new_beam.move()
                new_beams = [new_beam]
        elif value == "|":
            if beam.dx:
                beam.dx = 0
                beam.dy = -1
                new_beam = dataclasses.replace(beam, dy=1)
                new_beam.move()
                new_beams = [new_beam]
        beam.move()
    beams = [beam for beam in beams + new_beams if beam.is_inside()]
    print_beams(beams)
    a = 1

print(len(energized))
