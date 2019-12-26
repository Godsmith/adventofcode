from aoc.year2019.day14.day14 import ore_needed_for_fuel, reactions_from_data, \
    bsearch


class TestOreNeededForFuel:
    def test_single_fuel(self):
        reactions = reactions_from_data("1 ORE => 1 FUEL")
        assert ore_needed_for_fuel(1, reactions) == 1

    def test_two_reactions_needed(self):
        reactions = reactions_from_data("1 ORE => 1 FUEL")
        assert ore_needed_for_fuel(2, reactions) == 2

    def test_two_ore_needed_per_reaction(self):
        reactions = reactions_from_data("2 ORE => 1 FUEL")
        assert ore_needed_for_fuel(1, reactions) == 2

    def test_two_steps(self):
        reactions = reactions_from_data("""1 ORE => 1 A 
                                           1 A => 1 FUEL""")
        assert ore_needed_for_fuel(1, reactions) == 1

    def test_uneven(self):
        reactions = reactions_from_data("""1 ORE => 3 A 
                                           4 A => 1 FUEL""")
        assert ore_needed_for_fuel(1, reactions) == 2

    def test_reuse_leftovers(self):
        reactions = reactions_from_data("""1 ORE => 3 A
                                           4 A => 1 FUEL""")
        assert ore_needed_for_fuel(1, reactions) == 2


class TestSystem:
    def test_A(self):
        s = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""
        assert ore_needed_for_fuel(1, reactions_from_data(s)) == 31


class TestBsearch:
    def test_basic(self):
        f = lambda x: x * 2
        assert bsearch(f, 10, 1, 10) == 5

    def test_uneven(self):
        f = lambda x: x * 2
        assert bsearch(f, 11, 1, 10) == 5
