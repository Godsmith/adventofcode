from aocd import data
from collections import namedtuple
from math import lcm
import sys

from aoc.utils import rows


# Part 1

def earliest_bus(timestamp, periods):
    best_period = None
    min_wait_time = sys.maxsize

    for period in periods:
        earliest_bus_arrival_time = (timestamp // period + 1) * period
        wait_time = earliest_bus_arrival_time - timestamp
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            best_period = period

    return best_period * min_wait_time


timestamp = int(rows(data)[0])
periods = list(
    map(int, (period for period in rows(data)[1].split(",") if period != "x")))
print(earliest_bus(timestamp, periods))

# Part 1 in one line

print(sorted([(period * ((timestamp // period + 1) * period - timestamp),
               (timestamp // period + 1) * period - timestamp) for period in periods],
             key=lambda x: x[1])[0][0])

# Part 2

Bus = namedtuple('Bus', "period offset")


def create_new_bus(bus1: Bus, bus2: Bus):
    time = bus1.offset
    while (time - bus2.offset) % bus2.period != 0:
        time += bus1.period
    return Bus(period=lcm(bus1.period, bus2.period), offset=time)


def find_magical_time(periods):
    bus = Bus(period=1, offset=0)
    for offset, period in enumerate(periods):
        if period != 'x':
            next_bus = Bus(period=int(period), offset=offset)
            bus = create_new_bus(bus, next_bus)
    return bus.period - bus.offset


all_periods = rows(data)[1].split(",")
print(find_magical_time(all_periods))
