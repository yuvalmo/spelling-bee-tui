import re
import random

from textual.widgets import Static


HEX = '''
1   2

6   0   3

5   4
'''


class Hive(Static):
    DEFAULT_CLASSES = "box"

    def __init__(self, center: str, letters: str):
        self._center = center
        self._letters = list(letters)

        super().__init__(self._hex(), id="hive")

    def shuffle(self):
        random.shuffle(self._letters)
        self.update(self._hex())

    def _hex(self):
        letters = list(self._center) + self._letters
        hexagon = HEX

        for i, l in enumerate(letters):
            hexagon = re.sub(str(i), l, hexagon)

        return hexagon
