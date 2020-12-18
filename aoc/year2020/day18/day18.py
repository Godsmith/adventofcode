from aocd import data
from aoc.utils import rows
import re


class Number:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        self.number += other.number
        return self

    def __sub__(self, other):
        self.number *= other.number
        return self


class Number2(Number):
    def __mul__(self, other):
        self.number += other.number
        return self


print(sum(eval(
    re.sub(r"(\d)", r"Number(\1)", row).replace("*", "-")).number
          for row in rows(data)))
print(sum(eval(
    re.sub(r"(\d)", r"Number2(\1)", row).replace("*", "-").replace("+", "*")).number
          for row in rows(data)))
