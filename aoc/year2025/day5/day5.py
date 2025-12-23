from aocd import data

# data = """3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32"""


def main():
    ranges_string, available_string = data.split("\n\n")
    range_strings = ranges_string.splitlines()
    available_strings = available_string.splitlines()
    available_ids = list(map(int, available_strings))
    range_tuples = []
    for range_string in range_strings:
        start, stop = range_string.split("-")
        range_tuples.append((int(start), int(stop)))

    print(range_tuples)
    print(available_ids)

    range_tuples.sort()
    finished_tuples = [range_tuples.pop(0)]
    while range_tuples:
        current_tuple = range_tuples.pop(0)
        if current_tuple[0] <= finished_tuples[-1][1]:
            finished_tuples[-1] = (
                finished_tuples[-1][0],
                max(finished_tuples[-1][1], current_tuple[1]),
            )
        else:
            finished_tuples.append(current_tuple)
    print(finished_tuples)

    count = 0
    for id_ in available_ids:
        for start, stop in finished_tuples:
            if start <= id_ <= stop:
                count += 1
    print(count)

    total_range_size = 0
    for start, stop in finished_tuples:
        total_range_size += stop - start + 1

    print(total_range_size)


if __name__ == "__main__":
    main()
