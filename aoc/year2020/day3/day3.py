from aocd import data
from aoc.utils import rows

grid = rows(data)


def hit_trees(column_step, row_step):
    row = 0
    column = 0
    trees = 0
    while row < len(grid):
        if grid[row][column % len(grid[0])] == "#":
            trees += 1
        row += row_step
        column += column_step
    return trees


print(hit_trees(3, 1))
print(
    hit_trees(1, 1) * hit_trees(3, 1) * hit_trees(5, 1) * hit_trees(7, 1) * hit_trees(1,
                                                                                      2))
