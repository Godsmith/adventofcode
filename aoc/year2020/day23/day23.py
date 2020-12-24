from collections import deque

from aocd import data


def get_cups(ints):
    cups = {}
    for cup, cup_after in zip(ints, ints[1:]):
        cups[cup] = cup_after
    cups[ints[-1]] = ints[0]
    return cups


def move(cups, moves):
    current_cup = list(cups.keys())[0]
    for i in range(moves):
        picked_up = []
        cup_to_pick_up = cups[current_cup]
        for _ in range(3):
            picked_up.append(cup_to_pick_up)
            cup_to_pick_up = cups[cup_to_pick_up]
        cups[current_cup] = cup_to_pick_up
        destination_number = current_cup - 1
        while destination_number in picked_up:
            destination_number -= 1
        if destination_number == 0:
            destination_number = len(cups)
        cups[picked_up[2]] = cups[destination_number]
        cups[destination_number] = picked_up[0]
        current_cup = cups[current_cup]


def print_all_after_one(cups):
    cup = cups[1]
    for _ in range(len(cups) - 1):
        print(cup, end="")
        cup = cups[cup]
    print()


# Part 1

ints = list(map(int, data))

cups = get_cups(ints)
move(cups, 100)

print_all_after_one(cups)

# Part 2

ints2 = list(map(int, data))
ints2.extend(range(10, 1000001))
cups = get_cups(ints2)

move(cups, 10000000)

print(cups[1] * cups[cups[1]])
