from aocd import data
from aoc.utils import rows

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def calibration_number(row: str) -> int:
    digits = []
    for i, c in enumerate(row):
        if c.isnumeric():
            digits.append(int(c))
        else:
            for j, number in enumerate(numbers, 1):
                if row[i:].startswith(number):
                    digits.append(j)

    return int(digits[0]) * 10 + int(digits[-1])

print(sum(calibration_number(row) for row in rows(data)))
