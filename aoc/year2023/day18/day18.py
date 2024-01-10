from collections import deque
from dataclasses import dataclass
from aocd import data
from typing import Optional
from aoc.utils import rows

data = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""


dxdy_from_direction = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}

x = 0
y = 0
trenches = {(0, 0)}
for row in rows(data):
    direction, steps, color = row.split(" ")
    dx, dy = dxdy_from_direction[direction]
    for i in range(int(steps)):
        x += dx
        y += dy
        trenches.add((x, y))

min_x = min(x for x, _ in trenches)
min_y = min(y for _, y in trenches)
max_x = max(x for x, _ in trenches)
max_y = max(y for _, y in trenches)

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if (x, y) in trenches:
            print("#", end="")
        else:
            print(".", end="")
    print()

edges = {(min_x - 1, min_y - 1)}
visited = set()
while edges:
    x, y = edges.pop()
    visited.add((x, y))
    neighbors = ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
    for x, y in neighbors:
        if (x, y) in visited:
            continue
        if x < min_x - 1 or x > max_x + 1 or y < min_y - 1 or y > max_y + 1:
            continue
        if (x, y) in trenches:
            continue
        edges.add((x, y))

# for y in range(min_y - 1, max_y + 2):
#     for x in range(min_x - 1, max_x + 2):
#         if (x, y) in visited:
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()
print((max_x - min_x + 3) * (max_y - min_y + 3) - len(visited))


@dataclass
class Trench:
    x1: int
    y1: int
    x2: int
    y2: int

    def __post_init__(self):
        if self.x1 > self.x2:
            self.x1, self.x2 = self.x2, self.x1
        if self.y1 > self.y2:
            self.y1, self.y2 = self.y2, self.y1

    def cross_section(self, y: int) -> Optional[tuple[int, int]]:
        if self.y1 == self.y2:
            return (self.x1, self.x2) if y == self.y1 else None
        else:
            return (self.x1, self.x1) if self.y1 <= y <= self.y2 else None


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

xs = [trench.x1 for trench in trenches] + [trench.x2 for trench in trenches]
ys = [trench.y1 for trench in trenches] + [trench.y2 for trench in trenches]
min_x = min(xs)
min_y = min(ys)
max_x = max(xs)
max_y = max(ys)

area = 0
for y in range(min_y, max_y + 1):
    cross_sections = [trench.cross_section(y) for trench in trenches]
    cross_sections = [
        cross_section for cross_section in cross_sections if cross_section
    ]
    cross_sections.sort()

    is_inside = False
    x_start = 0
    print(cross_sections)
    for x1, x2 in cross_sections:
        if x1 != x2:
            if is_inside:
                continue
            else:
                darea = x2 - x1 + 1
                print(darea)
                area += darea
        else:
            if not is_inside:
                is_inside = True
                x_start = x1
            else:
                is_inside = False
                darea = x1 - x_start + 1
                area += darea
                print(darea)
print(area)
