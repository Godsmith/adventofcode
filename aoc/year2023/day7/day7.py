from aocd import data
from aoc.utils import rows
from collections import Counter

value_from_card = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

letter_hands = [row.split(" ")[0] for row in rows(data)]
bids = [int(row.split(" ")[1]) for row in rows(data)]

hands: list[list[int]] = []
for letter_hand in letter_hands:
    hand = [value_from_card[card] for card in letter_hand]
    hands.append(hand)


def get_type_score(hand: list[int]) -> int:
    counter = Counter(hand)
    values = sorted(counter.values())
    if 5 in values:
        return 7
    elif 4 in values:
        return 6
    elif 3 in values and 2 in values:
        return 5
    elif 3 in values:
        return 4
    if values.count(2) == 2:
        return 3
    if 2 in values:
        return 2
    return 1


def get_ordering_score(hand: list[int]) -> float:
    value_strings = []
    for value in hand:
        value_string = str(value)
        if len(value_string) == 1:
            value_string = f"0{value_string}"
        value_strings.append(value_string)
    return float(f"0.{''.join(value_strings)}")


scores = [get_type_score(hand) + get_ordering_score(hand) for hand in hands]

scores_hands_bids = list(sorted(zip(scores, hands, bids)))

print(scores_hands_bids)

total_winnings = sum(
    rank * bid for rank, (_, _, bid) in enumerate(scores_hands_bids, 1)
)

print(total_winnings)
