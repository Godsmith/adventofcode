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
# lists = """.F----7F7F7F7F-7....
# .|F--7||||||||FJ....
# .||.FJ||||||||L7....
# FJL7L7LJLJ||LJ.L-7..
# L--J.L7...LJS7F-7L7.
# ....F-J..F7FJ|L7L7L7
# ....L7.F7||L7|.L7L7|
# .....|FJLJ|FJ|F7|.LJ
# ....FJL-7.||.||||...
# ....L---J.LJ.LJLJ...""".split(
#     "\n"
# )

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

# Part 1
# print(len(loop_positions) / 2)

# Part 2

# Print loop
for y, row in enumerate(lists):
    for x, character in enumerate(row):
        if (x, y) in loop_positions:
            print(character, end="")
        else:
            print(" ", end="")

    print()

new_grid = {}
for x, y in grid.keys():
    new_grid[2 * x, 2 * y] = grid[x, y]

new_neighbors = dict()
for (x, y), neighboring_positions in neighbors.items():
    new_neighbors[2 * x, 2 * y] = {
        (2 * x1, 2 * y1) for (x1, y1) in neighboring_positions
    }

new_loop_positions = {(2 * x, 2 * y) for x, y in loop_positions}

# Fill in loop positions and grid
max_x = max(x for x, _ in new_grid.keys())
max_y = max(y for _, y in new_grid.keys())
for y in range(max_y + 1):
    for x in range(max_x + 1):
        added = False
        if (
            (x - 1, y) in new_loop_positions
            and (x + 1, y) in new_loop_positions
            and (x + 1, y) in new_neighbors[(x - 1, y)]
        ):
            new_grid[x, y] = "-"
            added = True
        elif (
            (x, y - 1) in new_loop_positions
            and (x, y + 1) in new_loop_positions
            and (x, y + 1) in new_neighbors[(x, y - 1)]
        ):
            new_grid[x, y] = "|"
            added = True
        if added:
            new_loop_positions.add((x, y))


def print_grid(grid: dict):
    max_x = max(x for x, _ in grid.keys())
    max_y = max(y for _, y in grid.keys())

    # Print loop
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in grid:
                print(grid[x, y], end="")
            else:
                print(" ", end="")

        print()


# print_grid(grid)
# print_grid(new_grid)

all_positions = {(x, y) for x in range(max_x + 1) for y in range(max_y + 1)}


def neighboring_nonloop_positions(x: int, y: int) -> set[tuple[int, int]]:
    return (
        {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)} - new_loop_positions
    ).intersection(all_positions)


def all_connected_positions(x: int, y: int):
    connected_positions = {(x, y)}
    next_positions = neighboring_nonloop_positions(x, y)
    while next_positions:
        current_position = next_positions.pop()
        connected_positions.add(current_position)
        next_positions.update(
            neighboring_nonloop_positions(*current_position) - connected_positions
        )
    return connected_positions


chunks = []
nonloop_positions_left = all_positions - new_loop_positions
while nonloop_positions_left:
    current_position = nonloop_positions_left.pop()
    chunk = all_connected_positions(*current_position)
    chunks.append(chunk)
    nonloop_positions_left -= chunk


def is_chunk_on_edge(chunk: set[tuple[int, int]]):
    for x, y in chunk:
        if x in (0, max_x):
            return True
        if y in (0, max_y):
            return True
    return False


# Print loop
# for y in range(max_y + 1):
#     for x in range(max_x + 1):
#         if (x, y) in new_loop_positions:
#             print(new_grid[x, y], end="")
#         elif (x, y) in enclosed:
#             print("O", end="")
#         else:
#             print(" ", end="")

#     print()
enclosed = set()
for chunk in chunks:
    if not is_chunk_on_edge(chunk):
        enclosed.update(chunk)
print(len([(x, y) for (x, y) in enclosed if x % 2 == 0 and y % 2 == 0]))
