from os import linesep

from rich.console import RenderableType
from textual.reactive import reactive
from textual.widgets import Static


class Answers(Static):
    DEFAULT_CLASSES = "box"

    score = reactive(0)
    answers = reactive(list())

    def __init__(self):
        super().__init__(id="answers")

    def add(self, word: str, score: int):
        self.score += score
        self.answers.append(word)

    def render(self) -> RenderableType:
        self.border_title = f"{self.score} Points"

        content = f"You've found {len(self.answers)} words.\n\n"
        content += linesep.join(sorted(self.answers))

        # TODO: Show in columns
        return content
