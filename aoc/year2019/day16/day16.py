from itertools import cycle
from aocd import data


def fft(s, count):
    for _ in range(count):
        s = phase(s)
    return s

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
    print(fft(data, 100)[:8])

if __name__ == '__main__':
    main()