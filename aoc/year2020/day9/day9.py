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
    start = 0
    stop = 2
    while (
            sum_ := sum(consecutive_numbers := numbers[start:stop + 1])
    ) != invalid_number:
        if sum_ < invalid_number:
            stop += 1
        elif sum_ > invalid_number:
            start += 1
    return min(consecutive_numbers) + max(consecutive_numbers)


print(invalid_number := get_first_invalid_number())
print(get_weakness(invalid_number))
