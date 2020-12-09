from aocd import data
from aoc.utils import ints
from itertools import combinations

numbers = ints(data)


def get_first_invalid_number():
    for i in range(25, len(numbers)):
        previous_numbers = numbers[i - 25:i]
        previous_sums = set(map(sum, (combination for combination in
                                      combinations(previous_numbers, 2))))
        if numbers[i] not in previous_sums:
            return numbers[i]


def get_weakness(invalid_number):
    for i, _ in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            contiguous_range = numbers[i:j + 1]
            if sum(contiguous_range) == invalid_number:
                return min(contiguous_range) + max(contiguous_range)


print(invalid_number := get_first_invalid_number())
print(get_weakness(invalid_number))
