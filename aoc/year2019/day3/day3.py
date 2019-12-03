from typing import List, Set, Tuple, Dict

from aocd import data

from aoc.utils import csv_rows

DIRECTIONS = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


def main():
#     data = """r75,d30,r83,u83,l12,d49,r71,u7,l72
# u62,r66,u55,r34,d71,r55,d58,r83"""
    #     data="""R8,U5,L5,D3
    # U7,R6,D4,L4"""
    wires = csv_rows(data)
    common_positions = positions(wires[0]) & positions(wires[1])
    print(min(
        abs(position[0]) + abs(position[1]) for position in common_positions))

    delays0 = delays(wires[0])
    delays1 = delays(wires[1])
    total_delays_of_common_positions = [delays0[position] + delays1[position]
                                        for position in common_positions]

    print(min(total_delays_of_common_positions))


def positions(wire: List[str]) -> Set[Tuple]:
    out = set()
    position = (0, 0)
    for instruction in wire:
        for _ in range(count(instruction)):
            position = add(position, direction(instruction))
            out.add(position)
    return out


def delays(wire: List[str]) -> Dict[Tuple, int]:
    out = {}
    position = (0, 0)
    delay = 0
    for instruction in wire:
        for _ in range(count(instruction)):
            delay += 1
            position = add(position, direction(instruction))
            if position not in out:
                out[position] = delay
    return out


def count(instruction):
    return int(instruction[1:])


def direction(instruction):
    return DIRECTIONS[instruction[0]]


def add(point1, point2):
    return point1[0] + point2[0], point1[1] + point2[1]


if __name__ == '__main__':
    main()
