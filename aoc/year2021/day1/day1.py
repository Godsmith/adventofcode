from typing import List

from aocd import data
from aoc.utils import ints
from more_itertools import sliding_window


def deeper_count(depths: List[int]):
    pairwise_depths = sliding_window(depths, 2)
    depth_deltas = map(lambda depths: depths[1] - depths[0], pairwise_depths)
    return len(list(filter(lambda depth_delta: depth_delta > 0, depth_deltas)))

# Part 1
depths = ints(data)
print(deeper_count(depths))

# Part 2
groups_of_three_depths = sliding_window(depths, 3)
averaged_depths = list(map(sum, groups_of_three_depths))
print(deeper_count(averaged_depths))
