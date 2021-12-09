from aocd import get_data

from aoc.utils import rows

lines = rows(get_data())
lines = [[int(c) for c in line] for line in lines]
risk = 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        for x2, y2 in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            try:
                if lines[y2][x2] <= lines[y][x]:
                    break
            except IndexError:
                pass
        else:
            risk += lines[y][x] + 1
print(risk)
