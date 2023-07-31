from os import linesep
from dataclasses import dataclass

from rich.console import RenderableType
from rich.text import Text

from textual.app import ComposeResult
from textual.containers import Vertical
from textual.events import Blur, Focus
from textual.reactive import reactive
from textual.widgets import Input, Static


@dataclass
class Word:
    value: str
    score: int
    pangram: bool


class Answers(Vertical):
    ''' Show a summary of the correct answers given by the
    player, the score, etc.
    '''
    # The score accumulated so far
    score = reactive(0)

    def __init__(self):
        super().__init__(classes="panel")

    def compose(self) -> ComposeResult:
        yield AnswerList()
        yield AnswerSearch()

    def add(self, word: Word) -> None:
        self.score += word.score
        self.border_title = f"{self.score} Points"

        # NOTE: We have to append the word this way
        #   to trigger the reactive attribute.
        #   Calling `append` does not trigger it.
        lst = self.query_one(AnswerList)
        lst.answers = lst.answers + [word]

    def on_input_changed(self, event: Input.Changed) -> None:
        lst = self.query_one(AnswerList)
        lst.search = event.value.lower()


class AnswerList(Static):
    ''' A searchable list of the given answers so far.
    '''
    # A list containing the correct answers
    answers = reactive(list(), layout=True)

    # A pattern to filter answers with
    search = reactive("", layout=True)

    @staticmethod
    def _make_text(w: Word) -> Text:
        return Text(
            w.value.capitalize(),
            style = "yellow" if w.pangram else ""
        )

    def _make_count(self, num: int, total: int) -> Text:
        count = Text(str(num)) \
              + Text.styled("/", "grey30") \
              + Text(str(total))
        count.align("right", self.size.width)
        return count

    def _starts_with_search(self, w: Word) -> bool:
        if not self.search:
            return True
        return w.value.startswith(self.search)

    def render(self) -> RenderableType:
        # List of correct answers
        words = list(
            map(
                self._make_text,
                filter(
                    self._starts_with_search,
                    sorted(
                        self.answers,
                        key = lambda x: x.value
                    )
                )
            )
        )

        # Count of words matching pattern, out of
        # the total number of words
        count = self._make_count(
            len(words),
            len(self.answers)
        )

        return Text(linesep).join((count, *words))


class AnswerSearch(Input):
    ''' Allows to search through the list of given
    answers.
    '''
    def __init__(self) -> None:
        super().__init__()
        self.on_blur(Blur())

    def on_blur(self, _: Blur) -> None:
        self.placeholder = "To search hit <TAB>"

    def on_focus(self, _: Focus) -> None:
        self.placeholder = "To search just type"
