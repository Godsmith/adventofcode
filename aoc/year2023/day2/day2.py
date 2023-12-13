from collections import defaultdict
from aocd import data
from aoc.utils import rows
import math

color_maxes = {"red": 12, "green": 13, "blue": 14}

id_sum = 0
power_sum = 0

def is_impossible(draw_string):
    draws = draw_string.split(";")
    for draw in draws:
        for amount_and_color in draw.split(","):
            amount_and_color = amount_and_color.strip()
            amount, color = amount_and_color.split(" ")
            amount = int(amount)
            if color_maxes[color] < amount:
                return True
    return False

def power(draw_string) -> int:
    counts = defaultdict(int)
    draws = draw_string.split(";")
    for draw in draws:
        for amount_and_color in draw.split(","):
            amount_and_color = amount_and_color.strip()
            amount, color = amount_and_color.split(" ")
            amount = int(amount)
            counts[color] = max(amount, counts[color])
    return math.prod(counts.values())

for row in rows(data):
    game_and_number, draw_string = row.split(":")
    game_number = int(game_and_number.split(" ")[1])
    if not is_impossible(draw_string):
        id_sum += game_number

    power_sum += power(draw_string)




print(id_sum)
print(power_sum)

