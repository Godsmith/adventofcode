from dataclasses import dataclass
from functools import reduce

from parse import findall
from aocd import get_data


@dataclass
class Fold:
    x_or_y: str
    value: int

    def fold(self, coordinates):
        return {self._transform(x, y) for x, y in coordinates}

    def _transform(self, x, y):
        if self.x_or_y == 'x' and x > self.value:
            return 2 * self.value - x, y
        elif self.x_or_y == 'y' and y > self.value:
            return x, 2 * self.value - y
        return x, y


data = get_data(year=2021, day=13)
coordinates = {(x, y) for x, y in findall("{:d},{:d}\n", data)}
folds = [Fold(x_or_y, value) for x_or_y, value in findall("fold along {}={:d}", data)]
print(len(folds[0].fold(coordinates)))

new_coordinates = reduce(lambda result, fold: fold.fold(result), folds, coordinates)

for y in range(max(y for x, y in new_coordinates) + 1):
    for x in range(max(x for x, y in new_coordinates) + 1):
        print('#' if (x, y) in new_coordinates else '.', end='')
    print()
