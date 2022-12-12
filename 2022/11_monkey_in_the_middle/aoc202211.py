import argparse
import math
import re

from monkey import Monkey

monkey_regex = re.compile("Monkey (\d+):")
div_test_regex = re.compile(r"^\s*Test: divisible by (\d+)")
operation_regex = re.compile("^\s*Operation: new = (.*)$")
true_false_regex = re.compile(r"^\s*If (?:true|false): throw to monkey (\d+)")


def parse(filename: str) -> []:
    """Parse input."""
    monkeys = []
    with open(filename, "r") as f:
        for monkey in f.read().split("\n\n"):
            (id_str, items_str, operation_str, div_test_str, true_str, false_str) = monkey.split("\n")
            monkey_id = get_number(id_str, monkey_regex)

            items = [int(item) for item in items_str.split(":")[1].strip().split(",")]

            match = operation_regex.match(operation_str)
            if match:
                operation = match.group(1)

            div_test = get_number(div_test_str, div_test_regex)
            true = get_number(true_str, true_false_regex)
            false = get_number(false_str, true_false_regex)

            monkeys.append(Monkey(monkey_id, items, operation, div_test, true, false))

    return monkeys


def get_number(string: str, regex: re.Pattern[str]) -> int:
    number = None
    match = regex.match(string)
    if match:
        number = int(match.group(1))

    return number


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
    parser = argparse.ArgumentParser(description="Monkey in the Middle")
    parser.add_argument("-i", dest="filename", required=True, metavar="FILE")
    args = parser.parse_args()

    solutions = solve(args.filename)

    print("\n".join(str(solution) for solution in solutions))
