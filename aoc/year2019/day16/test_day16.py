from itertools import islice
from aoc.year2019.day16.day16 import phase, iterator, real_fft, fft, \
    phase_last_half


def test_iterator():
    assert list(islice(iterator(1), 13)) == [0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1, 0, 0]


def test_phase():
    s = '12345678'
    assert phase(s) == "48226158"

def test_fft():
    s = '80871224585914546619083218645595'
    assert fft(s) == "24176176"

def test_real_fft():
    s = list(map(int, "03036732577212944063491565474664"))
    assert real_fft(s) == "84462026"

def test_my_phase():
    s = '11111111111111111'
    print(phase(s))

def test_phase_last_half():
    s = list(map(int, '12345678'))
    assert phase_last_half(s) == list(map(int, "12346158"))