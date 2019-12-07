from aoc.year2019.intcode import Intcode
from aoc.utils import ints

def output(program, phase_settings):
    intcode = Intcode(program)
    signal = 0
    for phase_setting in phase_settings:
        signal = intcode.run([phase_setting, signal]).output
    return signal


def main():
    pass


if __name__ == '__main__':
    main()