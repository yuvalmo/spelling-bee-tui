#!/bin/env python3

from src.text import highlight
from src.checker import WordChecker


def main():
    wc = WordChecker("i", "cenotx")

    while True:
        word = input()

        if not wc.check(word):
            print("Invalid word :(")
        elif wc.is_pangram(word):
            print(highlight(word, "i") + highlight(" pangram"))
        else:
            print(highlight(word, "i"))


if __name__ == "__main__":
    main()
