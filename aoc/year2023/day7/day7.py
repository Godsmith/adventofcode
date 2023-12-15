from aocd import data
from aoc.utils import rows
from collections import Counter

hands = [row.split(" ")[0] for row in rows(data)]
bids = [row.split(" ")[1] for row in rows(data)]


def get_type(hand: str):
    if len(set(hand)) == 1:
        return 7
    elif len(set(hand)) == 2:
        return 6
    counter = Counter(hand)
    values = sorted(counter.values())
    if set(sorted(values)) == {2, 3}:
        return 5
    elif any(value == 3 for value in values):
        return 4
