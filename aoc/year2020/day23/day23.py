from collections import deque

from aocd import data

class Cup:
    def __init__(self, number):
        self.number = number
        self.next_cup = None

    def __repr__(self):
        return f"Cup(number={self.number}, next_cup={self.next_cup.number})"

def print_cups(cup):
    for _ in cups:
        print(cup.number, end="")
        cup = cup.next_cup
    print()

def move(cups, moves):
    current_cup = list(cups.values())[0]
    for i in range(moves):
        print(i)
        #print_cups(current_cup)
        picked_up = []
        picked_up_numbers = set()
        cup_to_pick_up = current_cup.next_cup
        for _ in range(3):
            picked_up.append(cup_to_pick_up)
            picked_up_numbers.add(cup_to_pick_up.number)
            cup_to_pick_up = cup_to_pick_up.next_cup
        #print(f"picked up: {[cup.number for cup in picked_up]}")
        current_cup.next_cup = cup_to_pick_up
        destination_number = current_cup.number - 1
        if destination_number == 0:
            destination_number = len(cups)
        while destination_number in picked_up_numbers:
            destination_number -= 1
            if destination_number == 0:
                destination_number = len(cups)
        #print(f"destination: {destination_number}")
        destination_cup = cups[destination_number]
        picked_up[2].next_cup = destination_cup.next_cup
        destination_cup.next_cup = picked_up[0]
        current_cup = current_cup.next_cup

# DEBUG
#data = "389125467"
cups = {int(s): Cup(int(s)) for s in data}
for i, cup in enumerate(cups.values()):
    cup.next_cup = list(cups.values())[(i + 1) % len(cups)]

move(cups, 100)

cup = cups[1]
for _ in range(len(cups) - 1):
    cup = cup.next_cup
    print(cup.number, end="")


cups = {int(s): Cup(int(s)) for s in data}
for i in range(10, 1000001):
    cups[i] = Cup(i)
for i, cup in enumerate(cups.values()):
    cup.next_cup = list(cups.values())[(i + 1) % len(cups)]

move(cups, 10000000)

cup = cups[1]
for _ in range(len(cups) - 1):
    cup = cup.next_cup
    print(cup.number, end="")

#print(''.join(map(str,list(move(cups, 100))[1:])))

#cups = deque(list(cups) + list(range(10, 1000001)))
#print(''.join(map(str,list(move(cups, 10000000))[1:])))
