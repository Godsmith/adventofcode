import re


class Iterator:
    def __init__(self, start: int, stop: int):
        self.number = self._next_legal(start)
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > self.stop:
            raise StopIteration
        out = self.number
        self.number += 1
        self.number = self._next_legal(self.number)
        return out

    @classmethod
    def _next_legal(cls, number):
        s = str(number)
        i = cls._index_of_first_illegal(s)
        if i != -1:
            new_number = int(cls._next_legal_when_decreasing(s, i))
            return cls._next_legal(new_number)
        if not cls._has_double_digits(s):
            new_number = number + 1
            return cls._next_legal(new_number)
        return number

    @staticmethod
    def _next_legal_when_decreasing(s, i):
        return s[:i] + s[i - 1] * (len(s) - i)

    @staticmethod
    def _has_double_digits(s):
        for i in range(0, 10):
            if f'{i}{i}' in s:
                return True
        return False

    @staticmethod
    def _index_of_first_illegal(s):
        for i, c in enumerate(s[1:], 1):
            if s[i] < s[i - 1]:
                return i
        return -1


class Iterator2(Iterator):

    @staticmethod
    def _has_double_digits(s):
        xsx = f'x{s}x'
        for i in range(0, 10):
            if re.search(f'[^{i}]{i}{i}[^{i}]', xsx):
                return True
        return False


def main():
    a = 248345
    b = 746315
    print(len(list(Iterator(a, b))))
    print(len(list(Iterator2(a, b))))


if __name__ == '__main__':
    main()
