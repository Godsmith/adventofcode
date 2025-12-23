from aocd import data

value = 50
count = 0

# data = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82"""

rotations = data.splitlines()

for rotation in rotations:
    direction = 1 if rotation.startswith("R") else -1
    steps = int(rotation[1:])
    for _ in range(steps):
        value += direction
        value %= 100
        if value == 0:
            count += 1
    print(value)
print(count)
