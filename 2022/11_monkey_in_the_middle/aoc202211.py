import argparse
import math
import re

from monkey import Monkey

monkey_regex = re.compile("Monkey (\d+):")
div_test_regex = re.compile(r"^\s*Test: divisible by (\d+)")
operation_regex = re.compile("^\s*Operation: new = (.*)$")
true_false_regex = re.compile(r"^\s*If (true|false): throw to monkey (\d+)")


def parse(filename: str) -> []:
    """Parse input."""
    monkeys = []
    with open(filename, "r") as f:
        for monkey in f.read().split("\n\n"):
            (id_str, items_str, operation_str, div_test_str, true_str, false_str) = monkey.split("\n")
            match = monkey_regex.match(id_str)
            if match:
                monkey_id = int(match.group(1))

            items = [int(item) for item in items_str.split(":")[1].strip().split(",")]

            match = operation_regex.match(operation_str)
            if match:
                operation = match.group(1)

            match = div_test_regex.match(div_test_str)
            if match:
                div_test = int(match.group(1))

            match = true_false_regex.match(true_str)
            if match:
                true = int(match.group(2))

            match = true_false_regex.match(false_str)
            if match:
                false = int(match.group(2))

            monkeys.append(Monkey(monkey_id, items, operation, div_test, true, false))

    return monkeys


def part1(filename) -> int:
    """Solve part 1."""
    monkeys = parse(filename)

    for _ in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                worry_level = monkey.perform_operation(item)
                worry_level //= 3

                if worry_level % monkey.div_test == 0:
                    monkeys[monkey.true].items.append(worry_level)
                else:
                    monkeys[monkey.false].items.append(worry_level)

            monkey.items.clear()

    return math.prod(sorted([monkey.inspect_count for monkey in monkeys])[-2:])


def part2(filename) -> int:
    """Solve part 2."""
    monkeys = parse(filename)

    master_div = math.lcm(*[monkey.div_test for monkey in monkeys])

    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey.items:
                worry_level = monkey.perform_operation(item)
                worry_level %= master_div

                if worry_level % monkey.div_test == 0:
                    monkeys[monkey.true].items.append(worry_level)
                else:
                    monkeys[monkey.false].items.append(worry_level)
            monkey.items.clear()

    return math.prod(sorted([monkey.inspect_count for monkey in monkeys])[-2:])


def solve(filename: str) -> (int, int):
    """Solve the puzzle for the given input."""
    solution1 = part1(filename)
    solution2 = part2(filename)

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rope Bridge")
    parser.add_argument("-i", dest="filename", required=True, metavar="FILE")
    args = parser.parse_args()

    solutions = solve(args.filename)

    print("\n".join(str(solution) for solution in solutions))
