from collections import defaultdict
from typing import Set

from aocd import get_data

from aoc.utils import rows

connections = defaultdict(set)
for room1, room2 in [row.split("-") for row in rows(get_data(year=2021, day=12))]:
    connections[room1].add(room2)
    connections[room2].add(room1)


def visit(current_room: str, previous_rooms: Set[str]):
    if current_room == "end":
        return 1
    possible_next_rooms = {room for room in connections[current_room] if
                           room == room.upper() or room not in previous_rooms}
    path_sum = 0
    for next_room in possible_next_rooms:
        path_sum += visit(next_room, previous_rooms | {current_room})
    return path_sum

print(visit("start", set()))
