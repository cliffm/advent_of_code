import argparse
import copy
import struct
import re

instruction_regex = re.compile(r"move (\d+) from (\d+) to (\d+)")

def parse(filename):
    """Parse input."""
    stack_data = []
    instructions = []
    in_stack_data = True

    with open(filename, "r") as f:
        for line in [line.rstrip() for line in f]:
            if not line:
                in_stack_data = False
                continue

            if in_stack_data:
                stack_data.append(line)
            else:
                instructions.append(line)

        stacks = parse_stack_data(stack_data)

    return stacks, instructions


def parse_stack_data(stack_data):
    # isolate the stack numbers (last line of stack data)
    stack_numbers = stack_data.pop()
    # get the stack count
    stack_count = len(stack_numbers.strip(" ").split())
    # predefine an array of arrays using the stack count
    stacks = [[] for _ in range(stack_count)]

    # create format string for unpacking data
    fmt = "x".join(["xcx" for _ in range(stack_count)])

    # iterate over array, in reverse
    for line in stack_data[::-1]:
        # pad out line so length matches unpack format
        line = line.ljust(len(fmt))

        # unpack fixed width data, using above format
        boxes = [box.decode() for box in struct.unpack(fmt, bytearray(line.encode()))]
        # fill out stacks data structure, ignoring empty boxes
        for i, box in enumerate(boxes):
            if box != " ":
                stacks[i].append(box)

    return stacks


def move_boxes(box_count, from_stack, to_stack):
    for _ in range(box_count):
        box = from_stack.pop()
        to_stack.append(box)


def move_boxes_in_order(box_count, from_stack, to_stack):
    boxes = from_stack[-box_count:]
    del from_stack[len(from_stack) - box_count:]
    to_stack.extend(boxes)

    # boxes = []
    # for _ in range(box_count):
    #     box = from_stack.pop()
    #     boxes.append(box)
    #
    # for box in boxes[::-1]:
    #     to_stack.append(box)


def part1(puzzle_data):
    """Solve part 1."""
    stacks, instructions = puzzle_data
    # make a local copy so original is untouched
    stacks_local = copy.deepcopy(stacks)

    for instruction in instructions:
        match = instruction_regex.match(instruction)
        if match:
            box_count, from_stack, to_stack = (int(i) for i in match.groups())
            move_boxes(box_count, stacks_local[from_stack - 1], stacks_local[to_stack - 1])

    return "".join(stack[-1] for stack in stacks_local)


def part2(puzzle_data):
    """Solve part 2."""
    stacks, instructions = puzzle_data
    # make a local copy so original is untouched
    stacks_local = copy.deepcopy(stacks)

    for instruction in instructions:
        match = instruction_regex.match(instruction)
        if match:
            box_count, from_stack, to_stack = (int(i) for i in match.groups())
            move_boxes_in_order(box_count, stacks_local[from_stack - 1], stacks_local[to_stack - 1])

    return "".join(stack[-1] for stack in stacks_local)


def solve(filename):
    """Solve the puzzle for the given input."""
    puzzle_data = parse(filename)
    solution1 = part1(puzzle_data)
    solution2 = part2(puzzle_data)

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Supply Stacks")
    parser.add_argument("-i", dest="filename", required=True, metavar="FILE")
    args = parser.parse_args()

    solutions = solve(args.filename)

    print("\n".join(str(solution) for solution in solutions))
