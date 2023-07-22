from os import linesep
from dataclasses import dataclass

from rich.console import RenderableType
from rich.text import Text

from textual.reactive import reactive
from textual.widgets import Static


@dataclass
class Word:
    value: str
    score: int
    pangram: bool


class Answers(Static):
    DEFAULT_CLASSES = "box"

    score = reactive(0)
    answers = reactive(list())

    def __init__(self):
        super().__init__(id="answers")

    def add(self, word: Word):
        self.score += word.score
        self.answers.append(word)

    def render(self) -> RenderableType:
        self.border_title = f"{self.score} Points"

        summary = Text(
            f"You've found {len(self.answers)} words.\n\n"
        )

        words = [
            Text(x.value,
                 style="yellow" if x.pangram else "")
            for x in self.answers
        ]

        # TODO: Show in columns
        return summary + Text(linesep).join(words)
