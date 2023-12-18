from aocd import data
from aoc.utils import rows
from collections import Counter


hands = [row.split(" ")[0] for row in rows(data)]
bids = [int(row.split(" ")[1]) for row in rows(data)]


def get_type_score(hand: str) -> int:
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


def get_ordering_score(hand: str, jokers: bool = False) -> float:
    value_strings = []
    value_from_card = {
        "A": "14",
        "K": "13",
        "Q": "12",
        "J": "11",
        "T": "10",
    }
    if jokers:
        value_from_card["J"] = "01"
    for card in hand:
        value_string = value_from_card.get(card, card)
        if len(value_string) == 1:
            value_string = f"0{value_string}"
        value_strings.append(value_string)
    return float(f"0.{''.join(value_strings)}")


def print_total_winnings(scores):
    scores_hands_bids = list(sorted(zip(scores, hands, bids)))

    total_winnings = sum(
        rank * bid for rank, (_, _, bid) in enumerate(scores_hands_bids, 1)
    )

    print(total_winnings)


print_total_winnings(
    [get_type_score(hand) + get_ordering_score(hand) for hand in hands]
)

# scores = [get_max_type_score(hand) + get_ordering_score(hand, jokers=True) for hand in hands]
