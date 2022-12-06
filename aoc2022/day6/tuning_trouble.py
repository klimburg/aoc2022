from aoc2022.utils import read_input


def find_end_unique(input_txt: str, n_unique: int):
    """Find end of a sequence of n unique characters in a longer string"""
    marker = ""
    for idx, char in enumerate(input_txt):
        try:
            duplicate_index = marker.index(char)
            marker = marker[duplicate_index + 1 :] + char
        except ValueError:
            marker += char
            if len(marker) == n_unique:
                return idx + 1


def find_end_unique_set(input_txt: str, n_unique: int):
    """Find end of a sequence of n unique characters in a longer string"""
    for idx, _ in enumerate(input_txt[n_unique:]):
        if len(set(input_txt[idx : idx + n_unique])) == n_unique:
            return idx + n_unique


def solution_a(input_txt: str) -> int:
    """Find the start of packet marker.

    Identify the first position where the four most
    recently received characters were all different.
    """
    return find_end_unique(input_txt, 4)


def solution_b(input_txt: str) -> int:
    """Find the start of message marker.

    Identify the first position where the 14 most
    recently received characters were all different.
    """
    return find_end_unique(input_txt, 14)


if __name__ == "__main__":
    import timeit

    day_6_input = read_input(6).strip()
    start_of_packet = solution_a(day_6_input)
    print(f"Packet starts at {start_of_packet}")

    start_of_msg = solution_b(day_6_input)
    print(f"Message starts at {start_of_msg}")

    # figure out which solution is faster
    for n_unique in range(2, 16):
        list_time = timeit.timeit(
            "find_end_unique(day_6_input, n_unique)",
            globals=globals(),
            number=100,
        )
        set_time = timeit.timeit(
            "find_end_unique_set(day_6_input, n_unique)",
            globals=globals(),
            number=100,
        )

        print(
            f"n_unique: {n_unique}, list time: {list_time:1.5f}, set_time: {set_time:1.5f}"
        )
