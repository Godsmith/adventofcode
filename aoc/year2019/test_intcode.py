from aoc.year2019.intcode import Intcode, Instruction


def test_add():
    assert Intcode([1, 2, 2, 0, 99]).run()[:] == [4, 2, 2, 0, 99]


def test_mul():
    assert Intcode([2, 0, 4, 0, 99]).run()[:] == [198, 0, 4, 0, 99]


def test_input_output():
    i = Intcode([3, 0, 4, 0, 99])
    assert i.run([42]).output == 42


def test_immediate_mode():
    i = Intcode([1002, 4, 3, 4, 33])
    assert i.run()[:] == [1002, 4, 3, 4, 99]


def test_jump_if_false():
    i = Intcode([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9])
    assert i.run(0).output == 0
    i = Intcode([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9])
    assert i.run(2).output == 1


def test_jump_if_true():
    i = Intcode([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1])
    assert i.run(0).output == 0


def test_less_than():
    i = Intcode([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8])
    assert i.run(7).output == 1
    i = Intcode([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8])
    assert i.run(8).output == 0


def test_equals():
    i = Intcode([3, 3, 1108, -1, 8, 3, 4, 3, 99])
    assert i.run(8).output == 1
    i = Intcode([3, 3, 1108, -1, 8, 3, 4, 3, 99])
    assert i.run(7).output == 0


def test_program_is_reset_between_runs():
    intcode = Intcode([1, 2, 2, 0, 99])
    assert intcode.run()[:] == [4, 2, 2, 0, 99]
    assert intcode.run()[:] == [4, 2, 2, 0, 99]


class TestInstruction:
    def test_mode_of_parameter(self):
        assert Instruction([1099], 0)._mode_of_parameter(0) == 0
        assert Instruction([1099], 0)._mode_of_parameter(1) == 1
        assert Instruction([1099], 0)._mode_of_parameter(2) == 0
