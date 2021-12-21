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
