from aocd import data
from aoc.utils import ints
from math import prod
from itertools import combinations

print([prod([t for t in combinations(ints(data), d) if sum(t) == 2020][0]) for d in (2,3)])
