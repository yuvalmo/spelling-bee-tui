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
    DEFAULT_CLASSES = "panel"

    score = reactive(0)
    answers = reactive(list())

    def __init__(self):
        super().__init__(id="answers")

    def add(self, word: Word) -> None:
        self.score += word.score
        self.answers.append(word)

    def render(self) -> RenderableType:
        self.border_title = f"{self.score} Points"

        def count(s: str, l: list):
            if len(l) != 1:
                s += "s"
            return f"{len(l)} {s}"

        summary = Text(
            f"You have found {count('word', self.answers)}\n\n"
        )

        words = [
            Text(x.value.capitalize(),
                 style="yellow" if x.pangram else "")
            for x in sorted(self.answers, key=lambda x: x.value)
        ]

        # TODO: Show in columns
        return summary + Text(linesep).join(words)
