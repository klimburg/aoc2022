from collections import Counter

from aoc2022.utils import read_input


def find_end_unique(input_txt: str, n_unique: int) -> int:
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
    raise ValueError("No solution found")


def find_end_unique_set(input_txt: str, n_unique: int) -> int:
    """Find end of a sequence of n unique characters in a longer string"""
    for idx, _ in enumerate(input_txt[n_unique:]):
        if len(set(input_txt[idx : idx + n_unique])) == n_unique:
            return idx + n_unique
    raise ValueError("No solution found")


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


def find_end_unique_counter(input_txt: str, n_unique: int) -> int:

    freq = Counter(input_txt[:n_unique])
    for idx, char_to_increment in enumerate(input_txt[n_unique:]):
        if len(freq) == n_unique:  # if every character has a single entry in freq
            return idx + n_unique
        else:
            char_to_decrement = input_txt[idx]
            freq[char_to_decrement] -= 1
            freq[char_to_increment] += 1
            if freq[char_to_decrement] == 0:
                del freq[char_to_decrement]

    raise (ValueError)


if __name__ == "__main__":
    import string
    import timeit

    day_6_input = read_input(6).strip()
    start_of_packet = solution_a(day_6_input)
    print(f"Packet starts at {start_of_packet}")

    start_of_msg = solution_b(day_6_input)
    print(f"Message starts at {start_of_msg}")

    # figure out which solution is faster
    print("\nBenchmarking our solution")
    num_iterations = 100
    part_a_time = timeit.timeit(
        "solution_a(day_6_input)",
        globals=globals(),
        number=num_iterations,
    )

    part_b_time = timeit.timeit(
        "solution_b(day_6_input)",
        globals=globals(),
        number=num_iterations,
    )
    print(
        f"avg part_a: {part_a_time / num_iterations * 1000 :1.5f}ms, "
        f"avg part_b: {part_b_time / num_iterations * 1000 :1.5f}ms, "
    )

    print("\nBenchmarking our solutions with test inputs")
    false_starts = 40

    for n_unique in range(2, len(string.printable) + 1):
        input_text = ""
        for idx in range(false_starts):
            # add false starts that are no larger than 20 + idx long otherwise set gets
            # clobbered
            input_text += string.printable[: min(20 + idx, n_unique - 1)]
        input_text += string.printable[:n_unique] + "0"

        list_time = timeit.timeit(
            "find_end_unique(input_text, n_unique)",
            globals=globals(),
            number=num_iterations,
        )
        set_time = timeit.timeit(
            "find_end_unique_set(input_text, n_unique)",
            globals=globals(),
            number=num_iterations,
        )
        counter_time = timeit.timeit(
            "find_end_unique_counter(input_text, n_unique)",
            globals=globals(),
            number=num_iterations,
        )

        print(
            f"n_unique: {n_unique}, "
            f"avg list time: {list_time / num_iterations * 1000 :1.5f}ms, "
            f"avg set time: {set_time / num_iterations * 1000 :1.5f}ms, "
            f"avg counter time: {counter_time / num_iterations * 1000:1.5f}ms"
        )
