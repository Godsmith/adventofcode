from aocd import data
from itertools import permutations, cycle

from aoc.utils import ints
from aoc.year2019.intcode import Intcode


class Amplifier:
    def __init__(self, program, phase_setting):
        self.intcode = Intcode(program)
        self.started = False
        self.phase_setting = phase_setting

    def next_output(self, input_: int):
        if not self.started:
            self.started = True
            return self.intcode.next_output([self.phase_setting, input_])
        else:
            return self.intcode.next_output(input_)

    @property
    def finished(self):
        return self.intcode.finished


def output(program, phase_settings):
    intcode = Intcode(program)
    signal = 0
    for phase_setting in phase_settings:
        signal = intcode.run([phase_setting, signal])
    return signal


def feedback_output(program, phase_settings):
    amplifiers = [Amplifier(program, phase_setting) for phase_setting in phase_settings]
    signal = 0
    for amplifier in cycle(amplifiers):
        last_signal = signal
        signal = amplifier.next_output(signal)
        if signal is None:
            return last_signal
    return signal


def find_max_feedback_output(program):
    max_output = 0
    all_phase_settings = permutations((5, 6, 7, 8, 9))
    for phase_settings in all_phase_settings:
        max_output = max(max_output, feedback_output(program, phase_settings))
    return max_output


def find_max_output(program):
    max_output = 0
    all_phase_settings = permutations((0, 1, 2, 3, 4))
    for phase_settings in all_phase_settings:
        max_output = max(max_output, output(program, phase_settings))
    return max_output


def main():
    print(find_max_output(ints(data)))
    print(find_max_feedback_output(ints(data)))


if __name__ == '__main__':
    main()
