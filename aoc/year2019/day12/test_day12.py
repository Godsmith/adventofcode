from aoc.year2019.day12.day12 import Moon, Simulation


class TestMoon:
    def test_from_string(self):
        moon = Moon.from_string("<x=14, y=9, z=13>")
        assert moon.pos == (14, 9, 13)


class TestSimulation:
    def test_energy(self):
        moon_strings = """pos=<x= 2, y= 1, z=-3>, vel=<x=-3, y=-2, z= 1>
pos=<x= 1, y=-8, z= 0>, vel=<x=-1, y= 1, z= 3>
pos=<x= 3, y=-6, z= 1>, vel=<x= 3, y= 2, z=-3>
pos=<x= 2, y= 0, z= 4>, vel=<x= 1, y=-1, z=-1>""".split('\n')
        moons = list(map(Moon.from_string, moon_strings))

        simulation = Simulation(moons)
        assert simulation.energy == 179

    def test_energy_after_steps(self):
        moon_strings = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>""".split("\n")
        moons = list(map(Moon.from_string, moon_strings))
        simulation = Simulation(moons)

        assert simulation.energy_after_steps(100) == 1940

    def test_step(self):
        moon_strings = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>""".split("\n")
        moons = list(map(Moon.from_string, moon_strings))
        simulation = Simulation(moons)

        simulation.step()
        assert str(simulation) == """pos=<x=2, y=-1, z=1>, vel=<x=3, y=-1, z=-1>
pos=<x=3, y=-7, z=-4>, vel=<x=1, y=3, z=3>
pos=<x=1, y=-7, z=5>, vel=<x=-3, y=1, z=-3>
pos=<x=2, y=2, z=0>, vel=<x=-1, y=-3, z=1>"""
