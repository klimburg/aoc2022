"""Tests for day 7 of AOC 2022"""
import pytest

from aoc2022.day7.file_system import get_directory_sizes, solution_a, solution_b

TEST_INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


def test_get_directory_sizes():
    expected_dir_sizes = {"/a": 94853, "/d": 24933642, "/a/e": 584, "/": 48381165}
    assert get_directory_sizes(TEST_INPUT) == expected_dir_sizes


def test_solution_a():
    assert solution_a(TEST_INPUT) == 95437


def test_solution_b():
    assert solution_b(TEST_INPUT) == 24933642
