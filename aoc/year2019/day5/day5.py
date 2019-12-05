from aocd import data
from aoc.utils import ints

from aoc.year2019.intcode import Intcode


def main():
    p = Intcode(ints(data), 1)
    print(p.run().output)

    p = Intcode(ints(data), 5)
    print(p.run().output)


if __name__ == '__main__':
    main()
