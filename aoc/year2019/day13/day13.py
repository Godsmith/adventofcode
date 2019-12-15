from collections import defaultdict
from typing import List

from aocd import data

from aoc.utils import ints
from aoc.year2019.intcode import Intcode


class Screen:
    TILES = {0: " ", 1: "|", 2: "#", 3: "-", 4: "o"}
    MAX_X = 43
    MAX_Y = 19

    def __init__(self, instructions: List[int]):
        self._screen = defaultdict(lambda: 0)
        self._intcode = Intcode(instructions)

    def __str__(self):
        for y in range(self.MAX_Y + 1):
            for x in range(self.MAX_X + 1):
                print(self.TILES[self._screen[(x, y)]], end="")
            print()

    def input(self, input_=None):
        while True:
            x = self._intcode.next_output(input_)
            if x is None:
                break
            y = self._intcode.next_output()
            tile = self._intcode.next_output()
            self._screen[(x, y)] = tile

    def block_count(self):
        return len([tile for tile in self._screen.values() if tile == 2])


def main():
    screen = Screen(ints(data))
    screen.input()
    print(screen.block_count())

    play_for_free_data = list(ints(data))
    play_for_free_data[0] = 2


if __name__ == '__main__':
    main()
