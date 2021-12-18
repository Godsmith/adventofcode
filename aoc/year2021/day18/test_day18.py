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
        assert SnailfishNumber._parse(deque("[1,2]")) == [1,2]
        assert SnailfishNumber._parse(deque("[1,[2,3]]")) == [1,[2,3]]

    @pytest.mark.xfail
    def test_explode(self):
        s = SnailfishNumber('[[[[[9,8],1],2],3],4]')
        s.explode(0)
        assert str(s) == '[[[[0,9],2],3],4]'