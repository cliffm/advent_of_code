import argparse


def parse(filename):
    """Parse input."""
    input_lines = []
    with open(filename, "r") as f:
        for line in f:
            input_lines.append(tuple(line.rstrip().split(",")))

    return input_lines


def part1(puzzle_data):
    """Solve part 1."""
    overlap_count = 0
    for line in puzzle_data:
        range1, range2 = line
        range1_start, range1_end = [int(i) for i in range1.split("-")]
        range2_start, range2_end = [int(i) for i in range2.split("-")]
        if (range1_start >= range2_start and range1_end <= range2_end) or (
                range2_start >= range1_start and range2_end <= range1_end):
            overlap_count += 1

    return overlap_count


def part2(puzzle_data):
    """Solve part 2."""
    overlap_count = 0
    for line in puzzle_data:
        range1, range2 = line
        range1_start, range1_end = [int(i) for i in range1.split("-")]
        range2_start, range2_end = [int(i) for i in range2.split("-")]
        if ((range2_start <= range1_start <= range2_end) or (range2_start <= range1_end <= range2_end)) or (
                (range1_start <= range2_start <= range1_end) or (range1_start <= range2_end <= range1_end)):
            overlap_count += 1

    return overlap_count



def solve(filename):
    """Solve the puzzle for the given input."""
    puzzle_data = parse(filename)
    solution1 = part1(puzzle_data)
    solution2 = part2(puzzle_data)

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Camp Cleanup")
    parser.add_argument("-i", dest="filename", required=True, metavar="FILE")
    args = parser.parse_args()

    solutions = solve(args.filename)

    print("\n".join(str(solution) for solution in solutions))
