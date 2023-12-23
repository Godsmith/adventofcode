from aocd import data
from aoc.utils import rows, ints
import more_itertools

histories = [ints(row) for row in rows(data)]


def differences(sequence: list[int]):
    return [b - a for a, b in more_itertools.pairwise(sequence)]


def get_next_value(history: list[int]):
    sequences_of_differences = [history]
    while any(i != 0 for i in sequences_of_differences[-1]):
        sequences_of_differences.append(differences(sequences_of_differences[-1]))
    print(sequences_of_differences)
    sequences_of_differences[-1].append(0)
    for i in range(len(sequences_of_differences) - 2, -1, -1):
        delta = sequences_of_differences[i + 1][-1]
        last_in_current_sequence = sequences_of_differences[i][-1]
        sequences_of_differences[i].append(last_in_current_sequence + delta)
    print(sequences_of_differences)
    return sequences_of_differences[0][-1]


# print(get_next_value([0, 3, 6, 9, 12, 15]))

print(sum(get_next_value(history) for history in histories))
