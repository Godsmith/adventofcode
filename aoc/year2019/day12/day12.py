import re
from typing import Tuple

from aocd import data

from aoc.utils import rows


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
            pos = tuple(map( int, groups[0:3]))
            vel = tuple(map( int, groups[3:6]))
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

    def _delta_vel(self, pos1: Tuple[int, int, int], pos2: Tuple[int, int, int]) -> Tuple[
        int, int, int]:
        return tuple(self._sign_of_difference(pos2[i], pos1[i]) for i in range(3))

    @staticmethod
    def _sign_of_difference(a, b):
        if a == b:
            return 0
        else:
            return int((a - b) / abs(a - b))


    @property
    def energy(self):
        return sum(moon.energy for moon in self.moons)

    def energy_after_steps(self, count):
        for _ in range(count):
            self.step()
        return self.energy


def main():
    moons = list(map(Moon.from_string, rows(data)))
    simulation = Simulation(moons)
    print(simulation.energy_after_steps(1000))


if __name__ == '__main__':
    main()
