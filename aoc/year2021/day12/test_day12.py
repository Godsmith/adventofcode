from aoc.year2021.day12.day12 import count_paths

def test_first_2():
    data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
    assert count_paths(data, 2) == 36

def test_slightly_larger_1():
    data = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
    assert count_paths(data, 1) == 19

def test_slightly_larger_2():
    data = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
    assert count_paths(data, 2) == 103
