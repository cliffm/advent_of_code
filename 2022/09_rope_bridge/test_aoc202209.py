import pathlib

import pytest

import aoc202209 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1_data():
    filename = (PUZZLE_DIR / "example1.txt")
    return aoc.parse(filename)


@pytest.fixture
def example2_data():
    filename = (PUZZLE_DIR / "example2.txt")
    return aoc.parse(filename)


def test_parse1(example1_data):
    """Test that input is parsed properly."""
    assert example1_data == [("R", 4),
                             ("U", 4),
                             ("L", 3),
                             ("D", 1),
                             ("R", 4),
                             ("D", 1),
                             ("L", 5),
                             ("R", 2)]


def test_parse2(example2_data):
    """Test that input is parsed properly."""
    assert example2_data == [("R", 5),
                             ("U", 8),
                             ("L", 8),
                             ("D", 3),
                             ("R", 17),
                             ("D", 10),
                             ("L", 25),
                             ("U", 20)]


# @pytest.mark.skip(reason="no way of currently testing this")
def test_part1(example1_data):
    """Test part 1 on example 1 input."""
    assert aoc.part1(example1_data) == 13


# @pytest.mark.skip(reason="no way of currently testing this")
def test_part2_example1(example1_data):
    """Test part 2 on example 1 input."""
    assert aoc.part2(example1_data) == 1


# @pytest.mark.skip(reason="no way of currently testing this")
def test_part2_example2(example2_data):
    """Test part 2 on example 2 input."""
    assert aoc.part2(example2_data) == 36
