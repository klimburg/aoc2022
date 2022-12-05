"""AOC day 5"""


import re

from aoc2022.utils import read_input

MOVE_PATTERN = re.compile(r"move (\d+) from (\d+) to (\d+)")


def parse_input(input_txt: str) -> tuple[list[list[str]], list[str]]:
    """Split the input text into:
    * a list of deques representing the stacks of crates
    * a list of strings for the structions
    """
    stack_str, instructions = input_txt.split("\n\n")
    stack_rows = stack_str.split("\n")

    num_stacks = int(stack_rows[-1].strip().split(" ")[-1])
    stacks: list[list[str]] = [[] for _ in range(num_stacks)]
    for row in stack_rows[:-1][::-1]:
        # iterate from the bottom up
        for idx in range(num_stacks):
            # each 3 characters is one crate followed by a space to delimit
            # chunk in groups of 4, striping whitespace and brackets
            crate = (
                row[idx * 4 : (idx + 1) * 4].strip().replace("[", "").replace("]", "")
            )
            if crate != "":
                stacks[idx].append(crate)
    return stacks, instructions.strip().split("\n")


def move_crates_a(
    stacks: list[list[str]], num_crates: int, from_stack: int, to_stack: int
) -> list[list[str]]:
    """Move some crates from one stack to another

    This moves 1 at a time
    """
    for _ in range(num_crates):
        stacks[to_stack].append(stacks[from_stack].pop())
    return stacks


def move_crates_b(
    stacks: list[list[str]], num_crates: int, from_stack: int, to_stack: int
) -> list[list[str]]:
    """Move some crates from one stack to another

    This implementation moves all at once so they retain order
    """
    # grab the crates to move
    moved_crates = stacks[from_stack][-num_crates:]
    # update the from stack
    stacks[from_stack] = stacks[from_stack][:-num_crates]
    # update the to stack
    stacks[to_stack].extend(moved_crates)
    return stacks


def parse_move(input_str: str) -> tuple[int, int, int]:
    """Take a string move command

    N.B. stack indexes are zero index while inputs are 1 indexed

    Returns: a tuple of number of crates, from stack index and to stack index
    """
    found_values = re.findall(MOVE_PATTERN, input_str)[0]
    assert len(found_values) == 3
    num_crates, from_stack, to_stack = map(int, found_values)
    return num_crates, from_stack - 1, to_stack - 1


def solution_a(input_txt: str) -> str:
    """solution part a"""
    crates, instructions = parse_input(input_txt)
    for instruction in instructions:
        num_crates, from_idx, to_idx = parse_move(instruction)
        crates = move_crates_a(crates, num_crates, from_idx, to_idx)
    return "".join([stack[-1] for stack in crates])


def solution_b(input_txt: str) -> str:
    """solution part b"""
    crates, instructions = parse_input(input_txt)
    for instruction in instructions:
        num_crates, from_idx, to_idx = parse_move(instruction)
        crates = move_crates_b(crates, num_crates, from_idx, to_idx)
    return "".join([stack[-1] for stack in crates])


if __name__ == "__main__":
    input_day5 = read_input(5)
    message = solution_a(input_day5)
    print(f"Top crates a: {message}")

    message = solution_b(input_day5)
    print(f"Top crates b: {message}")
