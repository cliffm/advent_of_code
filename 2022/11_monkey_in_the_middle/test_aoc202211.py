import pathlib

import pytest

import aoc202211 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_data() -> str:
    filename = (PUZZLE_DIR / "example.txt")
    return filename


def test_parse1(example_data):
    """Test that input is parsed properly."""
    pass


# @pytest.mark.skip(reason="no way of currently testing this")
def test_part1(example_data) -> None:
    """Test part 1 on example 1 input."""
    assert aoc.part1(example_data) == 10605


# @pytest.mark.skip(reason="no way of currently testing this")
def test_part2_example1(example_data) -> None:
    """Test part 2 on example 1 input."""
    assert aoc.part2(example_data) == 2713310158
