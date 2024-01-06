from dataclasses import dataclass
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


@dataclass(frozen=True)
class Crucible:
    x: int
    y: int
    direction: tuple[int, int] = (1, 0)
    heat_loss: int = 0
    blocks_since_last_turn: int = 0
    max_blocks_without_turning: int = 2

    def __lt__(self, other):
        return self.heat_loss < other.heat_loss

    def create_new_crucibles(self) -> list["Crucible"]:
        new_crucibles = []
        directions_and_blocks_since_last_turn: list[tuple[tuple[int, int], int]] = [
            (turn_left(*self.direction), 0),
            (turn_right(*self.direction), 0),
        ]
        if self.blocks_since_last_turn < self.max_blocks_without_turning:
            directions_and_blocks_since_last_turn.append(
                (self.direction, self.blocks_since_last_turn + 1)
            )
        for direction, blocks_since_last_turn in directions_and_blocks_since_last_turn:
            x = self.x + direction[0]
            y = self.y + direction[1]
            if 0 <= x <= max_x and 0 <= y <= max_y:
                new_crucibles.append(
                    self.__class__(
                        x=x,
                        y=y,
                        direction=direction,
                        heat_loss=self.heat_loss + grid[(x, y)],
                        blocks_since_last_turn=blocks_since_last_turn,
                        max_blocks_without_turning=self.max_blocks_without_turning,
                    )
                )
        return new_crucibles

    def location(self):
        return (self.x, self.y, self.direction, self.blocks_since_last_turn)


def get_min_heat_loss():
    crucibles = []
    heappush(crucibles, Crucible(0, 0))
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
                return new_crucible.heat_loss
            if (
                new_crucible.location() not in previous_heat_losses
                or new_crucible.heat_loss
                < previous_heat_losses[new_crucible.location()]
            ):
                previous_heat_losses[new_crucible.location()] = new_crucible.heat_loss
                heappush(crucibles, new_crucible)


print(get_min_heat_loss())
