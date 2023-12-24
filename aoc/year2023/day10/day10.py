from collections import defaultdict
from aocd import data
from aoc.utils import character_lists

lists = character_lists(data)
# lists = """...........
# .S-------7.
# .|F-----7|.
# .||.....||.
# .||.....||.
# .|L-7.F-J|.
# .|..|.|..|.
# .L--J.L--J.
# ...........""".split(
#     "\n"
# )
lists = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...""".split(
    "\n"
)

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

loop_positions = {s_position}
next_possible_positions = set(neighbors[s_position])
while next_possible_positions:
    current_position = next_possible_positions.pop()
    loop_positions.add(current_position)
    next_possible_positions.update(neighbors[current_position] - loop_positions)

print(len(loop_positions) / 2)


# Part 2


# Did not work; captured parts outside the loop that were not connected to the edge

# def neighboring_nonloop_positions(x: int, y: int) -> set[tuple[int, int]]:
#     return (
#         {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)} - loop_positions
#     ).intersection(grid.keys())


# def all_connected_positions(x: int, y: int):
#     connected_positions = {(x, y)}
#     next_positions = neighboring_nonloop_positions(x, y)
#     while next_positions:
#         current_position = next_positions.pop()
#         connected_positions.add(current_position)
#         next_positions.update(
#             neighboring_nonloop_positions(*current_position) - connected_positions
#         )
#     return connected_positions


# chunks = []
# nonloop_positions_left = set(grid.keys()) - loop_positions
# while nonloop_positions_left:
#     current_position = nonloop_positions_left.pop()
#     chunk = all_connected_positions(*current_position)
#     chunks.append(chunk)
#     nonloop_positions_left -= chunk

# last_row = len(lists) - 1
# last_column = len(lists[0]) - 1


# def is_chunk_on_edge(chunk: set[tuple[int, int]]):
#     for x, y in chunk:
#         if x in (0, last_column):
#             return True
#         if y in (0, last_row):
#             return True
#     return False


# enclosed = set()
# for chunk in chunks:
#     if not is_chunk_on_edge(chunk):
#         enclosed.update(chunk)
# print(len(enclosed))

# for y, row in enumerate(lists):
#     for x, character in enumerate(row):
#         if (x, y) in enclosed:
#             print("x", end="")
#         else:
#             print(character, end="")
#     print()
