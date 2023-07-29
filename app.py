#!/bin/env python3

from functools import partial
from argparse import ArgumentParser, ArgumentTypeError

from src.game import Game
from src.history import History
from src.letters import Letters

from ui.app import SpellingBee


def str_of_len(length: int):
    def x(l, s):
        if len(s) == l:
            return s
        raise ArgumentTypeError(f"Argument must have length of {l}")
    return partial(x, length)


def parser() -> ArgumentParser:
    parser = ArgumentParser()
    subparsers = parser.add_subparsers()

    play_parser = subparsers.add_parser("play")
    play_parser.set_defaults(func = play)
    play_parser.add_argument(
        "letters",
        type=str_of_len(7),
        help="The letters of the hive. " \
             "The first letter is the center of the hive."
    )
    play_parser.add_argument(
        "--new-game", "-n",
        action="store_true",
        help="Create a new game. " \
             "The previous answers will be deleted."
    )

    list_parser = subparsers.add_parser("list")
    list_parser.set_defaults(func = list_saves)

    return parser

def play(args):
    # The first letter is the central one
    letters = Letters(
        args.letters[:1],
        args.letters[1:]
    )

    history = History()

    if args.new_game:
        history.reset(letters)

    # Load game from history
    game = history.load(letters) or Game(letters)

    # Launch app
    game = SpellingBee(game).run()

    # Save game to history
    if game and game.score:
        history.save(game)


def list_saves(_):
    history = History()

    for save in history.list():
        game = history.load(save)
        if not game:
            print(f"{save} | NA")
        else:
            print(f"{save} | {game.score}p")


def main():
    args = parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
