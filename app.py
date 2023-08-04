#!/bin/env python3

from functools import partial
from argparse import ArgumentParser, ArgumentTypeError

from rich.console import Console
from rich.text import Text

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
    list_parser.add_argument(
        "--sort-by-score", "-s",
        action="store_true",
        help="Show games from best to worst."
    )

    return parser


def play(args):
    letters = Letters.fromstr(args.letters)
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


def list_saves(args):
    history = History()
    console = Console()

    games = list(
        history.load(save) for save in history.list()
    )

    if args.sort_by_score:
        # Sort from best score to worst
        games.sort(
            reverse=True,
            key=lambda x: x.score if x else 0
        )
    else:
        # Sort alphabetically
        games.sort(
            key=lambda x: str(x.letters) if x else ""
        )

    for game in games:
        if not game:
            continue

        name = Text(str(game.letters))
        name.stylize("yellow", 0, 1)

        console.print(name, "|", game.score)


def main():
    args = parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
