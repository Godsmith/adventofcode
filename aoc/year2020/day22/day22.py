from collections import deque
from aocd import data

from aoc.utils import rows


def get_deck(player_data: str):
    return deque(map(int, reversed(rows(player_data)[1:])))


def get_decks(data: str):
    player1_data, player2_data = data.split("\n\n")
    return get_deck(player1_data), get_deck(player2_data)


def score(deck):
    return sum(card_value * score for card_value, score in zip(deck, range(1, 51)))



class Game:
    def __init__(self, deck1: deque, deck2: deque):
        self.deck1 = deck1
        self.deck2 = deck2
        self.previous_decklist_hashes = set()

    def play(self):
        while self.deck1 and self.deck2:
            if self._decklist_hash() in self.previous_decklist_hashes:
                return 1, self.deck1
            self.previous_decklist_hashes.add(self._decklist_hash())
            card1 = self.deck1.pop()
            card2 = self.deck2.pop()
            if card1 > len(deck1) or card2 > len(deck2):
                winner = 1 if card1 > card2 else 2
            else:
                winner, _ = Game(deque(list(self.deck1)[:card1]), deque(list(self.deck2)[:card2])).play()
            if winner == 1:
                deck1.extendleft([card1, card2])
            else:
                deck2.extendleft([card2, card1])
        if self.deck1:
            return 1, self.deck1
        else:
            return 2, self.deck2

    def _decklist_hash(self):
        return tuple(self.deck1 + deque("/") + self.deck2)


deck1, deck2 = get_decks(data)

while deck1 and deck2:
    card1 = deck1.pop()
    card2 = deck2.pop()
    if card1 > card2:
        deck1.extendleft([card1, card2])
    else:
        deck2.extendleft([card2, card1])

winning_deck = deck1 or deck2
print(score(winning_deck))

deck1, deck2 = get_decks(data)

print(score(Game(deck1, deck2).play()[1]))





