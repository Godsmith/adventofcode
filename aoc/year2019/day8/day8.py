from aocd import data
from itertools import zip_longest


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks
    >>> list(grouper('ABCDEFG', 3, 'x'))
    [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'x', 'x')]"""
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


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
