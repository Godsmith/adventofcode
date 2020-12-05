from aoc.utils import rows
from aocd import data


def boarding_pass_id(boarding_pass):
    binary = boarding_pass.replace('F', '0'). \
        replace('B', '1').replace('L', '0').replace('R', '1')
    row = int(binary[:7], 2)
    column = int(binary[7:], 2)
    return row * 8 + column


ids = set(boarding_pass_id(boarding_pass) for boarding_pass in rows(data))

print(max(ids))

for i in range(max(ids)):
    if i not in ids and i - 1 in ids and i + 1 in ids:
        print(i)
