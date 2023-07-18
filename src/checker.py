from typing import Optional
from .dictionary import IDictionary, Enchant


class WordChecker:
    ''' Checks if word is valid.
    '''
    def __init__(self,
                 central: str,
                 letters: str,
                 d: Optional[IDictionary] = None) -> None:
        self._central = central
        self._letters = set(central + letters)
        self._d = d or Enchant()

    def check(self, word: str) -> bool:
        if len(word) < 4:
            return False

        # Must contain central letter
        if self._central not in word:
            return False

        # Must contain only chosen letters
        if set(word) - self._letters:
            return False

        # Check with word dictionary
        if not self._d.check(word):
            return False
        
        return True

    def is_pangram(self, word: str) -> bool:
        return all(
            l in word for l in self._letters
        )
