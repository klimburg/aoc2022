import pytest

from aoc2022.day6.tuning_trouble import solution_a

TEST_INPUTS = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]
TEST_RESULTS = [7, 5, 6, 10, 11]


@pytest.mark.parametrize("input,result", (zip(TEST_INPUTS, TEST_RESULTS)))
def test_solution_a(input, result):
    assert solution_a(input) == result
