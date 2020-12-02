from aocd import data
from aoc.utils import rows
from collections import Counter

count = 0
count2 = 0
for row in rows(data):
    n1, n2, letter, text = row.replace(":", "").replace("-", " ").split()
    n1 = int(n1)
    n2 = int(n2)

    counter = Counter(text)
    if n1 <= counter[letter] <= n2:
        count += 1

    counter2 = Counter([text[n1 - 1], text[n2 - 1]])
    if counter2[letter] == 1:
        count2 += 1

print(count, count2)
