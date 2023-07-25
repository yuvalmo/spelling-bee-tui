#!/bin/env python3

from functools import partial
from argparse import ArgumentParser, ArgumentTypeError

from src.save import History
from src.letters import Letters

from ui.app import SpellingBee


def str_of_len(length: int):
    def x(l, s):
        if len(s) == l:
            return s
        raise ArgumentTypeError(f"Argument must have length of {l}")
    return partial(x, length)


def parser() -> ArgumentParser:
    p = ArgumentParser()

    p.add_argument(
        "letters",
        type=str_of_len(7),
        help="The letters of the hive. " \
             "The first letter is the center of the hive."
    )
    p.add_argument(
        "--new-game", "-n",
        action="store_true",
        help="Create a new game. " \
             "The previous answers will be deleted."
    )

    return p


def main():
    args = parser().parse_args()

    # The first letter is the central one
    letters = Letters(
        args.letters[:1],
        args.letters[1:]
    )

    if args.new_game:
        History().reset(letters)

    bee = SpellingBee(letters)
    bee.run()


if __name__ == "__main__":
    main()
