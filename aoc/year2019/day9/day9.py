from aocd import data
from aoc.year2019.intcode import Intcode
from aoc.utils import ints

i = Intcode(ints(data))

print(i.all_outputs(1))

i = Intcode(ints(data))
print(i.all_outputs(2))
