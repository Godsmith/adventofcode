import re
from aocd import data
from aoc.utils import rows
import itertools
import tqdm

lines = rows(data)


def get_sizes(conditions: str) -> list[int]:
    return [len(match) for match in re.findall("#+", conditions)]


def all_variant_conditions(condition_list: str) -> list[str]:
    question_mark_count = condition_list.count("?")
    variants = []
    for characters in itertools.product(".#", repeat=question_mark_count):
        new_conditions = condition_list
        for char in characters:
            new_conditions = new_conditions.replace("?", char, 1)
        variants.append(new_conditions)
    return variants


count_sum = 0
for line in tqdm.tqdm(lines):
    condition_list, records = line.split()
    sizes = [int(record) for record in records.split(",")]
    count_sum += sum(
        get_sizes(condition_list) == sizes
        for condition_list in all_variant_conditions(condition_list)
    )

print(count_sum)
