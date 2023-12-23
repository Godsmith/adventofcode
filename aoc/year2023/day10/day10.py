from collections import defaultdict
from aocd import data
from aoc.utils import character_lists

lists = character_lists(data)

grid = {}
for y, row in enumerate(lists):
    for x, character in enumerate(row):
        grid[x, y] = character

neighbor_deltas_from_character = {
    "F": [(0, 1), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "7": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "-": [(-1, 0), (1, 0)],
    "|": [(0, -1), (0, 1)],
}


s_position = (-1, -1)
neighbors = defaultdict(set)
for (x, y), char in grid.items():
    if char in neighbor_deltas_from_character:
        for dx, dy in neighbor_deltas_from_character[char]:
            neighbors[x, y].add((x + dx, y + dy))
    elif char == "S":
        s_position = (x, y)
for (neighbor_x, neighbor_y), neighbor_neighbors in list(neighbors.items()):
    if s_position in neighbor_neighbors:
        neighbors[s_position].add((neighbor_x, neighbor_y))

visited_positions = {s_position}
next_possible_positions = set(neighbors[s_position])
while next_possible_positions:
    current_position = next_possible_positions.pop()
    visited_positions.add(current_position)
    next_possible_positions.update(neighbors[current_position] - visited_positions)

print(len(visited_positions) / 2)
