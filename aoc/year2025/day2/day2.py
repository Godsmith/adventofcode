import itertools

from aocd import data

# data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

count = 0
ranges = data.split(",")
for r in ranges:
    start, stop = map(int, r.split("-"))
    for id_ in range(start, stop + 1):
        str_id = str(id_)
        # print(f"{id_=}")
        for length in range(1, len(str_id) // 2 + 1):
            batches = list(itertools.batched(str(id_), length))
            # Part 1
            # if len(batches) == 2 and batches[0] == batches[1]:
            # Part 2
            if len(set(batches)) == 1:
                print(id_)
                count += id_
                break
print(count)
