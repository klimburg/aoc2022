"""Solutions to day 1"""
from aoc2022.utils import read_input


def get_counts_per_elf(input_text: str) -> list[int]:
    """Input is a string of integers delimited by new lines
    blank lines indicate start of a new elfs calories
    """
    calorie_counts: list[int] = []
    calorie_count = 0
    for line in input_text.split("\n"):
        if line == "":
            calorie_counts.append(calorie_count)
            calorie_count = 0
        else:
            calorie_count += int(line)
    return calorie_counts


def solution_a(input_text: str) -> tuple[int, int]:
    """Solve part a"""
    counts_per_elf = get_counts_per_elf(input_text)
    max_calories = 0
    max_index = -1
    for index, calories in enumerate(counts_per_elf):
        if calories > max_calories:
            max_calories = calories
            max_index = index
    return max_index, max_calories


def solution_b(input_text: str):
    """solution b"""
    counts = get_counts_per_elf(input_text)
    sorted_counts = sorted(counts)
    return sum(sorted_counts[-3:])


if __name__ == "__main__":
    # part a
    day1_input = read_input(1)
    elf, num_calories = solution_a(day1_input)
    print(f"Elf {elf + 1} has {num_calories} Calories!")

    top_3_calories = solution_b(day1_input)
    print(f"Top 3 elfs have {top_3_calories} Calories!")
