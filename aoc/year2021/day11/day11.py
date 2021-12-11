from itertools import count, product

from aocd import get_data


def neighbors(x, y):
    return [(x2, y2) for x2, y2 in product(range(x - 1, x + 2), range(y - 1, y + 2)) if
            0 <= x2 < len(octopuses) and 0 <= y2 < len(octopuses)]


def flash(x, y):
    octopuses[y][x] = 0
    for x2, y2 in neighbors(x, y):
        if octopuses[y2][x2] > 0:
            octopuses[y2][x2] += 1
            if octopuses[y2][x2] > 9:
                flash(x2, y2)


def step():
    for y, line in enumerate(octopuses):
        for x, _ in enumerate(line):
            octopuses[y][x] += 1

    for y, line in enumerate(octopuses):
        for x, value in enumerate(line):
            if value > 9:
                flash(x, y)


def count_zeroes(octopuses):
    return [octopus for line in octopuses for octopus in line].count(0)


data = get_data()
octopuses = [[int(i) for i in row] for row in data.splitlines()]

flash_count = 0
for _ in range(100):
    step()
    flash_count += count_zeroes(octopuses)
print(flash_count)

for i in count(start=101):
    step()
    if count_zeroes(octopuses) == 100:
        print(i)
        break
