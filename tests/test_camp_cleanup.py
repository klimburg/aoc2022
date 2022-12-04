"""Tests for AOC day 4"""
import pytest

from aoc2022.day4.camp_cleanup import (
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
    assert make_range("2-4") == {2, 3, 4}
    assert make_range("123-125") == {123, 124, 125}


def test_parse_line():
    """Test a given line returns two sets as expected"""
    lines = TEST_INPUT.strip().split("\n")
    assert parse_line(lines[0]) == ({2, 3, 4}, {6, 7, 8})
    assert parse_line(lines[2]) == ({5, 6, 7}, {7, 8, 9})


@pytest.mark.parametrize(
    "set_a,set_b,overlap",
    [
        ({2, 3, 4}, {3, 4}, True),  # right is subset of left
        ({3, 4}, {2, 3, 4}, True),  # left is subset of right
        ({1, 2, 3}, {4, 5}, False),  # no subset
    ],
)
def test_fully_overlap(set_a, set_b, overlap):
    """test given two sets we can determine if either one is a subset of the other"""
    assert fully_overlap(set_a, set_b) is overlap


@pytest.mark.parametrize(
    "set_a,set_b,overlap",
    [
        ({2, 3, 4}, {3}, True),  # full overlap
        ({2, 3}, {3, 4}, True),  # partial overlap
        ({1, 2, 3}, {4, 5}, False),  # no overlap
    ],
)
def test_any_overlap(set_a, set_b, overlap):
    """test given two sets we can determine if either one is a subset of the other"""
    assert any_overlap(set_a, set_b) is overlap


def test_solution_a():
    """Test for solution a"""
    assert solution_a(TEST_INPUT) == 2


def test_solution_b():
    """ "Test for solution b"""
    assert solution_b(TEST_INPUT) == 4
