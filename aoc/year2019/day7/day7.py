from aocd import data
from itertools import permutations

from aoc.utils import ints
from aoc.year2019.intcode import Intcode

def output(program, phase_settings):
    intcode = Intcode(program)
    signal = 0
    for phase_setting in phase_settings:
        signal = intcode.run([phase_setting, signal])
    return signal

def find_max_output(program):
    max_output = 0
    all_phase_settings = permutations((0,1,2,3,4))
    for phase_settings in all_phase_settings:
        max_output = max(max_output, output(program, phase_settings))
    return max_output


def main():
    print(find_max_output(ints(data)))


if __name__ == '__main__':
    main()