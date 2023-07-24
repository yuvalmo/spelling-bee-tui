from typing import List

from .letters import Letters
from .checker import WordChecker


class Game:
    ''' Represents a game of Spelling Bee. Checks given
    answers, holds the score and past correct answers.
    '''

    def __init__(self, letters: Letters) -> None:
        self._checker = WordChecker(letters)

        self._score = 0
        self._answers = list()

    def try_word(self, word: str) -> None:
        ''' Check if this word is a correct answer.

        If incorrect -> throws ValueError
        If correct   -> does not throw
        '''
        # Will raise if word is invalid
        self._checker.check(word)

        if word in self._answers:
            raise ValueError("Already found")

        self._score += self.score_word(word)
        self._answers.append(word)

    def score_word(self, word: str) -> int:
        l = len(word)

        # TODO: Make 4 a constant
        if self._checker.is_pangram(word):
            return l + 7
        if l == 4:
            return 1
        if l > 4:
            return l

        return 0

    @property
    def checker(self) -> WordChecker:
        return self._checker

    @property
    def score(self) -> int:
        return self._score

    @property
    def answers(self) -> List[str]:
        # This is not sorted in case we'll want to see
        #   them in the order in which they were given
        return list(self._answers)
