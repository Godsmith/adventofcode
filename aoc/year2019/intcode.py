from typing import List
from operator import add, mul


class Intcode(list):
    def __init__(self, list_: List[int]):
        super().__init__(list_)

    def step(self, index) -> int:
        instruction = instructions[self[index]]
        return instruction.execute(self, index)

    def run(self):
        index = 0
        while index >= 0:
            index = self.step(index)
        return self


class Instruction:
    def __init__(self, length):
        self.length = length

    def execute(self, program, index):
        """ Modifies the state and returns the next index to execute"""
        self._execute(program, index)
        return index + self.length

    def _execute(self, program, index):
        pass


class Add(Instruction):
    operator = add

    def __init__(self):
        super().__init__(4)

    def _execute(self, program, index):
        x = program[program[index + 1]]
        y = program[program[index + 2]]
        target = program[index + 3]
        program[target] = self.operator(x, y)


class Mul(Add):
    operator = mul


class Halt(Instruction):
    def __init__(self):
        super().__init__(-1000000)


instructions = {1: Add(), 2: Mul(), 99: Halt()}
