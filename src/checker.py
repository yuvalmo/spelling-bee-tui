from typing import Optional

from .errors import BadLetters, MissingCenterLetter, NotInWordList, TooShort
from .letters import Letters
from .dictionary import IDictionary, Enchant


class WordChecker:
    ''' Checks if word is valid.
    '''
    def __init__(self,
                 letters: Letters,
                 d: Optional[IDictionary] = None) -> None:
        self._central = letters.central
        self._letters = set(letters.all)
        self._d = d or Enchant()

    def check(self, word: str) -> bool:
        if len(word) < 4:
            raise TooShort()

        # Must contain central letter
        if self._central not in word:
            raise MissingCenterLetter()

        # Must contain only chosen letters
        if set(word) - self._letters:
            raise BadLetters()

        # Check with word dictionary
        if not self._d.check(word):
            raise NotInWordList()
        
        return True

    def is_pangram(self, word: str) -> bool:
        return all(
            l in word for l in self._letters
        )
