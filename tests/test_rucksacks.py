"""Tests for day3"""

from aoc2022.day3.rucksacks import *

TEST_INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_solution_a():
    score = solution_a(TEST_INPUT)
    assert score == 157


def test_find_common_item():
    rucksacks = TEST_INPUT.strip().split()
    common_item = find_common_item(rucksacks[0])
    assert common_item == "p"
