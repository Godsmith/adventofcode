from aoc.year2019.day6.day6 import create_planets, distance_between


def test_distance():
    data = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""

    planets = create_planets(data)
    assert distance_between(planets, 'YOU', 'SAN') == 4

