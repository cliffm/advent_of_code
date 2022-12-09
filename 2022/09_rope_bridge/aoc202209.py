import argparse
from collections import namedtuple

RopeKnot = namedtuple('RopeKnot', 'x y')

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
    head = RopeKnot(0, 0)
    tail = RopeKnot(0, 0)

    # create a set for recording unique locations
    tail_visited_locations = set()
    # add starting location
    tail_visited_locations.add(tail)

    for move_instruction in puzzle_data:
        direction, spaces = move_instruction
        for _ in range(spaces):
            head = move_head(head, direction)
            tail = move_knot(tail, head)
            tail_visited_locations.add(tail)

    return len(tail_visited_locations)



def part2(puzzle_data: []) -> int:
    head = RopeKnot(0, 0)
    knots = [RopeKnot(0, 0) for _ in range(8)]
    tail = RopeKnot(0, 0)

    # create a set for recording unique locations
    tail_visited_locations = set()
    # add starting location
    tail_visited_locations.add(tail)

    for move_instruction in puzzle_data:
        direction, spaces = move_instruction
        for _ in range(spaces):
            head = move_head(head, direction)

            prev_knot = head
            for i, knot in enumerate(knots):
                knots[i] = move_knot(knot, prev_knot)
                prev_knot = knots[i]

            tail = move_knot(tail, prev_knot)
            tail_visited_locations.add(tail)

    return len(tail_visited_locations)

def move_head(head: RopeKnot, direction: str) -> RopeKnot:
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

    return RopeKnot(x, y)


def move_knot(trailing_knot: RopeKnot, prev_knot: RopeKnot) -> RopeKnot:
    """Move trailing knot, if previous knot is farther than one space away"""
    x, y = trailing_knot
    # tail is further away from head than one space
    if abs(prev_knot.x - trailing_knot.x) > 1 or abs(prev_knot.y - trailing_knot.y) > 1:
        if prev_knot.x == trailing_knot.x:
            # adjust y
            if prev_knot.y > trailing_knot.y:
                y += 1
            else:
                y -= 1
        elif prev_knot.y == trailing_knot.y:
            # adjust x
            if prev_knot.x > trailing_knot.x:
                x += 1
            else:
                x -= 1
        else:
            if prev_knot.y > trailing_knot.y:
                y += 1
            else:
                y -= 1

            if prev_knot.x > trailing_knot.x:
                x += 1
            else:
                x -= 1

    return RopeKnot(x, y)


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
