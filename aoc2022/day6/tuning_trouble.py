from aoc2022.utils import read_input


def solution_a(input_txt: str) -> int:
    """Find the start of packet marker.

    Identify the first position where the four most
    recently received characters were all different.
    """
    marker = ""
    for idx, char in enumerate(input_txt):
        try:
            duplicate_index = marker.index(char)
            marker = marker[duplicate_index + 1 :] + char
        except ValueError:
            marker += char
            if len(marker) == 4:
                return idx + 1


def solution_b(input_txt: str) -> int:
    """Find the start of message marker.

    Identify the first position where the 14 most
    recently received characters were all different.
    """
    marker = ""
    for idx, char in enumerate(input_txt):
        try:
            duplicate_index = marker.index(char)
            marker = marker[duplicate_index + 1 :] + char
        except ValueError:
            marker += char
            if len(marker) == 14:
                return idx + 1


if __name__ == "__main__":
    day_6_input = read_input(6).strip()
    start_of_packet = solution_a(day_6_input)
    print(f"Packet starts at {start_of_packet}")

    start_of_msg = solution_b(day_6_input)
    print(f"Message starts at {start_of_msg}")
