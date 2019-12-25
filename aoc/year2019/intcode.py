from collections import deque, defaultdict
from typing import List, Union, Generator, Optional, Tuple
from operator import add, mul, eq, ne, lt


class Intcode:
    def __init__(self, program: List[int]):
        self.program = defaultdict(lambda: 0)
        for i, value in enumerate(program):
            self.program[i] = value
        self._inputs = deque([])
        self.index = 0
        self.finished = False
        self.relative_base = 0

    def __getitem__(self, item):
        return self.program[item]

    def __setitem__(self, key, value):
        self.program[key] = value

    def _step(self, index) -> Tuple[int, Optional[int]]:
        opcode = str(self[index]).zfill(2)[-2:]
        return instructions[opcode](self, index).execute()

    def next_output(self, inputs: Union[int, List[int], None] = None):
        """ Returns the next integer output, or None if it is at the end."""
        if inputs is None:
            inputs = []
        if type(inputs) == int:
            inputs = [inputs]
        for input_ in inputs:
            self._inputs.append(input_)

        while not self.finished:
            self.index, output = self._step(self.index)
            if output is not None:
                return output

    def all_outputs(self, input_to_first_iteration: Optional[int] = None):
        outputs = []
        output = self.next_output(input_to_first_iteration)
        while output is not None:
            outputs.append(output)
            output = self.next_output()
        return outputs

    def next_input(self):
        return self._inputs.popleft()

    def set_input(self, input_):
        self._inputs = deque([input_])

    def to_list(self):
        """Only makes sense for consecutive programs"""
        return [value for value in self.program.values()]


class Instruction:
    LENGTH = 0

    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2

    def __init__(self, program, index):
        self.program = program
        self.index = index

    def execute(self) -> (int, Tuple[int, Optional[int]]):
        """ Modifies the state and returns the next index to execute"""
        output = self._execute()
        return self._next_index(), output

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
        elif mode == Instruction.RELATIVE:
            return self.program[
                self._value_of(parameter_index) + self.program.relative_base]
        else:
            raise ValueError(f"Invalid parameter mode {mode}.")

    def __setitem__(self, parameter_index, value):
        mode = self._mode_of_parameter(parameter_index)
        if mode == Instruction.POSITION:
            self.program[self._value_of(parameter_index)] = value
        elif mode == Instruction.RELATIVE:
            self.program[
                self._value_of(parameter_index) + self.program.relative_base] = value

    def _value_of(self, parameter_index):
        return self.program[self.index + parameter_index + 1]

    def _mode_of_parameter(self, parameter_index):
        return int(str(self.program[self.index]).zfill(6)[-(parameter_index + 3)])

    def _execute(self) -> Optional[int]:
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
        return self[0]


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


class AdjustRelativeBase(Instruction):
    LENGTH = 2

    def _execute(self):
        self.program.relative_base += self[0]


class Halt(Instruction):
    def _execute(self):
        self.program.finished = True


instructions = {'01': Add, '02': Mul, '03': Input, '04': Output, '05': JumpIfTrue,
                '06': JumpIfFalse, '07': LessThan, '08': Equals,
                '09': AdjustRelativeBase, '99': Halt}
