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
            case Scissor():
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
            case Scissor():
                return 0
            case _:
                raise ValueError("Other must be rock, paper or scissors")


class Scissor(Hand):
    """Scissors"""

    hand_value = 3

    def play(self, other: Hand) -> int:
        match other:
            case Rock():
                return 0
            case Paper():
                return 6
            case Scissor():
                return 3
            case _:
                raise ValueError("Other must be rock, paper or scissors")


def get_hand(input_letter: str) -> Hand:
    """Factory for instantiating hands"""
    match input_letter.lower():
        case "a" | "x":
            return Rock()
        case "b" | "y":
            return Paper()
        case "c" | "z":
            return Scissor()
        case _:
            raise ValueError("Valid inputs must be in ABCXYZ")


def play_game(opponent_move: Hand, my_move: Hand) -> int:
    """Play a game of rock paper scicssor and score it"""
    return my_move.play(opponent_move) + my_move.hand_value


def solution_a(input_text: str) -> int:
    """get the score for part a"""
    games = input_text.strip().split("\n")
    total_score = 0
    for game in games:
        opponent, mine = game.split(" ")
        total_score += play_game(get_hand(opponent), get_hand(mine))

    return total_score


if __name__ == "__main__":
    day_2_text = read_input(2)
    score = solution_a(day_2_text)
    print(f"Total score from strategy {score}")
