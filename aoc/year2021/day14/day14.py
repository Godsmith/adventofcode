from collections import Counter

from aocd import get_data
from more_itertools import pairwise


def run(data, iterations):
    new_element_from_pair = {tuple(line.split(" -> ")[0]): line.split(" -> ")[1] for line in data.splitlines()[2:]}
    new_pairs_from_pair = {(e1, e2): [(e1, inserted), (inserted, e2)] for (e1, e2), inserted in new_element_from_pair.items()}

    template = data.splitlines()[0]
    element_counter = Counter(template)
    pair_counter = Counter(pairwise(template))

    for _ in range(iterations):
        new_pair_counter = Counter()
        for pair in pair_counter:
            for new_pair in new_pairs_from_pair[pair]:
                new_pair_counter[new_pair] += pair_counter[pair]
            element_counter[new_element_from_pair[pair]] += pair_counter[pair]
        pair_counter = new_pair_counter

    return element_counter.most_common()[0][1] - element_counter.most_common()[-1][1]


print(run(get_data(), 10))
print(run(get_data(), 40))
