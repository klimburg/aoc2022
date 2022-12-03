"""Solutions for day 2"""
from aoc2022.utils import read_input


class Hand:
    """Base class for a rock paper scissors hand"""

    hand_value: int

    def play(self, other: "Hand") -> int:
        """Returns 0 for lose, 3 for draw, 6 for win"""
        raise NotImplementedError


class Rock(Hand):
    """Rock"""

    hand_value = 1

    def play(self, other) -> int:
        match other:
            case Rock():
                return 3
            case Paper():
                return 0
            case Scissors():
                return 6
            case _:
                raise ValueError("Other must be rock, paper or scissors")


class Paper(Hand):
    """Paper"""

    hand_value = 2

    def play(self, other: Hand) -> int:
        match other:
            case Rock():
                return 6
            case Paper():
                return 3
            case Scissors():
                return 0
            case _:
                raise ValueError("Other must be rock, paper or scissors")


class Scissors(Hand):
    """Scissors"""

    hand_value = 3

    def play(self, other: Hand) -> int:
        match other:
            case Rock():
                return 0
            case Paper():
                return 6
            case Scissors():
                return 3
            case _:
                raise ValueError("Other must be rock, paper or scissors")


HANDS = [Rock, Paper, Scissors]


def get_hand_for_part_a(input_letter: str) -> Hand:
    """Factory for instantiating hands, only valid for part a

    In part b we can still use this for picking opponents hand.
    """
    match input_letter.lower():
        case "a" | "x":
            return Rock()
        case "b" | "y":
            return Paper()
        case "c" | "z":
            return Scissors()
        case _:
            raise ValueError("Valid inputs must be in ABCXYZ")


def get_my_hand_for_part_b(opponents_hand: Hand, input_letter: str) -> Hand:
    """Factory for instantiating hands, only valid for part b"""
    desired_outcome = 0
    match input_letter.lower():
        case "x":
            desired_outcome = 0
        case "y":
            desired_outcome = 3
        case "c" | "z":
            desired_outcome = 6
        case _:
            raise ValueError("Valid inputs must be X, Y, or Z")
    for hand in HANDS:
        my_hand = hand()
        if my_hand.play(opponents_hand) == desired_outcome:
            return my_hand
    raise RuntimeError("No solution found this should never happen!")


def play_game(opponent_move: Hand, my_move: Hand) -> int:
    """Play a game of rock paper scicssor and score it"""
    return my_move.play(opponent_move) + my_move.hand_value


def solution_a(input_text: str) -> int:
    """get the score for part a"""
    games = input_text.strip().split("\n")
    total_score = 0
    for game in games:
        opponent, mine = game.split(" ")
        total_score += play_game(
            get_hand_for_part_a(opponent),
            get_hand_for_part_a(mine),
        )

    return total_score


def solution_b(input_text: str) -> int:
    games = input_text.strip().split("\n")
    total_score = 0
    for game in games:
        opponent, mine = game.split(" ")
        opponent_hand = get_hand_for_part_a(opponent)
        total_score += play_game(
            opponent_hand,
            get_my_hand_for_part_b(opponent_hand, mine),
        )

    return total_score


if __name__ == "__main__":
    day_2_text = read_input(2)
    score = solution_a(day_2_text)
    print(f"Total score from part a strategy {score}")

    score = solution_b(day_2_text)
    print(f"Total score from part b strategy {score}")
