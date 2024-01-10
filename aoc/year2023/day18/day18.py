from dataclasses import dataclass
from aocd import data
from aoc.utils import rows
from tqdm import tqdm

# data = """R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)"""


dxdy_from_direction = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}


@dataclass
class Trench:
    x1: int
    y1: int
    x2: int
    y2: int
    changes_inside_to_outside: bool = True

    def __post_init__(self):
        if self.x1 > self.x2:
            self.x1, self.x2 = self.x2, self.x1
        if self.y1 > self.y2:
            self.y1, self.y2 = self.y2, self.y1

    def has_overlap(self, y: int) -> bool:
        return self.y1 <= y <= self.y2

    def is_horizontal(self):
        return self.x1 != self.x2

    def set_changes_inside_to_outside(self, previous_trench, next_trench):
        if self.is_horizontal():
            is_previous_trench_above = (
                min((previous_trench.y1, previous_trench.y2)) < self.y1
            )
            is_next_trench_above = min((next_trench.y1, next_trench.y2)) < self.y1
            is_previous_trench_below = (
                max((previous_trench.y1, previous_trench.y2)) > self.y1
            )
            is_next_trench_below = max((next_trench.y1, next_trench.y2)) > self.y1
            self.changes_inside_to_outside = (
                is_previous_trench_above and is_next_trench_below
            ) or (is_previous_trench_below and is_next_trench_above)


def print_area(trenches):
    for i, trench in enumerate(trenches):
        previous_trench = trenches[(i - 1) % len(trenches)]
        next_trench = trenches[(i + 1) % len(trenches)]
        trench.set_changes_inside_to_outside(previous_trench, next_trench)

    ys = [trench.y1 for trench in trenches] + [trench.y2 for trench in trenches]
    min_y = min(ys)
    max_y = max(ys)

    area = 0
    for y in tqdm(range(min_y, max_y + 1)):
        overlapping_trenches = sorted(
            [trench for trench in trenches if trench.has_overlap(y)],
            key=lambda trench: trench.x1,
        )

        is_inside = False
        x_start = 0
        # print(overlapping_trenches)
        for trench in overlapping_trenches:
            if trench.changes_inside_to_outside:
                if not is_inside:
                    x_start = trench.x1
                else:
                    darea = trench.x2 - x_start + 1
                    area += darea
                    # print(darea)
                is_inside = not is_inside
            else:
                if is_inside:
                    continue
                else:
                    darea = trench.x2 - trench.x1 + 1
                    area += darea
                    # print(darea)
    print(area)


trenches = []

x = 0
y = 0
for row in rows(data):
    direction, steps, color = row.split(" ")
    dx, dy = dxdy_from_direction[direction]
    dx *= int(steps)
    dy *= int(steps)
    trenches.append(Trench(x, y, x + dx, y + dy))
    # Prevent overlap between horizontal and vertical trenches:
    # Reduce all vertical trench lengths by 2
    if dy != 0:
        trenches[-1].y1 += 1
        trenches[-1].y2 -= 1
    x += dx
    y += dy

print_area(trenches)

trenches = []


def steps_and_direction_from_color(color: str) -> tuple[int, str]:
    steps_hex = color[2:7]
    steps = int(steps_hex, 16)
    direction_from_digit = {"0": "R", "1": "D", "2": "L", "3": "U"}
    return steps, direction_from_digit[color[7]]


x = 0
y = 0
for row in rows(data):
    _, _, color = row.split(" ")
    steps, direction = steps_and_direction_from_color(color)
    dx, dy = dxdy_from_direction[direction]
    dx *= int(steps)
    dy *= int(steps)
    trenches.append(Trench(x, y, x + dx, y + dy))
    # Prevent overlap between horizontal and vertical trenches:
    # Reduce all vertical trench lengths by 2
    if dy != 0:
        trenches[-1].y1 += 1
        trenches[-1].y2 -= 1
    x += dx
    y += dy

print_area(trenches)
