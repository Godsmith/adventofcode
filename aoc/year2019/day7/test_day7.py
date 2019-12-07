from aoc.utils import ints

from aoc.year2019.day7.day7 import output, feedback_output


def test_output():
    program = ints('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0')
    phase_settings = (4, 3, 2, 1, 0)
    assert output(program, phase_settings) == 43210


def test_feedback_output():
    program = ints(
        '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5')
    phase_settings = (9, 8, 7, 6, 5)
    assert feedback_output(program, phase_settings) == 139629729
