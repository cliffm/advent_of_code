import pathlib
import pytest
import aoc202205 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_data():
    filename = (PUZZLE_DIR / "example.txt")
    return aoc.parse(filename)


def test_parse(example_data):
    """Test that input is parsed properly."""
    assert example_data == ([["Z", "N"], ["M", "C", "D"], ["P"]], ["move 1 from 2 to 1",
                                                                   "move 3 from 1 to 3",
                                                                   "move 2 from 2 to 1",
                                                                   "move 1 from 1 to 2"])


def test_part1(example_data):
    """Test part 1 on example input."""
    assert aoc.part1(example_data) == "CMZ"


#@pytest.mark.skip(reason="no way of currently testing this")
def test_part2(example_data):
    """Test part 2 on example input."""
    assert aoc.part2(example_data) == "MCD"
