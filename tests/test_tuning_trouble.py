import pytest

from aoc2022.day6.tuning_trouble import find_end_unique_counter, solution_a, solution_b

TEST_INPUTS = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]
TEST_RESULTS_A = [7, 5, 6, 10, 11]
TEST_RESULTS_B = [19, 23, 23, 29, 26]


@pytest.mark.parametrize("input,result", (zip(TEST_INPUTS, TEST_RESULTS_A)))
def test_solution_a(input, result):
    assert solution_a(input) == result


@pytest.mark.parametrize("input,result", (zip(TEST_INPUTS, TEST_RESULTS_B)))
def test_solution_b(input, result):
    assert solution_b(input) == result


@pytest.mark.parametrize("input,result", (zip(TEST_INPUTS, TEST_RESULTS_B)))
def test_solution_counter(input, result):
    assert find_end_unique_counter(input, 14) == result
