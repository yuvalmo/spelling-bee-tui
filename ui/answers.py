from os import linesep
from dataclasses import dataclass

from rich.console import RenderableType
from rich.text import Text

from textual.events import Blur, Focus
from textual.reactive import reactive
from textual.widget import Widget
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
    answers = reactive(list(), layout=True)

    # A pattern to filter answers with
    search = reactive("", layout=True)

    def __init__(self):
        super().__init__(id="answers")

    def add(self, word: Word) -> None:
        # NOTE: We have to append the word this way
        #   to trigger the reactive attribute.
        #   Calling `append` does not trigger it.
        self.answers = self.answers + [word]
        self.score += word.score

    def render(self) -> RenderableType:
        # TODO: Fix this. This is weird
        if isinstance(self.parent, Widget):
            panel: Widget = self.parent
            panel.border_title = f"{self.score} Points"

        def _starts_with_search(w: Word) -> bool:
            if not self.search:
                return True
            return w.value.startswith(self.search)

        def _make_text(w: Word) -> Text:
            return Text(
                w.value.capitalize(),
                style = "yellow" if w.pangram else ""
            )

        # List of correct answers
        words = list(
            map(
                _make_text,
                filter(
                    _starts_with_search,
                    sorted(
                        self.answers,
                        key = lambda x: x.value
                    )
                )
            )
        )

        n_searched = len(words)
        n_total = len(self.answers)

        # Count of correct answers
        count = Text(str(n_searched)) \
              + Text.styled("/", "grey30") \
              + Text(str(n_total))
        count.align("right", self.size.width)

        return Text(linesep).join(
            [count] + words
        )


class AnswerSearch(Input):
    ''' Allows to search through the list of given
    answers.
    '''
    def __init__(self) -> None:
        super().__init__(id="answer-search")
        self.on_blur(Blur())

    def on_blur(self, _: Blur) -> None:
        self.placeholder = "To search hit <TAB>"

    def on_focus(self, _: Focus) -> None:
        self.placeholder = "To search just type"

    def on_input_changed(self, event: Input.Changed) -> None:
        # TODO: Restructure so we don't have to access
        #   parent.
        if not self.parent:
            return
        answers = self.parent.query_one(Answers)
        answers.search = event.value.lower()
