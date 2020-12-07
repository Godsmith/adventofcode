from aocd import data
from aoc.utils import rows
import re

bags = {}
for row in rows(data):
    color = re.match("(.*) bags contain", row).groups()[0]
    contents = re.findall(r"(\d+) (.*?) bag", row)
    bags[color] = contents


def get_contained_colors(color):
    for _, subcolor in bags[color]:
        yield from get_contained_colors(subcolor)
        yield subcolor


def get_number_of_bags(color):
    return sum(int(count) + get_number_of_bags(subcolor) * int(count)
               for count, subcolor in bags[color])


print(len(list(color for color in bags if "shiny gold" in get_contained_colors(color))))
print(get_number_of_bags("shiny gold"))
