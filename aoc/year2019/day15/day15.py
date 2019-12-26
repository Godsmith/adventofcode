from typing import Tuple, Dict

from aocd import data

from aoc.astar import astar_tuples
from aoc.utils import ints
from aoc.year2019.intcode import Intcode


class Droid:
    TILES = {0: '#',
             1: '.',
             2: 'X'}

    def __init__(self):
        self.intcode = Intcode(ints(data))
        self.area = {(0, 0): '.'}
        self.position = (0, 0)
        self.previous_positions = []
        self.finished = False

    def __str__(self):
        xs = [position[0] for position in self.area]
        ys = [position[1] for position in self.area]
        out = []
        for y in range(min(ys), max(ys) + 1):
            for x in range(min(xs), max(xs) + 1):
                if (x, y) not in self.area:
                    out.append(' ')
                elif self.position == (x, y):
                    out.append('D')
                else:
                    out.append(self.area[(x, y)])
            out.append('\n')
        return ''.join(out)

    def movement_command_to_an_unexplored_position(self):
        for command, neighbor in self.neighbors.items():
            if neighbor not in self.area:
                return command
        return None

    def command(self, input_):
        if input_ is None:
            print(str(self))
            raise AssertionError('command cannot be None')
        output = self.intcode.next_output(input_)
        position = self.neighbors[input_]
        self.area[position] = self.TILES[output]

        if output > 0:
            self.previous_positions.append(self.position)
            self.position = position

    def back_up(self):
        command = self.movement_command_to_get_to_last_position()
        self.intcode.next_output(command)
        self.position = self.previous_positions.pop()
        if not self.previous_positions:
            self.finished = True

    def movement_command_to_get_to_last_position(self):
        """Example: self.position=(2,2). previous_position=(1,2). Delta=(1,0).
           command=3
           self.position = (2,2), previous_position = (2,1). Delta=(0,1)
           command = 1"""
        delta = (self.position[0] - self.previous_positions[-1][0],
                 self.position[1] - self.previous_positions[-1][1])
        commands = {(1, 0): 3, (-1, 0): 4, (0, 1): 1, (0, -1): 2}
        # print(f'back up from {self.position} to {self.previous_positions[-1]}')
        # print(str(self))
        return commands[delta]

    @property
    def oxygen_position(self):
        for position, value in self.area.items():
            if value == "X":
                return position
        raise ValueError("Could not find oxygen")

    @property
    def neighbors(self) -> Dict[int, Tuple[int, int]]:
        return {1: (self.position[0], self.position[1] - 1),
                2: (self.position[0], self.position[1] + 1),
                3: (self.position[0] - 1, self.position[1]),
                4: (self.position[0] + 1, self.position[1])}


def main():
    droid = Droid()
    while not droid.finished:
        command = droid.movement_command_to_an_unexplored_position()
        if command is None:
            droid.back_up()
        else:
            droid.command(command)
    print(str(droid))
    path = astar_tuples(droid.area, (0, 0), droid.oxygen_position,
                        wall_tiles=["#"], floor_tiles=[".", "X"],
                        adjacent=[(0, -1), (0, 1), (-1, 0), (1, 0)])
    print(len(path) - 1)


if __name__ == '__main__':
    main()
