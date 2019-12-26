from dataclasses import dataclass
from collections import Counter
from math import ceil
from queue import Queue
from typing import Dict

from aocd import data


@dataclass
class Recipe:
    output_reagent: str
    output_amount: int
    inputs: Counter

    def __repr__(self):
        return f"{self.inputs} => {self.output_amount} {self.output_reagent}"

    @classmethod
    def from_string(cls, s):
        inputs = Counter()
        all_inputs_string, output_string = s.split('=>')
        input_strings = all_inputs_string.split(',')
        for input_string in input_strings:
            amount_string, reagent_string = input_string.strip().split(' ')
            inputs[reagent_string.strip()] = int(amount_string)

        output_amount_string, output_reagent_string = output_string.strip().split(
            ' ')
        return cls(output_reagent_string.strip(), int(output_amount_string),
                   inputs)


def reactions_from_data(data):
    # print(data)
    out = {}
    for row in data.split('\n'):
        recipe = Recipe.from_string(row)
        out[recipe.output_reagent] = recipe

    return out


def ore_needed_for_fuel(fuel_amount, recipes: Dict[str, Recipe]):
    reserves = Counter()
    orders = Queue()
    orders.put({"ingredient": "FUEL", "amount": fuel_amount})
    ore_needed = 0
    while not orders.empty():
        order = orders.get()
        ingredient = order["ingredient"]
        amount_needed = order["amount"]
        if ingredient == 'ORE':
            ore_needed += amount_needed
        elif amount_needed <= reserves[ingredient]:
            reserves -= Counter({ingredient: amount_needed})
        else:
            amount_needed -= reserves[ingredient]
            recipe = recipes[ingredient]
            batches = ceil(amount_needed / recipe.output_amount)
            for input_ in recipe.inputs:
                new_order = {"ingredient": input_,
                             "amount": recipe.inputs[input_] * batches}
                orders.put(new_order)
            leftover_amount = batches * recipe.output_amount - amount_needed
            reserves[ingredient] = leftover_amount
    return ore_needed

def bsearch(f, target, low, high):
    """ Given a function f(x), return the value x for which f(x) is closest to
    but does not exceed target. x is between low and high."""
    if abs(low - high) <= 1:
        if f(high) == target:
            return high
        return low
    low_value = f(low)
    high_value = f(high)
    middle = (low + high) // 2
    #print(f"f({low}) == {low_value}, f({high}) == {high_value}")
    if abs(low_value - target) < abs(high_value - target):
        return bsearch(f, target, low, middle)
    else:
        return bsearch(f, target, middle, high)



def main():
    reactions = reactions_from_data(data)
    print(ore_needed_for_fuel(1, reactions))

    f = lambda x: ore_needed_for_fuel(x, reactions)
    print(bsearch(f, 1000000000000, 1, 1000000000))


if __name__ == '__main__':
    main()
