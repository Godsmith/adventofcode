from collections import Counter, defaultdict
from aocd import data
from aoc.utils import ints


def solve(days):
    counter = Counter(ints(data))
    for generation in range(days):
        new_counter = defaultdict(lambda: 0)
        for value, count in counter.items():
            if value == 0:
                new_counter[8] += count
                new_counter[6] += count
            else:
                new_counter[value - 1] += count
        counter = new_counter
    return sum(counter.values())


print(solve(80))
print(solve(256))
