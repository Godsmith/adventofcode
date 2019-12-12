from math import pi

from aoc.year2019.day10.day10 import Starfield


def test_detected_count():
    s = """.#..#
.....
#####
....#
...##"""
    starfield = Starfield(s)
    assert starfield.detected_count(3, 4) == 8


def test_detected_count2():
    s = """.#..#
.....
#####
....#
...##"""
    starfield = Starfield(s)
    assert starfield.detected_count(4, 0) == 7


def test_best_location():
    s = """.#..#
.....
#####
....#
...##"""
    starfield = Starfield(s)
    assert starfield.best_location() == ((3, 4), 8)


def test_best_location2():
    s = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""
    starfield = Starfield(s)
    assert starfield.best_location() == ((11, 13), 210)


class TestAngleTo:
    def test_n(self):
        assert Starfield.angle_to((0, 0), (0, -1)) == 0

    def test_ne(self):
        assert Starfield.angle_to((0, 0), (1, -1)) == pi / 4

    def test_e(self):
        assert Starfield.angle_to((0, 0), (1, 0)) == pi / 2

    def test_se(self):
        assert Starfield.angle_to((0, 0), (1, 1)) == pi / 2 + pi / 4

    def test_s(self):
        assert Starfield.angle_to((0, 0), (0, 1)) == pi

    def test_sw(self):
        assert Starfield.angle_to((0, 0), (-1, 1)) == pi + pi / 4

    def test_nw(self):
        assert Starfield.angle_to((0, 0), (-1, -1)) == 1.75 * pi


class TestDestroy:
    s = """.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....#...###..
..#.#.....#....##"""

    def test_destroy_one(self):
        starfield = Starfield(self.s)
        assert list(starfield.destroy((8, 3), 1)) == [(8, 1)]


class TestDestroyLarge:
    s = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""

    def test_destroy(self):
        starfield = Starfield(self.s)
        assert list(starfield.destroy((11, 13), 1))[-1] == (11, 12)
        assert list(starfield.destroy((11, 13), 200))[-1] == (8, 2)
