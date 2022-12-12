import pathlib

import pytest

import aoc202211 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_data():
    filename = (PUZZLE_DIR / "example.txt")
    return aoc.parse(filename)


def test_parse1(example_data):
    """Test that input is parsed properly."""
    # assert example_data == []
    pass


# @pytest.mark.skip(reason="no way of currently testing this")
def test_part1(example_data):
    """Test part 1 on example 1 input."""
    assert aoc.part1(example_data) == 10605


# @pytest.mark.skip(reason="no way of currently testing this")
def test_part2_example1(example_data):
    """Test part 2 on example 1 input."""
    aoc.part2(example_data) == 2713310158
