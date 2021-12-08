from statistics import mean
from aocd import get_data
from aoc.utils import ints

positions = ints(get_data())


def fuel_cost_part_1(position, target):
    return abs(position - target)


def fuel_cost_part_2(position, target):
    return int(abs(position - target) * (abs(position - target) + 1) / 2)


def minimum_cost(fuel_cost_method):
    min_cost = 100000000
    for target_position in range(max(positions)):
        min_cost = min(min_cost, sum(fuel_cost_method(position, target_position) for position in positions))
    return min_cost


print(minimum_cost(fuel_cost_part_1))
print(minimum_cost(fuel_cost_part_2))
