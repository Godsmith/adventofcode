from collections import Counter, defaultdict

from aocd import data
from copy import deepcopy
from aoc.utils import rows


def run(lines):
    acc = 0
    row = 0
    visited = set()
    while row < len(lines):
        if row in visited:
            return acc, 1
        visited.add(row)

        instruction, value = lines[row].split()
        if instruction == "acc":
            acc += int(value)
        elif instruction == "jmp":
            row += int(value) - 1

        row += 1

    return acc, 0


print(run(rows(data))[0])

for i, line in enumerate(rows(data)):
    new_lines = deepcopy(rows(data))
    if "nop" in line:
        new_lines[i] = line.replace("nop", "jmp")
    elif "jmp" in line:
        new_lines[i] = line.replace("jmp", "nop")

    acc, return_code = run(new_lines)

    if return_code == 0:
        print(acc)
        break
