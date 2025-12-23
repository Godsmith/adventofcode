from aocd import data


def main():
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
        count += zero_count(direction, steps, value)
        value += direction * steps
        value %= 100
    print(count)


def zero_count(direction, steps, value):
    count = 0
    for _ in range(steps):
        value += direction
        value %= 100
        if value == 0:
            count += 1
    return count


if __name__ == "__main__":
    main()
