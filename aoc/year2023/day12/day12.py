from functools import cache
from typing import Iterable
from aocd import data
from aoc.utils import rows


def record_starts_with_group_of_size(record: str, size: int):
    if len(record) < size:
        return False
    starting_string = record[:size]
    return (size == len(record) or record[size] in (".", "?")) and all(
        c in ["#", "?"] for c in starting_string
    )


@cache
def count_variants(record: str, sizes: tuple):
    if not sizes:
        return 0 if "#" in record else 1
    if not record:
        return 0
    count = 0
    if record_starts_with_group_of_size(record, sizes[0]):
        count += count_variants(record[sizes[0] + 1 :], sizes[1:])
    if record[0] != "#":
        count += count_variants(record[1:], sizes)
    return count


def unfold(record: str, sizes: tuple) -> tuple[str, tuple]:
    return "?".join([record] * 5), sizes * 5


lines = rows(data)
record_and_sizes = []
for line in lines:
    record, size_strings = line.split()
    sizes = tuple(int(size_string) for size_string in size_strings.split(","))
    record_and_sizes.append((record, sizes))

print(sum(count_variants(record, sizes) for record, sizes in record_and_sizes))

unfolded_records_and_sizes = [
    unfold(record, sizes) for record, sizes in record_and_sizes
]
print(
    sum(count_variants(record, sizes) for record, sizes in unfolded_records_and_sizes)
)
