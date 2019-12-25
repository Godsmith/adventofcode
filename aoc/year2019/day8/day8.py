from aocd import data
from aoc.utils import grouper


def main():
    layers = list(grouper(data, 25 * 6))
    d = {layer.count('0'): layer.count('1') * layer.count('2') for layer in layers}
    print(d[min(d)])

    final = []
    for i in range(25 * 6):
        for layer in layers:
            if layer[i] != '2':
                final.append(layer[i])
                break

    for row in grouper(final, 25):
        print(''.join(row).replace('0', ' ').replace('1', '#'))


if __name__ == '__main__':
    main()
