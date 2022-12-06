import argparse


def parse(filename):
    """Parse input."""
    elves = []
    elf_calories = 0

    with open(filename, "r") as f:
        for line in f:

            if not line.strip():
                elves.append(elf_calories)
                elf_calories = 0
            else:
                elf_calories += int(line)

        if elf_calories > 0:
            elves.append(elf_calories)

    return elves


def part1(data):
    """Solve part 1."""
    return max(data)


def part2(data):
    """Solve part 2."""
    return sum(sorted(data)[-3:])


def solve(filename):
    """Solve the puzzle for the given input."""
    data = parse(filename)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calorie Counting")
    parser.add_argument("-i", dest="filename", required=True, metavar="FILE")
    args = parser.parse_args()

    solutions = solve(args.filename)

    print("\n".join(str(solution) for solution in solutions))
