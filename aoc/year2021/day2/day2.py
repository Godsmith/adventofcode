from typing import List

from aocd import data
from aoc.utils import rows
from more_itertools import sliding_window

strings = rows(data)

# Part 1

total_steps_forward = sum([int(s.split()[1]) for s in strings if "forward" in s])
total_steps_down = sum([int(s.split()[1]) for s in strings if "down" in s])
total_steps_up = sum([int(s.split()[1]) for s in strings if "up" in s])

depth = total_steps_down - total_steps_up

print(total_steps_forward * depth)


# Part 2

def value(s):
    return int(s.split()[1])


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
