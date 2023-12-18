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
