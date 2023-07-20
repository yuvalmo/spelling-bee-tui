import re
import random

from textual.widgets import Static
from src.letters import Letters


HEX = '''
1   2

6   0   3

5   4
'''


class Hive(Static):
    DEFAULT_CLASSES = "box"

    def __init__(self, letters: Letters):
        self._central = letters.central
        self._letters = list(letters.letters)

        super().__init__(self._hex(), id="hive")

    def shuffle(self):
        random.shuffle(self._letters)
        self.update(self._hex())

    def _hex(self):
        letters = list(self._central) + self._letters
        hexagon = HEX

        for i, l in enumerate(letters):
            hexagon = re.sub(str(i), l, hexagon)

        return hexagon
