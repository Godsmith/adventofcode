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
        # A leftward rotation is a rightward rotation with a mirrored starting value
        mirrored_value = (100 - value) % 100 if direction == -1 else value
        count += (mirrored_value + steps) // 100
        value = (value + direction * steps) % 100
    print(count)


if __name__ == "__main__":
    main()
