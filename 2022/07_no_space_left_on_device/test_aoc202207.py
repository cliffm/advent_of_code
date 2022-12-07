import pathlib
import pytest
import aoc202207 as aoc
from bigtree import Node, tree_to_dict

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example_data():
    filename = (PUZZLE_DIR / "example.txt")
    return aoc.parse(filename)


def test_parse(example_data):
    """Test that input is parsed properly."""
    test_data = {'//': {'name': '/'}, '///a': {'name': 'a'}, '///a/e': {'name': 'e'}, '///a/e/i': {'name': 'i'},
                 '///a/f': {'name': 'f'}, '///a/g': {'name': 'g'}, '///a/h.lst': {'name': 'h.lst'},
                 '///b.txt': {'name': 'b.txt'},
                 '///c.dat': {'name': 'c.dat'}, '///d': {'name': 'd'}, '///d/j': {'name': 'j'},
                 '///d/d.log': {'name': 'd.log'},
                 '///d/d.ext': {'name': 'd.ext'}, '///d/k': {'name': 'k'}}
    assert test_data == tree_to_dict(example_data)


#@pytest.mark.skip(reason="no way of currently testing this")
def test_part1(example_data):
    """Test part 1 on example input."""
    assert aoc.part1(example_data) == 95437


#@pytest.mark.skip(reason="no way of currently testing this")
def test_part2(example_data):
    """Test part 2 on example input."""
    assert aoc.part2(example_data) == 24933642
