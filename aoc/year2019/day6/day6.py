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

    def distance_to_planet(self, planet):
        return list(self.parents).index(planet)


def create_planets(data):
    planets = defaultdict(Planet)
    for row in data.split('\n'):
        parent, planet = row.split(')')
        planets[planet].parent = planets[parent]
    return planets


def first_common_object(list1, list2):
    for o in list1:
        if o in list2:
            return o


def distance_between(planets, planet1, planet2):
    planet = first_common_object(list(planets[planet1].parents),
                                 list(planets[planet2].parents))
    return planets['YOU'].distance_to_planet(planet) + planets[
        'SAN'].distance_to_planet(planet)


def main():
    planets = create_planets(data)
    print(sum(len(list(planet.parents)) for planet in planets.values()))
    print(distance_between(planets, 'YOU', 'SAN'))


if __name__ == '__main__':
    main()
