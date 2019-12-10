from math import gcd
from typing import List, Tuple
from itertools import combinations

from aocd import data
from aoc.utils import rows


class Starfield:
    def __init__(self, asteroid_string):
        region = rows(asteroid_string)
        self.row_count = len(region)
        self.column_count = len(region[0])

        coordinates = {(x, y) for y in range(self.row_count) for x in
                       range(self.column_count)}

        self.asteroids = set()
        for y, row in enumerate(region):
            for x, c in enumerate(row):
                if c == "#":
                    self.asteroids.add((x, y))

    def detected_count(self, station_x, station_y):
        count = 0
        for x, y in self.asteroids - {(station_x, station_y)}:
            if x == 4 and y == 3:
                x = x
            dx = x - station_x
            dy = y - station_y
            steps = max(abs(dx), abs(dy))
            for i in range(1, steps):
                dx2 = i * dx / steps
                dy2 = i * dy / steps

                x2 = station_x + dx2
                y2 = station_y + dy2
                if (x2, y2) in self.asteroids:
                    # Another asteroid in the way
                    break
            else:
                count += 1
        return count

    def best_location(self):
        detected_counts = {self.detected_count(*asteroid): asteroid for asteroid in
                           self.asteroids}
        return detected_counts[max(detected_counts)], max(detected_counts)

    @staticmethod
    def _common_divisors(a, b):
        if a == 0:
            yield from range(2, abs(b) + 1)
        if b == 0:
            yield from range(2, abs(a) + 1)
        for i in range(2, min(abs(a), abs(b)) + 1):
            if a % i == b % i == 0:
                yield i


def main():
    s = """.###..#######..####..##...#
########.#.###...###.#....#
###..#...#######...#..####.
.##.#.....#....##.#.#.....#
###.#######.###..##......#.
#..###..###.##.#.#####....#
#.##..###....#####...##.##.
####.##..#...#####.#..###.#
#..#....####.####.###.#.###
#..#..#....###...#####..#..
##...####.######....#.####.
####.##...###.####..##....#
#.#..#.###.#.##.####..#...#
..##..##....#.#..##..#.#..#
##.##.#..######.#..#..####.
#.....#####.##........#####
###.#.#######..#.#.##..#..#
###...#..#.#..##.##..#####.
.##.#..#...#####.###.##.##.
...#.#.######.#####.#.####.
#..##..###...###.#.#..#.#.#
.#..#.#......#.###...###..#
#.##.#.#..#.#......#..#..##
.##.##.##.#...##.##.##.#..#
#.###.#.#...##..#####.###.#
#.####.#..#.#.##.######.#..
.#.#####.##...#...#.##...#."""
    starfield = Starfield(s)
    print(starfield.best_location())


if __name__ == '__main__':
    main()
