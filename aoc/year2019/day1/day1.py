from aocd import data
from aoc.utils import ints


def fuel(mass: int) -> int:
    return mass // 3 - 2


def total_fuel(mass: int) -> int:
    fuel_req = mass // 3 - 2
    if fuel_req < 0:
        return 0
    return fuel_req + total_fuel(fuel_req)


# part 1
print(sum(map(fuel, ints(data))))

# part 2
print(sum(map(total_fuel, ints(data))))
