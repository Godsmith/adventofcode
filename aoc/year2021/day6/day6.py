from aocd import data

from aoc.utils import ints

lanternfish = ints(data)

for generation in range(80):
    new_lanternfish = []
    for i in lanternfish:
        if i == 0:
            new_lanternfish.extend([6, 8])
        else:
            new_lanternfish.append(i - 1)
    lanternfish = new_lanternfish
    print(generation)

print(len(lanternfish))