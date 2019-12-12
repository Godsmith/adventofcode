from collections import defaultdict

from aocd import data
from aoc.year2019.intcode import Intcode
from aoc.utils import ints


class PaintRobot:
    DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def __init__(self, program, color_of_first_panel=0):
        self.x = 0
        self.y = 0
        self.intcode = Intcode(program)
        self.panels = {(0, 0): color_of_first_panel}
        self.direction = (0, -1)
        self.finished = False

    def color_of_current_panel(self):
        # We cannot use defaultdict since it creates a new entry on read
        if not (self.x, self.y) in self.panels:
            return 0
        else:
            return self.panels[(self.x, self.y)]

    def step(self):
        new_color = self.intcode.next_output(self.color_of_current_panel())
        new_direction = self.intcode.next_output()
        if new_color is None or new_direction is None:
            self.finished = True
            return

        self.panels[(self.x, self.y)] = new_color

        if new_direction == 0:
            self.turn_left()
        else:
            self.turn_right()

        self.move()

    @property
    def number_of_panels_painted(self):
        return len(self.panels)

    def turn_left(self):
        new_index = self.DIRECTIONS.index(self.direction) - 1
        self.direction = self.DIRECTIONS[new_index]

    def turn_right(self):
        new_index = (self.DIRECTIONS.index(self.direction) + 1) % len(self.DIRECTIONS)
        self.direction = self.DIRECTIONS[new_index]

    def move(self):
        self.x += self.direction[0]
        self.y += self.direction[1]


def main():
    robot = PaintRobot(ints(data))
    while not robot.finished:
        robot.step()
    print(robot.number_of_panels_painted)


if __name__ == '__main__':
    main()
