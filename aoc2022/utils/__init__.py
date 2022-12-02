from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]


def read_input(day: int) -> str:
    """Given a day and part read the desired input to string"""
    data = Path(WORKSPACE_ROOT) / "aoc2022" / "inputs" / f"input_{day}.txt"
    return data.read_text()
    