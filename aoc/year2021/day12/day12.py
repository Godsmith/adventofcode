from collections import defaultdict, Counter
from typing import Set, Dict

from aocd import get_data

from aoc.utils import rows


def visit(connections: Dict[str, Set[str]], room_limit: int, room_counter: Counter[str, int], current_room: str):
    if current_room == "end":
        return 1
    new_room_counter = Counter(room_counter) + Counter({current_room: 1})
    new_lowercase_room_counter = {room: count for room, count in new_room_counter.items() if room == room.lower()}
    disallowed_rooms = {'start'} | set(new_lowercase_room_counter.keys()) if max(
        new_lowercase_room_counter.values()) == room_limit else set()
    possible_next_rooms = {room for room in connections[current_room]} - disallowed_rooms
    return sum(visit(connections, room_limit, new_room_counter, room) for room in possible_next_rooms)


def count_paths(data: str, room_limit: int):
    connections = defaultdict(set)
    for room1, room2 in [row.split("-") for row in rows(data)]:
        connections[room1].add(room2)
        connections[room2].add(room1)
    return visit(connections, room_limit, Counter(), "start")


print(count_paths(get_data(year=2021, day=12), 1))
print(count_paths(get_data(year=2021, day=12), 2))
