from aoc.year2021.day15.day15 import step, Cavern


def test_step():
    data = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
    cavern = Cavern(data)
    assert step(cavern, 0, 0, 0, set()) == 40