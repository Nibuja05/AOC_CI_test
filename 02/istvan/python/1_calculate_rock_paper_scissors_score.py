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
class GameRound:
    opponent: Shape
    me: Shape


@dataclass
class RoundResult:
    opponent: Shape
    me: Shape
    outcome: Outcome
    score: int


def parse_line_to_round(line: str):
    me = None
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
                me = Shape.ROCK
            case 'Y':
                me = Shape.PAPER
            case 'Z':
                me = Shape.SCISSORS
    if me is None or opponent is None:
        raise Exception("Parsing Error")
    return GameRound(opponent=opponent, me=me)


def parse_rounds_from_input():
    game_rounds: list[GameRound] = []

    with open('input') as in_file:
        for line in in_file:
            game_rounds.append(parse_line_to_round(line))

    return game_rounds


def shape_to_score(shape: Shape) -> int:
    return shape


def round_to_outcome(game_round: GameRound) -> Outcome:
    if game_round.me == game_round.opponent:
        return Outcome.DRAW
    if game_round.me == Shape.ROCK and game_round.opponent == Shape.SCISSORS:
        return Outcome.WIN
    if game_round.me == Shape.PAPER and game_round.opponent == Shape.ROCK:
        return Outcome.WIN
    if game_round.me == Shape.SCISSORS and game_round.opponent == Shape.PAPER:
        return Outcome.WIN
    return Outcome.LOSS


def result_from_game_round(game_round: GameRound) -> RoundResult:
    shape_score = shape_to_score(game_round.me)
    round_outcome = round_to_outcome(game_round)
    outcome_score = round_outcome
    return RoundResult(me=game_round.me,
                       opponent=game_round.opponent,
                       outcome=round_outcome,
                       score=shape_score + outcome_score
                       )


def main():
    game_rounds = parse_rounds_from_input()
    round_results = [result_from_game_round(game_round) for game_round in game_rounds]
    total_score = sum([round_result.score for round_result in round_results])
    print(total_score)


if __name__ == '__main__':
    main()
