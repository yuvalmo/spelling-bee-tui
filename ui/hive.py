import re
import random

from rich.console import RenderableType
from rich.text import Text

from textual.widgets import Static
from textual.reactive import reactive

from src.letters import Letters

from .highlighter import BeeHighlighter


HEX = '''
   1     2


6     0     3


   5     4
'''


class Hive(Static):
    letters = reactive(list(""))

    def __init__(self, letters: Letters):
        super().__init__(id="hive")

        self.central = list(letters.central)
        self.letters = list(letters.letters)
        self.highlighter = BeeHighlighter(letters)

    def shuffle(self):
        ''' Rearrange letters (excluding central) in
        random order.
        '''
        self.letters = random.sample(self.letters,
                                     len(self.letters))

    def render(self) -> RenderableType:
        h = HEX

        for i, l in enumerate(self.central + self.letters):
            h = re.sub(str(i), l, h)

        text = Text(h)
        self.highlighter.highlight(text)

        return text
