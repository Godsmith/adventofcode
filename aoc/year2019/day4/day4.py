class Iterator:
    def __init__(self, start: int, stop: int):
        self.number = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self._go_to_next_legal()
        if self.number >= self.stop:
            raise StopIteration
        return self.number

    def _go_to_next_legal(self):
        self.number += 1
        s = str(self.number)
        i = self._index_of_first_illegal(s)
        if i == -1:
            return self.number

        self.number = int(self._next_legal(s, i))

    @staticmethod
    def _next_legal(s, i):
        return s[:i] + s[i - 1] * (len(s) - i)



    @staticmethod
    def _index_of_first_illegal(s):
        for i, c in enumerate(s[1:], 1):
            if s[i] < s[i - 1]:
                return i
        return -1


def main():
    it = Iterator(111, 999)
    for i in it:
        print(i)


if __name__ == '__main__':
    main()
