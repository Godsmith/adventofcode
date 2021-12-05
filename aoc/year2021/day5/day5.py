from collections import Counter

from aocd import data
from aoc.utils import rows
from more_itertools import flatten



def to_tuples(line, diagonals):
    point1_string, point2_string = line.split(" -> ")
    x1, y1 = [int(x) for x in point1_string.split(",")]
    x2, y2 = [int(x) for x in point2_string.split(",")]
    if x1 != x2 and y1 != y2:
        if diagonals:
            dx = (x2 - x1) / abs(x2-x1)
            dy = (y2 - y1) / abs(y2-y1)
            x, y = (x1, y1)
            return_value = [(x, y)]
            while True:
                x += dx
                y += dy
                return_value.append((x, y))
                if x == x2:
                    return return_value
        else:
            return []
    x1, x2 = sorted((x1, x2))
    y1, y2 = sorted((y1, y2))
    return [(x,y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]

def overlaps(data, diagonals):
    lines = rows(data)
    tuples = list(flatten(to_tuples(line, diagonals) for line in lines))
    c = Counter(tuples)
    a = [count for t, count in c.most_common() if count > 1]
    return len(a)

if __name__ == '__main__':
    print(overlaps(data, diagonals=False))
    print(overlaps(data, diagonals=True))

