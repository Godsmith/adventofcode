from aocd import data


def main():
    #     data = """987654321111111
    # 811111111111119
    # 234234234234278
    # 818181911112111"""

    banks = list(map(lambda bank: list(map(int, bank)), data.splitlines()))

    sum_ = 0

    # for bank in banks:
    #     ints = list(map(int, bank))
    #     max_int = max(ints[:-1])
    #     max_int_index = ints.index(max_int)
    #     rest_of_ints = ints[max_int_index + 1 :]
    #     max_int_of_rest_of_ints = max(rest_of_ints)
    #     print(bank, ints, max_int, max_int_index, rest_of_ints, max_int_of_rest_of_ints)
    #     sum_ += 10 * max_int + max_int_of_rest_of_ints
    # print(sum_)
    # Part 1
    # BATTERY_COUNT = 2
    # Part 2
    BATTERY_COUNT = 12
    for bank in banks:
        digits = []
        current_bank = bank
        for i in range(BATTERY_COUNT - 1, -1, -1):
            index = next_index(current_bank, i)
            # print(current_bank, index)
            digits.append(current_bank[index])
            current_bank = current_bank[index + 1 :]
        joltage = int("".join(map(str, digits)))
        print(joltage)
        sum_ += joltage
    print(sum_)


def next_index(bank: list[int], digits_left_after: int):
    bank = bank.copy()
    bank = bank[:-digits_left_after] if digits_left_after else bank
    max_int = max(bank)
    index = bank.index(max_int)
    # print(bank, max_int, index)
    return index


if __name__ == "__main__":
    main()
