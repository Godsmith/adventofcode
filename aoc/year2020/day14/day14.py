from itertools import product
from typing import Dict, Callable

from aocd import data
from aoc.utils import rows
import re


def apply_mask(mask: str, value: int, address: int) -> Dict[int, int]:
    binary_value = f"{value:b}".rjust(len(mask), "0")
    masked_binary_value = list(binary_value)
    for i, _ in enumerate(binary_value):
        if mask[i] != "X":
            masked_binary_value[i] = mask[i]
    return {address: int(''.join(masked_binary_value), 2)}


def apply_mask2(mask: str, value: int, address: int) -> Dict[int, int]:
    binary_address = f"{address:b}".rjust(len(mask), "0")
    masked_binary_address = list(binary_address)
    out = {}
    for x_value_list in product([0, 1], repeat=mask.count("X")):
        x_value_generator = iter(x_value_list)
        for i, _ in enumerate(binary_address):
            if mask[i] == "0":
                masked_binary_address[i] = binary_address[i]
            elif mask[i] == "1":
                masked_binary_address[i] = "1"
            elif mask[i] == "X":
                masked_binary_address[i] = str(next(x_value_generator))
        new_address = int(''.join(masked_binary_address), 2)
        out[new_address] = value
    return out


def run(apply_mask: Callable[[str, int, int], Dict[int, int]]):
    mask = None
    mem = {}
    for row in rows(data):
        if groups := re.findall("mask = (.*)", row):
            mask = groups[0]
        elif groups := re.findall("mem\[(.*)\] = (.*)", row):
            address, value = groups[0]
            mem = mem | apply_mask(mask, int(value), int(address))

    return sum(mem.values())


print(run(apply_mask))
print(run(apply_mask2))
