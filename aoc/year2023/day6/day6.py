from tqdm import tqdm
import math


def distance_travelled(charge_up_time: int, time: int):
    speed = charge_up_time
    time_to_move = time - charge_up_time
    return time_to_move * speed


# Very slow, could be made much faster by Newton search for example
def ways_to_win(time: int, distance: int):
    ways = 0
    for charge_up_time in tqdm(range(time)):
        if distance_travelled(charge_up_time, time) > distance:
            ways += 1
    return ways


import math

print(
    math.prod(
        ways_to_win(t, d) for t, d in ((40, 233), (82, 1011), (84, 1110), (92, 1487))
    )
)
print(ways_to_win(71530, 940200))
print(ways_to_win(40828492, 233101111101487))
