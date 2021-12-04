from typing import Set

from aocd import data


class BingoBoard:
    def __init__(self, string):
        string_rows = string.split("\n")
        self.matrix = list([[int(number) for number in row.split()] for row in string_rows])

        self.all_numbers = set()
        for row in self.matrix:
            for number in row:
                self.all_numbers.add(number)

        self.possible_bingos = [set(row) for row in self.matrix]
        for position in range(5):
            self.possible_bingos.append({row[position] for row in self.matrix})

    def __repr__(self):
        return str(self.matrix)

    def draw_and_check_bingo(self, number: int) -> bool:
        for possible_bingo in self.possible_bingos:
            possible_bingo.discard(number)
            if len(possible_bingo) == 0:
                return True
        return False

    def score(self, draws_so_far: Set[int], just_drawn: int):
        remaining_numbers = self.all_numbers - draws_so_far
        return sum(remaining_numbers) * just_drawn


def get_score_of_first_board_to_win(draws, bingo_boards):
    draws_so_far = set()
    for draw in draws:
        draws_so_far.add(draw)
        for bingo_board in bingo_boards:
            if bingo_board.draw_and_check_bingo(draw):
                return bingo_board.score(draws_so_far, draw)


def get_score_of_last_board_to_win(draws, bingo_boards):
    draws_so_far = set()
    for draw in draws:
        bingo_boards_to_remove = []
        draws_so_far.add(draw)
        for bingo_board in bingo_boards:
            if bingo_board.draw_and_check_bingo(draw):
                if len(bingo_boards) == 1:
                    return bingo_board.score(draws_so_far, draw)
                bingo_boards_to_remove.append(bingo_board)
        for bingo_board in bingo_boards_to_remove:
            bingo_boards.remove(bingo_board)


if __name__ == '__main__':
    draws_string, *board_strings = data.split("\n\n")
    draws = [int(number) for number in draws_string.split(",")]
    bingo_boards = [BingoBoard(board_string) for board_string in board_strings]
    print(get_score_of_first_board_to_win(draws, bingo_boards))
    print(get_score_of_last_board_to_win(draws, bingo_boards))
