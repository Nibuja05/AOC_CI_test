from enum import IntEnum
from dataclasses import dataclass


class Shape(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Outcome(IntEnum):
    LOSS = 0
    DRAW = 3
    WIN = 6


@dataclass
class PartialRoundResult:
    opponent: Shape
    outcome: Outcome


@dataclass
class RoundResult:
    opponent: Shape
    me: Shape
    outcome: Outcome
    score: int


def parse_line_to_round(line: str):
    outcome = None
    opponent = None
    for char in line:
        match char:
            case 'A':
                opponent = Shape.ROCK
            case 'B':
                opponent = Shape.PAPER
            case 'C':
                opponent = Shape.SCISSORS
            case 'X':
                outcome = Outcome.LOSS
            case 'Y':
                outcome = Outcome.DRAW
            case 'Z':
                outcome = Outcome.WIN
    if outcome is None or opponent is None:
        raise Exception("Parsing Error")
    return PartialRoundResult(opponent=opponent, outcome=outcome)


def parse_rounds_from_input():
    game_rounds: list[PartialRoundResult] = []

    with open('input') as in_file:
        for line in in_file:
            game_rounds.append(parse_line_to_round(line))

    return game_rounds


def my_shape_from_partial_result(partial_result: PartialRoundResult) -> Shape:
    lookup_table = {
        Shape.ROCK: {
            Outcome.LOSS: Shape(Shape.SCISSORS),
            Outcome.DRAW: Shape(Shape.ROCK),
            Outcome.WIN: Shape(Shape.PAPER)
        },
        Shape.PAPER: {
            Outcome.LOSS: Shape.ROCK,
            Outcome.DRAW: Shape.PAPER,
            Outcome.WIN: Shape.SCISSORS
        },
        Shape.SCISSORS: {
            Outcome.LOSS: Shape.PAPER,
            Outcome.DRAW: Shape.SCISSORS,
            Outcome.WIN: Shape.ROCK
        },
    }
    return lookup_table[partial_result.opponent][partial_result.outcome]


def result_from_partial(partial_result: PartialRoundResult) -> RoundResult:
    my_shape = my_shape_from_partial_result(partial_result)
    shape_score = my_shape
    outcome_score = partial_result.outcome
    return RoundResult(me=my_shape,
                       opponent=partial_result.opponent,
                       outcome=partial_result.outcome,
                       score=shape_score + outcome_score
                       )


def main():
    game_rounds = parse_rounds_from_input()
    round_results = [result_from_partial(game_round) for game_round in game_rounds]
    total_score = sum([round_result.score for round_result in round_results])
    print(total_score)


if __name__ == '__main__':
    main()
