#!/bin/env python3

from src.letters import Letters
from ui.app import SpellingBee


def main():
    let = Letters("p", "ghinow")
    bee = SpellingBee(let)
    bee.run()


if __name__ == "__main__":
    main()
