from aocd import get_data
from aoc.utils import rows

lines = rows(get_data())

ILLEGAL_POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
COMPLETION_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}
CLOSING = {"(": ")", "[": "]", "{": "}", "<": ">"}

illegal_score = 0
completion_scores = []
for line in lines:
    chunk = []
    for c in line:
        if c in "([{<":
            chunk.append(c)
        elif c == CLOSING[chunk[-1]]:
            chunk.pop()
        else:
            illegal_score += ILLEGAL_POINTS[c]
            break
    else:
        completion_score = 0
        for c in map(CLOSING.get, reversed(chunk)):
            completion_score = completion_score * 5 + COMPLETION_POINTS[c]
        completion_scores.append(completion_score)

print(illegal_score)
print(sorted(completion_scores)[(len(completion_scores) - 1) // 2])
