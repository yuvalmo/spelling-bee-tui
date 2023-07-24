from textual import on
from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Footer, Input, Static
from textual.containers import Center, Container, Vertical

from src.letters import Letters
from src.game import Game

from .hive import Hive
from .answers import Answers, Word
from .highlighter import BeeHighlighter


def textbox(letters: Letters) -> Widget:
    hl = BeeHighlighter(letters)

    return Input(
        id="textbox",
        placeholder="Enter word...",
        highlighter=hl
    )


class SpellingBee(App):
    ''' Spelling Bee app.
    '''
    CSS_PATH = "style.css"

    BINDINGS = [
        ("ctrl+r", "shuffle_hive", "Shuffle letters")
    ]

    def __init__(self, letters: Letters):
        super().__init__()
        self._letters = letters
        self._game = Game(letters)

    def compose(self) -> ComposeResult:
        info = '''
the
New York Times
presents:

The Spelling Bee
'''

        yield Static(info, id="info", classes="panel")
        with Vertical():
            yield Static("Spelling Bee", id="title", classes="panel")
            with Container(id="main-panel", classes="panel"):
                with Center():
                    yield textbox(self._letters)
                yield Static(id="error-msg")
                yield Hive(self._letters)
        yield Answers()
        yield Footer()

    def action_shuffle_hive(self):
        self.query_one(Hive).shuffle()

    @on(Input.Submitted)
    def check_word(self, event: Input.Submitted) -> None:
        word = event.value

        try:
            self._game.try_word(word)
            self.query_one(Answers).add(Word(
                value = word,
                score = self._game.score_word(word),
                pangram = self._game.checker.is_pangram(word)
            ))
        except ValueError:
            pass  # TODO: Show error message
