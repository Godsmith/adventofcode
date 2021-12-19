import math
from collections import deque
from typing import Union, List


class SnailfishNumber:
    def __init__(self, string: str):
        self.list = self._parse(deque(string))
        self.locations = self._locations()

    def __repr__(self):
        return repr(self.list).replace(" ", "")

    def __add__(self, other: 'SnailfishNumber'):
        self.list = [self.list, other.list]
        self.locations = self._locations()

        while True:
            if self._can_explode():
                self._explode()
            elif self._can_split():
                self._split()
            else:
                break

        return self

    @classmethod
    def final_sum(cls, text: str):
        return sum([SnailfishNumber(row) for row in text.splitlines()], start=SnailfishNumber('[]'))

    @property
    def magnitude(self):
        return self._magnitude(self.list)

    @classmethod
    def _magnitude(cls, list_or_int: Union[List, int]):
        if isinstance(list_or_int, int):
            return list_or_int
        else:
            return cls._magnitude(list_or_int[0]) * 3 + cls._magnitude(list_or_int[1]) * 2

    @staticmethod
    def _parse(source: deque[str]) -> List:
        list_ = []
        source.popleft()
        while source:
            if source[0].isnumeric():
                if source[1].isnumeric():
                    value = int(source.popleft() + source.popleft())
                else:
                    value = int(source.popleft())
                list_.append(value)
            elif source[0] == "[":
                list_.append(SnailfishNumber._parse(SnailfishNumber._pop_until_enclosed_list_and_return(source)))
            else:
                source.popleft()
        return list_

    @staticmethod
    def _pop_until_enclosed_list_and_return(source: deque[str]) -> deque[str]:
        new_deque = deque()
        while new_deque.count("[") > new_deque.count("]") or not new_deque:
            new_deque.append(source.popleft())
        return new_deque

    def _locations(self):
        return self._get_locations(self.list, [])

    def __getitem__(self, location: List):
        element = self.list
        for i in location:
            element = element[i]
        return element

    def __setitem__(self, location: List, value: Union[List, int]):
        element = self.list
        for i in location[:-1]:
            element = element[i]
        element[location[-1]] = value

    @classmethod
    def _get_locations(cls, list_: List, location_of_list: []):
        locations = []
        for current_location, element in enumerate(list_):
            if isinstance(element, int):
                locations.append(location_of_list + [current_location])
            elif isinstance(element, list):
                locations.extend(cls._get_locations(element, location_of_list + [current_location]))
        return locations

    def _can_explode(self):
        return any(len(location) > 4 for location in self.locations)

    def _can_split(self):
        return any(self[location] >= 10 for location in self.locations)

    def _explode(self):
        shall_explode = [len(location) > 4 for location in self.locations]
        explode_index = shall_explode.index(True)
        explode_location = self.locations[explode_index]
        left_value, right_value = self[explode_location[:-1]]

        self[explode_location[:-1]] = 0
        if explode_index < len(self.locations) - 2:  # -2 since explode_index is index of left digit
            self[self.locations[explode_index + 2]] += right_value  # +2 since explode_index is index of left digit
        if explode_index > 0:
            self[self.locations[explode_index - 1]] += left_value

        self.locations = self._locations()

    def _split(self):
        split_location = [location for location in self.locations if self[location] >= 10][0]
        value = self[split_location]
        left_value = math.floor(value / 2)
        right_value = math.ceil(value / 2)
        self[split_location] = [left_value, right_value]

        self.locations = self._locations()