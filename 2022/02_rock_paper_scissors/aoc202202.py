import argparse
from enum import Enum


class Shapes(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcomes(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6


def parse(filename):
    """Parse input."""
    rounds = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            rounds.append(tuple(line.split()))

    return rounds


def part1(data):
    """Solve part 1."""
    score = 0
    for d in data:
        player1, player2 = d
        player1 = decode_player1_move(player1)

        if player2 == "X":
            player2 = Shapes.ROCK
        elif player2 == "Y":
            player2 = Shapes.PAPER
        else:
            player2 = Shapes.SCISSORS

        score += score_round((player1, player2))

    return score


def part2(data):
    """Solve part 2."""
    score = 0
    for d in data:
        player1, outcome = d
        player1 = decode_player1_move(player1)

        # LOSE
        if outcome == "X":
            if player1 == Shapes.ROCK:
                player2 = Shapes.SCISSORS
            elif player1 == Shapes.PAPER:
                player2 = Shapes.ROCK
            else:
                player2 = Shapes.PAPER
            score += Outcomes.LOSE.value + player2.value
        # DRAW
        elif outcome == "Y":
            player2 = player1
            score += Outcomes.DRAW.value + player2.value
        # WIN
        else:
            if player1 == Shapes.ROCK:
                player2 = Shapes.PAPER
            elif player1 == Shapes.PAPER:
                player2 = Shapes.SCISSORS
            else:
                player2 = Shapes.ROCK
            score += Outcomes.WIN.value + player2.value

    return score


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


def decode_player1_move(player):
    match player:
        case "A":
            shape = Shapes.ROCK
        case "B":
            shape = Shapes.PAPER
        case "C":
            shape = Shapes.SCISSORS
    return shape


def score_round(rnd):
    (player1, player2) = rnd

    score = player2.value
    if player1 == player2:
        score += Outcomes.DRAW.value
    else:
        if player1 == Shapes.ROCK:
            score += Outcomes.WIN.value if player2 == Shapes.PAPER else Outcomes.LOSE.value
        elif player1 == Shapes.PAPER:
            score += Outcomes.WIN.value if player2 == Shapes.SCISSORS else Outcomes.LOSE.value
        else:
            score += Outcomes.WIN.value if player2 == Shapes.ROCK else Outcomes.LOSE.value

    return score


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rock Paper Scissors")
    parser.add_argument("-i", dest="filename", required=True, metavar="FILE")
    args = parser.parse_args()

    solutions = solve(args.filename)

    print("\n".join(str(solution) for solution in solutions))

