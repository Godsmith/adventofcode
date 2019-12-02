from typing import List


class Intcode(list):
    def __init__(self, list_: List[int]):
        super().__init__(list_)
        self.index = 0

    def step(self):
        opcode = self[self.index]
        if opcode == 99:
            return
        x = self[self[self.index + 1]]
        y = self[self[self.index + 2]]
        target = self[self.index + 3]
        if opcode == 1:
            self[target] = x + y
        if opcode == 2:
            self[target] = x * y
        self.index += 4

    def run(self):
        while self[self.index] != 99:
            self.step()
        return self
