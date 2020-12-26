from itertools import count

CARD_PUBLIC_KEY = 14205034
DOOR_PUBLIC_KEY = 18047856

def transform_one_step(value, subject_number):
    return (value * subject_number) % 20201227

def transform(loop_size, subject_number=7):
    value = 1
    for _ in range(loop_size):
        value = transform_one_step(value, subject_number)
    return value


def get_loop_size(target, subject_number=7):
    value = 1
    for loop_size in count(1):
        value = transform_one_step(value, subject_number)
        if value == target:
            return loop_size


card_loop_size = get_loop_size(CARD_PUBLIC_KEY)
print(transform(card_loop_size, DOOR_PUBLIC_KEY))
