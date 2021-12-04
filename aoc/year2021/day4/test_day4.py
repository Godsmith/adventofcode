from aoc.year2021.day4.day4 import BingoBoard

string = """14 21 17 24  4
    10 16 15  9 19
    18  8 23 26 20
    22 11 13  6  5
     2  0 12  3  7"""


class TestBingoBoard:
    def test_all_numbers(self):
        board = BingoBoard(string)
        assert board.all_numbers == {0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                                     24, 26}

    def test_possible_bingos(self):
        board = BingoBoard(string)
        assert board.possible_bingos == [{4, 14, 17, 21, 24}, {9, 10, 15, 16, 19}, {8, 18, 20, 23, 26},
                                         {5, 6, 11, 13, 22}, {0, 2, 3, 7, 12}, {2, 10, 14, 18, 22}, {0, 8, 11, 16, 21},
                                         {12, 13, 15, 17, 23}, {3, 6, 9, 24, 26}, {4, 5, 7, 19, 20}]

    def test_draw_and_check_bingo(self):
        board = BingoBoard(string)
        assert board.draw_and_check_bingo(14) is False
        assert board.draw_and_check_bingo(21) is False
        assert board.draw_and_check_bingo(17) is False
        assert board.draw_and_check_bingo(24) is False
        assert board.draw_and_check_bingo(4) is True
