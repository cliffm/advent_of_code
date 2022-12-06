import pathlib
import pytest
import aoc202204 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_data():
    filename = (PUZZLE_DIR / "example.txt")
    return aoc.parse(filename)


def test_parse(example_data):
    """Test that input is parsed properly."""
    assert example_data == [("2-4", "6-8"),
                            ("2-3", "4-5"),
                            ("5-7", "7-9"),
                            ("2-8", "3-7"),
                            ("6-6", "4-6"),
                            ("2-6", "4-8")]

def test_part1(example_data):
    """Test part 1 on example input."""
    assert aoc.part1(example_data) == 2

#@pytest.mark.skip(reason="no way of currently testing this")
def test_part2(example_data):
    """Test part 2 on example input."""
    assert aoc.part2(example_data) == 4
