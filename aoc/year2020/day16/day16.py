from collections import defaultdict
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
    for row in rows(data):
        if "," in row:
            yield list(map(int, row.split(",")))


def get_illegal_numbers():
    for ticket in tickets[1:]:
        for number in ticket:
            if number not in legal_numbers:
                yield number


def is_legal(ticket):
    for number in ticket:
        if number not in legal_numbers:
            return False
    return True


def get_fields(lines):
    fields = {}
    for row in lines:
        if matches := re.findall(r"(.*): (\d*)-(\d*) or (\d*)-(\d*)", row):
            for field_name, start1, stop1, start2, stop2 in matches:
                fields[field_name] = set(range(int(start1), int(stop1) + 1))
                fields[field_name].update(range(int(start2), int(stop2) + 1))
    return fields


def get_possible_field_names_from_position(fields, tickets) -> Dict[int, Set[str]]:
    possible_field_names_from_position = defaultdict(set)
    for field_name in fields:
        for i, _ in enumerate(tickets[0]):
            possible_field_names_from_position[i].add(field_name)

    for ticket in tickets:
        for i, number in enumerate(ticket):
            for field_name in fields:
                if number not in fields[field_name]:
                    if field_name in possible_field_names_from_position[i]:
                        possible_field_names_from_position[i].remove(field_name)
    return possible_field_names_from_position


def get_field_name_from_position(possible_field_names_from_position) -> Dict[int, str]:
    field_name_from_position = {}
    while len(field_name_from_position) < len(tickets[0]):
        for position, field_names in possible_field_names_from_position.items():
            if len(field_names) == 1:
                field_name = list(field_names)[0]
                field_name_from_position[position] = field_name
                for position in possible_field_names_from_position:
                    if field_name in possible_field_names_from_position[position]:
                        possible_field_names_from_position[position].remove(field_name)
    return field_name_from_position


# Part 1

legal_numbers = set(get_legal_numbers())
tickets = list(get_tickets())
print(sum(get_illegal_numbers()))

# Part 2

fields = get_fields(rows(data))
legal_tickets = list(filter(is_legal, tickets))
possible_field_names_from_position = get_possible_field_names_from_position(fields, legal_tickets)
field_name_from_position = get_field_name_from_position(possible_field_names_from_position)

print(prod(tickets[0][index] for index, field in field_name_from_position.items()
           if field.startswith("departure")))
