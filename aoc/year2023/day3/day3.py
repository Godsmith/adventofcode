from dataclasses import dataclass
import itertools
from aocd import data
from aoc.utils import character_lists

schematic: list[list[str]] = character_lists(data)

def get_character(row_nr: int, column_nr: int) -> str:
    if row_nr >= len(schematic) or row_nr < 0 or column_nr < 0 or column_nr >= len(schematic[0]):
        return "."
    return schematic[row_nr][column_nr]

@dataclass
class Number:
    number: int
    row: int
    start_column: int
    stop_column: int

    def is_part_number(self):
        for other_row_nr, other_column_nr in itertools.product(range(self.row -1, self.row + 2), range(self.start_column -1, self.stop_column + 2)):
            c = get_character(other_row_nr, other_column_nr)
            if c != "." and not c.isnumeric():
                return True
        return False

    def is_adjacent_to(self, row_nr: int, column_nr: int):
        return row_nr in range(self.row - 1, self.row + 2) and column_nr in range(self.start_column - 1, self.stop_column + 2)



digits = []
start_column = 0
collecting = False
numbers: list[Number] = []
for row_nr, row in enumerate(schematic):
    for column_nr, character in enumerate(row):
        if collecting is False:
            if character.isnumeric():
                collecting = True
                start_column = column_nr
        if collecting:
            if character.isnumeric():
                digits.append(character)
            else:
                numbers.append(Number(int(''.join(digits)), row_nr, start_column, column_nr - 1))
                digits = []
                collecting = False
    if collecting:
        numbers.append(Number(int(''.join(digits)), row_nr, start_column, len(schematic[0]) - 1))
        digits = []
        collecting = False

print(sum(number.number for number in numbers if number.is_part_number()))

# Part 2

gear_ratio_sum = 0
for row_nr, row in enumerate(schematic):
    for column_nr, character in enumerate(row):
        if character == "*":
            adjacent_numbers = [number for number in numbers if number.is_adjacent_to(row_nr, column_nr)]
            if len(adjacent_numbers) == 2:
                gear_ratio_sum += adjacent_numbers[0].number * adjacent_numbers[1].number
                
print(gear_ratio_sum)
