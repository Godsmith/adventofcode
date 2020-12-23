from collections import deque

from aocd import data

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
        if destination_number == 0:
            destination_number = len(cups)
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


cups = {}
for cup, cup_after in zip(data, data[1:]):
    cups[int(cup)] = int(cup_after)
cups[int(data[-1])] = int(data[0])

move(cups, 100)

print_all_after_one(cups)

cups = {}
for cup, cup_after in zip(data, data[1:]):
    cups[int(cup)] = int(cup_after)
cups[int(data[-1])] = 10
for i, j in zip(range(10, 1000001), range(11, 1000002)):
    cups[i] = j
cups[1000000] = int(data[0])
#print(cups[7])

move(cups, 10000000)

print(cups[1] * cups[cups[1]])
