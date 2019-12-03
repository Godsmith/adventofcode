from typing import List, Set, Tuple

from aocd import data

from aoc.utils import csv_rows

DIRECTIONS = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


def main():
#     data = """R75,D30,R83,U83,L12,D49,R71,U7,L72
# U62,R66,U55,R34,D71,R55,D58,R83"""
#     data="""R8,U5,L5,D3
# U7,R6,D4,L4"""
    wires = csv_rows(data)
    common_positions = positions(wires[0]) & positions(wires[1])
    print(min(abs(position[0]) + abs(position[1]) for position in common_positions))

def positions(wire: List[str]) -> Set[Tuple]:
    out = set()
    position = (0, 0)
    for instruction in wire:
        for _ in range(count(instruction)):
            position = add(position, direction(instruction))
            out.add(position)
    return out



def count(instruction):
    return int(instruction[1:])


def direction(instruction):
    return DIRECTIONS[instruction[0]]


def add(point1, point2):
    return point1[0] + point2[0], point1[1] + point2[1]


if __name__ == '__main__':
    main()
