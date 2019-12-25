from collections import defaultdict
from typing import List, Tuple

from aocd import data

from aoc.utils import ints, sign_of_difference
from aoc.year2019.intcode import Intcode

PADDLE_Y = 18


class Screen:
    TILES = {0: " ", 1: "|", 2: "#", 3: "-", 4: "o"}
    MAX_X = 43
    MAX_Y = 19

    def __init__(self, instructions: List[int]):
        self._screen = defaultdict(lambda: 0)
        self._intcode = Intcode(instructions)
        self._ball_position = (0, 0)
        self._last_ball_position = (0, 0)
        self.game_over = False

    def __str__(self):
        strings = []
        for y in range(self.MAX_Y + 1):
            for x in range(self.MAX_X + 1):
                strings.append(self.TILES[self._screen[(x, y)]])
            strings.append('\n')
        return ''.join(strings)

    def input(self, input_):
        while True:
            self._intcode.set_input(input_)
            x = self._intcode.next_output()
            y = self._intcode.next_output()
            tile = self._intcode.next_output()
            if tile is None:
                self.game_over = True
                break
            self._screen[(x, y)] = tile
            print("tile")
            if tile == 4:
                print("ball!")
                self._last_ball_position = self._ball_position
                self._ball_position = (x, y)
            if tile == 3:
                print("paddle!")
                break

    @property
    def block_count(self):
        return len([tile for tile in self._screen.values() if tile == 2])

    @property
    def paddle_x(self):
        for (x, _), tile in self._screen.items():
            if tile == 3:
                return x
        return 0

    @property
    def ball_position(self):
        return self._ball_position

    @property
    def last_ball_position(self):
        return self._last_ball_position

    @property
    def target_paddle_position(self):
        if self._ball_position[0] - self._last_ball_position[0] > 1:
            # moving right
            return self._ball_position[0] + 1
        else:
            return self._ball_position[0] - 1

    @property
    def score(self):
        return self._screen[(-1, 0)]



def main():
    # part 1
    screen = Screen(ints(data))
    screen.input(0)
    print(screen.block_count)

    # part 2

    play_for_free_instructions = list(ints(data))
    play_for_free_instructions[0] = 2
    screen = Screen(play_for_free_instructions)

    while True:
        input_ = sign_of_difference(screen.target_paddle_position, screen.paddle_x)
        screen.input(input_)
        print(screen)
        print(
            f"ball_x: {screen.ball_position}, "
            f"paddle_x: {screen.paddle_x}, "
            f"input: {input_}")
        if screen.block_count == 0:
            break
        if screen.game_over:
            break
    print(screen.score)


def target_paddle_position(ball_position, last_ball_position):
    # If the ball is moving upwards, just track the ball position
    if ball_position[1] < last_ball_position[1]:
        return ball_position[0]


if __name__ == '__main__':
    main()
