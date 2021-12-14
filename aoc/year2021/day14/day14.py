from collections import Counter

from aocd import get_data
from more_itertools import pairwise


def get_rules(data):
    return {tuple(line.split(" -> ")[0]): line.split(" -> ")[1] for line in data.splitlines()[2:]}


def part1(data):
    template = data.splitlines()[0]
    rules = get_rules(data)

    for _ in range(10):
        new_template = []
        for pair in pairwise(template):
            new_template.append(pair[0])
            if pair in rules:
                new_template.append(rules[pair])
        new_template.append(template[-1])
        template = new_template

    most_common = Counter(template).most_common()
    print(most_common[0][1] - most_common[-1][1])


def part2(data):
    element_rules = get_rules(data)
    pair_rules = {(e1, e2): [(e1, inserted), (inserted, e2)] for (e1, e2), inserted in element_rules.items()}

    template = data.splitlines()[0]
    element_counter = Counter(template)
    pair_counter = Counter(pairwise(template))

    for _ in range(40):
        new_pair_counter = Counter()
        for pair in pair_counter:
            for new_pair in pair_rules[pair]:
                new_pair_counter[new_pair] += pair_counter[pair]
            element_counter[element_rules[pair]] += pair_counter[pair]
        pair_counter = new_pair_counter

    print(element_counter.most_common()[0][1] - element_counter.most_common()[-1][1])


part1(get_data())
part2(get_data())
