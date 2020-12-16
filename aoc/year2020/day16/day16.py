from math import prod
from typing import Dict, Set

from aocd import data
import re

from aoc.utils import rows


def get_legal_numbers():
    for row in rows(data):
        if ranges := re.findall(r"(\d*)-(\d*)", row):
            for start, stop in ranges:
                yield from range(int(start), int(stop) + 1)


def get_tickets():
    return [list(map(int, row.split(","))) for row in rows(data) if "," in row]


def get_illegal_numbers():
    return [number for ticket in tickets[1:] for number in ticket if
            number not in legal_numbers]


def is_legal(ticket):
    return all(number in legal_numbers for number in ticket)


def get_permitted_numbers_from_field_name(lines):
    permitted_numbers_from_field_name = {}
    for row in lines:
        if matches := re.findall(r"(.*): (\d*)-(\d*) or (\d*)-(\d*)", row):
            for field_name, start1, stop1, start2, stop2 in matches:
                permitted_numbers_from_field_name[field_name] = (
                        set(range(int(start1), int(stop1) + 1)) |
                        set(range(int(start2), int(stop2) + 1)))
    return permitted_numbers_from_field_name


def get_possible_field_names_from_position(permitted_numbers_from_field_name,
                                           tickets) -> Dict[int, Set[str]]:
    possible_field_names_from_position = {
        i: set(permitted_numbers_from_field_name.keys())
        for i in range(len(tickets[0]))}

    for ticket in tickets:
        for i, number in enumerate(ticket):
            for field_name in permitted_numbers_from_field_name:
                if number not in permitted_numbers_from_field_name[field_name]:
                    possible_field_names_from_position[i].discard(field_name)
    return possible_field_names_from_position


def get_field_name_from_position(possible_field_names_from_position) -> Dict[int, str]:
    field_name_from_position = {}
    while len(field_name_from_position) < len(tickets[0]):
        for position, field_names in possible_field_names_from_position.items():
            if len(field_names) == 1:
                field_name = list(field_names)[0]
                field_name_from_position[position] = field_name
                for position in possible_field_names_from_position:
                    possible_field_names_from_position[position].discard(field_name)
    return field_name_from_position


# Part 1

legal_numbers = set(get_legal_numbers())
tickets = list(get_tickets())
print(sum(get_illegal_numbers()))

# Part 2

permitted_numbers_from_field_name = get_permitted_numbers_from_field_name(rows(data))
legal_tickets = list(filter(is_legal, tickets))
possible_field_names_from_position = get_possible_field_names_from_position(
    permitted_numbers_from_field_name,
    legal_tickets)
field_name_from_position = get_field_name_from_position(
    possible_field_names_from_position)

print(prod(tickets[0][index] for index, field in field_name_from_position.items()
           if field.startswith("departure")))
