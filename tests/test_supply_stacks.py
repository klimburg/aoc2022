"""tests for day 5"""
# pylint: disable=missing-function-docstring

from aoc2022.day5.supply_stacks import parse_input, solution_a, solution_b

TEST_INPUT = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".lstrip(
    "\n"
)


def test_parse_input():
    stacks, instructions = parse_input(TEST_INPUT)
    print(stacks)
    assert stacks == [["Z", "N"], ["M", "C", "D"], ["P"]]


def test_solution_a():
    assert solution_a(TEST_INPUT) == "CMZ"

def test_solution_b():
    assert solution_b(TEST_INPUT) == "MCD"
