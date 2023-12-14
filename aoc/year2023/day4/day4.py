from collections import deque
from aocd import data
from dataclasses import dataclass
from aoc.utils import rows
import itertools
import copy

points = 0
for card in rows(data):
    card_nr, winning_and_my_numbers = card.split(":")
    winning_numbers_str, my_numbers_str = winning_and_my_numbers.split("|")
    winning_numbers = {int(i) for i in winning_numbers_str.split(" ") if i}
    my_numbers = { int(i) for i in my_numbers_str.split(" ") if i }
    overlap = winning_numbers.intersection(my_numbers)
    if overlap:
        points += 2 ** (len(overlap) - 1)

print(points)

# Part 2

@dataclass
class Card:
    card_nr: int
    winning_numbers: set[int]
    my_numbers: set[int]

    @classmethod
    def from_row(cls, row: str):
        card_nr, winning_and_my_numbers = row.split(":")
        winning_numbers_str, my_numbers_str = winning_and_my_numbers.split("|")
        winning_numbers = {int(i) for i in winning_numbers_str.split(" ") if i}
        my_numbers = { int(i) for i in my_numbers_str.split(" ") if i }
        return cls(int(card_nr.split(" ")[-1]), winning_numbers, my_numbers)

    def winning_number_count(self):
        return len(self.winning_numbers.intersection(self.my_numbers))
    

cards = [ Card.from_row(row) for row in rows( data ) ]
card_from_number = {card.card_nr: card for card in cards}
count_from_number = {card.card_nr: 1 for card in cards}

def get_cards_from_card(card: Card)-> list[Card]:
    score = card.winning_number_count()
    card_numbers_won = range(card.card_nr + 1, card.card_nr + 1 + score)
    return [card_from_number[card_nr] for card_nr in card_numbers_won]

cards_scored_count = 0
for card_nr, card in card_from_number.items():
    won_card_numbers = list(range(card_nr + 1, card_nr + card.winning_number_count() + 1))
    for new_card_nr in won_card_numbers:
        if new_card_nr <= len(cards):
            count_from_number[new_card_nr] += count_from_number[card_nr]

print(sum(count_from_number.values()))



