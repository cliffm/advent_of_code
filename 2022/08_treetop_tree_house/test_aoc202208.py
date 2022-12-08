import pathlib
import pytest
import aoc202208 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_data():
    filename = (PUZZLE_DIR / "example.txt")
    return aoc.parse(filename)


def test_parse(example_data):
    """Test that input is parsed properly."""
    assert example_data == [[3, 0, 3, 7, 3], [2, 5, 5, 1, 2], [6, 5, 3, 3, 2], [3, 3, 5, 4, 9], [3, 5, 3, 9, 0]]


# @pytest.mark.skip(reason="no way of currently testing this")
def test_part1(example_data):
    """Test part 1 on example input."""
    assert aoc.part1(example_data) == 21


#@pytest.mark.skip(reason="no way of currently testing this")
def test_part2(example_data):
    """Test part 2 on example input."""
    assert aoc.part2(example_data) == 8
