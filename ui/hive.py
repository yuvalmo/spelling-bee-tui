import re
import random

from textual.widgets import Static
from textual.reactive import reactive

from src.letters import Letters


HEX = '''
1     2


6     0     3


5     4
'''


class Hive(Static):
    DEFAULT_CLASSES = "box"

    letters = reactive(list(""))

    def __init__(self, letters: Letters):
        super().__init__(id="hive")

        self.central = list(letters.central)
        self.letters = list(letters.letters)

    def shuffle(self):
        ''' Rearrange letters (excluding central) in random order.
        '''
        self.letters = random.sample(self.letters, len(self.letters))

    def render(self) -> str:
        h = HEX

        for i, l in enumerate(self.central + self.letters):
            h = re.sub(str(i), l, h)

        return h
