from aoc2022.day1.calorie_counts import get_counts_per_elf, solution_a, solution_b

TEST_INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

def test_counts_per_elf():
    print(TEST_INPUT)
    counts = get_counts_per_elf(TEST_INPUT)
    assert len(counts) == 5
    assert counts == [6000, 4000, 11000, 24000, 10000]

def test_solution_a():
    elf, calories = solution_a(TEST_INPUT)
    assert elf == 3
    assert calories == 24000

def test_solution_b():
    sum_top_three = solution_b(TEST_INPUT)    
    assert sum_top_three == 45000