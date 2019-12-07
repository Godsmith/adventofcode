from collections import deque
from typing import List, Union
from operator import add, mul, eq, ne, lt


class Intcode(list):
    def __init__(self, program: List[int]):
        super().__init__(program)
        self._original_program = list(program)
        self.output = None
        self._inputs = deque([])

    def step(self, index) -> int:
        opcode = str(self[index]).zfill(2)[-2:]
        return instructions[opcode](self, index).execute()

    def run(self, inputs: Union[int, List[int], None]=None):
        self[:] = list(self._original_program)
        if inputs is None:
            inputs = []
        if type(inputs) == int:
            inputs = [inputs]
        for input_ in inputs:
            self._inputs.append(input_)

        index = 0
        while index >= 0:
            index = self.step(index)
        return self

    def next_input(self):
        return self._inputs.popleft()


class Instruction:
    LENGTH = 0

    POSITION = 0
    IMMEDIATE = 1

    def __init__(self, program, index):
        self.program = program
        self.index = index

    def execute(self):
        """ Modifies the state and returns the next index to execute"""
        self._execute()
        return self._next_index()

    def _next_index(self):
        return self.index + self.LENGTH

    def __getitem__(self, parameter_index):
        if parameter_index >= self.LENGTH or parameter_index < 0:
            raise ValueError(
                f"Trying to access parameter {parameter_index} of {self.__class__}.")
        mode = self._mode_of_parameter(parameter_index)
        if mode == Instruction.POSITION:
            return self.program[self._value_of(parameter_index)]
        elif mode == Instruction.IMMEDIATE:
            return self._value_of(parameter_index)
        else:
            raise ValueError(f"Invalid parameter mode {mode}.")

    def __setitem__(self, parameter_index, value):
        self.program[self._value_of(parameter_index)] = value

    def _value_of(self, parameter_index):
        return self.program[self.index + parameter_index + 1]

    def _mode_of_parameter(self, parameter_index):
        return int(str(self.program[self.index]).zfill(6)[-(parameter_index + 3)])

    def _execute(self):
        pass


class Add(Instruction):
    OPERATOR = add
    LENGTH = 4

    def _execute(self):
        self[2] = self.OPERATOR(self[0], self[1])


class Mul(Add):
    OPERATOR = mul


class Input(Instruction):
    LENGTH = 2

    def _execute(self):
        self[0] = self.program.next_input()


class Output(Input):
    def _execute(self):
        self.program.output = self[0]


class JumpIfTrue(Instruction):
    LENGTH = 3
    OPERATOR = ne

    def _next_index(self):
        return self[1] if self.OPERATOR(self[0], 0) else self.index + self.LENGTH


class JumpIfFalse(JumpIfTrue):
    OPERATOR = eq


class LessThan(Instruction):
    LENGTH = 4
    OPERATOR = lt

    def _execute(self):
        self[2] = int(self.OPERATOR(self[0], self[1]))


class Equals(LessThan):
    OPERATOR = eq


class Halt(Instruction):
    LENGTH = -10000000


instructions = {'01': Add, '02': Mul, '03': Input, '04': Output, '05': JumpIfTrue,
                '06': JumpIfFalse, '07': LessThan, '08': Equals,
                '99': Halt}
