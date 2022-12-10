import argparse


def parse(filename: str) -> []:
    """Parse input."""
    instructions = []
    with open(filename, "r") as f:
        instructions = [line.rstrip() for line in f]

    return instructions


def part1(puzzle_data: []) -> int:
    """Solve part 1."""
    register = 1
    clock = 0
    signal_strenghs = []
    measurement_windows = [20, 60, 100, 140, 180, 220]

    for i, line in enumerate(puzzle_data):
        instruction, *arg = line.split()

        if instruction == "noop":
            clock += 1
            if clock in measurement_windows:
                signal_strenghs.append(clock * register)
        elif instruction == "addx":
            arg = int(arg[0])
            for _ in range(2):
                clock += 1
                if clock in measurement_windows:
                    signal_strenghs.append(clock * register)
            register += arg

    return sum(signal_strenghs)


def part2(puzzle_data: []):
    """Solve part 2."""
    register = 1
    clock = 0

    for i, line in enumerate(puzzle_data):
        instruction, *arg = line.split()

        if instruction == "noop":
            set_pixel(clock, register)
            clock += 1

        elif instruction == "addx":
            arg = int(arg[0])
            for _ in range(2):
                set_pixel(clock, register)
                clock += 1

            register += arg


def set_pixel(clock, register):
    if register - 1 <= (clock % 40) <= register + 1:
        print("#", end="")
    else:
        print(".", end="")

    if (clock + 1) % 40 == 0:
        print()


def solve(filename: str) -> (int, int):
    """Solve the puzzle for the given input."""
    puzzle_data = parse(filename)
    solution1 = part1(puzzle_data)
    solution2 = part2(puzzle_data)

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rope Bridge")
    parser.add_argument("-i", dest="filename", required=True, metavar="FILE")
    args = parser.parse_args()

    solutions = solve(args.filename)

    print("\n".join(str(solution) for solution in solutions))
