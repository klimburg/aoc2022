"""Tests for AOC day 4"""
import pytest

from aoc2022.day4.camp_cleanup_no_sets import (
    any_overlap,
    fully_overlap,
    make_range,
    parse_line,
    solution_a,
    solution_b,
)

TEST_INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def test_make_range():
    """Test we can make a range from str rep"""
    assert make_range("2-4") == (2, 4)
    assert make_range("123-125") == (123, 125)


def test_parse_line():
    """Test a given line returns two sets as expected"""
    lines = TEST_INPUT.strip().split("\n")
    assert parse_line(lines[0]) == ((2, 4), (6, 8))
    assert parse_line(lines[2]) == ((5, 7), (7, 9))


@pytest.mark.parametrize(
    "range_a,range_b,overlap",
    [
        ((2, 4), (3, 4), True),  # right is subset of left
        ((3, 4), (2, 4), True),  # left is subset of right
        ((1, 3), (4, 5), False),  # no overlap
        ((1, 3), (2, 4), False),  # partial overlap
    ],
)
def test_fully_overlap(range_a, range_b, overlap):
    """test given two sets we can determine if either one is a subset of the other"""
    assert fully_overlap(range_a, range_b) is overlap


@pytest.mark.parametrize(
    "range_a,range_b,overlap",
    [
        ((2, 4), (3, 4), True),  # right is subset of left
        ((3, 4), (2, 4), True),  # left is subset of right
        ((1, 3), (4, 5), False),  # no overlap
        ((4, 5), (1, 3), False),  # no overlap
        ((1, 3), (2, 4), True),  # b starts in a
        ((2, 4), (1, 3), True),  # b ends in a, a starts in b
        ((5, 6), (4, 7), True),  # a is fully inside b
    ],
)
def test_any_overlap(range_a, range_b, overlap):
    """test given two sets we can determine if either one is a subset of the other"""
    assert any_overlap(range_a, range_b) is overlap


def test_solution_a():
    """Test for solution a"""
    assert solution_a(TEST_INPUT) == 2


def test_solution_b():
    """ "Test for solution b"""
    assert solution_b(TEST_INPUT) == 4
