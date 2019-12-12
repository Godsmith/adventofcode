from collections import defaultdict
from math import gcd, tan, atan, pi, atan2
from typing import List, Tuple
from itertools import combinations, cycle

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
    def angle_to(giant_laser, asteroid):
        a = atan2((asteroid[1] - giant_laser[1]), (asteroid[0] - giant_laser[0]))
        b = a + pi / 2
        if b < 0:
            return b + 2 * pi
        return b

    def destroy(self, giant_laser, count):

        asteroids_from_angle = defaultdict(list)
        for asteroid in self.asteroids:
            angle = self.angle_to(giant_laser, asteroid)
            asteroids_from_angle[angle].append(asteroid)
        i = 0
        angles = cycle(sorted(asteroids_from_angle.keys()))
        while i < count:
            angle = next(angles)
            if asteroids_from_angle[angle]:
                i += 1
                yield self.remove_closest_to(giant_laser, asteroids_from_angle[angle])

    def remove_closest_to(self, giant_laser: Tuple[int, int],
                          asteroids: List[Tuple[int, int]]) -> Tuple[int, int]:
        min_distance = 10000
        closest_asteroid = None
        for asteroid in asteroids:
            d = self.distance_between(giant_laser, asteroid)
            if d < min_distance:
                min_distance = d
                closest_asteroid = asteroid
        asteroids.remove(closest_asteroid)
        return closest_asteroid

    @staticmethod
    def distance_between(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])


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
    station, count = starfield.best_location()
    print(count)
    asteroid = list(starfield.destroy(station, 200))[-1]
    print(asteroid[0] * 100 + asteroid[1])


if __name__ == '__main__':
    main()
