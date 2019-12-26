from typing import Tuple, List, Dict


class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return f"Node<{self.position}>"


def astar_tuples(tuples: Dict[Tuple[int, int], str], start, end,
                 wall_tiles: List[str],
                 floor_tiles: List[str], adjacent=None):
    """Here, tuples is a dictionary (x, y) -> z instead, where the values
    of z is determined by wall and floor.
    """
    DICT = {}
    for wall_tile in wall_tiles:
        DICT[wall_tile] = 1
    for floor_tile in floor_tiles:
        DICT[floor_tile] = 0
    xs = [position[0] for position in tuples]
    ys = [position[1] for position in tuples]
    rows = []
    for y in range(min(ys), max(ys) + 1):
        row = []
        for x in range(min(xs), max(xs) + 1):
            if (x, y) not in tuples:
                row.append(1)
            else:
                row.append(DICT[tuples[(x, y)]])
        rows.append(row)

    translated_start = (start[0] - min(xs), start[1] - min(ys))
    translated_end = (end[0] - min(xs), end[1] - min(ys))
    return astar(rows, translated_start, translated_end, adjacent)


def astar(maze: List[List[int]], start: Tuple[int, int], end: Tuple[int, int],
          adjacent=None):
    """Returns a list of tuples as a path from the given start to the given end in the given maze
    In maze, 0 is open space, 1 is wall.
    """
    if maze[end[1]][end[0]] != 0:
        raise ValueError("End in wall!")

    if adjacent is None:
        adjacent = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1),
                    (1, -1), (1, 1)]
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        for new_position in adjacent:  # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0],
                             current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or \
                    node_position[1] > (len(maze[len(maze) - 1]) - 1) or \
                    node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[1]][node_position[0]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if child in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                    (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if is_child_with_higher_g_on_open_list(child, open_list):
                continue

            # Add the child to the open list
            open_list.append(child)

def is_child_with_higher_g_on_open_list(child, open_list):
    for open_node in open_list:
        if child == open_node and child.g > open_node.g:
            return True
    return False
