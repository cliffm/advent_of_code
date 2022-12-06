import argparse

def parse(filename):
    """Parse input."""
    with open(filename, "r") as f:
        input_lines = [line.rstrip() for line in f]

    return input_lines


def part1(puzzle_data):
    """Solve part 1."""
    answers = []
    for line in puzzle_data:
        answers.append(find_sequence(line, 4))

    return answers


def part2(puzzle_data):
    """Solve part 2."""
    answers = []
    for line in puzzle_data:
        answers.append(find_sequence(line, 14))

    return answers


def find_sequence(line, sequence_length):
    sequence = []
    pos = 0
    for i, char in enumerate(line):
        if char in sequence:
            idx = sequence.index(char)
            sequence = sequence[idx + 1:]
            sequence.append(char)
        else:
            sequence.append(char)

        if len(sequence) == sequence_length:
            pos = i + 1
            break

    return pos


def solve(filename):
    """Solve the puzzle for the given input."""
    puzzle_data = parse(filename)
    solution1 = part1(puzzle_data)
    solution2 = part2(puzzle_data)

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tuning Trouble")
    parser.add_argument("-i", dest="filename", required=True, metavar="FILE")
    args = parser.parse_args()

    solutions = solve(args.filename)

    print("\n".join(str(solution) for solution in solutions))
