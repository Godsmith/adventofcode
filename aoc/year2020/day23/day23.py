from collections import deque

from aocd import data

print(data)

cups = deque(map(int, data))

#cups = deque([3,8,9,1,2,5,4,6,7])

def move(cups, moves):
    for i in range(moves):
        print(i)
        #print(cups)
        current_cup = cups[0]
        cups.rotate(-1)
        picked_up = deque()
        picked_up.append(cups.popleft())
        picked_up.append(cups.popleft())
        picked_up.append(cups.popleft())
        #print(f"pick up: {picked_up}")
        destination_cup = current_cup - 1
        while destination_cup not in cups:
            destination_cup -= 1
            if destination_cup < min(cups):
                destination_cup = max(cups)
        #print(f"destination: {destination_cup}")
        destination_index = cups.index(destination_cup) + 1
        cups.insert(destination_index, picked_up.pop())
        cups.insert(destination_index, picked_up.pop())
        cups.insert(destination_index, picked_up.pop())
    return cups

while cups[0] != 1:
    cups.rotate()
print(''.join(map(str,list(move(cups, 100))[1:])))

cups = deque(list(cups) + list(range(10, 1000001)))
print(''.join(map(str,list(move(cups, 10000000))[1:])))
