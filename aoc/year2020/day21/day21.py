import re

from aocd import data
from aoc.utils import rows

possible_ingredients_from_allergen = {}
all_ingredients = set()
for row in rows(data):
    ingredients = re.findall('(\S+)', row.split("(")[0])
    all_ingredients.update(ingredients)
    allergens = re.findall('([a-z]+)', row.split("contains")[1])
    for allergen in allergens:
        if allergen not in possible_ingredients_from_allergen:
            possible_ingredients_from_allergen[allergen] = set(ingredients)
        else:
            ingredients_to_discard = []
            for ingredient in possible_ingredients_from_allergen[allergen]:
                if ingredient not in ingredients:
                    ingredients_to_discard.append(ingredient)
            for ingredient in ingredients_to_discard:
                possible_ingredients_from_allergen[allergen].discard(ingredient)

all_ingredients_that_can_contain_allergens = set()
for ingredients in possible_ingredients_from_allergen.values():
    all_ingredients_that_can_contain_allergens.update(ingredients)

count = 0
for row in rows(data):
    ingredients = re.findall('(\S+)', row.split("(")[0])
    for ingredient in ingredients:
        if ingredient not in all_ingredients_that_can_contain_allergens:
            count += 1
print(count)

ingredient_from_allergen = {}
while len(ingredient_from_allergen) < len(possible_ingredients_from_allergen):
    for allergen in possible_ingredients_from_allergen:
        if len(possible_ingredients_from_allergen[allergen]) == 1:
            ingredient = list(possible_ingredients_from_allergen[allergen])[0]
            ingredient_from_allergen[allergen] = ingredient
            for allergen2 in possible_ingredients_from_allergen:
                possible_ingredients_from_allergen[allergen2].discard(ingredient)

print(','.join(ingredient_from_allergen[allergen] for allergen in sorted(list(ingredient_from_allergen.keys()))))
