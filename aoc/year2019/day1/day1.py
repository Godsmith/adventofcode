from aocd import data
from aoc.utils import ints


def fuel(mass: int) -> int:
    fuel_req = mass // 3 - 2
    if fuel_req < 0:
        return 0
    return fuel_req


def total_fuel(mass: int) -> int:
    out = 0
    last_mass = mass
    while True:
        fuel_for_last_mass = fuel(last_mass)
        out += fuel_for_last_mass
        last_mass = fuel_for_last_mass
        if fuel_for_last_mass == 0:
            break

    return out


# part 1
print(sum(map(fuel, ints(data))))

# part 2
print(sum(map(total_fuel, ints(data))))
