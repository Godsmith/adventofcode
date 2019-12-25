from collections import defaultdict
from typing import List, Tuple

from aocd import data

from aoc.utils import ints, sign_of_difference, grouper
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
        outputs = self._intcode.run_to_next_input(input_)
        for x, y, tile in grouper(outputs, 3):
            self._screen[(x, y)] = tile
            if tile == 4:
                self._last_ball_position = self._ball_position
                self._ball_position = (x, y)
            if self._ball_position[1] == 19:
                self.game_over = True

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
        """If the ball is just above the paddle, hold still. Otherwise, try to be
        one tile ahead of the current trajectory."""
        if self._ball_position[1] == 17:
            return self._ball_position[0]
        if self._ball_position[0] - self._last_ball_position[0] > 0:
            # moving right
            return self._ball_position[0] + 1
        else:
            return self._ball_position[0] - 1

    @property
    def score(self):
        return self._screen[(-1, 0)]


DEBUG = False


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
        if DEBUG:
            print(screen)
            print(
                f"ball_x: {screen.ball_position}, "
                f"paddle_x: {screen.paddle_x}, "
                f"target_paddle_position: {screen.target_paddle_position}, "
                f"input: {input_}")
        if screen.block_count == 0:
            break
        if screen.game_over:
            break
    print(screen.score)


if __name__ == '__main__':
    main()
