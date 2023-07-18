import enchant

from abc import ABC, abstractmethod
from typing_extensions import override


class IDictionary(ABC):
    ''' Used to check if word is real.
    '''
    @abstractmethod
    def check(self, word: str) -> bool:
        pass


class NullDict(IDictionary):
    ''' Accepts all words.
    '''
    @override
    def check(self, _: str) -> bool:
        return True


class Enchant(IDictionary):
    ''' Based on the PyEnchant library.
    '''
    def __init__(self) -> None:
        super().__init__()
        self.d = enchant.Dict("en_US")

    @override
    def check(self, word: str) -> bool:
        return self.d.check(word)
