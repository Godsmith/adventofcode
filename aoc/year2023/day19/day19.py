from dataclasses import dataclass
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


@dataclass
class Rule:
    category: str
    operator: Operator
    value: int
    destination: str

    def applies_to(self, part: Part):
        return self.operator(getattr(part, self.category), self.value)


@dataclass
class Workflow:
    rules: list[Rule]
    default_destination: str

    def get_destination(self, part: Part) -> str:
        for rule in self.rules:
            if rule.applies_to(part):
                return rule.destination
        return self.default_destination


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
        rules.append(Rule(category, operator_, int(value_string), destination))
    workflows[name] = Workflow(rules, default_destination)

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
