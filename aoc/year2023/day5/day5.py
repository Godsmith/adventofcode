from collections import deque
import itertools
from typing import Iterable
from aocd import data
import attr
from aoc.utils import rows


@attr.define
class Range:
    start: int
    length: int

    @property
    def stop(self):
        """The first value the range is NOT (exclusive)"""
        return self.start + self.length

    def contains(self, number: int):
        return self.start <= number < self.start + self.length


@attr.define
class MapRange:
    dest_start: int
    source_start: int
    length: int

    @property
    def source_stop(self):
        """The first value the range is NOT (exclusive)"""
        return self.source_start + self.length

    def translate(self, range: Range):
        return Range(range.start + self.dest_start - self.source_start, range.length)


class Map:
    def __init__(self, paragraph) -> None:
        self.map_ranges = [
            MapRange(*map(int, row.split())) for row in rows(paragraph)[1:]
        ]
        self.map_ranges.sort(key=lambda map_range: map_range.source_start)

    def __repr__(self):
        return repr(self.map_ranges)

    def convert(self, number: int) -> int:
        for map_range in self.map_ranges:
            if (
                map_range.source_start
                <= number
                < map_range.source_start + map_range.length
            ):
                return number - map_range.source_start + map_range.dest_start
        return number

    def convert_ranges(self, ranges: Iterable[Range]) -> list[Range]:
        input_ranges = deque(ranges)
        output_ranges = []
        while input_ranges:
            input_range = input_ranges.popleft()
            for map_range in self.map_ranges:
                if (
                    map_range.source_start
                    <= input_range.start
                    < map_range.source_start + map_range.length
                ):
                    # Input starts inside map range
                    # Output starts at the same place as the input
                    # Output ends at the same place as the input or at the end of
                    # the map range, whichever comes first
                    output_range_start = input_range.start
                    if input_range.stop < map_range.source_stop:
                        output_range_stop = input_range.stop
                    else:
                        output_range_stop = map_range.source_stop
                        new_input_range_length = input_range.stop - output_range_stop
                        input_ranges.append(
                            Range(map_range.source_stop, new_input_range_length)
                        )
                    output_range_length = output_range_stop - output_range_start
                    output_range = Range(output_range_start, output_range_length)
                    output_ranges.append(map_range.translate(output_range))
                    break
            else:
                # Input starts outside all map ranges
                # Output starts at the same place as the input
                # Output ends at the same place as the input or the start of the first
                # map range that it overlaps, whichever comes first
                output_range_start = input_range.start
                for map_range in self.map_ranges:
                    if input_range.contains(map_range.source_start):
                        output_range_stop = map_range.source_start
                        output_range_length = output_range_stop - output_range_start
                        new_input_range_length = input_range.stop - output_range_stop
                        input_ranges.append(
                            Range(output_range_stop, new_input_range_length)
                        )
                        break
                else:
                    output_range_length = input_range.length
                output_ranges.append(Range(output_range_start, output_range_length))
        return output_ranges


def run(input_data: str):
    paragraphs = input_data.split("\n\n")

    map_ = Map(
        """blah:
    2 12 2"""
    )
    # print(map_.convert_ranges([Range(1, 5)]))

    maps = [Map(paragraph) for paragraph in paragraphs[1:]]
    # print(maps[0])

    seeds = list(map(int, paragraphs[0].split(" ")[1:]))

    def chunker(seq, size):
        return (seq[pos : pos + size] for pos in range(0, len(seq), size))

    seed_ranges = [Range(start, length) for start, length in chunker(seeds, 2)]
    seed_ranges.sort(key=lambda range_: range_.start)

    for map_ in maps:
        # print("map")
        seed_ranges = map_.convert_ranges(seed_ranges)
        print(seed_ranges)
    print(min(range_.start for range_ in seed_ranges))


run(data)

run(
    """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
)
