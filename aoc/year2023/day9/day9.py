from collections import deque
from aocd import data
from aoc.utils import rows, ints
import more_itertools

histories = [deque(ints(row)) for row in rows(data)]


def differences(sequence: deque[int]):
    return deque(b - a for a, b in more_itertools.pairwise(sequence))


def get_sequences_of_differences(history: deque[int]):
    sequences_of_differences = [history]
    while any(i != 0 for i in sequences_of_differences[-1]):
        sequences_of_differences.append(differences(sequences_of_differences[-1]))
    sequences_of_differences[-1].append(0)
    return sequences_of_differences


def get_next_value(history: deque[int]):
    sequences_of_differences = get_sequences_of_differences(history)
    for i in range(len(sequences_of_differences) - 2, -1, -1):
        delta = sequences_of_differences[i + 1][-1]
        last_in_current_sequence = sequences_of_differences[i][-1]
        sequences_of_differences[i].append(last_in_current_sequence + delta)
    return sequences_of_differences[0][-1]


def get_previous_value(history: deque[int]):
    sequences_of_differences = get_sequences_of_differences(history)
    for i in range(len(sequences_of_differences) - 2, -1, -1):
        delta = sequences_of_differences[i + 1][0]
        first_in_current_sequence = sequences_of_differences[i][0]
        sequences_of_differences[i].appendleft(first_in_current_sequence - delta)
    return sequences_of_differences[0][0]


# print(get_next_value([0, 3, 6, 9, 12, 15]))

print(sum(get_next_value(history) for history in histories))


print(sum(get_previous_value(history) for history in histories))
# print(get_previous_value(deque([0, 3, 6, 9, 12, 15])))
