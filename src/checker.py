from typing import Optional

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
            raise ValueError("Too short")

        # Must contain central letter
        if self._central not in word:
            raise ValueError("Missing center letter")

        # Must contain only chosen letters
        if set(word) - self._letters:
            raise ValueError("Bad letters")

        # Check with word dictionary
        if not self._d.check(word):
            raise ValueError("Not in word list")
        
        return True

    def is_pangram(self, word: str) -> bool:
        return all(
            l in word for l in self._letters
        )
