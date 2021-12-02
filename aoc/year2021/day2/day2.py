from typing import List

from aocd import data
from aoc.utils import rows

strings = rows(data)


# Part 1

def value(s):
    return int(s.split()[1])

def total(strings: List[str], command: str):
    return sum(value(s) for s in strings if command in s)


depth = total(strings, "down") - total(strings, "up")

print(total(strings, "forward") * depth)


# Part 2


aim = 0
depth = 0
horizontal_position = 0
for s in strings:
    if 'forward' in s:
        horizontal_position += value(s)
        depth += aim * value(s)
    elif 'down' in s:
        aim += value(s)
    else:
        aim -= value(s)

print(depth * horizontal_position)
