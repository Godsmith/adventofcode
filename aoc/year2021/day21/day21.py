import functools


class Player:
    def __init__(self, position):
        self.position = position
        self.score = 0

    def move(self, steps: int):
        self.position += steps
        while self.position > 10:
            self.position -= 10
        self.score += self.position


class Die:
    def __init__(self):
        self.next_value = 1
        self.roll_count = 0

    def roll(self) -> int:
        self.roll_count += 1

        return_value = self.next_value
        self.next_value += 1
        if self.next_value > 100:
            self.next_value = 1

        return return_value

    def roll_three_times(self):
        return self.roll() + self.roll() + self.roll()


def run(player1_position, player2_position) -> int:
    die = Die()
    player1 = Player(player1_position)
    player2 = Player(player2_position)
    while True:
        player1.move(die.roll_three_times())
        if player1.score >= 1000:
            return die.roll_count * player2.score
        player2.move(die.roll_three_times())
        if player2.score >= 1000:
            return die.roll_count * player1.score


print(run(8, 2))

STEPS_AND_COUNTS = ((3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1))


@functools.lru_cache(maxsize=None)
def play(player1_position, player2_position, player1_score, player2_score):
    if player1_score >= 21:
        return 1, 0
    elif player2_score >= 21:
        return 0, 1

    player1_wins = 0
    player2_wins = 0

    for steps, count in STEPS_AND_COUNTS:
        new_player1_position = player1_position + steps
        while new_player1_position > 10:
            new_player1_position -= 10
        new_player1_score = player1_score + new_player1_position
        new_player2_wins, new_player1_wins = play(player2_position, new_player1_position, player2_score, new_player1_score)
        player1_wins += new_player1_wins * count
        player2_wins += new_player2_wins * count

    return player1_wins, player2_wins


print(max(play(8, 2, 0, 0)))
# print(play(4, 8, 0, 0))
