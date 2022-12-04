"""AOC day 4"""

RangeTuple = tuple[int, int]  # start of range, end of range


def make_range(str_range: str) -> RangeTuple:
    """Given a string representation of a range return the corresponding set

    e.g. "2-4" -> (2, 4)
    """
    start, end = map(int, str_range.split("-"))
    return start, end


def parse_line(line: str) -> tuple[RangeTuple, RangeTuple]:
    """Take an input line and return two ranges

    e.g. `2-4,6-8` -> `((2, 4), (6, 8))`
    """
    range_a, range_b = map(make_range, line.split(","))
    return range_a, range_b


def fully_overlap(range_a: RangeTuple, range_b: RangeTuple) -> bool:
    """Check if either set is a subset of the other"""
    b_inside_a = (range_b[0] >= range_a[0]) & (range_b[1] <= range_a[1])
    a_inside_b = (range_a[0] >= range_b[0]) & (range_a[1] <= range_b[1])
    return b_inside_a or a_inside_b


def any_overlap(range_a: RangeTuple, range_b: RangeTuple) -> bool:
    """Check if there is any overlap in two ranges
    B starts in A
    123...
    ..345

    B ends in A / A starts in B
    ..345
    123..

    A ends in B

    """
    a_overlaps_b = (range_a[1] >= range_b[0]) & (range_a[0] <= range_b[1])
    b_overlaps_a = (range_b[1] >= range_a[0]) & (range_b[0] <= range_a[1])

    return a_overlaps_b & b_overlaps_a


def solution_a(input_txt: str) -> int:
    """Solution for part a

    How many assignment pairs fully overlap?
    """
    overlaps = 0
    for line in input_txt.strip().split("\n"):
        range_a, range_b = parse_line(line)
        overlaps += int(fully_overlap(range_a, range_b))

    return overlaps


def solution_b(input_txt: str) -> int:
    """Solution for part b

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
