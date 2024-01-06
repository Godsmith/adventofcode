from dataclasses import dataclass
from aoc.utils import rows
from aocd import data


data = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""


# Idea: spawn new crucibles all the teime, collect the crucible properties
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
    last_direction: tuple[int, int] = (0, 0)
    last_last_direction: tuple[int, int] = (0, 0)
    heat_loss: int = 0

    def create_new_crucibles(self) -> list["Crucible"]:
        new_crucibles = []
        directions = [turn_left(*self.direction), turn_right(*self.direction)]
        if not self.direction == self.last_direction == self.last_last_direction:
            directions.append(self.direction)
        for direction in directions:
            x = self.x + direction[0]
            y = self.y + direction[1]
            if 0 <= x <= max_x and 0 <= y <= max_y:
                new_crucibles.append(
                    self.__class__(
                        x,
                        y,
                        direction,
                        self.direction,
                        self.last_direction,
                        self.heat_loss + grid[(x, y)],
                    )
                )
        return new_crucibles

    def location(self):
        return (
            self.x,
            self.y,
            self.direction,
            self.last_direction,
            self.last_last_direction,
        )


crucibles = [Crucible(0, 0)]
previous_heat_losses = {}

while crucibles:
    new_crucibles = []
    for crucible in crucibles:
        # Spawn up to three crucibles in the adjoining locations
        for new_crucible in crucible.create_new_crucibles():
            if (
                new_crucible.location() not in previous_heat_losses
                or new_crucible.heat_loss
                < previous_heat_losses[new_crucible.location()]
            ):
                previous_heat_losses[new_crucible.location()] = new_crucible.heat_loss
                new_crucibles.append(new_crucible)
    crucibles = new_crucibles
    # print(len(crucibles))
    # print(crucibles[0].heat_loss, naive_heat_loss)

heat_losses = {
    value
    for (x, y, _, _, _), value in previous_heat_losses.items()
    if x == max_x and y == max_y
}

print(min(heat_losses))
