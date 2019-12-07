from aoc.utils import ints

from aoc.year2019.day7.day7 import output


def test_output():
    program = ints('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0')
    phase_settings = (4, 3, 2, 1, 0)
    assert output(program, phase_settings) == 43210
