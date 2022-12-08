from collections import defaultdict
import os


def solution_a(input_txt: str) -> int:
    """solve part a

    Find all of the directories with a total size of at most 100000,
    then calculate the sum of their total sizes.
    """
    MAX_DIR_SIZE = 100_000
    dir_sizes = get_directory_sizes(input_txt)
    return sum(size for size in dir_sizes.values() if size <= MAX_DIR_SIZE)


def get_directory_sizes(input_txt: str) -> dict[str, int]:
    """Returns a flat dictionary of all directories and their sizes"""
    file_system: defaultdict[str, int] = defaultdict(int)
    current_directory = "/"
    for line in input_txt.strip().split("\n"):
        if "$ cd" in line:
            subdir = line.replace("$ cd ", "")
            if subdir == "/":
                current_directory = "/"
            else:
                current_directory = os.path.abspath(
                    os.path.join(current_directory, subdir)
                )
        elif line == "$ ls":
            continue
        else:
            value_1, value_2 = line.split(" ")
            if value_1 == "dir":
                new_dir = os.path.join(current_directory, value_2)
                file_system[new_dir] += 0
                assert file_system[new_dir] == 0
            else:
                if current_directory == "/":
                    directories = ["/"]
                else:
                    directories = ["/"] + current_directory.split("/")[1:]
                for index in range(len(directories)):
                    directory = os.path.join(*directories[: index + 1])
                    file_system[directory] += int(value_1)
    return file_system


def solution_b(input_txt: str) -> int:
    """solve part b"""
    TOTAL_DISK_SPACE = 70_000_000
    SPACE_NEEDED = 30_000_000
    dir_sizes = get_directory_sizes(input_txt)
    actual_size = dir_sizes["/"]
    available = TOTAL_DISK_SPACE - actual_size
    to_delete = SPACE_NEEDED - available
    big_enough = [dir_size for dir_size in dir_sizes.values() if dir_size > to_delete]
    return sorted(big_enough)[0]


if __name__ == "__main__":
    from aoc2022.utils import read_input

    day7_input = read_input(7)
    print("Solution A: ", solution_a(day7_input))
    print("Solution B: ", solution_b(day7_input))
