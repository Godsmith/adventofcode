from collections import namedtuple
from dataclasses import dataclass
import dataclasses
from aoc.utils import rows
from aocd import data


# data = r""".|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\
# ..../.\\..
# .-.-/..|..
# .|....-|.\
# ..//.|...."""

grid = rows(data)
max_x = len(grid[0]) - 1
max_y = len(grid) - 1


@dataclass
class Beam:
    x: int
    y: int
    dx: int
    dy: int

    def __repr__(self) -> str:
        return f"Beam({x}, {y}, {dx}, {dy})"

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


def print_energized(energized):
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if (x, y) in energized:
                print("#", end="")
            else:
                print(char, end="")
        print()


def get_energized_count(beams: list[Beam]):
    energized = set()
    existing_beams = set()
    while beams:
        energized.update((beam.x, beam.y) for beam in beams)
        for beam in list(beams):
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
                    beams.append(new_beam)
            elif value == "|":
                if beam.dx:
                    beam.dx = 0
                    beam.dy = -1
                    new_beam = dataclasses.replace(beam, dy=1)
                    beams.append(new_beam)
            beam.move()
        # energized.update((beam.x, beam.y) for beam in beams)
        beams = [beam for beam in beams if beam.is_inside()]
        beams = [
            beam
            for beam in beams
            if (beam.x, beam.y, beam.dx, beam.dy) not in existing_beams
        ]
        # energized.update((beam.x, beam.y) for beam in beams)
        existing_beams.update((beam.x, beam.y, beam.dx, beam.dy) for beam in beams)
    return len(energized)


energized = get_energized_count(beams)

print(energized)

energized_counts = []
for x in range(max_x + 1):
    print(f"{x}/{max_x}")
    for y in range(max_y + 1):
        directions = []
        if x == 0:
            directions.append((1, 0))
        if x == max_x:
            directions.append((-1, 0))
        if y == 0:
            directions.append((0, 1))
        if y == max_y:
            directions.append((0, -1))
        for dx, dy in directions:
            beam = Beam(x, y, dx, dy)
            print(repr(beam))
            energized_counts.append(get_energized_count([beam]))
print(max(energized_counts))
