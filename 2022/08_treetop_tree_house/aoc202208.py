import argparse
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def parse(filename):
    """Parse input."""
    matrix = []
    with open(filename, "r") as f:
        for line in [line.rstrip() for line in f]:
            matrix.append([int(c) for c in line])

    return matrix


def part1(puzzle_data: []) -> int:
    """Solve part 1."""
    visible_trees = 0
    rows: int = len(puzzle_data)

    for i in range(rows):
        cols = len(puzzle_data[i])
        for j in range(cols):
            # count edges
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                visible_trees += 1
            elif check_direction(Direction.UP, puzzle_data, i, j):
                visible_trees += 1
            elif check_direction(Direction.DOWN, puzzle_data, i, j):
                visible_trees += 1
            elif check_direction(Direction.LEFT, puzzle_data, i, j):
                visible_trees += 1
            elif check_direction(Direction.RIGHT, puzzle_data, i, j):
                visible_trees += 1

    return visible_trees


def part2(puzzle_data: []) -> int:
    """Solve part 2."""
    scenic_scores = []

    rows = len(puzzle_data)

    for i in range(rows):
        cols = len(puzzle_data[i])
        for j in range(cols):
            # ignore edges
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                continue

            up_score = get_scenic_score(Direction.UP, puzzle_data, i, j)
            down_score = get_scenic_score(Direction.DOWN, puzzle_data, i, j)
            left_score = get_scenic_score(Direction.LEFT, puzzle_data, i, j)
            right_score = get_scenic_score(Direction.RIGHT, puzzle_data, i, j)

            scenic_scores.append(up_score * down_score * left_score * right_score)

    return max(scenic_scores)


def get_scenic_score(direction: Direction, matrix: [], row: int, col: int) -> int:
    scenic_score = 0
    tree = matrix[row][col]
    match direction:
        case Direction.UP:
            for i in range(row - 1, -1, -1):
                scenic_score += 1
                if tree <= matrix[i][col]: break
        case Direction.DOWN:
            for i in range(row + 1, len(matrix)):
                scenic_score += 1
                if tree <= matrix[i][col]: break
        case Direction.LEFT:
            for j in range(col - 1, -1, -1):
                scenic_score += 1
                if tree <= matrix[row][j]: break
        case Direction.RIGHT:
            for j in range(col + 1, len(matrix[row])):
                scenic_score += 1
                if tree <= matrix[row][j]: break

    return scenic_score


def check_direction(direction: Direction, matrix: [], row: int, col: int) -> bool:
    visible = True
    tree = matrix[row][col]
    match direction:
        case Direction.UP:
            for i in range(row - 1, -1, -1):
                if tree <= matrix[i][col]:
                    visible = False
                    break
        case Direction.DOWN:
            for i in range(row + 1, len(matrix)):
                if tree <= matrix[i][col]:
                    visible = False
                    break
        case Direction.LEFT:
            for j in range(col - 1, -1, -1):
                if tree <= matrix[row][j]:
                    visible = False
                    break
        case Direction.RIGHT:
            for j in range(col + 1, len(matrix[row])):
                if tree <= matrix[row][j]:
                    visible = False
                    break

    return visible


def solve(filename):
    """Solve the puzzle for the given input."""
    puzzle_data = parse(filename)
    solution1 = part1(puzzle_data)
    solution2 = part2(puzzle_data)

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Treetop Tree House")
    parser.add_argument("-i", dest="filename", required=True, metavar="FILE")
    args = parser.parse_args()

    solutions = solve(args.filename)

    print("\n".join(str(solution) for solution in solutions))
