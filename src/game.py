from typing import List

from .letters import Letters
from .checker import WordChecker


class Game:
    ''' Represents a game of Spelling Bee. Checks given answers,
    holds the score and past correct answers.
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
        # Raise if not a word
        # Raise if already given as answer

        # Update score
        # Update answers

        raise ValueError(f"{word}")

    @property
    def score(self) -> int:
        return self._score

    @property
    def answers(self) -> List[str]:
        # This is not sorted in case we'll want to see
        #   them in the order in which they were given
        return list(self._answers)

    def score_word(self, word: str) -> int:
        l = len(word)

        if self._checker.is_pangram(word):
            return l + 7
        if l == 4:
            return 1
        if l > 4:
            return l

        return 0
