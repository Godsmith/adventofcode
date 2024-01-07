from dataclasses import dataclass

from typing import Optional
from aoc.utils import rows
from aocd import data
from heapq import heappush, heappop


# data = """2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533"""

# data = """111111111111
# 999999999991
# 999999999991
# 999999999991
# 999999999991"""


# Idea: spawn new crucibles all the time, collect the crucible properties
# in a set and stop a crucible if we have been there before but
# with less or equal heat loss


def turn_left(x, y):
    return y, -x


def turn_right(x, y):
    return -y, x


grid = {}
for y, row in enumerate(rows(data)):
    for x, char in enumerate(row):
        grid[(x, y)] = int(char)

max_x = max(x for x, _ in grid)
max_y = max(y for _, y in grid)


def heat_loss(start_x, start_y, end_x, end_y):
    heat_loss = 0
    if start_y == end_y:
        dx = (end_x - start_x) // abs(end_x - start_x)
        for x in range(start_x + dx, end_x + dx, dx):
            heat_loss += grid[(x, start_y)]
    else:
        dy = (end_y - start_y) // abs(end_y - start_y)
        for y in range(start_y + dy, end_y + dy, dy):
            heat_loss += grid[(start_x, y)]
    return heat_loss


@dataclass(frozen=True)
class Crucible:
    x: int
    y: int
    direction: tuple[int, int] = (1, 0)
    heat_loss: int = 0
    blocks_since_last_turn: int = 0
    max_blocks_without_turning: int = 3
    after_turn_minimum: int = 1
    history: Optional[list[tuple[int, int]]] = None

    def __lt__(self, other):
        return self.heat_loss < other.heat_loss

    def create_new_crucibles(self) -> list["Crucible"]:
        new_crucibles = []
        directions_and_blocks_since_last_turn_and_minimum_move: list[
            tuple[tuple[int, int], int, int]
        ] = [
            (
                turn_left(*self.direction),
                self.after_turn_minimum,
                self.after_turn_minimum,
            ),
            (
                turn_right(*self.direction),
                self.after_turn_minimum,
                self.after_turn_minimum,
            ),
        ]
        if self.blocks_since_last_turn < self.max_blocks_without_turning:
            directions_and_blocks_since_last_turn_and_minimum_move.append(
                (self.direction, self.blocks_since_last_turn + 1, 1)
            )
        for (
            direction,
            blocks_since_last_turn,
            minimum_move,
        ) in directions_and_blocks_since_last_turn_and_minimum_move:
            x = self.x + direction[0] * minimum_move
            y = self.y + direction[1] * minimum_move
            if 0 <= x <= max_x and 0 <= y <= max_y:
                new_crucibles.append(
                    self.__class__(
                        x=x,
                        y=y,
                        direction=direction,
                        heat_loss=self.heat_loss + heat_loss(self.x, self.y, x, y),
                        blocks_since_last_turn=blocks_since_last_turn,
                        max_blocks_without_turning=self.max_blocks_without_turning,
                        after_turn_minimum=self.after_turn_minimum,
                        history=(self.history or []) + [(x, y)],
                    )
                )
        return new_crucibles

    def location(self):
        return (self.x, self.y, self.direction, self.blocks_since_last_turn)


def get_min_heat_loss(max_blocks_without_turning, after_turn_minimum):
    crucibles = []
    heappush(
        crucibles,
        Crucible(
            0,
            0,
            max_blocks_without_turning=max_blocks_without_turning,
            after_turn_minimum=after_turn_minimum,
        ),
    )
    previous_heat_losses = {}

    i = 0
    while crucibles:
        crucible = heappop(crucibles)
        i += 1
        i %= 10000
        if i == 0:
            print(max_x + max_y - crucible.x - crucible.y)
        # Spawn up to three crucibles in the adjoining locations
        for new_crucible in crucible.create_new_crucibles():
            if new_crucible.x == max_x and new_crucible.y == max_y:
                for y in range(max_y + 1):
                    for x in range(max_x + 1):
                        if (x, y) in new_crucible.history:
                            print("#", end="")
                        else:
                            print(".", end="")
                    print()
                print(new_crucible.history)
                return new_crucible.heat_loss
            if (
                new_crucible.location() not in previous_heat_losses
                or new_crucible.heat_loss
                < previous_heat_losses[new_crucible.location()]
            ):
                previous_heat_losses[new_crucible.location()] = new_crucible.heat_loss
                heappush(crucibles, new_crucible)


print(get_min_heat_loss(3, 1))
print(get_min_heat_loss(10, 4))
