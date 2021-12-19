from aocd import get_data

from aoc.year2021.day18.snailfishnumber import SnailfishNumber

s = SnailfishNumber.final_sum(get_data(day=18, year=2021))

print(s.magnitude)


