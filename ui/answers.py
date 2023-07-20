from os import linesep

from rich.console import RenderableType
from textual.reactive import reactive
from textual.widgets import Static

from src.letters import Letters
from src.game import Game


class Answers(Static):
    DEFAULT_CLASSES = "box"

    score = reactive(0)
    answers = reactive(list())

    def __init__(self, letters: Letters):
        super().__init__(id="answers")
        self._game = Game(letters)

    def check(self, word: str):
        try:
            self._game.try_word(word)
            self.score = self._game.score
            self.answers = self._game.answers
        except ValueError:
            pass  # TODO: Show error message

    def render(self) -> RenderableType:
        self.border_title = f"{self.score} Points"

        # TODO: Show in columns
        return linesep.join(sorted(self.answers))
