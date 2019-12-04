from aoc.year2019.day4.day4 import Iterator, Iterator2


class TestIndexOfFirstIllegal:
    def test_legal(self):
        assert Iterator._index_of_first_illegal('123') == -1

    def test_illegal(self):
        assert Iterator._index_of_first_illegal('103') == 1


class TestNextLegal:
    def test_basic(self):
        assert Iterator._next_legal_when_decreasing('103', 1) == '111'
        assert Iterator._next_legal_when_decreasing('993', 2) == '999'


def test_start():
    assert 111 in list(Iterator(111, 113))


def test_middle():
    assert 112 in list(Iterator(111, 113))


def test_stop():
    assert 113 in list(Iterator(111, 113))

def test_skip_not_double_digits():
    assert list(Iterator(1233, 1244)) == [1233, 1244]

def test_iterator2():
    assert list(Iterator2(699999, 699999)) == []