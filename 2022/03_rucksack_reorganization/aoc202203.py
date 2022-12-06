import argparse


def parse(filename):
    """Parse input."""
    with open(filename, "r") as f:
        input_lines = [line.rstrip('\n') for line in f]

    return input_lines


def part1(puzzle_data):
    """Solve part 1."""
    priority_sum = 0
    for line in puzzle_data:
        # create a set with the first half of string
        left = set(line[:len(line)//2])
        # create a set with the second half of string
        right = set(line[len(line)//2:])

        # get the first common element
        common = left.intersection(right).pop()
        # sum the priorities based on values from problem
        priority_sum += get_priority_value(common)

    return priority_sum


def part2(puzzle_data):
    """Solve part 2."""
    priority_sum = 0
    for i in range(0, len(puzzle_data), 3):
        # create sets for the next 3 lines
        elf1 = set(puzzle_data[i])
        elf2 = set(puzzle_data[i + 1])
        elf3 = set(puzzle_data[i + 2])

        # get the first common element of the three sets
        common = (elf1 & elf2 & elf3).pop()

        # sum the priorities based on values from problem
        priority_sum += get_priority_value(common)

    return priority_sum


def get_priority_value(char):
    if 97 <= ord(char) <= 122:
        priority = ord(char) - 96
    elif 65 <= ord(char) <= 90:
        priority = ord(char) - 38
    else:
        priority = 0

    return priority


def solve(filename):
    """Solve the puzzle for the given input."""
    puzzle_data = parse(filename)
    solution1 = part1(puzzle_data)
    solution2 = part2(puzzle_data)

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rucksack Reorganization")
    parser.add_argument("-i", dest="filename", required=True, metavar="FILE")
    args = parser.parse_args()

    solutions = solve(args.filename)

    print("\n".join(str(solution) for solution in solutions))
