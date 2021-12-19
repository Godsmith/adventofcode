from collections import deque

from aoc.year2021.day18.snailfishnumber import SnailfishNumber


class TestSnailfishNumber:
    def test_repr(self):
        assert repr(SnailfishNumber("[[1,2],3]")) == "[[1,2],3]"
        assert repr(SnailfishNumber("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")) == "[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"

    def test_pop_until_enclosed_list_and_return(self):
        assert SnailfishNumber._pop_until_enclosed_list_and_return(deque("[1,2]")) == deque("[1,2]")
        assert SnailfishNumber._pop_until_enclosed_list_and_return(deque("[1,2]]")) == deque("[1,2]")
        assert SnailfishNumber._pop_until_enclosed_list_and_return(deque("[1,[2,3]]")) == deque("[1,[2,3]]")

    def test_parse(self):
        assert SnailfishNumber._parse(deque("[1,2]")) == [1, 2]
        assert SnailfishNumber._parse(deque("[1,[2,3]]")) == [1, [2, 3]]

    def test_parse_multidigit(self):
        assert SnailfishNumber._parse(deque("[10,2]")) == [10,2]


    def test_indices(self):
        assert SnailfishNumber("[1,2]")._locations() == [[0], [1]]
        assert SnailfishNumber("[1,[2,3]]")._locations() == [[0], [1, 0], [1, 1]]

    def test_indices_harder(self):
        assert SnailfishNumber("[[1,2],[3,4]]")._locations() == [[0, 0], [0, 1], [1, 0], [1, 1]]

    def test_getitem(self):
        assert SnailfishNumber("[1,2]")[[0]] == 1

    def test_setitem(self):
        s = SnailfishNumber("[1,2]")
        s[[0]] = 2
        assert repr(s) == "[2,2]"

    def test_setitem_nested(self):
        s = SnailfishNumber("[1,[2,3]]")
        s[[1, 1]] = 4
        assert repr(s) == "[1,[2,4]]"

    def test_getitem_nested(self):
        assert SnailfishNumber("[[1,2],[3,4]]")[[0, 0]] == 1
        assert SnailfishNumber("[[1,2],[3,4]]")[[1, 1]] == 4

    def test_explode_leftmost(self):
        s = SnailfishNumber('[[[[[9,8],1],2],3],4]')
        s._explode()
        assert str(s) == '[[[[0,9],2],3],4]'

    def test_explode_rightmost(self):
        s = SnailfishNumber('[7,[6,[5,[4,[3,2]]]]]')
        s._explode()
        assert str(s) == '[7,[6,[5,[7,0]]]]'

    def test_explode_again(self):
        s = SnailfishNumber('[[6,[5,[4,[3,2]]]],1]')
        s._explode()
        assert str(s) == '[[6,[5,[7,0]]],3]'

    def test_explode_to_new_explosion_risk(self):
        s = SnailfishNumber('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')
        s._explode()
        assert str(s) == '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'

    def test_split(self):
        s = SnailfishNumber('[11,2]')
        s._split()
        assert str(s) == '[[5,6],2]'

    def test_add(self):
        s = SnailfishNumber('[[[[4,3],4],4],[7,[[8,4],9]]]') + SnailfishNumber('[1,1]')
        assert str(s) == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'

    def test_add_again(self):
        s = SnailfishNumber('[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]') + SnailfishNumber('[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]')
        assert str(s) == '[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]'
        assert s.magnitude == 3993

    def test_add_does_not_change_original_numbers(self):
        s1 = SnailfishNumber('[[[[4,3],4],4],[7,[[8,4],9]]]')
        s2 = SnailfishNumber('[1,1]')
        s1 + s2
        assert str(s1) == '[[[[4,3],4],4],[7,[[8,4],9]]]'
        assert str(s2) == '[1,1]'

    def test_magnitude(self):
        assert SnailfishNumber('[[1,2],[[3,4],5]]').magnitude == 143

    def test_final_sum(self):
        text = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
        s = SnailfishNumber.final_sum(text)
        assert str(s) == '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'
        assert s.magnitude == 4140

    def test_largest_permutation_magnitude(self):
        text = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""
        assert SnailfishNumber.largest_permutation_magnitude(text) == 3993


