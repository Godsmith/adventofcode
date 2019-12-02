from aocd import data

from aoc.utils import ints
from aoc.year2019.intcode import Intcode


def main():
    # part 1
    p = Intcode(ints(data))
    p[1] = 12
    p[2] = 2
    p.run()
    print(p[0])

    # part2
    for noun in range(0, 100):
        for verb in range(0, 100):
            p = Intcode(ints(data))
            p[1] = noun
            p[2] = verb
            if p.run()[0] == 19690720:
                print(100 * noun + verb)
                return


if __name__ == '__main__':
    main()