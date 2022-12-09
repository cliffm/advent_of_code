import argparse
from collections import namedtuple

RopeEnd = namedtuple('RopeEnd', 'x y')

def parse(filename):
    """Parse input."""
    movement_instructions = []
    with open(filename, "r") as f:
        for line in [line.rstrip() for line in f]:
            direction, spaces = line.split()
            movement_instructions.append((direction, int(spaces)))

    return movement_instructions


def part1(puzzle_data: []) -> int:
    """Solve part 1."""
    head = RopeEnd(0, 0)
    tail = RopeEnd(0, 0)

    # create a set for recording unique locations
    tail_visited_locations = set()
    # add starting location
    tail_visited_locations.add(tail)

    for move_instruction in puzzle_data:
        direction, spaces = move_instruction
        for _ in range(spaces):
            head = move_head(head, direction)
            tail = move_tail(tail, head)
            tail_visited_locations.add(tail)

    return len(tail_visited_locations)



def part2(puzzle_data: []) -> int:
    """Solve part 2."""
    pass


def move_head(head: RopeEnd, direction: str) -> RopeEnd:
    """Move head rope end, one space in specified direction"""
    x, y = head
    match direction:
        case "U":
            y = head.y + 1
        case "D":
            y = head.y - 1
        case "L":
            x = head.x - 1
        case "R":
            x = head.x + 1

    return RopeEnd(x, y)


def move_tail(tail: RopeEnd, head: RopeEnd) -> RopeEnd:
    """Move tail rope end, if head is farther than one space away"""
    x, y = tail
    # tail is further away from head than one space
    if abs(head.x - tail.x) > 1 or abs(head.y - tail.y) > 1:
        if head.x == tail.x:
            # adjust y
            if head.y > tail.y:
                y += 1
            else:
                y -= 1
        elif head.y == tail.y:
            # adjust x
            if head.x > tail.x:
                x += 1
            else:
                x -= 1
        else:
            if head.y > tail.y:
                y += 1
            else:
                y -= 1

            if head.x > tail.x:
                x += 1
            else:
                x -= 1

    return RopeEnd(x, y)


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
