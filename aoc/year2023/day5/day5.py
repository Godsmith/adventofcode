from aocd import data
import attr
from aoc.utils import rows

paragraphs = data.split("\n\n")

@attr.define
class Range:
    dest_start: int
    source_start: int
    length: int


class Map:
    def __init__(self, paragraph) -> None:
        self.ranges = [Range(*map(int, row.split())) for row in rows(paragraph)[1:]]

    def __repr__(self):
        return repr(self.ranges)

    def convert(self, number: int) -> int:
        for range in self.ranges:
            if range.source_start <= number < range.source_start + range.length:
                return number - range.source_start + range.dest_start
        return number
    

maps = [Map(paragraph) for paragraph in paragraphs[1:]]
print(maps[0])

seeds = list(map(int, paragraphs[0].split(" ")[1:]))

results = []
for seed in seeds:
    value = seed
    for map_ in maps:
        value = map_.convert(value)
    results.append(value)

print(min(results))


