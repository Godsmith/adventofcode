from aocd import data

groups = data.split('\n\n')
unique_answers_per_group = [set(group) - {'\n'} for group in groups]
print(sum(len(answers) for answers in unique_answers_per_group))

common_answers = 0
for group in groups:
    persons = [set(person) for person in group.split("\n")]
    common_answers += len(persons.pop().intersection(*persons))

print(common_answers)
