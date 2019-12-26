from itertools import cycle
from typing import List

from aocd import data


def fft(s):
    for _ in range(100):
        s = phase(s)
    return s[:8]


def real_fft(s):
    s *= 10000
    for _ in range(100):
        s = phase_last_half(s)
    offset = int(''.join(map(str, s[:7])))
    return ''.join(map(str, s[offset:offset + 8]))


def phase_last_half(ints: List[int]):
    sum_ = 0
    for i in range(len(ints) - 1, len(ints) // 2 - 1, -1):
        sum_ = (sum_ + ints[i]) % 10
        ints[i] = sum_
    return ints


def phase(s):
    ints = [int(c) for c in s]
    out = []
    for i, _ in enumerate(ints):
        sum_ = 0
        for x, y in zip(ints, iterator(i)):
            sum_ += x * y
        if sum_ < 0:
            sum_ *= -1
        sum_ %= 10
        out.append(str(sum_))
    return ''.join(out)


def iterator(i):
    i = i + 1
    out = cycle([0] * i + [1] * i + [0] * i + [-1] * i)
    next(out)
    return out


def main():
    print(fft(data))
    print(real_fft(list(map(int, data))))


if __name__ == '__main__':
    main()
