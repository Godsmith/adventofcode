from collections import defaultdict
from typing import Tuple, Set

from aocd import get_data

data = get_data(year=2021, day=15)


class Cavern:
    def __init__(self, data: str):
        self.risk_levels = [list(map(int, row)) for row in data.splitlines()]
        self.height = len(self.risk_levels)
        self.width = len(self.risk_levels[0])
        # add starting position? or not needed?
        self.minimum_total_risks = defaultdict(lambda: 1000)

    def possible_next_steps(self, x: int, y: int, previous_positions: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        return {(x2, y2) for x2, y2 in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
                if 0 <= x2 < self.width and 0 <= y2 < self.height and (x2, y2) not in previous_positions}




def step(cavern: Cavern, x: int, y: int, total_risk: int, previous_positions: Set[Tuple[int, int]]):
    if (x, y) == (0, 0):
        new_total_risk = 0
    else:
        new_total_risk = total_risk + cavern.risk_levels[y][x]
    if (x, y) == (cavern.width - 1, cavern.height - 1):
        return new_total_risk
    new_previous_positions = previous_positions | {(x, y)}
    if new_total_risk < cavern.minimum_total_risks[(x, y)]:
        cavern.minimum_total_risks[(x, y)] = new_total_risk
        risks = []
        for x2, y2 in cavern.possible_next_steps(x, y, new_previous_positions):
            risks.append(step(cavern, x2, y2, new_total_risk, new_previous_positions))
        return min(risks) if risks else 10000000
    else:
        return 100000000

if __name__ == '__main__':
    cavern = Cavern(data)
    print(step(cavern, 0, 0, 0, set()))
