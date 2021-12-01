from aocd import data
from aoc.utils import ints
from more_itertools import sliding_window


def deeper_count(depths):
    count = 0
    for i, depth in enumerate(depths):
        if i == 0:
            continue
        if depth > depths[i - 1]:
            count += 1
    return count


depths = ints(data)

print(deeper_count(depths))

groups_of_three_depths = sliding_window(depths, 3)
averaged_depths = list(map(sum, groups_of_three_depths))

print(deeper_count(averaged_depths))
