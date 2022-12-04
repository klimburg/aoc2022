"""Day 3 of AOC"""
from string import ascii_letters

from aoc2022.utils import read_input


def find_common_item(rucksack: str) -> str:
    """Take the rucksack string representation and find the common item in each half"""
    half_index = len(rucksack) // 2
    compartment_a = rucksack[:half_index]
    compartment_b = rucksack[half_index:]
    common_set = set(compartment_a) & set(compartment_b)
    assert len(common_set) == 1
    return common_set.pop()


def find_badge(rucksacks: list[str]) -> str:
    """Take 3 rucksacks and find the common item in all of them, that is the badge"""
    assert len(rucksacks) == 3
    common_set = set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2])
    assert len(common_set) == 1
    return common_set.pop()


def get_item_priority(character: str) -> int:
    """Get an items priority

    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
    """
    return ascii_letters.index(character) + 1


def solution_a(input_txt: str) -> int:
    """Solution for part a"""
    rucksacks = input_txt.strip().split()
    score = 0
    for rucksack in rucksacks:
        common_item = find_common_item(rucksack)
        score += get_item_priority(common_item)

    return score


def solution_b(input_txt: str) -> int:
    """Solution for part b"""
    rucksacks = input_txt.strip().split()
    score = 0
    chunk_size = 3
    for index in range(0, len(rucksacks), chunk_size):
        common_item = find_badge(rucksacks[index : index + 3])
        score += get_item_priority(common_item)

    return score


if __name__ == "__main__":
    day3_input = read_input(3)
    score_a = solution_a(day3_input)
    print(f"Score for part a is {score_a}")
    score_b = solution_b(day3_input)
    print(f"Score for part b is {score_b}")
