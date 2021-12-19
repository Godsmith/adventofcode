from collections import deque

from aoc.year2021.day18.day18 import SnailfishNumber
import pytest


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
