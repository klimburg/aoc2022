"""AOC day 4"""


def make_range(str_range: str) -> set[int]:
    """Given a string representation of a range return the corresponding set

    e.g. "2-4" -> {2, 3, 4}
    """
    start, end = map(int, str_range.split("-"))
    return set(range(start, end + 1))


def parse_line(line: str) -> tuple[set[int], set[int]]:
    """Take an input line and return two ranges

    e.g. `2-4,6-8` -> `({2, 3, 4}, {6, 7, 8})`
    """
    range_a, range_b = map(make_range, line.split(","))
    return range_a, range_b


def fully_overlap(set_a: set[int], set_b: set[int]) -> bool:
    """Check if either set is a subset of the other"""
    return set_a.issubset(set_b) or set_b.issubset(set_a)


def any_overlap(set_a: set[int], set_b: set[int]) -> bool:
    """check if there is any overlap in two sets"""
    return bool(set_a.intersection(set_b))


def solution_a(input_txt: str) -> int:
    """solution for part a

    How many assignment pairs fully overlap?
    """
    overlaps = 0
    for line in input_txt.strip().split("\n"):
        range_a, range_b = parse_line(line)
        overlaps += int(fully_overlap(range_a, range_b))

    return overlaps


def solution_b(input_txt: str) -> int:
    """solution for part b

    How many assignment pairs partially overlap?
    """
    overlaps = 0
    for line in input_txt.strip().split("\n"):
        range_a, range_b = parse_line(line)
        overlaps += int(any_overlap(range_a, range_b))

    return overlaps


if __name__ == "__main__":
    from aoc2022.utils import read_input

    day4_input = read_input(4)
    num_overlaps = solution_a(day4_input)
    print(f"There were {num_overlaps} pairs that fully overlapped!")

    num_partial_overlaps = solution_b(day4_input)
    print(f"There were {num_partial_overlaps} pairs that partially overlapped!")
