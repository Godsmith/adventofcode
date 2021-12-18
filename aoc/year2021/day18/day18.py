from typing import List, Union
from collections import deque


class SnailfishNumber:
    def __init__(self, string: str):
        self.list = self._parse(deque(string))

    def __repr__(self):
        return repr(self.list).replace(" ", "")

    @staticmethod
    def _parse(source: deque[str]) -> List:
        list_ = []
        source.popleft()
        while source:
            if source[0].isnumeric():
                list_.append(int(source.popleft()))
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

    def explode(self):
        pass
