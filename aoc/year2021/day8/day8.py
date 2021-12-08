from aocd import get_data
from aoc.utils import rows


def digit_count(lines, *signal_pattern_lengths):
    output_values = [line.split("|")[1].strip() for line in lines]
    character_counts = [len(value) for line in output_values for value in line.split()]
    return sum(character_counts.count(length) for length in signal_pattern_lengths)


def get_output_value(line):
    signal_patterns = [set(s) for s in line.split("|")[0].split()]
    wire_for_segment = {}

    def wire_sets_with_length(length):
        return [set(signal_pattern) for signal_pattern in signal_patterns if len(signal_pattern) == length]

    wire_set_for_digit = {1: wire_sets_with_length(2)[0], 4: wire_sets_with_length(4)[0],
                          7: wire_sets_with_length(3)[0], 8: wire_sets_with_length(7)[0]}

    # a
    wire_for_segment["a"] = (wire_set_for_digit[7] - wire_set_for_digit[1]).pop()

    # g
    for wire_set in wire_sets_with_length(6):
        if wire_set_for_digit[4].issubset(wire_set):
            wire_set_for_digit[9] = wire_set
            wire_for_segment["g"] = (wire_set_for_digit[9] - wire_set_for_digit[4] - {wire_for_segment["a"]}).pop()

    # e
    wire_for_segment['e'] = (wire_set_for_digit[8] - wire_set_for_digit[9]).pop()

    # c
    for wire_set in wire_sets_with_length(6):
        difference_compared_to_eight = wire_set_for_digit[8] - wire_set
        if difference_compared_to_eight.issubset(wire_set_for_digit[1]):
            wire_set_for_digit[6] = wire_set
            wire_for_segment['c'] = difference_compared_to_eight.pop()

    # d
    for wire_set in wire_sets_with_length(5):
        if wire_set_for_digit[7].issubset(wire_set):
            wire_for_segment["d"] = (wire_set - wire_set_for_digit[7] - {wire_for_segment["g"]}).pop()
            wire_set_for_digit[3] = wire_set

    # f
    wire_for_segment["f"] = (wire_set_for_digit[1] - {wire_for_segment["c"]}).pop()

    # b
    wire_for_segment["b"] = (wire_set_for_digit[9] - wire_set_for_digit[3]).pop()

    # Remaining digits
    wire_set_for_digit[0] = wire_set_for_digit[8] - {wire_for_segment["d"]}
    wire_set_for_digit[2] = wire_set_for_digit[8] - {wire_for_segment["b"]} - {wire_for_segment["f"]}
    wire_set_for_digit[5] = wire_set_for_digit[6] - {wire_for_segment["e"]}

    # Reverse dictionary for easy lookup
    digit_from_wire_set = {frozenset(wire_set_for_digit[i]): i for i in wire_set_for_digit.keys()}

    output_signal_patterns = [frozenset(s) for s in line.split("|")[1].split()]
    return sum(digit_from_wire_set[signal_pattern] * value for signal_pattern, value in
               zip(output_signal_patterns, [1000, 100, 10, 1]))


lines = rows(get_data())
print(digit_count(lines, 2, 3, 4, 7))
print(sum(get_output_value(line) for line in lines))
