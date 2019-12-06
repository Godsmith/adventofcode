from collections import defaultdict

from aocd import data

class Planet:
    def __init__(self):
        self.parent = None

    @property
    def parents(self):
        planet = self
        while planet.parent:
            yield planet.parent
            planet = planet.parent

def main():
    planets = defaultdict(Planet)
    for row in data.split('\n'):
        parent, planet = row.split(')')
        planets[planet].parent = planets[parent]
    print(sum(len(list(planet.parents)) for planet in planets.values()))

if __name__ == '__main__':
    main()

