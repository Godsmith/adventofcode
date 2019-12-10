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
