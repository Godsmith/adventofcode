from aocd import data
from aoc.utils import rows
import re
from functools import partial

rules = {}
for row in rows(data):
    if ":" in row:
        id_, rule = re.match(r"(\d*): (.*)", row).groups()
        rules[int(id_)] = rule

messages = [row for row in rows(data) if ":" not in row and row != ""]

max_recursion_depth = max(map(len, messages))


def regex_rule_from_match(match: re.Match, depth):
    if depth > max_recursion_depth:
        return ""
    return regex_for_rule(rules[int(match.group())], depth=depth + 1)


def regex_for_rule(rule, depth=1):
    if match := re.match(r'"(.)"', rule):
        return match.groups()[0]
    regex_rule_from_match_with_depth = partial(regex_rule_from_match, depth=depth)
    regex = re.sub(r"\b\d+\b", regex_rule_from_match_with_depth, rule)
    return f"({regex.replace(' ', '')})"


def count_messages_that_match_rule_0():
    pattern = re.compile(regex_for_rule("^" + rules[0] + "$"))
    return len([message for message in messages if re.match(pattern, message)])


print(count_messages_that_match_rule_0())

rules[8] = "42 | 42 8"
rules[11] = "42 31 | 42 11 31"

print(count_messages_that_match_rule_0())
