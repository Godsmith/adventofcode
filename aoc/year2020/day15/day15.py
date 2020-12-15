def last_number2(numbers, count):
    locations = {}
    for i, number in enumerate(numbers):
        locations[number] = i
    while len(numbers) < count:
        numbers.append(len(numbers) - 1 - locations[numbers[-1]]
                       if numbers[-1] in locations
                       else 0)
        locations[numbers[-2]] = len(numbers) - 2
    return numbers[-1]


print(last_number2([0, 5, 4, 1, 10, 14, 7], 2020))
print(last_number2([0, 5, 4, 1, 10, 14, 7], 30000000))
