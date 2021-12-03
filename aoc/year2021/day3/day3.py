from collections import Counter
from typing import Callable, List, Iterable

from aocd import data
from aoc.utils import rows

strings = rows(data)

# Part 1


final = []
for position in zip(*strings):
    final.append(Counter(position).most_common()[0][0])
final = ''.join(final)
inverse = final.replace("1", "2").replace("0", "1").replace("2", "0")
print(int(final, 2) * int(inverse, 2))


# Part 2

def most_common_bit(bits: Iterable[str]):
    counter_result = Counter(bits).most_common()
    if len(counter_result) == 1:
        return counter_result[0][0]
    if counter_result[0][1] == counter_result[1][1]:
        return "1"
    return counter_result[0][0]


def least_common_bit(bits: Iterable[str]):
    return "0" if most_common_bit(bits) == "1" else "1"


def get_rating(common_bit_function: Callable[[Iterable[str]], str], strings: List[str]):
    remaining_strings = set(strings)
    for i, _ in enumerate(strings[0]):
        bits_in_position = list(zip(*remaining_strings))[i]
        most_common = common_bit_function(bits_in_position)
        remaining_strings = {string for string in remaining_strings if string[i] == most_common}
        if len(remaining_strings) == 1:
            break

    return int(remaining_strings.pop(), 2)


print(get_rating(most_common_bit, strings) * get_rating(least_common_bit, strings))
