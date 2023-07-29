from os import linesep
from dataclasses import dataclass

from rich.console import RenderableType
from rich.text import Text

from textual.events import Blur, Focus
from textual.reactive import reactive
from textual.widgets import Input, Static


@dataclass
class Word:
    value: str
    score: int
    pangram: bool


class Answers(Static):
    ''' Show a summary of the correct answers given by the
    player, the score, etc.
    '''

    score = reactive(0)
    answers = reactive(list())

    # A pattern to filter answers with
    search = reactive("")

    def __init__(self):
        super().__init__(id="answers")

    def add(self, word: Word) -> None:
        self.score += word.score
        self.answers.append(word)

    def render(self) -> RenderableType:
        # TODO: Fix this. currently does nothing.
        # self.border_title = f"{self.score} Points"

        def count(s: str, l: list):
            if len(l) != 1:
                s += "s"
            return f"{len(l)} {s}"

        summary = Text(
            f"You have found {count('word', self.answers)}\n\n"
        )

        # TODO: Make this prettier.
        words = [
            Text(x.value.capitalize(),
                 style="yellow" if x.pangram else "")
            for x in sorted(self.answers, key=lambda x: x.value)
            if x.value.startswith(self.search)
        ]

        # TODO: Show in columns
        return summary + Text(linesep).join(words)


class AnswerSearch(Input):
    ''' Allows to search through the list of given
    answers.
    '''
    def __init__(self) -> None:
        super().__init__(id="answer-search")
        self.on_blur(Blur())

    def on_blur(self, _: Blur) -> None:
        self.placeholder = "To search hit <Tab>"

    def on_focus(self, _: Focus) -> None:
        self.placeholder = "To search just type"

    def on_input_changed(self, event: Input.Changed) -> None:
        # TODO: Restructure so we don't have to access
        #   parent.
        if not self.parent:
            return
        answers = self.parent.query_one(Answers)
        answers.search = event.value.lower()
