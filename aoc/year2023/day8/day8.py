from collections import defaultdict
import re
from aocd import data
from aoc.utils import rows
import itertools

instructions, nodes = data.split("\n\n")

network = defaultdict(dict)
for node in rows(nodes):
    if match := re.match(r"(.{3}) = \((.{3}), (.{3})\)", node):
        current, left, right = match.groups()
        network[current]["L"] = left
        network[current]["R"] = right


position = "AAA"
for i, instruction in enumerate(itertools.cycle(instructions), 1):
    position = network[position][instruction]
    if position == "ZZZ":
        print(i)
        break

# TRY 2

# entire_cycle_map = {}
# for position in network:
#     ending_position = position
#     for instruction in instructions:
#         ending_position = network[position][instruction]
#     entire_cycle_map[position] = ending_position

# positions = [position for position in network if position.endswith("A")]
# for i in itertools.count(len(instructions), len(instructions)):
#     positions = [entire_cycle_map[position] for position in positions]
#     if all(position.endswith("Z") for position in positions):
#         print(i)
#         break

# TRY 1

# positions = [position for position in network if position.endswith("A")]
# for i, instruction in enumerate(itertools.cycle(instructions), 1):
#     positions = [network[position][instruction] for position in positions]
#     print(positions)
#     if all(position.endswith("Z") for position in positions):
#         print(i)
#         break

# TRY 3

# Probably won't work because the number of combinations is 1E14

# from functools import cache


# @cache
# def step(set_: frozenset, instruction: str):
#     return frozenset(network[position][instruction] for position in set_)


# positions = frozenset(position for position in network if position.endswith("A"))
# for i, instruction in enumerate(itertools.cycle(instructions), 1):
#     positions = step(positions, instruction)
#     print(step.cache_info())
#     if all(position.endswith("Z") for position in positions):
#         print(i)
#         break
