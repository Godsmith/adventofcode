import copy
from dataclasses import dataclass, field
from itertools import chain
import re
import operator
from typing import Any, Callable
from collections import namedtuple
from aocd import data

Operator = Callable[[Any, Any], bool]

# data = """px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}

# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}"""

Part = namedtuple("Part", ["x", "m", "a", "s"])

accept_all_operator = lambda x, y: True


@dataclass(frozen=True)
class Rule:
    destination: str
    category: str = "x"
    operator: Operator = accept_all_operator
    value: int = 0

    def applies_to(self, part: Part):
        return self.operator(getattr(part, self.category), self.value)


@dataclass
class Workflow:
    name: str
    rules: list[Rule]

    def get_destination(self, part: Part) -> str:
        for rule in self.rules:
            if rule.applies_to(part):
                return rule.destination


workflows_chunk, parts_chunk = data.split("\n\n")

workflow_rows = workflows_chunk.splitlines()
workflows: dict[str, Workflow] = {}
for row in workflow_rows:
    name, rest = row.split("{")
    rule_strings = rest[:-1].split(",")
    default_destination = rule_strings[-1]
    rules = []
    for rule_string in rule_strings[:-1]:
        operator_ = operator.gt if ">" in rule_string else operator.lt
        condition_string, destination = rule_string.split(":")
        category, value_string = re.split("[<>]", condition_string)
        rules.append(Rule(destination, category, operator_, int(value_string)))
    rules.append(Rule(default_destination))
    workflows[name] = Workflow(name, rules)

parts_rows = parts_chunk.splitlines()
parts = [Part(*map(int, re.findall(r"\d+", row))) for row in parts_rows]


def get_destination(part: Part):
    destination = "in"
    while destination not in ("A", "R"):
        workflow = workflows[destination]
        destination = workflow.get_destination(part)
    return destination


accepted_parts = [part for part in parts if get_destination(part) == "A"]

print(sum(sum(part) for part in accepted_parts))


# Part 2
# Key finding: every workflow only ever sends to one place


def rating_range() -> list[int]:
    return list(range(1, 4001))


@dataclass
class PartRatingRange:
    x: list[int] = field(default_factory=rating_range)
    m: list[int] = field(default_factory=rating_range)
    a: list[int] = field(default_factory=rating_range)
    s: list[int] = field(default_factory=rating_range)

    def __repr__(self):
        return f"PartRatingRange(x={len(self.x)},m={len(self.m)},a={len(self.a)},s={len(self.s)})"

    @property
    def combinations(self):
        return len(self.x) * len(self.m) * len(self.a) * len(self.s)


def comply_with_rule(range_: PartRatingRange, rule: Rule):
    list_ = getattr(range_, rule.category)
    new_range = copy.deepcopy(range_)
    setattr(
        new_range,
        rule.category,
        [value for value in list_ if rule.operator(value, rule.value)],
    )
    return new_range


def skip_rule(range_: PartRatingRange, rule: Rule):
    list_ = getattr(range_, rule.category)
    new_range = copy.deepcopy(range_)
    setattr(
        new_range,
        rule.category,
        [value for value in list_ if not rule.operator(value, rule.value)],
    )
    return new_range


accepted_ranges = []
ranges_and_workflows: list[tuple[PartRatingRange, Workflow]] = [
    (PartRatingRange(), workflows["in"])
]
while ranges_and_workflows:
    prr, workflow = ranges_and_workflows.pop()
    for rule in workflow.rules:
        new_prr = comply_with_rule(prr, rule)
        if rule.destination == "A":
            accepted_ranges.append(new_prr)
        elif rule.destination == "R":
            pass
        else:
            ranges_and_workflows.append((new_prr, workflows[rule.destination]))
        prr = skip_rule(prr, rule)

print(accepted_ranges)
print(sum(range_.combinations for range_ in accepted_ranges))
