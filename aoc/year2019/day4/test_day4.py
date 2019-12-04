from aoc.year2019.day4.day4 import Iterator

class TestIndexOfFirstIllegal:
    def test_legal(self):
        assert Iterator._index_of_first_illegal('123') == -1

    def test_illegal(self):
        assert Iterator._index_of_first_illegal('103') == 1

class TestNextLegal:
    def test_basic(self):
        assert Iterator._next_legal('103', 1) == '111'
        assert Iterator._next_legal('993', 2) == '999'
