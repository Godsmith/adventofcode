from collections import deque
from aocd import data

from aoc.utils import rows


def get_deck(player_data: str):
    return deque(map(int, rows(player_data)[1:]))


def get_decks(data: str):
    player1_data, player2_data = data.split("\n\n")
    return get_deck(player1_data), get_deck(player2_data)


def score(deck):
    return sum(
        card_value * score for card_value, score in zip(deck, range(len(deck), 0, -1)))


class Game:
    def __init__(self, deck1: deque, deck2: deque):
        self.deck1 = deck1
        self.deck2 = deck2
        self.previous_decklist_hashes = set()

    def play(self) -> tuple[int, deque]:
        while self.deck1 and self.deck2:
            card1 = self.deck1.popleft()
            card2 = self.deck2.popleft()
            winner = 1 if card1 > card2 else 2
            self._give_winner_cards(winner, card1, card2)
        return winner, self.deck1 or self.deck2

    def _give_winner_cards(self, winner, card1, card2):
        if winner == 1:
            self.deck1.extend([card1, card2])
        else:
            self.deck2.extend([card2, card1])

    def _decklist_hash(self):
        return tuple(self.deck1 + deque("/") + self.deck2)


class Game2(Game):
    def play(self):
        while self.deck1 and self.deck2:
            if self._decklist_hash() in self.previous_decklist_hashes:
                return 1, self.deck1
            self.previous_decklist_hashes.add(self._decklist_hash())

            card1 = self.deck1.popleft()
            card2 = self.deck2.popleft()
            if card1 > len(self.deck1) or card2 > len(self.deck2):
                winner = 1 if card1 > card2 else 2
            else:
                winner, _ = Game2(deque(list(self.deck1)[:card1]),
                                  deque(list(self.deck2)[:card2])).play()
            self._give_winner_cards(winner, card1, card2)
        return winner, self.deck1 or self.deck2


print(score(Game(*get_decks(data)).play()[1]))
print(score(Game2(*get_decks(data)).play()[1]))
