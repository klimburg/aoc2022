from aoc2022.day2.rock_paper_scissors import *

TEST_INPUT = """A Y
B X
C Z
"""


def test_solution_a():
    score = solution_a(TEST_INPUT)
    assert score == 15


def test_solution_b():
    score = solution_b(TEST_INPUT)
    assert score == 12