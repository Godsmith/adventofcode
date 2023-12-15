def distance_travelled(charge_up_time: int, time: int):
    speed = charge_up_time
    time_to_move = time - charge_up_time
    return time_to_move * speed

def ways_to_win(time:int, distance: int):
    return len([1 for charge_up_time in range(time) if distance_travelled(charge_up_time, time) > distance])

import math

print(math.prod(ways_to_win(t, d) for t, d in ((40,233),(82,1011),(84,1110),(92,1487))))
