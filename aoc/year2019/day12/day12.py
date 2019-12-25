import re
from math import sqrt, gcd
from typing import Tuple

from aocd import data

from aoc.utils import rows, sign_of_difference


class Moon:
    def __init__(self, pos, vel=(0, 0, 0)):
        self.pos = pos
        self.vel = vel

    def __repr__(self):
        return "pos=<x=%s, y=%s, z=%s>, vel=<x=%s, y=%s, z=%s>" % (self.pos + self.vel)

    @classmethod
    def from_string(cls, s):
        if "pos=" in s:
            pattern = "pos=<x=(.*), y=(.*), z=(.*)>, vel=<x=(.*), y=(.*), z=(.*)>"
            groups = re.match(pattern, s).groups()
            pos = tuple(map(int, groups[0:3]))
            vel = tuple(map(int, groups[3:6]))
            return cls(pos, vel)
        else:
            pattern = "<x=(.*), y=(.*), z=(.*)>"
            return cls(tuple(map(int, re.match(pattern, s).groups())))

    @property
    def energy(self):
        potential_energy = sum(map(abs, self.pos))
        kinetic_energy = sum(map(abs, self.vel))
        return potential_energy * kinetic_energy

    def add_vel(self, vel: Tuple[int, int, int]):
        self.vel = tuple(vel[i] + self.vel[i] for i in range(3))

    def move(self):
        self.pos = tuple(self.pos[i] + self.vel[i] for i in range(3))


class Simulation:
    def __init__(self, moons):
        self.moons = moons

    def __repr__(self):
        return '\n'.join(repr(moon) for moon in self.moons)

    def step(self):
        for moon in self.moons:
            other_moons = [other_moon for other_moon in self.moons if
                           moon != other_moon]
            for other_moon in other_moons:
                moon.add_vel(self._delta_vel(moon.pos, other_moon.pos))

        for moon in self.moons:
            moon.move()

    def _delta_vel(self, pos1: Tuple[int, int, int], pos2: Tuple[int, int, int]) -> \
            Tuple[
                int, int, int]:
        return tuple(sign_of_difference(pos2[i], pos1[i]) for i in range(3))

    @property
    def energy(self):
        return sum(moon.energy for moon in self.moons)

    def energy_after_steps(self, count):
        for _ in range(count):
            self.step()
        return self.energy

    def first_repeating(self, i):
        count_from_pos_vel = {}
        count = 0
        while True:
            pos_and_vel = tuple((moon.pos[i], moon.vel[i]) for moon in
                                self.moons)
            if pos_and_vel in count_from_pos_vel:
                return count

            count_from_pos_vel[pos_and_vel] = count
            count += 1
            self.step()

    @property
    def cycle_length(self):
        x = self.first_repeating(0)
        y = self.first_repeating(1)
        z = self.first_repeating(2)
        common_divisor = gcd(x, gcd(y, z))

        return int(x * y * z / pow(common_divisor, 3))


def main():
    moons = list(map(Moon.from_string, rows(data)))
    simulation = Simulation(moons)
    print(simulation.energy_after_steps(1000))

    simulation = Simulation(moons)
    print(simulation.cycle_length)


if __name__ == '__main__':
    main()
