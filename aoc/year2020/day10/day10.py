from aocd import data
from aoc.utils import ints
from collections import Counter


# Part 1

def diffs(numbers):
    for i, n in enumerate(numbers[1:], 1):
        yield n - numbers[i - 1]


adapters = sorted(ints(data))
joltages = [0] + adapters + [max(adapters) + 3]
counter = Counter(diffs(joltages))

print(counter[1] * counter[3])

# Part 2

def count_arrangements(start, stop):
    count = 0
    for next_step in {start + 1, start + 2, start + 3} & set(joltages):
        if next_step == stop:
            count += 1
        elif next_step < stop:
            count += count_arrangements(next_step, stop)
    return count


nodes = [0] + [joltage for joltage in joltages if
               joltage >= 3 and
               joltage - 2 not in joltages and
               joltage - 1 not in joltages]

times = 1
for i, node in enumerate(nodes[1:], 1):
    times *= count_arrangements(nodes[i - 1], node)

print(times)
