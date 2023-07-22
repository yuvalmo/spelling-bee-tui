from typing_extensions import override

from rich.text import Text
from rich.highlighter import Highlighter

from src.letters import Letters


class BeeHighlighter(Highlighter):

    def __init__(self, letters: Letters) -> None:
        super().__init__()
        self.letters = letters

    @override
    def highlight(self, text: Text) -> None:
        for i, c in enumerate(str(text)):
            if c in self.letters.central:
                style = "yellow"
            elif c in self.letters.letters:
                style = ""
            else:
                style = "#404040"

            if style:
                text.stylize(style, i, i+1)
